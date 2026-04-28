#!/usr/bin/env python3
"""
CPU investment research orchestrator.

Purpose:
- Run Codex and Claude Code as two separate research agents.
- Keep every output in a separate file.
- Append all turns to a full transcript.
- Force structured critique and revision.
- Stop after fixed rounds or when no material disputes remain.

You can override Codex and Claude CLI commands with --codex-cmd and --claude-cmd.
"""

from __future__ import annotations

import argparse
import json
import shlex
import subprocess
import textwrap
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Optional


DEFAULT_CODEX_CMD = "codex exec --skip-git-repo-check"
DEFAULT_CLAUDE_CMD = "claude -p"


@dataclass
class Agent:
    name: str
    command: list[str]


ROOT = Path("cpu-investment-research")
NOTES = ROOT / "notes"
TRANSCRIPT_DIR = ROOT / "transcript"
CLAIMS = ROOT / "claims"
FINAL = ROOT / "final"
SOURCES = ROOT / "sources"
STATE = ROOT / "state.json"

FULL_TRANSCRIPT = TRANSCRIPT_DIR / "full_debate.md"
CLAIM_REGISTER = CLAIMS / "claim_register.md"
SOURCE_LOG = SOURCES / "source_log.md"


def now() -> str:
    return datetime.now().isoformat(timespec="seconds")


class SetupError(RuntimeError):
    pass


def configure_paths(root: Path) -> None:
    global ROOT, NOTES, TRANSCRIPT_DIR, CLAIMS, FINAL, SOURCES, STATE
    global FULL_TRANSCRIPT, CLAIM_REGISTER, SOURCE_LOG

    ROOT = root
    NOTES = ROOT / "notes"
    TRANSCRIPT_DIR = ROOT / "transcript"
    CLAIMS = ROOT / "claims"
    FINAL = ROOT / "final"
    SOURCES = ROOT / "sources"
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


def setup_dirs() -> None:
    for p in [ROOT, NOTES, TRANSCRIPT_DIR, CLAIMS, FINAL, SOURCES]:
        ensure_dir(p)

    if not FULL_TRANSCRIPT.exists():
        FULL_TRANSCRIPT.write_text("# CPU Investment Research Debate Transcript\n\n", encoding="utf-8")

    if not CLAIM_REGISTER.exists():
        CLAIM_REGISTER.write_text(
            textwrap.dedent(
                """\
                # Claim Register

                | ID | Claim | Company | Category | Source | Confidence | Challenged By | Status |
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

                Use this file to track source URLs, filings, earnings calls, market data sources, and unresolved evidence gaps.

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


def run_agent(agent: Agent, prompt: str, output_file: Path, timeout_seconds: int) -> str:
    """
    Runs one CLI agent.

    Important:
    - Some CLIs accept prompt as stdin.
    - Some require prompt as an argument.
    - This function uses stdin first because it is safer for long prompts.
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
        output = (
            f"ERROR: {agent.name} exited with code {result.returncode}.\n\n"
            + output
        )

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


def base_context() -> str:
    return textwrap.dedent(
        f"""\
        You are participating in a structured investment research process.

        Topic:
        Investigate the investment feasibility of CPU-related public companies.

        Core areas:
        - Server CPU market
        - Data center CPU demand
        - AI server CPU attach rate
        - Hyperscaler capex and server architecture
        - OEM/ODM server configurations and shipment trends
        - CPU ASP and pricing pressure
        - x86 vs ARM server adoption
        - AMD, Intel, ARM Holdings, Qualcomm, Broadcom, Marvell, TSMC, Supermicro, Dell, HPE, Lenovo, Quanta, Wiwynn, Inventec
        - Public equity investment implications

        Hard rules:
        1. Separate confirmed facts, management guidance, analyst estimates, market rumors, and your own assumptions.
        2. Every important claim must include a source or be marked UNSUPPORTED.
        3. Do not treat consensus narrative as fact.
        4. Do not force agreement.
        5. Use explicit confidence levels: High / Medium / Low / Unknown.
        6. Identify missing data.
        7. When critiquing, be adversarial but evidence-driven.
        8. Output structured Markdown.
        9. Maintain a claim register format when possible.

        Current project files:
        - Full transcript: {FULL_TRANSCRIPT}
        - Claim register: {CLAIM_REGISTER}
        - Source log: {SOURCE_LOG}
        """
    )


def initial_research_prompt(agent_name: str, stance: str) -> str:
    return base_context() + textwrap.dedent(
        f"""\
        
        Role:
        You are {agent_name}, acting as {stance}.

        Task:
        Produce an initial independent research memo.

        Required output sections:
        1. Executive thesis
        2. Industry map
        3. Company universe
        4. Demand drivers
        5. Server CPU market structure
        6. Hyperscaler and data center order signals
        7. OEM/ODM server configuration and shipment implications
        8. CPU pricing / ASP / margin discussion
        9. x86 vs ARM substitution risk
        10. Company-by-company analysis
        11. Bull case
        12. Bear case
        13. Base case
        14. Key claims table
        15. Evidence gaps
        16. Initial ranking: Strong candidate / Watchlist / Avoid
        17. What must be verified next

        Key claims table format:
        | ID | Claim | Company | Category | Source | Confidence | Status |
        |---|---|---|---|---|---|---|

        Be direct. Do not write generic semiconductor background unless it affects investment conclusion.
        """
    )


def critique_prompt(
    critic_name: str,
    other_name: str,
    other_report: str,
    round_number: int,
) -> str:
    return base_context() + textwrap.dedent(
        f"""\
        
        Role:
        You are {critic_name}, acting as an opposing investment analyst.

        You are reviewing {other_name}'s research from round {round_number}.

        Your job:
        1. Identify unsupported claims.
        2. Identify stale or questionable data.
        3. Identify logical gaps.
        4. Identify missing companies, competitors, substitution risks, or supply-chain links.
        5. Challenge valuation assumptions.
        6. Challenge market-share assumptions.
        7. Challenge CPU pricing / ASP assumptions.
        8. Distinguish fatal flaws from minor issues.
        9. Update or add to the claim register.
        10. State what evidence would change your mind.

        Required output sections:
        1. Highest-risk errors
        2. Unsupported claims
        3. Questionable assumptions
        4. Missing evidence
        5. Company-specific objections
        6. Revised ranking, if any
        7. Claim challenges table
        8. Required follow-up research

        Claim challenges table:
        | Claim ID | Problem | Severity | Suggested Fix | Status |
        |---|---|---|---|---|

        Do not agree for politeness.
        Do not summarize the other report except where necessary.

        Other report:
        ```markdown
        {other_report}
        ```
        """
    )


def revision_prompt(
    agent_name: str,
    own_prior: str,
    critique_received: str,
    round_number: int,
) -> str:
    return base_context() + textwrap.dedent(
        f"""\
        
        Role:
        You are {agent_name}. You are revising your research after receiving critique.

        Task:
        Respond to the critique from round {round_number}.

        For every major challenge:
        - Accept
        - Reject
        - Revise
        - Mark as needs more evidence

        Required output sections:
        1. Changes made to thesis
        2. Challenges accepted
        3. Challenges rejected, with reason
        4. Claims revised
        5. Claims downgraded due to insufficient evidence
        6. Updated bull/base/bear view
        7. Updated company ranking
        8. Remaining unresolved disputes
        9. Updated claim register rows

        Do not pretend uncertainty is resolved.

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


def final_memo_prompt(transcript: str) -> str:
    return base_context() + textwrap.dedent(
        f"""\
        
        Role:
        You are the chair of an investment committee.

        Given the full debate transcript, produce the final investment memo.

        Required output sections:
        1. Executive summary
        2. Final investment conclusion
        3. Consensus findings
        4. Remaining disputes
        5. Unknowns / data gaps
        6. Market structure
        7. Demand outlook
        8. Server configuration and CPU attach-rate analysis
        9. OEM/ODM shipment implications
        10. CPU pricing / ASP / margin implications
        11. Company-by-company thesis
        12. Final ranking: Strong candidate / Watchlist / Avoid
        13. Bull/base/bear scenarios
        14. Key risks
        15. What would change the thesis
        16. Claim register summary
        17. Source quality assessment

        Rules:
        - Do not hide uncertainty.
        - Do not force consensus.
        - Mark unsupported claims clearly.
        - Prefer fewer high-quality conclusions over many weak conclusions.
        - Be explicit about whether this is actionable or only watchlist-level research.

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


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rounds", type=int, default=2, help="Critique/revision rounds after initial research.")
    parser.add_argument("--timeout", type=int, default=3600, help="Timeout per agent call in seconds.")
    parser.add_argument("--transcript-max-chars", type=int, default=120_000)
    parser.add_argument("--skip-final", action="store_true")
    parser.add_argument("--codex-cmd", default=DEFAULT_CODEX_CMD, help="Codex command to run. The prompt is passed on stdin.")
    parser.add_argument("--claude-cmd", default=DEFAULT_CLAUDE_CMD, help="Claude command to run. The prompt is passed on stdin.")
    parser.add_argument("--output-dir", default=str(ROOT), help="Directory where research outputs are written.")
    parser.add_argument("--dry-run", action="store_true", help="Print the planned commands and exit without running agents.")
    args = parser.parse_args()

    configure_paths(Path(args.output_dir).expanduser())

    codex = Agent("codex", parse_agent_command(parser, "--codex-cmd", args.codex_cmd))
    claude = Agent("claude", parse_agent_command(parser, "--claude-cmd", args.claude_cmd))

    if args.dry_run:
        print(f"Parsed Codex command: {codex.command}")
        print(f"Parsed Claude command: {claude.command}")
        print(f"Planned output directory: {ROOT}")
        print(f"Planned number of rounds: {args.rounds}")
        return

    try:
        setup_dirs()
    except SetupError as e:
        parser.exit(2, f"error: {e}\n")

    state = {
        "started_at": now(),
        "rounds": args.rounds,
        "codex_command": codex.command,
        "claude_command": claude.command,
    }
    save_state(state)

    # Round 0: independent initial reports.
    codex_initial_file = NOTES / "codex_initial.md"
    claude_initial_file = NOTES / "claude_initial.md"

    codex_initial = run_agent(
        codex,
        initial_research_prompt("Codex", "a bullish but evidence-disciplined CPU equity researcher"),
        codex_initial_file,
        args.timeout,
    )

    claude_initial = run_agent(
        claude,
        initial_research_prompt("Claude", "a bearish but evidence-disciplined CPU equity researcher"),
        claude_initial_file,
        args.timeout,
    )

    codex_current = codex_initial
    claude_current = claude_initial

    # Debate rounds.
    for r in range(1, args.rounds + 1):
        codex_critiques_claude_file = NOTES / f"round_{r}_codex_critiques_claude.md"
        claude_critiques_codex_file = NOTES / f"round_{r}_claude_critiques_codex.md"

        codex_critique = run_agent(
            codex,
            critique_prompt("Codex", "Claude", claude_current, r),
            codex_critiques_claude_file,
            args.timeout,
        )

        claude_critique = run_agent(
            claude,
            critique_prompt("Claude", "Codex", codex_current, r),
            claude_critiques_codex_file,
            args.timeout,
        )

        codex_revision_file = NOTES / f"round_{r}_codex_revision.md"
        claude_revision_file = NOTES / f"round_{r}_claude_revision.md"

        codex_current = run_agent(
            codex,
            revision_prompt("Codex", codex_current, claude_critique, r),
            codex_revision_file,
            args.timeout,
        )

        claude_current = run_agent(
            claude,
            revision_prompt("Claude", claude_current, codex_critique, r),
            claude_revision_file,
            args.timeout,
        )

    if not args.skip_final:
        transcript = read_file(FULL_TRANSCRIPT, max_chars=args.transcript_max_chars)
        final_file = FINAL / "final_investment_memo.md"

        # Use Codex as chair for the final memo.
        run_agent(
            codex,
            final_memo_prompt(transcript),
            final_file,
            args.timeout,
        )

        print(f"\nFinal memo written to: {final_file}")
    else:
        print("\nSkipped final memo.")

    print(f"Full transcript written to: {FULL_TRANSCRIPT}")
    print(f"Claim register template: {CLAIM_REGISTER}")
    print(f"Source log template: {SOURCE_LOG}")


if __name__ == "__main__":
    main()
