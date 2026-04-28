#!/usr/bin/env python3
"""
Generic research orchestrator.

Purpose:
- Run two CLI-based AI agents as independent researchers.
- Keep every output in a separate file.
- Append all turns to a full transcript.
- Force structured critique, correction, and revision.
- Make the research topic configurable from topic.md, CLI arguments, or a topic file.

Examples:
  python research_orchestrator.py \
    --topic "Compare AMD vs Intel for server CPU investment" \
    --core-area "server CPU demand" \
    --core-area "hyperscaler capex" \
    --entity AMD --entity Intel --entity ARM \
    --output-dir cpu-research

  # If ./topic.md exists, this is enough:
  python research_orchestrator.py

  # Or explicitly point to a different topic file:
  python research_orchestrator.py \
    --topic-file my-topic.md \
    --rounds 3 \
    --agent-a-cmd "codex exec --skip-git-repo-check" \
    --agent-b-cmd "claude -p"
"""

from __future__ import annotations

import argparse
import json
import re
import shlex
import subprocess
import textwrap
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Optional


DEFAULT_AGENT_A_CMD = "codex exec --skip-git-repo-check"
DEFAULT_AGENT_B_CMD = "claude -p"

DEFAULT_TOPIC = "Investigate the selected research topic and produce an evidence-ranked conclusion."
DEFAULT_OUTPUT_DIR = "research-orchestrator-output"
DEFAULT_TOPIC_FILE = "topic.md"
DEFAULT_DECISION_LABELS = ["Strong candidate", "Watchlist", "Avoid", "Insufficient evidence"]


@dataclass(frozen=True)
class Agent:
    name: str
    command: list[str]
    stance: str


@dataclass(frozen=True)
class ResearchConfig:
    topic: str
    core_areas: list[str]
    entities: list[str]
    output_sections: list[str]
    decision_labels: list[str]
    claim_subject_label: str
    final_report_name: str
    aggressive_critique: bool


ROOT = Path(DEFAULT_OUTPUT_DIR)
NOTES = ROOT / "notes"
TRANSCRIPT_DIR = ROOT / "transcript"
CLAIMS = ROOT / "claims"
FINAL = ROOT / "final"
SOURCES = ROOT / "sources"
PROMPTS = ROOT / "prompts"
STATE = ROOT / "state.json"

FULL_TRANSCRIPT = TRANSCRIPT_DIR / "full_debate.md"
CLAIM_REGISTER = CLAIMS / "claim_register.md"
SOURCE_LOG = SOURCES / "source_log.md"


def now() -> str:
    return datetime.now().isoformat(timespec="seconds")


class SetupError(RuntimeError):
    pass


def slugify(value: str, fallback: str = "research") -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = value.strip("-")
    return value or fallback


def configure_paths(root: Path) -> None:
    global ROOT, NOTES, TRANSCRIPT_DIR, CLAIMS, FINAL, SOURCES, PROMPTS, STATE
    global FULL_TRANSCRIPT, CLAIM_REGISTER, SOURCE_LOG

    ROOT = root
    NOTES = ROOT / "notes"
    TRANSCRIPT_DIR = ROOT / "transcript"
    CLAIMS = ROOT / "claims"
    FINAL = ROOT / "final"
    SOURCES = ROOT / "sources"
    PROMPTS = ROOT / "prompts"
    STATE = ROOT / "state.json"

    FULL_TRANSCRIPT = TRANSCRIPT_DIR / "full_debate.md"
    CLAIM_REGISTER = CLAIMS / "claim_register.md"
    SOURCE_LOG = SOURCES / "source_log.md"


def ensure_dir(path: Path) -> None:
    try:
        path.mkdir(parents=True, exist_ok=True)
    except FileExistsError as e:
        if path.exists() and not path.is_dir():
            raise SetupError(
                f"Cannot create directory '{path}': a non-directory already exists there. "
                "Remove or rename that file, or rerun with --output-dir <different-directory>."
            ) from e
        raise


def setup_dirs(config: ResearchConfig) -> None:
    for p in [ROOT, NOTES, TRANSCRIPT_DIR, CLAIMS, FINAL, SOURCES, PROMPTS]:
        ensure_dir(p)

    if not FULL_TRANSCRIPT.exists():
        FULL_TRANSCRIPT.write_text(
            f"# Research Debate Transcript\n\nTopic: {config.topic}\n\n",
            encoding="utf-8",
        )

    if not CLAIM_REGISTER.exists():
        CLAIM_REGISTER.write_text(
            textwrap.dedent(
                f"""\
                # Claim Register

                | ID | Claim | {config.claim_subject_label} | Category | Source | Confidence | Challenged By | Status |
                |---|---|---|---|---|---|---|---|
                """
            ),
            encoding="utf-8",
        )

    if not SOURCE_LOG.exists():
        SOURCE_LOG.write_text(
            textwrap.dedent(
                """\
                # Source Log

                Use this file to track source URLs, primary documents, datasets, filings, papers, interviews, market data sources, and unresolved evidence gaps.

                | ID | Source | Type | Date | Used For | Reliability |
                |---|---|---|---|---|---|
                """
            ),
            encoding="utf-8",
        )


def atomic_write(path: Path, content: str) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(content, encoding="utf-8")
    tmp.replace(path)


def append_transcript(title: str, content: str) -> None:
    with FULL_TRANSCRIPT.open("a", encoding="utf-8") as f:
        f.write(f"\n\n---\n\n# {title}\n\n")
        f.write(f"Timestamp: {now()}\n\n")
        f.write(content)
        f.write("\n")


def write_prompt_debug(name: str, prompt: str) -> None:
    atomic_write(PROMPTS / f"{name}.md", prompt)


def run_agent(agent: Agent, prompt: str, output_file: Path, timeout_seconds: int) -> str:
    """
    Runs one CLI agent.

    The prompt is passed on stdin because it is safer for long prompts than shell arguments.
    """

    print(f"[{now()}] Running {agent.name}: {output_file.name}")

    try:
        result = subprocess.run(
            agent.command,
            input=prompt,
            text=True,
            capture_output=True,
            timeout=timeout_seconds,
            check=False,
        )
    except subprocess.TimeoutExpired as e:
        output = (
            f"ERROR: {agent.name} timed out after {timeout_seconds} seconds.\n\n"
            f"Partial stdout:\n{e.stdout or ''}\n\n"
            f"Partial stderr:\n{e.stderr or ''}\n"
        )
        atomic_write(output_file, output)
        append_transcript(f"{agent.name} timeout: {output_file.stem}", output)
        return output

    output = result.stdout.strip()

    if result.stderr.strip():
        output += "\n\n--- STDERR ---\n\n" + result.stderr.strip()

    if result.returncode != 0:
        output = f"ERROR: {agent.name} exited with code {result.returncode}.\n\n" + output

    atomic_write(output_file, output)
    append_transcript(f"{agent.name}: {output_file.stem}", output)
    return output


def read_file(path: Path, max_chars: Optional[int] = None) -> str:
    if not path.exists():
        return ""
    content = path.read_text(encoding="utf-8")
    if max_chars is not None and len(content) > max_chars:
        return content[-max_chars:]
    return content


def bullets(title: str, values: list[str], empty_text: str) -> str:
    if values:
        body = "\n".join(f"- {v}" for v in values)
    else:
        body = f"- {empty_text}"
    return f"{title}:\n{body}"


def numbered_sections(sections: list[str]) -> str:
    return "\n".join(f"{i}. {section}" for i, section in enumerate(sections, start=1))


def base_context(config: ResearchConfig) -> str:
    critique_mode = (
        "Be adversarial, skeptical, and correction-seeking. Your goal is to find what is wrong, overstated, stale, missing, or weakly sourced. "
        "Do not balance criticism with compliments. Do not preserve claims just because they sound plausible."
        if config.aggressive_critique
        else "Be evidence-driven and direct when critiquing."
    )

    return textwrap.dedent(
        f"""\
        You are participating in a structured multi-agent research process.

        Topic:
        {config.topic}

        {bullets("Core areas", config.core_areas, "No fixed core areas were supplied. Infer the most important subtopics from the topic.")}

        {bullets("Named entities / targets to consider", config.entities, "No fixed entities were supplied. Build the relevant universe yourself and explain omissions.")}

        Hard rules:
        1. Separate confirmed facts, primary-source claims, expert/analyst estimates, rumors, and your own assumptions.
        2. Every important claim must include a source or be marked UNSUPPORTED.
        3. Prefer primary sources and recent sources when the topic is time-sensitive.
        4. Do not treat consensus narrative as fact.
        5. Do not force agreement.
        6. Use explicit confidence levels: High / Medium / Low / Unknown.
        7. Identify missing data and what would be needed to resolve it.
        8. {critique_mode}
        9. Output structured Markdown.
        10. Maintain the claim register format when possible.
        11. When correcting another agent, quote or identify the exact claim being challenged and explain the better replacement.
        12. If a claim is vague, force it into a testable form or reject it.

        Current project files:
        - Full transcript: {FULL_TRANSCRIPT}
        - Claim register: {CLAIM_REGISTER}
        - Source log: {SOURCE_LOG}
        """
    )


def initial_research_prompt(agent: Agent, config: ResearchConfig) -> str:
    sections = numbered_sections(config.output_sections)
    labels = " / ".join(config.decision_labels)
    return base_context(config) + textwrap.dedent(
        f"""\

        Role:
        You are {agent.name}, acting as {agent.stance}.

        Task:
        Produce an initial independent research memo on the topic.

        Required output sections:
        {sections}

        Include a final classification using these labels:
        {labels}

        Key claims table format:
        | ID | Claim | {config.claim_subject_label} | Category | Source | Confidence | Status |
        |---|---|---|---|---|---|---|

        Standards:
        - Be direct.
        - Do not write generic background unless it affects the conclusion.
        - Surface contradictions and uncertainty instead of smoothing them over.
        - Use concise but specific evidence.
        """
    )


def critique_prompt(
    critic: Agent,
    other: Agent,
    other_report: str,
    round_number: int,
    config: ResearchConfig,
) -> str:
    return base_context(config) + textwrap.dedent(
        f"""\

        Role:
        You are {critic.name}, acting as a hostile but evidence-bound reviewer of {other.name}'s research.

        You are reviewing {other.name}'s research from round {round_number}.

        Your job is not to be fair in tone; it is to be fair in evidence. Be aggressive about correction.

        Required behavior:
        1. Attack unsupported claims.
        2. Attack stale, cherry-picked, or non-primary data.
        3. Attack vague wording that hides uncertainty.
        4. Attack logical gaps and causal leaps.
        5. Attack missing alternatives, competitors, substitution risks, confounders, incentives, or base rates.
        6. Attack any ranking, recommendation, or conclusion that is not justified by evidence.
        7. Challenge assumptions numerically where possible.
        8. Distinguish fatal flaws from minor issues.
        9. Propose corrected claims, not just objections.
        10. Add or update claim-register rows.
        11. State what evidence would change your mind.
        12. Mark claims that should be deleted, downgraded, or rewritten.

        Required output sections:
        1. Claims that should be deleted
        2. Claims that must be downgraded
        3. Claims that need rewritten wording
        4. Unsupported or weakly sourced claims
        5. Stale or questionable evidence
        6. Logical gaps and causal errors
        7. Missing evidence and missing alternatives
        8. Ranking / conclusion objections
        9. Corrected claim table
        10. Required follow-up research

        Corrected claim table:
        | Original Claim ID/Text | Problem | Severity | Correction or Replacement | Evidence Needed | Status |
        |---|---|---|---|---|---|

        Rules:
        - Do not praise the other report.
        - Do not summarize the other report except to identify a disputed claim.
        - Do not accept a claim because it is plausible. Demand evidence.
        - If the report uses unclear language like "likely", "strong", "large", or "material", force a measurable definition.

        Other report:
        ```markdown
        {other_report}
        ```
        """
    )


def revision_prompt(
    agent: Agent,
    own_prior: str,
    critique_received: str,
    round_number: int,
    config: ResearchConfig,
) -> str:
    return base_context(config) + textwrap.dedent(
        f"""\

        Role:
        You are {agent.name}. You are revising your research after receiving hostile critique.

        Task:
        Respond to the critique from round {round_number}.

        For every major challenge, choose exactly one disposition:
        - Accept
        - Reject
        - Revise
        - Delete
        - Mark as needs more evidence

        Required output sections:
        1. Thesis changes
        2. Challenges accepted
        3. Challenges rejected, with evidence-based reason
        4. Claims revised
        5. Claims deleted
        6. Claims downgraded due to insufficient evidence
        7. Updated bull/base/bear or pro/con view
        8. Updated ranking or conclusion
        9. Remaining unresolved disputes
        10. Updated claim register rows

        Rules:
        - Do not defend weak claims out of ego.
        - Do not pretend uncertainty is resolved.
        - If the critic is right, say so and fix the claim.
        - If the critic is wrong, explain exactly why using evidence or logic.
        - Preserve only claims that survive adversarial review.

        Your prior report:
        ```markdown
        {own_prior}
        ```

        Critique received:
        ```markdown
        {critique_received}
        ```
        """
    )


def final_memo_prompt(transcript: str, config: ResearchConfig) -> str:
    labels = " / ".join(config.decision_labels)
    return base_context(config) + textwrap.dedent(
        f"""\

        Role:
        You are the chair of a research review committee.

        Given the full debate transcript, produce the final research memo.

        Required output sections:
        1. Executive summary
        2. Final conclusion
        3. What survived adversarial review
        4. What was corrected or deleted
        5. Remaining disputes
        6. Unknowns / data gaps
        7. Evidence quality assessment
        8. Topic-specific analysis
        9. Entity-by-entity or option-by-option analysis, if applicable
        10. Final classification using: {labels}
        11. Bull/base/bear, pro/con, or scenario analysis as appropriate
        12. Key risks
        13. What would change the conclusion
        14. Claim register summary
        15. Source quality assessment

        Rules:
        - Do not hide uncertainty.
        - Do not force consensus.
        - Mark unsupported claims clearly.
        - Prefer fewer high-quality conclusions over many weak conclusions.
        - Be explicit about whether the conclusion is actionable or only preliminary.
        - Identify which agent was more accurate where the transcript supports that judgment.

        Full debate transcript:
        ```markdown
        {transcript}
        ```
        """
    )


def save_state(data: dict) -> None:
    atomic_write(STATE, json.dumps(data, indent=2, ensure_ascii=False))


def parse_agent_command(parser: argparse.ArgumentParser, option_name: str, command: str) -> list[str]:
    try:
        parsed = shlex.split(command)
    except ValueError as e:
        parser.error(f"{option_name}: {e}")

    if not parsed:
        parser.error(f"{option_name} must not be empty.")

    return parsed


def read_topic_file(path: Path, parser: argparse.ArgumentParser, label: str) -> str:
    if not path.exists():
        parser.error(f"{label} does not exist: {path}")
    if not path.is_file():
        parser.error(f"{label} is not a file: {path}")

    topic = path.read_text(encoding="utf-8").strip()
    if not topic:
        parser.error(f"{label} is empty: {path}")
    return topic


def read_topic(args: argparse.Namespace, parser: argparse.ArgumentParser) -> tuple[str, str]:
    if args.topic and args.topic_file:
        parser.error("Use either --topic or --topic-file, not both.")

    if args.topic:
        topic = args.topic.strip()
        if not topic:
            parser.error("--topic must not be empty.")
        return topic, "--topic"

    if args.topic_file:
        path = Path(args.topic_file).expanduser()
        return read_topic_file(path, parser, "--topic-file"), str(path)

    default_topic_path = Path(args.default_topic_file).expanduser()
    if default_topic_path.exists():
        return read_topic_file(default_topic_path, parser, "default topic file"), str(default_topic_path)

    if args.require_topic_file:
        parser.error(
            f"No topic supplied and default topic file was not found: {default_topic_path}. "
            "Create topic.md, pass --topic, or pass --topic-file <path>."
        )

    return DEFAULT_TOPIC, "built-in default"

def split_csv_values(values: list[str]) -> list[str]:
    output: list[str] = []
    for value in values:
        for part in value.split(","):
            cleaned = part.strip()
            if cleaned:
                output.append(cleaned)
    return output


def build_config(args: argparse.Namespace, parser: argparse.ArgumentParser) -> tuple[ResearchConfig, str]:
    topic, topic_source = read_topic(args, parser)

    output_sections = args.output_section or [
        "Executive thesis",
        "Scope and definitions",
        "Research universe / options considered",
        "Evidence map",
        "Key facts and sources",
        "Main drivers or causal mechanisms",
        "Counterarguments and disconfirming evidence",
        "Bull case / strongest positive interpretation",
        "Bear case / strongest negative interpretation",
        "Base case / most likely interpretation",
        "Key claims table",
        "Evidence gaps",
        "Initial classification / ranking",
        "What must be verified next",
    ]

    decision_labels = split_csv_values(args.decision_label) if args.decision_label else DEFAULT_DECISION_LABELS

    final_report_name = args.final_report_name
    if not final_report_name:
        final_report_name = f"final_{slugify(topic)[:60]}_memo.md"
    elif not final_report_name.endswith(".md"):
        final_report_name += ".md"

    config = ResearchConfig(
        topic=topic,
        core_areas=args.core_area,
        entities=args.entity,
        output_sections=output_sections,
        decision_labels=decision_labels,
        claim_subject_label=args.claim_subject_label,
        final_report_name=final_report_name,
        aggressive_critique=not args.less_aggressive_critique,
    )
    return config, topic_source


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a generic two-agent adversarial research process.")
    parser.add_argument("--topic", help="Research topic/question. Overrides the default topic.md file.")
    parser.add_argument("--topic-file", help="Markdown/text file containing the research brief. Overrides the default topic.md file.")
    parser.add_argument("--default-topic-file", default=DEFAULT_TOPIC_FILE, help="Default topic file to read when --topic and --topic-file are omitted. Defaults to ./topic.md.")
    parser.add_argument("--require-topic-file", action="store_true", help="Fail if no topic is supplied and the default topic file is missing.")
    parser.add_argument("--core-area", action="append", default=[], help="Important subtopic to force into the research. Repeatable.")
    parser.add_argument("--entity", action="append", default=[], help="Named company/person/project/option/etc. to consider. Repeatable.")
    parser.add_argument("--output-section", action="append", help="Required initial memo section. Repeatable. Overrides defaults.")
    parser.add_argument("--decision-label", action="append", help="Allowed final labels. Repeatable or comma-separated.")
    parser.add_argument("--claim-subject-label", default="Subject", help="Column name for the claim table subject, e.g. Company, Project, Policy, Paper.")
    parser.add_argument("--final-report-name", help="Final report filename. Defaults to a slug based on topic.")

    parser.add_argument("--rounds", type=int, default=2, help="Critique/revision rounds after initial research.")
    parser.add_argument("--timeout", type=int, default=3600, help="Timeout per agent call in seconds.")
    parser.add_argument("--transcript-max-chars", type=int, default=120_000)
    parser.add_argument("--skip-final", action="store_true")
    parser.add_argument("--less-aggressive-critique", action="store_true", help="Soften critique prompts slightly. Default is aggressive.")

    parser.add_argument("--agent-a-name", default="codex")
    parser.add_argument("--agent-b-name", default="claude")
    parser.add_argument("--agent-a-stance", default="an evidence-disciplined researcher looking for the strongest supportable thesis")
    parser.add_argument("--agent-b-stance", default="a skeptical researcher looking for flaws, alternatives, and disconfirming evidence")
    parser.add_argument("--agent-a-cmd", default=DEFAULT_AGENT_A_CMD, help="Agent A command. Prompt is passed on stdin.")
    parser.add_argument("--agent-b-cmd", default=DEFAULT_AGENT_B_CMD, help="Agent B command. Prompt is passed on stdin.")

    # Backward-compatible aliases for the original script.
    parser.add_argument("--codex-cmd", help="Alias for --agent-a-cmd.")
    parser.add_argument("--claude-cmd", help="Alias for --agent-b-cmd.")

    parser.add_argument("--output-dir", default=DEFAULT_OUTPUT_DIR, help="Directory where research outputs are written.")
    parser.add_argument("--dry-run", action="store_true", help="Print planned commands/config and exit without running agents.")
    args = parser.parse_args()

    if args.rounds < 0:
        parser.error("--rounds must be >= 0")

    if args.codex_cmd:
        args.agent_a_cmd = args.codex_cmd
    if args.claude_cmd:
        args.agent_b_cmd = args.claude_cmd

    config, topic_source = build_config(args, parser)
    configure_paths(Path(args.output_dir).expanduser())

    agent_a = Agent(
        args.agent_a_name,
        parse_agent_command(parser, "--agent-a-cmd", args.agent_a_cmd),
        args.agent_a_stance,
    )
    agent_b = Agent(
        args.agent_b_name,
        parse_agent_command(parser, "--agent-b-cmd", args.agent_b_cmd),
        args.agent_b_stance,
    )

    if args.dry_run:
        print(f"Topic source: {topic_source}")
        print(f"Topic: {config.topic}")
        print(f"Core areas: {config.core_areas}")
        print(f"Entities: {config.entities}")
        print(f"Decision labels: {config.decision_labels}")
        print(f"Agent A: {agent_a.name} -> {agent_a.command}")
        print(f"Agent B: {agent_b.name} -> {agent_b.command}")
        print(f"Planned output directory: {ROOT}")
        print(f"Planned number of rounds: {args.rounds}")
        print(f"Final report name: {config.final_report_name}")
        return

    try:
        setup_dirs(config)
    except SetupError as e:
        parser.exit(2, f"error: {e}\n")

    state = {
        "started_at": now(),
        "topic": config.topic,
        "topic_source": topic_source,
        "core_areas": config.core_areas,
        "entities": config.entities,
        "rounds": args.rounds,
        "agent_a": {"name": agent_a.name, "command": agent_a.command, "stance": agent_a.stance},
        "agent_b": {"name": agent_b.name, "command": agent_b.command, "stance": agent_b.stance},
        "aggressive_critique": config.aggressive_critique,
    }
    save_state(state)

    # Round 0: independent initial reports.
    agent_a_initial_file = NOTES / f"{slugify(agent_a.name)}_initial.md"
    agent_b_initial_file = NOTES / f"{slugify(agent_b.name)}_initial.md"

    agent_a_initial_prompt = initial_research_prompt(agent_a, config)
    agent_b_initial_prompt = initial_research_prompt(agent_b, config)
    write_prompt_debug(f"{slugify(agent_a.name)}_initial_prompt", agent_a_initial_prompt)
    write_prompt_debug(f"{slugify(agent_b.name)}_initial_prompt", agent_b_initial_prompt)

    agent_a_current = run_agent(agent_a, agent_a_initial_prompt, agent_a_initial_file, args.timeout)
    agent_b_current = run_agent(agent_b, agent_b_initial_prompt, agent_b_initial_file, args.timeout)

    # Debate rounds.
    for r in range(1, args.rounds + 1):
        agent_a_critiques_b_file = NOTES / f"round_{r}_{slugify(agent_a.name)}_critiques_{slugify(agent_b.name)}.md"
        agent_b_critiques_a_file = NOTES / f"round_{r}_{slugify(agent_b.name)}_critiques_{slugify(agent_a.name)}.md"

        agent_a_critique_prompt = critique_prompt(agent_a, agent_b, agent_b_current, r, config)
        agent_b_critique_prompt = critique_prompt(agent_b, agent_a, agent_a_current, r, config)
        write_prompt_debug(f"round_{r}_{slugify(agent_a.name)}_critiques_{slugify(agent_b.name)}_prompt", agent_a_critique_prompt)
        write_prompt_debug(f"round_{r}_{slugify(agent_b.name)}_critiques_{slugify(agent_a.name)}_prompt", agent_b_critique_prompt)

        agent_a_critique = run_agent(agent_a, agent_a_critique_prompt, agent_a_critiques_b_file, args.timeout)
        agent_b_critique = run_agent(agent_b, agent_b_critique_prompt, agent_b_critiques_a_file, args.timeout)

        agent_a_revision_file = NOTES / f"round_{r}_{slugify(agent_a.name)}_revision.md"
        agent_b_revision_file = NOTES / f"round_{r}_{slugify(agent_b.name)}_revision.md"

        agent_a_revision_prompt = revision_prompt(agent_a, agent_a_current, agent_b_critique, r, config)
        agent_b_revision_prompt = revision_prompt(agent_b, agent_b_current, agent_a_critique, r, config)
        write_prompt_debug(f"round_{r}_{slugify(agent_a.name)}_revision_prompt", agent_a_revision_prompt)
        write_prompt_debug(f"round_{r}_{slugify(agent_b.name)}_revision_prompt", agent_b_revision_prompt)

        agent_a_current = run_agent(agent_a, agent_a_revision_prompt, agent_a_revision_file, args.timeout)
        agent_b_current = run_agent(agent_b, agent_b_revision_prompt, agent_b_revision_file, args.timeout)

    if not args.skip_final:
        transcript = read_file(FULL_TRANSCRIPT, max_chars=args.transcript_max_chars)
        final_file = FINAL / config.final_report_name

        # Use Agent A as chair for the final memo. Agent A defaults to Codex.
        final_prompt = final_memo_prompt(transcript, config)
        write_prompt_debug("final_memo_prompt", final_prompt)
        run_agent(agent_a, final_prompt, final_file, args.timeout)
        print(f"\nFinal memo written to: {final_file}")
    else:
        print("\nSkipped final memo.")

    print(f"Full transcript written to: {FULL_TRANSCRIPT}")
    print(f"Claim register template: {CLAIM_REGISTER}")
    print(f"Source log template: {SOURCE_LOG}")
    print(f"Prompt debug files written to: {PROMPTS}")


if __name__ == "__main__":
    main()
