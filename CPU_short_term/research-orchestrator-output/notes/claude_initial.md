# Initial Research Memo — CPU "Agentic AI" Short-Term Trade in INTC / AMD

**Author role:** Skeptical researcher (adversarial, correction-seeking)
**Date:** 2026-04-26
**Holding period scope:** < 3 months
**Allocation cap:** < 5% portfolio

---

## 0. Critical Disclosure on Data Access

I do **not** have live market data, real-time quotes, current analyst notes, options chains, or post-cutoff earnings transcripts in this session. My training horizon ends January 2026; today is 2026-04-26, so roughly 3+ months of price action, earnings, and analyst flow that are central to this trade are **not directly verifiable from my context**. Any specific number for "1W / 1M / 3M move," "current short interest," or "next earnings date" must be marked **UNSUPPORTED** until a tooled agent fetches it. I will reason structurally and call out exactly which inputs the next agent must pull.

This is the single biggest weakness of any memo I write here. The user should weight my structural reasoning more than any number I cite.

---

## 1. Executive Thesis

The "CPU story for agentic AI" is **mostly narrative-grade, not fundamental-grade**, and is a structurally weaker thematic trade than DRAM/HBM or CPO. INTC and AMD likely move together on this narrative even though their underlying exposures are very different — INTC's recent strength (if any) is more plausibly explained by turnaround/foundry/government and short-covering than by CPU-AI demand; AMD's strength is more credibly tied to **GPU** (MI300/MI325/MI350) and EPYC share gains, not a distinct "agentic CPU" story.

**Initial verdict (to be debated):** Watchlist, not buy now. Skip if no clean entry. AMD is the only defensible vehicle if forced to choose; INTC is a higher-beta narrative/turnaround proxy, not a CPU-AI play. The trade is **weaker than the recent DRAM and CPO trades** because the direct AI revenue link is thin.

**Confidence:** Low–Medium (structural reasoning is solid, but real-time setup unverified).

---

## 2. Scope and Definitions

- **"CPU story for agentic AI":** the claim that the rise of multi-step agentic workloads (planning, tool use, orchestration, long context) increases incremental demand for general-purpose server CPUs (Xeon / EPYC), host CPUs in GPU servers, or client AI CPUs, in a way that should re-rate INTC/AMD over the next 1–3 months.
- **Trade:** common stock, < 5% allocation, < 3 month hold, momentum/catalyst-driven, exit on thesis break.
- **Out of scope:** long-term INTC turnaround, AMD vs NVDA AI accelerator share, foundry economics beyond their effect on a 3-month tape.

I will reject the lazy framing "AI needs more CPUs" and force every claim into a testable form below.

---

## 3. Research Universe / Options Considered

Vehicles considered for this thematic trade:
1. **AMD common stock** — primary candidate. Direct CPU + GPU exposure.
2. **INTC common stock** — narrative beneficiary, weak fundamental link to *agentic* CPU demand.
3. **Both 50/50** — diversifies single-name risk; dilutes thesis purity.
4. **Pair: long AMD / short INTC** — if you believe the CPU-AI thesis is real, AMD is the share-gainer. Out of scope per "common shares" preference but worth flagging.
5. **Sector ETF (SOXX/SMH)** — benchmark; if the trade's edge over SMH isn't clear, the trade fails the "meaningfully better than ETF" test.
6. **Adjacent thematic alternatives** — DRAM (MU, SK Hynix ADR proxies), HBM, CPO names (e.g. networking optics), AI server ODMs, power/cooling. Mentioned because the user explicitly asked for relative comparison.
7. **Options (calls, call spreads)** — only if IV is reasonable and the catalyst window is defined; without live IV data this is a hypothetical.
8. **Skip / wait for pullback** — always on the table.

Omissions explained: I do not include Arm Holdings (ARM) despite obvious CPU relevance because the user specified INTC and AMD; ARM would be a separate trade with different drivers. NVDA is excluded because it is a GPU, not CPU, story and is the implicit benchmark this trade is trying to "catch up to."

---

## 4. Evidence Map

| Domain | What I can reason about structurally | What requires live data | Pre-tool confidence |
|---|---|---|---|
| Recent price action (1W/1M/3M) | Direction plausibility only | Exact returns, volume, RS vs SMH | UNSUPPORTED |
| Earnings dates | Approximate quarterly cadence | Exact April/May 2026 dates and consensus | UNSUPPORTED |
| Server CPU share | AMD has been gaining EPYC share through 2024–2025; trend likely intact | Latest Mercury/IDC quarterly print | Medium |
| AI host-CPU pull-through | Each AI server uses ~2 host CPUs; ratio fixed | Actual ASP/mix data | Medium |
| Agentic workload CPU intensity | Plausible but unproven that "agentic" workloads materially shift CPU demand | Hyperscaler commentary, MLPerf-style benchmarks | Low |
| AI PC / client CPU demand | Has been narrative-heavy, demand-light through 2025 | Q1 2026 PC unit data, ASP mix | Low–Medium |
| INTC turnaround status | Lip-Bu Tan era, foundry split-out discussion ongoing as of late 2025 | Latest 18A yield/customer commitments | Low–Medium |
| Short interest / options positioning | Cannot infer | Live data required | UNSUPPORTED |
| Analyst flow | Cannot infer post-Jan 2026 | Live data required | UNSUPPORTED |

---

## 5. Key Facts and Sources

Facts I am willing to assert at Medium+ confidence based on training data through Jan 2026:

- **F1.** AMD has been gaining server CPU revenue share from Intel for multiple consecutive years through 2024–2025. *Source: Mercury Research quarterly server CPU share reports cited widely in financial press through 2025.* Confidence: Medium-High.
- **F2.** AI accelerator (GPU) capex by hyperscalers has dwarfed incremental server CPU spend in 2024–2025; the CPU/GPU dollar ratio in AI servers has *declined*, not risen. *Source: hyperscaler capex disclosures, NVDA data center revenue trajectory.* Confidence: High.
- **F3.** Each NVIDIA HGX/DGX-class AI server typically pairs 2 host CPUs (often EPYC, sometimes Xeon) with 8 GPUs, so CPU unit demand grows with AI server units, but at a much smaller dollar contribution per server. *Source: public NVIDIA reference architectures.* Confidence: High.
- **F4.** Intel's data center group has structurally underperformed AMD's in growth and margin from 2022 through 2025. *Source: 10-Q segment disclosures.* Confidence: High.
- **F5.** "Agentic AI" as a market narrative accelerated meaningfully in H2 2024 through 2025; whether it has produced *measurable* incremental CPU revenue at INTC/AMD is **unconfirmed** in any guidance I can recall. Confidence: Medium that the narrative exists; Low that revenue is identifiable.
- **F6.** DRAM/HBM has a *direct, contracted* revenue link to AI training (HBM3/3E ships into every H100/H200/B100/B200/MI300 class accelerator), providing visibility CPU lacks. *Source: Micron, SK Hynix, Samsung disclosures and NVDA BoM analyses.* Confidence: High.
- **F7.** CPO / co-packaged optics narrative is grounded in real cluster-scaling bottlenecks at 800G/1.6T networking — a more concrete demand mechanism than "CPUs for agents." Confidence: Medium-High.

Everything below this line about the *current trade setup* — recent price moves, near-term catalysts, options positioning — is **UNSUPPORTED** in this memo and must be filled in by a tool-using agent.

---

## 6. Main Drivers / Causal Mechanisms (Decomposed)

Re-stating the "CPU story" as testable claims:

| Claim ID | Mechanism | Plausibility | Direct revenue link to INTC/AMD next 3M? |
|---|---|---|---|
| M1 | Agentic workloads use more CPU cycles per inference (orchestration, tool calls, memory) | Plausible at workload level, but inference cost is still GPU-dominated by 1–2 orders of magnitude | Weak |
| M2 | More AI servers ⇒ more host CPUs (fixed 2:8 ratio) | Mechanically true, already in numbers | Already priced; not a new catalyst |
| M3 | Inference shifts to CPU for small/edge models | Plausible long-term, weak in 3M window | Very weak |
| M4 | AI PC refresh cycle for client CPUs (Lunar Lake, Strix/Strix Halo) | Plausible but PC unit data has disappointed in 2024–2025 | Weak–Medium |
| M5 | Hyperscaler general-purpose server refresh accelerates alongside AI buildout | Real; AMD has been the bigger beneficiary | Medium for AMD, Low for INTC |
| M6 | Sovereign / enterprise on-prem AI infra drives Xeon/EPYC | Long lead times, lumpy, hard to time in 3M | Weak |
| M7 | INTC turnaround / foundry / government support / takeover chatter | Real driver of INTC tape but **not a CPU-AI story** | Strong for INTC tape, irrelevant to thesis |

**Skeptical observation:** Most of what is being sold as "CPU-AI story" for INTC is actually M7 (turnaround/government/foundry) wearing an AI costume. If the next agent claims the CPU-AI narrative is "real" for INTC, this is the first claim I will challenge.

---

## 7. Counterarguments and Disconfirming Evidence

1. **GPU still eats the AI dollar.** Hyperscaler capex 2024–2025 shows accelerator spend growing faster than server CPU spend. If the CPU-AI thesis were real, we'd expect the CPU-to-GPU revenue ratio to be *rising*. It is not. (F2)
2. **Agentic workloads don't change the silicon mix at the rack level.** Agent orchestration runs on CPUs that are already provisioned in every AI server. There is no obvious step-function in CPU dollar content per AI server.
3. **AI PC has consistently disappointed.** The "AI PC" narrative has been promoted heavily since 2024 and has not produced unit/ASP upside meaningful enough to move INTC client revenue. Re-using it now under a new "agentic" label is suspect.
4. **INTC and AMD are not the same trade.** Lumping them risks the investor buying INTC for a thesis that only AMD plausibly satisfies. INTC's recent moves (when they happen) are typically explained by short squeezes, M&A/foundry headlines, or government — none of which are durable for 3-month momentum trades.
5. **Crowding risk.** If the narrative is loud enough to be in retail/financial-media discourse, the easy money is likely already made. The user explicitly wants to avoid chasing.
6. **The DRAM and CPO comps are unfavorable.** Both have cleaner, contracted, near-term AI revenue linkage (F6, F7). "CPU for agentic" lacks a billing-cycle mechanism that converts narrative to revenue inside 90 days.
7. **Macro tail risk.** A Nasdaq drawdown or AI-capex scare hits high-beta semis hardest. INTC/AMD positions in a sector unwind would lose more than SMH.

---

## 8. Bull Case (Strongest Positive Interpretation)

- AMD prints a Q1 2026 beat-and-raise driven by EPYC share gains *and* MI3xx ramp, with management language explicitly tying agentic/inference workloads to platform pull-through. The stock gaps and runs into mid-year on momentum + index flows.
- INTC catches a sympathy bid plus a discrete catalyst (foundry customer announcement, government package, takeover/strategic action, 18A yield update). Short covering amplifies.
- Sector rotation into laggard semis broadens; SMH outperforms; INTC/AMD outperform SMH because of "catch-up" framing.
- Options positioning is light enough that a momentum impulse is not immediately faded.

In this scenario, AMD +15–25% and INTC +20–40% over 8–12 weeks are conceivable. The trade works.

**This case requires a real catalyst, not narrative alone.** Without an earnings beat or discrete event, the bull case collapses to "momentum continuation," which is precisely what the user said they want to avoid chasing.

---

## 9. Bear Case (Strongest Negative Interpretation)

- The "CPU agentic" story is a media construct draped over what is really an INTC turnaround story and an AMD GPU story. It fails to attract incremental institutional money once examined.
- AMD reports in-line, raises modestly; the stock is sold on "not enough" because the bar is high after a run. Classic post-earnings semis fade.
- INTC reports messy quarter (foundry losses, DCAI weak), retraces sharply. Short squeeze unwinds.
- A Nasdaq drawdown or hyperscaler capex pause (any soft commentary from MSFT/META/GOOG/AMZN) hits AI-beta and the trade is stopped out within 2 weeks.
- DRAM/HBM and CPO continue to outperform, drawing thematic capital away from the CPU narrative.

Downside in 3M: AMD -15–25%, INTC -20–35%, with high correlation in a risk-off semis tape.

---

## 10. Base Case (Most Likely Interpretation)

- AMD: choppy, range-bound to modestly higher; outperforms INTC; reaction to Q1 2026 print is the dominant 3M variable. Without a clearly bullish print, return is roughly SMH-like with higher volatility.
- INTC: dominated by non-AI catalysts (foundry, government, M&A chatter, cost cuts). The CPU-AI narrative contributes maybe 10–20% of the explanation for any rally; the rest is turnaround beta.
- The CPU-AI theme **does not** independently produce a clean 3-month momentum move comparable to the DRAM or CPO trades.

**Base-case verdict:** Watchlist. Trade only on confirmed setup (earnings beat with raised guide, or a clean technical breakout on volume after a pullback). Default action: **do not chase**.

---

## 11. Key Claims Table

| ID | Claim | Subject | Category | Source | Confidence | Status |
|---|---|---|---|---|---|---|
| C1 | AMD gained server CPU share from Intel through 2024–2025 | AMD/INTC | Confirmed fact | Mercury Research (industry standard) | Medium-High | Accept pending live update |
| C2 | AI server CPU dollar content is declining as a % of AI server BoM | Industry | Confirmed fact | Hyperscaler capex disclosures, NVDA references | High | Accept |
| C3 | "Agentic AI" measurably increases server CPU revenue at INTC/AMD | Both | Narrative | None I can cite | Low | UNSUPPORTED — challenge required |
| C4 | INTC's recent share strength (if any) is primarily a CPU-AI story | INTC | Narrative | None | Low | UNSUPPORTED — likely false; turnaround/foundry is dominant |
| C5 | AMD's data center growth is more GPU-driven than CPU-driven currently | AMD | Inference from disclosures | AMD segment guidance through 2025 | Medium-High | Accept |
| C6 | DRAM/HBM has a stronger direct AI revenue link than CPU | Comp | Confirmed fact | Micron/SK Hynix/Samsung disclosures | High | Accept |
| C7 | CPO has a more concrete near-term demand mechanism than CPU-agentic | Comp | Analyst consensus | Networking analyst commentary 2024–2025 | Medium | Accept tentatively |
| C8 | AI PC has under-delivered relative to narrative through 2025 | INTC | Confirmed fact | PC OEM/IDC data | Medium-High | Accept |
| C9 | Recent INTC and AMD price moves over 1W/1M/3M | Both | Market data | Live quote required | UNSUPPORTED | Must be fetched |
| C10 | Next earnings dates within the 3M window | Both | Calendar | IR pages | UNSUPPORTED | Must be fetched |
| C11 | Short interest / options positioning suggests squeeze setup | Both | Market data | Live data required | UNSUPPORTED | Must be fetched |
| C12 | The trade is comparable in strength to recent DRAM trade | Comp | Judgment | Reasoned | Medium-Low | Tentative: weaker than DRAM |
| C13 | The trade is comparable in strength to recent CPO trade | Comp | Judgment | Reasoned | Medium-Low | Tentative: weaker than CPO |
| C14 | Allocation < 5% with < 3M hold makes options possibly more efficient if IV is reasonable | Construction | Judgment | Reasoned | Low without IV data | UNSUPPORTED on IV |

---

## 12. Evidence Gaps (Must Be Closed Before Trading)

1. **Actual price action** for INTC and AMD over 1W / 1M / 3M, with volume and RS vs SMH/SOXX/QQQ/SPY.
2. **Next earnings dates and consensus** for both. The trade only makes sense if a catalyst falls inside the 3M window.
3. **Recent (post-Jan 2026) analyst commentary** specifically tying agentic AI to CPU revenue, not just AI generally.
4. **Hyperscaler capex commentary from the most recent earnings round** (MSFT/META/GOOG/AMZN) — especially any quoted CPU vs GPU mix language.
5. **Short interest and options skew/IV** — needed to gauge squeeze potential and to choose shares vs options vs spreads.
6. **Latest server CPU share data** (Mercury) — to confirm AMD share gains are still intact.
7. **Any concrete news catalysts** on INTC foundry/government/M&A in the past 90 days that might explain price action and that I would otherwise misattribute to a CPU-AI narrative.
8. **Sector flow data** — is money rotating *into* INTC/AMD or *into* DRAM/CPO/networking? If the latter, the CPU trade is the laggard pick in a stronger thematic field.
9. **Technical levels** — recent breakout/breakdown levels and prior consolidation zones for invalidation rules.
10. **MI350/MI400 roadmap timing** — relevant to AMD's separate (non-CPU) AI catalyst stack.

---

## 13. Initial Classification / Ranking

| Ticker / Construct | Initial Label | Reason |
|---|---|---|
| **AMD common, full position now** | Watchlist | Best vehicle for the thesis, but entry/catalyst unverified; risk of chasing |
| **AMD on confirmed pullback + earnings beat** | Strong candidate | Cleanest setup if conditions met |
| **INTC common, full position now** | Avoid | CPU-AI thesis is weakest here; recent strength likely turnaround/short-cover; high single-name event risk |
| **INTC on discrete non-AI catalyst (foundry/M&A)** | Watchlist (different thesis) | Not a CPU-AI trade; should be re-scoped |
| **Both 50/50** | Avoid | Conflates two different theses; adds INTC-specific risk for no extra thematic exposure |
| **Skip / SMH instead** | Strong candidate as benchmark | If edge over SMH not demonstrable, this is the right action |
| **Long AMD / short INTC pair** | Out of stated scope but interesting | Cleanest expression if user relaxes "common shares" |

**Headline classification: Watchlist.** I refuse to issue a "Strong candidate" label for either name without live setup data. I will not call it "Avoid" outright either, because AMD on a clean post-earnings setup could legitimately be a Strong candidate.

---

## 14. What Must Be Verified Next

In priority order — the next agent (or tooled run) should:

1. Pull **INTC and AMD 1W/1M/3M returns**, volume, and relative strength vs SMH/SOXX/QQQ. Without this, every "is it late?" question is unanswerable.
2. Pull **next earnings dates and consensus EPS/rev** for both inside the 3M window. No catalyst inside the window ⇒ trade is purely momentum.
3. Search for **post-Jan 2026 analyst notes or company commentary** explicitly tying *agentic AI* to *CPU* revenue (not generic AI). If no credible source does this, claim C3 must be marked Unsupported and the entire thesis downgraded.
4. Pull **most recent hyperscaler capex commentary** for any CPU-mix language.
5. Pull **short interest, options IV, 25-delta skew** for INTC and AMD. Determines vehicle choice.
6. Pull **latest Mercury server CPU share** print to confirm or deny AMD share gain trajectory.
7. Identify **discrete INTC non-AI catalysts in the last 90 days** to correctly attribute INTC tape action.
8. Compare 3M returns of **DRAM / HBM names (MU, SK Hynix proxies), CPO names, AI networking names** to INTC/AMD to verify the relative strength claim that CPU is the *weaker* thematic.
9. Identify any **upcoming AI / data center events** (Computex, Hot Chips, hyperscaler events, Intel/AMD investor days) inside the 3M window.
10. Establish **clean technical levels** for entry/invalidation on both names.

Once these are filled in, I will be ready to challenge any opposing agent's specific numerical claims, force them to mark unsupported items, and either upgrade AMD to Strong candidate or push the entire trade to Avoid.

---

## Final Classification

**Watchlist** — leaning Avoid for INTC standalone, leaning conditional Strong candidate for AMD only with confirmed setup. The CPU/agentic AI narrative is **structurally weaker than DRAM and CPO**, and I will not treat it as comparable until shown direct revenue evidence post-Jan 2026.

**Confidence in this classification:** Medium on structural reasoning, Low on tradability without live data. The next round must close the evidence gaps in §14 before any allocation decision.