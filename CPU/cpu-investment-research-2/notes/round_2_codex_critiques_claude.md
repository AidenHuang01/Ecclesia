Updated the register and source log:
- [claim_register.md](/mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/claims/claim_register.md:21): added `CDR-17` through `CDR-27`.
- [source_log.md](/mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/sources/source_log.md:26): added `S-20` through `S-24`.

**1. Highest-Risk Errors**
1. **Intel upgrade is premature.** Confirmed fact: Intel DCAI was `$5.1B`, `+22% YoY`, and Intel says Xeon 6 is used as DGX Rubin NVL8 host CPU. Sources: [Intel Q1 2026](https://www.intc.com/news-events/press-releases/detail/1767/intel-reports-first-quarter-2026-financial-results), [Intel Rubin NVL8](https://newsroom.intel.com/data-center/intel-xeon-6-used-as-host-cpus-in-nvidia-dgx-rubin-nvl8-systems). Investment conclusion still needs volume, ASP, margin, and valuation. Confidence: **Medium-High**.
2. **“CPU equities trade as AI capex beta” is UNSUPPORTED.** That is a market-factor claim, not a business-model fact. No regression, CPU revenue bridge, or capex-to-CPU conversion model is cited. Confidence: **Low**.
3. **Claude’s “structural arguments survive at Medium confidence” bundles unlike claims.** Captive Arm substitution is directionally supported by AWS Graviton, Azure Cobalt, and Google Axion disclosures; OEM margin thinness is confirmed mainly for SMCI/Wiwynn; CPU equity beta is not confirmed. Sources: [AWS Graviton5](https://www.aboutamazon.com/news/aws/aws-graviton-5-cpu-amazon-ec2), `S-13`, `S-14`, [SMCI](https://ir.supermicro.com/news/news-details/2026/Supermicro-Announces-Second-Quarter-Fiscal-Year-2026-Financial-Results/default.aspx), [Wiwynn](https://www.wiwynn.com/news/wiwynn-reports-fourth-quarter-2025-unaudited-financial-results). Confidence: **Medium**.
4. **SMCI risk framing is stale if treated as only a 2024 accounting issue.** Supermicro disclosed an April 2026 independent-director investigation tied to an export-control indictment of former associated individuals. Source: [SMCI April 2026 update](https://ir.supermicro.com/news/news-details/2026/Supermicro-Provides-Update-on-Investigation-by-Independent-Board-Directors/default.aspx). Confidence: **High for disclosure, Unknown for financial impact**.

**2. Unsupported Claims**
| Claim | Problem | Confidence |
|---|---|---:|
| CPU equities are AI capex beta | No equity-factor evidence or CPU revenue bridge. | Low |
| Intel merits Tactical Watchlist on S-02/S-19 alone | Facts are real; investment conclusion is under-modeled. | Medium-Low |
| OEM/ODM economics are broadly margin-thin | Supported for SMCI/Wiwynn; Dell ISG operating margin is materially different. Source: [Dell FY26](https://investors.delltechnologies.com/news-releases/news-release-details/dell-technologies-delivers-fourth-quarter-and-full-year-fiscal-3). | Medium |
| Arm valuation can only be deferred | Correct process step, but incomplete without royalty dollars, Arm China, and customer concentration. Source: [Arm Q3 FYE26](https://newsroom.arm.com/news/arm-q3-fye26-results). | Medium |

**3. Questionable Assumptions**
- ARM substitution is real directionally, but displaced merchant x86 revenue is still unquantified. AWS says Graviton was more than half of new AWS CPU capacity, but that is a management claim, not a full market-share dataset. Confidence: **Medium**.
- AI server CPU attach may be lower than legacy CPU racks, but the actual CPU dollars per rack remain missing. This is still the central fatal gap. Confidence: **Unknown**.
- TSMC is confirmed as a strong AI/HPC beneficiary, but not specifically a CPU equity thesis. TSMC Q1 2026 results and management report show strong advanced-node/HPC exposure, not CPU-only revenue. Sources: [TSMC Q1 release](https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-04/bd8eb0403902fdea59a2f5e390e48d010b50edc9/1Q26%20EarningsRelease_WoG.pdf), [TSMC Q1 management report](https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-04/9f060092ba29ff3630cfdaefd67774026195e135/1Q26ManagementReport.pdf). Confidence: **Medium**.

**4. Missing Evidence**
- CPU dollars per rack: legacy 2S x86, GB200/GB300, DGX Rubin NVL8, MI300/MI350/MI400, Trainium, TPU, Maia.
- AMD EPYC-only revenue and growth; AMD Data Center includes EPYC and Instinct. Source: [AMD FY2025](https://www.amd.com/en/newsroom/press-releases/2026-2-3-amd-reports-fourth-quarter-and-full-year-2025-fina.html).
- Xeon product mix, ASP, and DCAI operating margin.
- Independent server CPU unit/revenue share from Mercury, IDC, Omdia, or Gartner.
- Arm royalty dollars per server CPU/core.
- OEM/ODM AI server backlog terms, cancellation risk, and margin by configuration.
- Full valuation model for AMD, Intel, Arm, TSMC, Dell, SMCI.

**5. Company-Specific Objections**
- **AMD:** Data Center growth is not EPYC-only; CPU thesis still needs EPYC/Instinct split. Confidence: **High fact / Medium-Low inference**.
- **Intel:** Better than “Avoid,” but Tactical Watchlist needs proof that DCAI growth is durable and profitable. Confidence: **Medium-Low**.
- **Arm:** Deferring valuation is right, but adoption share without royalty economics is not investable. Confidence: **Medium**.
- **Qualcomm:** Avoid for CPU-pure thesis is reasonable, but option value is not zero; 10-K confirms data-center intent and custom CPU cores, while Centriq shows prior execution risk. Sources: [Qualcomm 10-K](https://www.sec.gov/Archives/edgar/data/0000804328/000080432825000085/qcom-20250928.htm), [Centriq launch](https://www.qualcomm.com/news/releases/2017/11/qualcomm-datacenter-technologies-announces-commercial-shipment-qualcomm).
- **SMCI/Wiwynn:** Margin evidence is bearish, not neutral. SMCI Q2 FY26 GM was 6.3%; Wiwynn Q4 2025 GM was 7.2%. Sources: `S-08`, `S-09`.
- **Broadcom/Marvell:** Keep as substitution and relative-return benchmarks, not CPU longs. Sources: [Broadcom FY25](https://investors.broadcom.com/news-releases/news-release-details/broadcom-inc-announces-fourth-quarter-and-fiscal-year-2025), [Marvell FY26](https://investor.marvell.com/news-events/press-releases/detail/1011/marvell-technology-inc-reports-fourth-quarter-and-fiscal-year-2026-financial-results).

**6. Revised Ranking**
| Rank | Companies | View |
|---|---|---|
| Strong CPU-pure candidate | None | Fatal evidence gaps remain. |
| Qualified / needs model | TSMC, AMD, Dell, Intel | Real exposure, but CPU conversion or valuation unresolved. |
| Deferred | Arm | Technology exposure confirmed; valuation and royalty model absent. |
| Benchmark / substitution | Broadcom, Marvell, NVIDIA | Useful comparables, not CPU-pure longs. |
| Avoid for CPU-pure thesis | Qualcomm, HPE, SMCI, Wiwynn, Quanta, Inventec, Lenovo | Either indirect, low-margin, or insufficient CPU economics. |

**7. Claim Challenges Table**
| Claim ID | Problem | Severity | Suggested Fix | Status |
|---|---|---|---|---|
| CDR-17 | AI capex beta claim lacks evidence. | Fatal | Run factor regression and CPU revenue bridge. | Added / Open |
| CDR-18 | Arm substitution not quantified. | Major | Estimate displaced sockets and revenue by hyperscaler. | Added / Open |
| CDR-19 | OEM margin claim overgeneralized. | Major | Split SMCI, Wiwynn, Dell, Quanta, Inventec. | Added / Open |
| CDR-20 | Intel upgrade under-modeled. | Major | Add DCAI 2-year stack, ASP, mix, margin, valuation. | Added / Open |
| CDR-21 | Arm deferral incomplete. | Major | Add royalty-dollar and valuation model. | Added / Open |
| CDR-23 | CPU dollars per rack missing. | Fatal | Build rack BOM/attach table. | Added / Open |
| CDR-24 | TSMC CPU read-through overbroad. | Major | Separate AI/HPC foundry thesis from CPU thesis. | Added / Open |
| CDR-27 | SMCI risk framing stale. | Major | Update for April 2026 investigation. | Added / Open |

**8. Required Follow-Up Research**
1. Build CPU-dollar-per-rack table; this is the evidence that would most change my view.
2. Pull Mercury/IDC/Omdia server CPU share through Q1 2026.
3. Build AMD EPYC-only and Intel Xeon-only revenue estimates.
4. Channel-check server CPU ASPs; keep price-hike rumors out of base case until verified.
5. Build valuation snapshots for AMD, Intel, Arm, TSMC, Dell, SMCI.
6. Quantify Graviton/Cobalt/Axion displacement of merchant x86.
7. Update SMCI governance/export-control risk status before any quality ranking.

--- STDERR ---

Reading prompt from stdin...
OpenAI Codex v0.125.0 (research preview)
--------
workdir: /mnt/c/Users/hyc97/workspace/Ecclesia/CPU
model: gpt-5.5
provider: openai
approval: never
sandbox: workspace-write [workdir, /tmp, $TMPDIR, /home/yucheng/.codex/memories]
reasoning effort: xhigh
reasoning summaries: none
session id: 019dc85e-8fd5-75c3-9f06-071c7cbb07de
--------
user
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
- Full transcript: cpu-investment-research-2/transcript/full_debate.md
- Claim register: cpu-investment-research-2/claims/claim_register.md
- Source log: cpu-investment-research-2/sources/source_log.md

        Role:
        You are Codex, acting as an opposing investment analyst.

        You are reviewing Claude's research from round 2.

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
        (Note: write permission to `claim_register.md` was not granted, so CDR-17 through CDR-25 above are proposed rows for the next register update — the round-2 revisions remain captured in this response.)

---

**Closing**: The Codex critique correctly forced me to separate **structural bear arguments** (CPU equities trade as AI capex beta; merchant x86 faces real captive-ARM substitution at hyperscalers; OEM/ODM AI-server economics are margin-thin where confirmed) from **bear quantifications I had no source for** (3–7% BOM, sub-20% EPYC growth, Sierra Forest mix). The structural arguments survive at Medium confidence; the quantifications are withdrawn. The most material verdict change is **Intel: Avoid → Tactical Watchlist (bear bias)** on the strength of S-02 and S-19, and **Arm: Avoid → Verdict deferred** because I cannot defend the valuation claim without a model.
        ```

codex
I’ll inspect the existing transcript, claim register, and source log first so the critique keys off the project’s current evidence base instead of the short excerpt alone. Then I’ll verify the highest-risk market and company claims against current primary or clearly labeled secondary sources.
exec
/usr/bin/zsh -lc "sed -n '1,220p' cpu-investment-research-2/claims/claim_register.md" in /mnt/c/Users/hyc97/workspace/Ecclesia/CPU
exec
/usr/bin/zsh -lc 'wc -l cpu-investment-research-2/transcript/full_debate.md cpu-investment-research-2/claims/claim_register.md cpu-investment-research-2/sources/source_log.md' in /mnt/c/Users/hyc97/workspace/Ecclesia/CPU
exec
/usr/bin/zsh -lc "sed -n '1,260p' cpu-investment-research-2/sources/source_log.md" in /mnt/c/Users/hyc97/workspace/Ecclesia/CPU
 succeeded in 208ms:
# Claim Register

| ID | Claim | Company | Category | Source | Confidence | Challenged By | Status |
|---|---|---|---|---|---|---|---|
| CDR-01 | CPU silicon is only 3-7% of AI server BOM / <5% of GB200-class rack BOM. | Industry | BOM / pricing | Claude round 1; no primary teardown cited | Low | Codex round 1 opposition | UNSUPPORTED; fatal to bear thesis until platform-level BOM is sourced |
| CDR-02 | 60-70% of incremental hyperscaler compute capex flows into accelerated systems. | Industry | Capex allocation | Claude round 1 assumption | Low | Codex round 1 opposition | UNSUPPORTED; needs capex-to-server architecture bridge |
| CDR-03 | Merchant x86 competes for a shrinking slice of incremental cloud CPU capacity. | AMD / Intel | Market share | S-10, S-11, S-13, S-14 support ARM adoption directionally; no independent share series cited | Medium-Low | Codex round 1 opposition | PARTIALLY SUPPORTED; requires Mercury/IDC/Omdia unit, revenue, and core-hour share |
| CDR-04 | Nvidia AI rack architecture means ARM CPU displacement for x86. | Nvidia / Intel / AMD / Arm | Architecture | S-12 confirms GB200/GB300 use Grace Arm; S-19 confirms Xeon 6 host CPU in DGX Rubin NVL8 | Medium | Codex round 1 opposition | OVERBROAD; split by platform rather than treating all Nvidia systems as ARM-hosted |
| CDR-05 | Custom ASIC racks have the lowest CPU intensity and are directly subtractive to merchant CPU vendors. | Broadcom / Marvell / hyperscalers | Substitution risk | Claude round 1; no TPU/Trainium/MAIA host-CPU counts cited | Low | Codex round 1 opposition | UNSUPPORTED; needs architecture attach data |
| CDR-06 | AMD EPYC growth is probably sub-20%, with Instinct doing the heavy lifting. | AMD | Revenue mix | S-01 confirms Data Center includes EPYC and Instinct but not the split | Low | Codex round 1 opposition | UNSUPPORTED; do not use without EPYC/Instinct triangulation |
| CDR-07 | Intel DCAI Q1 2026 strength may be mostly Sierra Forest mix / easy comp / low ASP host CPUs. | Intel | Revenue quality / ASP | S-02 confirms DCAI +22%; mix explanation is Claude inference | Low | Codex round 1 opposition | UNSUPPORTED; needs Intel product mix, ASP, and gross margin evidence |
| CDR-08 | Server-system ASP inflation is not CPU ASP inflation. | Industry | Pricing | S-15 confirms system ASP +92.8%; CPU ASP split unavailable | Medium-High | Codex round 1 opposition | VALID CAVEAT; needs CPU-specific price dataset before bullish or bearish pricing claims |
| CDR-09 | 10-20% server CPU price hikes since March 2026. | Intel / AMD | Pricing | Secondary press / channel rumor; no company confirmation in register | Low | Codex round 1 opposition | MARKET RUMOR; do not model as fact |
| CDR-10 | Arm royalty per server CPU is low single-digit percentage of CPU ASP. | Arm | Unit economics | Claude round 1; no contract / AALA / CSS economics cited | Low | Codex round 1 opposition | UNSUPPORTED; needs royalty-dollar model |
| CDR-11 | Arm Holdings is an Avoid on valuation because the multiple is extreme. | Arm | Valuation | Claude round 1; no current multiple table or DCF cited | Unknown | Codex round 1 opposition | UNSUPPORTED; needs price, share count, forward revenue/EPS/FCF scenarios |
| CDR-12 | TSMC is priced for AI upside. | TSMC | Valuation | Claude round 1; no valuation comp table cited | Unknown | Codex round 1 opposition | UNSUPPORTED; needs valuation and scenario analysis |
| CDR-13 | OEM/ODM gross margins will remain 6-10% and not recover. | SMCI / Wiwynn / Dell / Quanta / Inventec | Margin | S-08 and S-09 support SMCI/Wiwynn low recent GM; Dell evidence in S-07 is more mixed | Medium-Low | Codex round 1 opposition | OVERGENERALIZED; split by company, product mix, and operating margin |
| CDR-14 | Dell is the highest-quality OEM and the only OEM worth Watchlist status. | Dell / OEMs | Ranking / quality | S-07 supports explicit AI orders/backlog and ISG growth; no peer valuation/quality scorecard cited | Medium-Low | Codex round 1 opposition | PARTIALLY SUPPORTED; needs peer scorecard and AI-server margin disclosure |
| CDR-15 | Broadcom and Marvell should be excluded from the CPU framework. | Broadcom / Marvell | Universe definition | S-16 and S-17 confirm AI custom silicon / data center exposure, not CPU revenue | Medium | Codex round 1 opposition | TOO NARROW; exclude from pure CPU revenue, include as substitution and relative-return benchmarks |
| CDR-16 | Hyperscaler capex may decelerate in 2H26 and hit OEM/ODM and merchant CPU first. | Industry | Cycle risk | Claude round 1 scenario; S-03, S-04, S-05, S-06 show high 2026 capex guidance | Low | Codex round 1 opposition | UNSUPPORTED SCENARIO; retain as bear case only |

 succeeded in 208ms:
# Source Log

Use this file to track source URLs, filings, earnings calls, market data sources, and unresolved evidence gaps.

| ID | Source | Type | Date | Used For | Reliability |
|---|---|---|---|---|---|
| S-01 | https://www.amd.com/en/newsroom/press-releases/2026-2-3-amd-reports-fourth-quarter-and-full-year-2025-fina.html | Company earnings release | 2026-02-03 | AMD FY2025 Data Center revenue; EPYC + Instinct disclosure issue | High |
| S-02 | https://www.intc.com/news-events/press-releases/detail/1767/intel-reports-first-quarter-2026-financial-results | Company earnings release | 2026-04-23 | Intel Q1 2026 DCAI revenue, management CPU demand framing, DGX Rubin NVL8 business highlight | High |
| S-03 | https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q2 | Company earnings call transcript | 2026-01-28 | Microsoft FY26 Q2 capex and GPUs/CPUs wording | High |
| S-04 | https://abc.xyz/investor/events/event-details/2026/2025-Q4-Earnings-Call-2026-Dr_C033hS6/default.aspx | Company earnings call transcript | 2026-02-04 | Alphabet 2026 capex guide and server/data-center allocation commentary | High |
| S-05 | https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Fourth-Quarter-Results/default.aspx | Company earnings release | 2026-02-05 | Amazon 2026 capex guide | High |
| S-06 | https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Fourth-Quarter-and-Full-Year-2025-Results/ | Company earnings release | 2026-01-28 | Meta 2026 capex guide | High |
| S-07 | https://investors.delltechnologies.com/news-releases/news-release-details/dell-technologies-delivers-fourth-quarter-and-full-year-fiscal-3 | Company earnings release | 2026-02-26 | Dell FY26 AI server orders, shipments, backlog, ISG revenue and operating income | High |
| S-08 | https://ir.supermicro.com/news/news-details/2026/Supermicro-Announces-Second-Quarter-Fiscal-Year-2026-Financial-Results/default.aspx | Company earnings release | 2026-02-03 | Supermicro Q2 FY2026 revenue and gross margin | High |
| S-09 | https://www.wiwynn.com/news/wiwynn-reports-fourth-quarter-2025-unaudited-financial-results | Company unaudited financial release | 2026-03-03 | Wiwynn Q4 2025 gross margin, FY2025 revenue growth, AI product mix | Medium-High |
| S-10 | https://newsroom.arm.com/news/arm-q3-fye26-results | Company earnings summary | 2026-02-04 | Arm Q3 FYE26 revenue, royalty growth, Neoverse cores, top-hyperscaler share management claim | Medium-High |
| S-11 | https://www.aboutamazon.com/news/aws/aws-graviton-5-cpu-amazon-ec2/ | Company product announcement | 2025-12-04 | AWS Graviton share of new AWS CPU capacity | High for management claim |
| S-12 | https://www.nvidia.com/en-us/data-center/gb200-nvl72/ | Company product page | 2026 crawled | NVIDIA GB200/GB300 Grace CPU counts and Arm architecture | High |
| S-13 | https://azure.microsoft.com/en-us/blog/azure-cobalt-100-based-virtual-machines-are-now-generally-available/ | Company product announcement | 2024-10-16 | Microsoft Cobalt 100 GA and Arm-based Azure VM details | High |
| S-14 | https://cloud.google.com/products/axion | Company product page | 2026 crawled | Google Axion custom Arm CPU and C4A/N4A instance details | High |
| S-15 | https://www.gartner.com/en/documents/6998066 | Market research summary | 2025-09-26 | 2Q25 server shipments, vendor revenue, server-system ASP | Medium; paywalled analyst estimate |
| S-16 | https://investors.broadcom.com/news-releases/news-release-details/broadcom-inc-announces-fourth-quarter-and-fiscal-year-2025 | Company earnings release | 2025-12-11 | Broadcom Q4 FY2025 AI semiconductor growth and AI revenue guide | High |
| S-17 | https://investor.marvell.com/news-events/press-releases/detail/1011/marvell-technology-inc-reports-fourth-quarter-and-fiscal-year-2026-financial-results | Company earnings release | 2026-03-05 | Marvell FY2026 revenue growth and data center share of revenue | High |
| S-18 | https://www.sec.gov/Archives/edgar/data/0000804328/000080432825000085/qcom-20250928.htm | SEC 10-K | 2025-11-05 | Qualcomm Oryon/data center product intent and segment context | High |
| S-19 | https://newsroom.intel.com/data-center/intel-xeon-6-used-as-host-cpus-in-nvidia-dgx-rubin-nvl8-systems | Company product announcement | 2026-03-16 | Intel Xeon 6 host CPU role in NVIDIA DGX Rubin NVL8 systems | High for Intel claim |

 succeeded in 219ms:
  3775 cpu-investment-research-2/transcript/full_debate.md
    20 cpu-investment-research-2/claims/claim_register.md
    25 cpu-investment-research-2/sources/source_log.md
  3820 total

codex
The current register already contains 16 challenged claims, mostly from round 1. I’m going to locate the round-2 section in the transcript and the proposed CDR-17 through CDR-25 rows so I can turn them into concrete register updates rather than re-litigating only the excerpt.
exec
/usr/bin/zsh -lc 'rg -n "CDR-17|round 2|Round 2|Closing|proposed rows|Tactical Watchlist|Verdict deferred|Avoid" cpu-investment-research-2/transcript/full_debate.md' in /mnt/c/Users/hyc97/workspace/Ecclesia/CPU
exec
/usr/bin/zsh -lc 'tail -n 260 cpu-investment-research-2/transcript/full_debate.md' in /mnt/c/Users/hyc97/workspace/Ecclesia/CPU
 succeeded in 198ms:

--- STDERR ---

Reading prompt from stdin...
OpenAI Codex v0.125.0 (research preview)
--------
workdir: /mnt/c/Users/hyc97/workspace/Ecclesia/CPU
model: gpt-5.5
provider: openai
approval: never
sandbox: workspace-write [workdir, /tmp, $TMPDIR, /home/yucheng/.codex/memories]
reasoning effort: xhigh
reasoning summaries: none
session id: 019dc848-47d1-72e1-a202-8ff372f21a0b
--------
user
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
- Full transcript: cpu-investment-research-2/transcript/full_debate.md
- Claim register: cpu-investment-research-2/claims/claim_register.md
- Source log: cpu-investment-research-2/sources/source_log.md

Role:
You are Codex, acting as a bullish but evidence-disciplined CPU equity researcher.

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

codex
I’ll ground the memo in the existing debate files first, then verify the time-sensitive market and company claims against current public sources before writing.
exec
/usr/bin/zsh -lc 'wc -l cpu-investment-research-2/transcript/full_debate.md cpu-investment-research-2/claims/claim_register.md cpu-investment-research-2/sources/source_log.md' in /mnt/c/Users/hyc97/workspace/Ecclesia/CPU
exec
/usr/bin/zsh -lc 'pwd && rg --files cpu-investment-research-2 | sort' in /mnt/c/Users/hyc97/workspace/Ecclesia/CPU
exec
/usr/bin/zsh -lc "sed -n '1,220p' cpu-investment-research-2/claims/claim_register.md" in /mnt/c/Users/hyc97/workspace/Ecclesia/CPU
exec
/usr/bin/zsh -lc "sed -n '1,260p' cpu-investment-research-2/sources/source_log.md" in /mnt/c/Users/hyc97/workspace/Ecclesia/CPU
 succeeded in 185ms:
/mnt/c/Users/hyc97/workspace/Ecclesia/CPU
cpu-investment-research-2/claims/claim_register.md
cpu-investment-research-2/sources/source_log.md
cpu-investment-research-2/state.json
cpu-investment-research-2/transcript/full_debate.md

 succeeded in 207ms:
  2 cpu-investment-research-2/transcript/full_debate.md
  4 cpu-investment-research-2/claims/claim_register.md
  6 cpu-investment-research-2/sources/source_log.md
 12 total

web search: 
web search: 
web search: 
web search: https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q2
web search: 
web search: 'Capital expenditures were $37.5 billion' in https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q2
web search: 
web search: 'For the full year 2026' in https://s206.q4cdn.com/479360582/files/doc_events/2026/Feb/04/2025_Q4_Earnings_Transcript.pdf
web search: 
web search: https://www.nvidia.com/en-us/data-center/gb200-nvl72/
web search: 
web search: 'Xeon 6' in https://newsroom.intel.com/data-center/intel-xeon-6-used-as-host-cpus-in-nvidia-dgx-rubin-nvl8-systems
web search: 
web search: AWS Graviton half of new CPU capacity 50% new CPU capacity Graviton 2025
web search: 
web search: https://www.amd.com/en/newsroom/press-releases/2026-2-3-amd-reports-fourth-quarter-and-full-year-2025-fina.html
web search: 
web search: 'Data Center segment revenue was' in https://www.amd.com/en/newsroom/press-releases/2026-2-3-amd-reports-fourth-quarter-and-full-year-2025-fina.html
web search: 
web search: https://newsroom.arm.com/blog/arm-compute-subsystems-css-explainer
web search: 
web search: Arm Holdings Q3 FYE26 revenue 26% royalty revenue 27% official shareholder letter pdf
web search: 
web search: TSMC CoWoS capacity 2026 bottleneck AI packaging allocation Nvidia AMD Broadcom 2026 official earnings call
web search: 
web search: site:investor.tsmc.com TSMC 4Q 2025 earnings call transcript CoWoS demand exceeds supply 2026 advanced packaging
web search: 
web search: https://www.aboutamazon.com/news/aws/aws-graviton-5-cpu-amazon-ec2
web search: 
web search: '52.4%' in https://www.idc.com/promo/servers/
web search: 
web search: Qualcomm Centriq server CPU discontinued 2018 official
web search: 
web search: HPE completes Juniper acquisition 2025 official HPE networking strategy
codex
# Round 2 Codex Revision — Response to Critique

## 1. Changes Made To Thesis

**Thesis revised downward.** I no longer treat hyperscaler capex as a direct CPU bull signal. It is a **confirmed infrastructure-demand signal**, but CPU revenue conversion is **unproven** without rack-level CPU dollars, attach rate, architecture mix, and ASP data.

**Old conclusion:** AMD, Arm, TSMC, Dell, Wiwynn as Strong candidates.  
**New conclusion:** **No unqualified Strong candidate for a CPU-pure thesis.** AMD, Intel, Arm, TSMC, and Dell remain investable candidates only with explicit caveats. Wiwynn is downgraded.

**Core revision:** AI may raise absolute CPU demand in inference and orchestration, but accelerated rack economics can reduce CPU dollars as a percentage of capex. This weakens the CPU-specific equity thesis.

Confidence: **Medium**.

## 2. Challenges Accepted

| Challenge | Disposition | Reason |
|---|---:|---|
| F1: Capex to CPU revenue chain not demonstrated | **Accept** | Central weakness. Capex is not CPU revenue. CPU dollars per rack remain missing. |
| F2: Microsoft capex wording over-interpreted | **Accept / Revise** | Microsoft says roughly two-thirds of capex was short-lived assets, primarily GPUs and CPUs, but does not disclose CPU share. Source: [Microsoft FY26 Q2 call](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q2). |
| F4: AI-server revenue can decouple from CPU sockets | **Accept** | Gartner 2Q25 shows server revenue +89.9% while shipments declined 1.5%, implying system ASP inflation is not CPU-unit growth. Source: [Gartner](https://www.gartner.com/en/documents/6998066). |
| F5: No valuation framework | **Accept** | Any “Strong candidate” label is invalid without multiples, FCF yield, EPS/FCF scenarios, or implied IRR. |
| AMD CPU-only disclosure gap | **Accept** | AMD Data Center includes EPYC CPUs and Instinct GPUs; EPYC-only growth is not disclosed. Source: [AMD FY25 results](https://www.amd.com/en/newsroom/press-releases/2026-2-3-amd-reports-fourth-quarter-and-full-year-2025-fina.html). |
| Arm royalty economics gap | **Accept** | Neoverse core deployment does not translate cleanly into royalty dollars. |
| Wiwynn margin critique | **Accept** | Q4 GM of 7.2% is not a semiconductor-like margin profile. Source: [Wiwynn Q4 2025](https://www.wiwynn.com/news/wiwynn-reports-fourth-quarter-2025-unaudited-financial-results). |
| NVIDIA / hyperscaler Arm substitution missing | **Accept** | GB200 NVL72 uses 36 Grace CPUs and 72 Blackwell GPUs; AWS says Graviton is over half of new AWS CPU capacity. Sources: [NVIDIA GB200](https://www.nvidia.com/en-us/data-center/gb200-nvl72/), [AWS Graviton5](https://www.aboutamazon.com/news/aws/aws-graviton-5-cpu-amazon-ec2). |
| HPE Juniper omission | **Accept** | HPE is now partly a networking strategy, not just server exposure. Source: [HPE Juniper close](https://www.hpe.com/us/en/newsroom/press-release/2025/07/hewlett-packard-enterprise-closes-acquisition-of-juniper-networks-to-offer-industry-leading-comprehensive-cloud-native-ai-driven-portfolio.html). |

## 3. Challenges Rejected, With Reason

| Challenge | Disposition | Reason |
|---|---:|---|
| Dell $64B / $43B figure may be false | **Reject factual challenge; accept interpretation risk** | Dell officially disclosed >$64B AI-optimized server orders, >$25B shipped, and $43B backlog. But this is AI-server revenue/order flow, not CPU revenue. Source: [Dell FY26 results](https://investors.delltechnologies.com/news-releases/news-release-details/dell-technologies-delivers-fourth-quarter-and-full-year-fiscal-3). |
| Alphabet / Meta / Amazon capex figures unsupported | **Reject factual challenge** | Official sources confirm Alphabet $175B-$185B, Meta $115B-$135B, and Amazon about $200B 2026 capex. Sources: [Alphabet transcript](https://s206.q4cdn.com/479360582/files/doc_events/2026/Feb/04/2025_Q4_Earnings_Transcript.pdf), [Meta Q4 2025](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Fourth-Quarter-and-Full-Year-2025-Results/), [Amazon Q4 2025](https://www.aboutamazon.com/news/company-news/amazon-earnings-q4-2025-report). |
| Broadcom / Marvell should be removed entirely | **Reject** | They should not be ranked as CPU plays, but they matter as substitution and relative-return benchmarks in AI infrastructure. |

## 4. Claims Revised

| Prior Claim | Revised Claim | Confidence |
|---|---|---:|
| Hyperscaler capex supports CPU upside | Hyperscaler capex supports infrastructure demand; CPU conversion is unquantified. | **Medium** |
| Microsoft two-thirds capex was GPUs/CPUs | Two-thirds was short-lived assets, primarily GPUs and CPUs; CPU slice unknown. | **High fact / Low CPU read-through** |
| Dell backlog supports CPU thesis | Dell backlog supports AI-server demand; CPU content and margin capture unknown. | **High fact / Low CPU read-through** |
| AMD is best direct CPU candidate | AMD is a qualified CPU candidate; EPYC-only revenue and share data are missing. | **Medium** |
| Intel DCAI +22% is recovery | Intel DCAI improved YoY, but “recovery” needs two-year stack and margin/ASP evidence. | **Medium-Low** |
| Arm is strong structural candidate | Arm is structurally exposed, but royalty dollars and valuation are unresolved. | **Medium** |
| Wiwynn is Strong ODM beta | Wiwynn is downgraded; growth is real but margin quality is weak. | **Medium** |

## 5. Claims Downgraded Due To Insufficient Evidence

| Claim | New Status |
|---|---|
| AI inference lifts merchant x86 CPU revenue materially | **Needs more evidence** |
| CPU attach rate rises with AI servers | **UNSUPPORTED** |
| AMD EPYC growth remains >25% | **UNSUPPORTED** |
| Intel CPU pricing tightens structurally | **UNSUPPORTED** |
| Arm hyperscaler share near 50% is independently verified | **Downgraded to management claim / Low independent confidence** |
| Server CPU price hikes of 10%-20% are real transactions | **Market rumor; exclude from base case** |
| TSMC is unconditionally bullish across all architectures | **Revised; capacity allocation and packaging constraints matter** |
| OEM/ODM AI revenue is high-quality earnings growth | **Downgraded** |

## 6. Updated Bull / Base / Bear View

**Bull Case — Low / Medium Confidence**  
Inference, agents, and cloud refresh create enough general-purpose compute demand that absolute CPU dollars grow even as CPU share of AI rack BOM falls. AMD EPYC grows faster than Intel, Intel benefits from x86 host CPU roles such as DGX Rubin NVL8, Arm royalties compound from Graviton/Cobalt/Axion/Grace/Vera, and TSMC captures the diversified silicon and packaging layer. Needs CPU-per-rack and share data.

**Base Case — Medium Confidence**  
AI capex remains strong, but CPU captures a smaller slice than GPUs, ASICs, networking, HBM, and packaging. AMD and Intel grow CPU revenue modestly, Arm gains architecture share, and TSMC remains the best diversified exposure. OEM/ODM revenue grows faster than profit.

**Bear Case — Medium Confidence**  
Accelerated racks, internal Arm CPUs, and custom ASIC systems displace merchant x86 sockets at hyperscalers. Server-system ASP rises while CPU sockets and CPU ASP lag. OEM/ODM margins stay compressed. AMD/Intel CPU upside disappoints despite headline capex growth.

## 7. Updated Company Ranking

| Ranking | Companies | Rationale |
|---|---|---|
| **Strong candidate** | None unconditionally | Missing valuation, CPU attach, CPU ASP, and share data. |
| **Qualified candidate** | TSMC, AMD, Intel, Arm, Dell | Real exposure, but each has a gating uncertainty. |
| **Watchlist / benchmark** | Broadcom, Marvell, NVIDIA, HPE, Lenovo, Quanta, Wiwynn, Inventec, Supermicro, Foxconn, Celestica | Useful for AI infrastructure or order-flow comparison; not clean CPU plays. |
| **Avoid for CPU-pure thesis** | Qualcomm | Server CPU revenue/customer proof absent; prior Centriq attempt raises execution skepticism. Source: [Qualcomm Centriq 2017 launch](https://www.qualcomm.com/news/releases/2017/11/qualcomm-datacenter-technologies-announces-commercial-shipment-qualcomm). |

## 8. Remaining Unresolved Disputes

1. CPU dollars per rack: 2S x86, GB200/GB300, MI300X/MI350, Trainium, TPU, Maia.
2. EPYC-only and Xeon-only revenue growth.
3. Mercury / IDC / Omdia server CPU unit and revenue share through Q1 2026.
4. CPU ASP by SKU and customer class.
5. Arm royalty dollars per server CPU/core.
6. Hyperscaler internal CPU displacement of merchant x86 sockets.
7. Dell AI-server order duration, cancellation risk, and margin profile.
8. TSMC CoWoS / SoIC allocation among NVIDIA, AMD, Broadcom, hyperscalers, and Apple.
9. Valuation framework for AMD, Intel, Arm, TSMC, Dell, SMCI.

## 9. Updated Claim Register Rows

| ID | Claim | Source | Confidence | Status |
|---|---|---|---:|---|
| K3-R | Inference boosts general-purpose server demand, but this is an analyst estimate, not CPU attach proof. | [TrendForce](https://www.trendforce.com/presscenter/news/20260120-12887.html) | Low-Medium | Revised |
| K4-R | AMD FY25 Data Center revenue was $16.6B, +32%, but includes EPYC and Instinct. | [AMD](https://www.amd.com/en/newsroom/press-releases/2026-2-3-amd-reports-fourth-quarter-and-full-year-2025-fina.html) | High fact / Medium-Low CPU inference | Revised |
| K6-R | Microsoft FY26 Q2 capex was $37.5B; CPU share is not disclosed. | [Microsoft](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q2) | High fact / Low CPU read-through | Revised |
| K7-R | Dell disclosed >$64B AI-server orders and $43B backlog; CPU content unknown. | [Dell](https://investors.delltechnologies.com/news-releases/news-release-details/dell-technologies-delivers-fourth-quarter-and-full-year-fiscal-3) | High fact / Low CPU read-through | Revised |
| K8-R | Supermicro Q2 FY26 sales were $12.7B and GM 6.3%; margin risk is structural until proven otherwise. | [SMCI](https://ir.supermicro.com/news/news-details/2026/Supermicro-Announces-Second-Quarter-Fiscal-Year-2026-Financial-Results/default.aspx) | High | Revised negative |
| K11-R | Arm Neoverse >1B cores and near-50% top-hyperscaler share is management claim, not independent share data. | [Arm](https://newsroom.arm.com/news/arm-q3-fye26-results) | Medium fact / Low independent verification | Downgraded |
| K18-R | 10%-20% server CPU price hike report remains market rumor. | Prior Tom’s Hardware citation | Low | Excluded from base case |
| C19 | CPU dollars per AI rack vs traditional rack are missing. | UNSUPPORTED | Unknown | Fatal evidence gap |
| C20 | Server-system ASP inflation is not CPU ASP inflation. | [Gartner](https://www.gartner.com/en/documents/6998066) | Medium-High | Added |
| C21 | NVIDIA Grace/Vera, AWS Graviton, Azure Cobalt, and Google Axion are direct x86 substitution vectors. | [NVIDIA](https://www.nvidia.com/en-us/data-center/gb200-nvl72/), [AWS](https://www.aboutamazon.com/news/aws/aws-graviton-5-cpu-amazon-ec2), [Azure](https://azure.microsoft.com/en-us/blog/azure-cobalt-100-based-virtual-machines-are-now-generally-available/), [Google Axion](https://cloud.google.com/products/axion) | Medium | Added |
| C23 | No valuation framework means no unqualified Strong ratings. | UNSUPPORTED until valuation work completed | Unknown | Added |
2026-04-26T05:56:22.736401Z ERROR codex_core::session: failed to record rollout items: thread 019dc858-20b3-7063-8211-177096e4bc06 not found
tokens used
218,963


---

# claude: round_1_claude_revision

Timestamp: 2026-04-25T22:58:53

(Note: write permission to `claim_register.md` was not granted, so CDR-17 through CDR-25 above are proposed rows for the next register update — the round-2 revisions remain captured in this response.)

---

**Closing**: The Codex critique correctly forced me to separate **structural bear arguments** (CPU equities trade as AI capex beta; merchant x86 faces real captive-ARM substitution at hyperscalers; OEM/ODM AI-server economics are margin-thin where confirmed) from **bear quantifications I had no source for** (3–7% BOM, sub-20% EPYC growth, Sierra Forest mix). The structural arguments survive at Medium confidence; the quantifications are withdrawn. The most material verdict change is **Intel: Avoid → Tactical Watchlist (bear bias)** on the strength of S-02 and S-19, and **Arm: Avoid → Verdict deferred** because I cannot defend the valuation claim without a model.

 succeeded in 212ms:
88:- **Qualcomm:** Avoid for CPU thesis. Data center CPUs are “in development”; AI200/AI250 and Alphawave add optionality, but server CPU revenue/customer proof is absent.
151:| Avoid for CPU thesis | Qualcomm |
230:16. Initial ranking: Strong candidate / Watchlist / Avoid
414:- **Qualcomm:** Avoid for CPU thesis. Data center CPUs are “in development”; AI200/AI250 and Alphawave add optionality, but server CPU revenue/customer proof is absent.
477:| Avoid for CPU thesis | Qualcomm |
513:- **Intel**: Avoid as a CPU thesis. Foundry losses, structural share loss, and unproven 18A ramp dominate any DCAI green shoot.
514:- **Arm Holdings**: Avoid on valuation, not on technology. Royalty per server CPU is small; multiple is extreme.
515:- **Qualcomm**: Avoid as CPU thesis (agree with bull side here).
637:### Intel — Avoid (CPU thesis only)
643:### Arm Holdings — Avoid (valuation)
650:### Qualcomm — Avoid (CPU thesis)
670:### Supermicro — Avoid as long, possible tactical
673:- **Verdict**: Avoid as quality holding. Trade only with tight risk management.
680:### HPE — Avoid (CPU thesis)
695:### Wiwynn — Avoid as quality holding
770:| **Avoid** | Intel, Arm Holdings (valuation), Supermicro, Wiwynn, HPE, Inventec, Qualcomm | Each fails the risk-reward bar for distinct reasons |
791:**Closing note**: I do not dispute most of the bull-side facts. I dispute their investment implication. The same data set — large hyperscaler capex, growing AI server units, share gains in select x86 designs, ARM royalty growth — is consistent with a **mediocre risk-reward in CPU equities at current valuations** when accelerator and foundry equities offer cleaner exposure to the same underlying compute demand. The bear thesis is not "AI is overhyped"; it is "the CPU is the wrong layer of the stack to express AI conviction."
840:- **Intel:** Avoid is too harsh if Q1 DCAI strength and disclosed Nvidia Rubin NVL8 host-CPU role persist. Still execution-heavy.
842:- **Qualcomm:** Avoid as CPU thesis remains reasonable; its 10-K says it intends to use custom CPU cores for data center products, but no material server CPU revenue is shown. Source: [Qualcomm 10-K](https://www.sec.gov/Archives/edgar/data/0000804328/000080432825000085/qcom-20250928.htm).
853:| Avoid as CPU thesis | Qualcomm |
856:Main change: upgrade **Intel from Avoid to Watchlist / tactical CPU beta** pending Q2 confirmation.
982:- **Intel**: Avoid as a CPU thesis. Foundry losses, structural share loss, and unproven 18A ramp dominate any DCAI green shoot.
983:- **Arm Holdings**: Avoid on valuation, not on technology. Royalty per server CPU is small; multiple is extreme.
984:- **Qualcomm**: Avoid as CPU thesis (agree with bull side here).
1106:### Intel — Avoid (CPU thesis only)
1112:### Arm Holdings — Avoid (valuation)
1119:### Qualcomm — Avoid (CPU thesis)
1139:### Supermicro — Avoid as long, possible tactical
1142:- **Verdict**: Avoid as quality holding. Trade only with tight risk management.
1149:### HPE — Avoid (CPU thesis)
1164:### Wiwynn — Avoid as quality holding
1239:| **Avoid** | Intel, Arm Holdings (valuation), Supermicro, Wiwynn, HPE, Inventec, Qualcomm | Each fails the risk-reward bar for distinct reasons |
1260:**Closing note**: I do not dispute most of the bull-side facts. I dispute their investment implication. The same data set — large hyperscaler capex, growing AI server units, share gains in select x86 designs, ARM royalty growth — is consistent with a **mediocre risk-reward in CPU equities at current valuations** when accelerator and foundry equities offer cleaner exposure to the same underlying compute demand. The bear thesis is not "AI is overhyped"; it is "the CPU is the wrong layer of the stack to express AI conviction."
1407:513:- **Intel**: Avoid as a CPU thesis. Foundry losses, structural share loss, and unproven 18A ramp dominate any DCAI green shoot.
1408:514:- **Arm Holdings**: Avoid on valuation, not on technology. Royalty per server CPU is small; multiple is extreme.
1409:515:- **Qualcomm**: Avoid as CPU thesis (agree with bull side here).
1461:637:### Intel — Avoid (CPU thesis only)
1465:643:### Arm Holdings — Avoid (valuation)
1473:670:### Supermicro — Avoid as long, possible tactical
1477:695:### Wiwynn — Avoid as quality holding
1524:770:| **Avoid** | Intel, Arm Holdings (valuation), Supermicro, Wiwynn, HPE, Inventec, Qualcomm | Each fails the risk-reward bar for distinct reasons |
1536:791:**Closing note**: I do not dispute most of the bull-side facts. I dispute their investment implication. The same data set — large hyperscaler capex, growing AI server units, share gains in select x86 designs, ARM royalty growth — is consistent with a **mediocre risk-reward in CPU equities at current valuations** when accelerator and foundry equities offer cleaner exposure to the same underlying compute demand. The bear thesis is not "AI is overhyped"; it is "the CPU is the wrong layer of the stack to express AI conviction."
1610:+| CDR-11 | Arm Holdings is an Avoid on valuation because the multiple is extreme. | Arm | Valuation | Claude round 1; no current multiple table or DCF cited | Unknown | Codex round 1 opposition | UNSUPPORTED; needs price, share count, forward revenue/EPS/FCF scenarios |
1662:+| CDR-11 | Arm Holdings is an Avoid on valuation because the multiple is extreme. | Arm | Valuation | Claude round 1; no current multiple table or DCF cited | Unknown | Codex round 1 opposition | UNSUPPORTED; needs price, share count, forward revenue/EPS/FCF scenarios |
1717:| CDR-11 | Arm Holdings is an Avoid on valuation because the multiple is extreme. | Arm | Valuation | Claude round 1; no current multiple table or DCF cited | Unknown | Codex round 1 opposition | UNSUPPORTED; needs price, share count, forward revenue/EPS/FCF scenarios |
1769:+| CDR-11 | Arm Holdings is an Avoid on valuation because the multiple is extreme. | Arm | Valuation | Claude round 1; no current multiple table or DCF cited | Unknown | Codex round 1 opposition | UNSUPPORTED; needs price, share count, forward revenue/EPS/FCF scenarios |
1824:-| CDR-11 | Arm Holdings is an Avoid on valuation because the multiple is extreme. | Arm | Valuation | Claude round 1; no current multiple table or DCF cited | Unknown | Codex round 1 opposition | UNSUPPORTED; needs price, share count, forward revenue/EPS/FCF scenarios |
1880:+| CDR-11 | Arm Holdings is an Avoid on valuation because the multiple is extreme. | Arm | Valuation | Claude round 1; no current multiple table or DCF cited | Unknown | Codex round 1 opposition | UNSUPPORTED; needs price, share count, forward revenue/EPS/FCF scenarios |
2094:- **Intel:** Avoid is too harsh if Q1 DCAI strength and disclosed Nvidia Rubin NVL8 host-CPU role persist. Still execution-heavy.
2096:- **Qualcomm:** Avoid as CPU thesis remains reasonable; its 10-K says it intends to use custom CPU cores for data center products, but no material server CPU revenue is shown. Source: [Qualcomm 10-K](https://www.sec.gov/Archives/edgar/data/0000804328/000080432825000085/qcom-20250928.htm).
2107:| Avoid as CPU thesis | Qualcomm |
2110:Main change: upgrade **Intel from Avoid to Watchlist / tactical CPU beta** pending Q2 confirmation.
2154:+| CDR-11 | Arm Holdings is an Avoid on valuation because the multiple is extreme. | Arm | Valuation | Claude round 1; no current multiple table or DCF cited | Unknown | Codex round 1 opposition | UNSUPPORTED; needs price, share count, forward revenue/EPS/FCF scenarios |
2302:**Qualcomm (objection: agree on Avoid for CPU thesis, but reasoning incomplete)**
2339:| **Avoid for CPU-pure thesis** | Qualcomm, HPE, Supermicro, Wiwynn, Quanta, Inventec, Lenovo, Marvell | Either not a CPU play, or quality of CPU-driven earnings is too low. |
2357:| K9 | Wiwynn +163.7% revenue / 7.2% Q4 GM — bull/bear interpretation should be bear. | Major | Re-rank Wiwynn from Strong to Watchlist or Avoid. | Open |
2376:## 8. Required Follow-Up Research (Round 2)
2400:If none of these materialize in Round 2, my ranking stands and the bull thesis as Codex framed it does not survive scrutiny.
2413:# Round 2 Codex Revision — Response to Critique
2491:| **Avoid for CPU-pure thesis** | Qualcomm | Server CPU revenue/customer proof absent; prior Centriq attempt raises execution skepticism. Source: [Qualcomm Centriq 2017 launch](https://www.qualcomm.com/news/releases/2017/11/qualcomm-datacenter-technologies-announces-commercial-shipment-qualcomm). |
2672:- **Qualcomm:** Avoid for CPU thesis. Data center CPUs are “in development”; AI200/AI250 and Alphawave add optionality, but server CPU revenue/customer proof is absent.
2735:| Avoid for CPU thesis | Qualcomm |
2814:16. Initial ranking: Strong candidate / Watchlist / Avoid
2998:- **Qualcomm:** Avoid for CPU thesis. Data center CPUs are “in development”; AI200/AI250 and Alphawave add optionality, but server CPU revenue/customer proof is absent.
3061:| Avoid for CPU thesis | Qualcomm |
3180:**Qualcomm (objection: agree on Avoid for CPU thesis, but reasoning incomplete)**
3217:| **Avoid for CPU-pure thesis** | Qualcomm, HPE, Supermicro, Wiwynn, Quanta, Inventec, Lenovo, Marvell | Either not a CPU play, or quality of CPU-driven earnings is too low. |
3235:| K9 | Wiwynn +163.7% revenue / 7.2% Q4 GM — bull/bear interpretation should be bear. | Major | Re-rank Wiwynn from Strong to Watchlist or Avoid. | Open |
3254:## 8. Required Follow-Up Research (Round 2)
3278:If none of these materialize in Round 2, my ranking stands and the bull thesis as Codex framed it does not survive scrutiny.
3322:| CDR-11 | Arm Holdings is an Avoid on valuation because the multiple is extreme. | Arm | Valuation | Claude round 1; no current multiple table or DCF cited | Unknown | Codex round 1 opposition | UNSUPPORTED; needs price, share count, forward revenue/EPS/FCF scenarios |
3444:- **Qualcomm:** Avoid for CPU thesis. Data center CPUs are “in development”; AI200/AI250 and Alphawave add optionality, but server CPU revenue/customer proof is absent.
3507:| Avoid for CPU thesis | Qualcomm |
3586:16. Initial ranking: Strong candidate / Watchlist / Avoid
3653:# Round 2 Codex Revision — Response to Critique
3731:| **Avoid for CPU-pure thesis** | Qualcomm | Server CPU revenue/customer proof absent; prior Centriq attempt raises execution skepticism. Source: [Qualcomm Centriq 2017 launch](https://www.qualcomm.com/news/releases/2017/11/qualcomm-datacenter-technologies-announces-commercial-shipment-qualcomm). |
3771:(Note: write permission to `claim_register.md` was not granted, so CDR-17 through CDR-25 above are proposed rows for the next register update — the round-2 revisions remain captured in this response.)
3775:**Closing**: The Codex critique correctly forced me to separate **structural bear arguments** (CPU equities trade as AI capex beta; merchant x86 faces real captive-ARM substitution at hyperscalers; OEM/ODM AI-server economics are margin-thin where confirmed) from **bear quantifications I had no source for** (3–7% BOM, sub-20% EPYC growth, Sierra Forest mix). The structural arguments survive at Medium confidence; the quantifications are withdrawn. The most material verdict change is **Intel: Avoid → Tactical Watchlist (bear bias)** on the strength of S-02 and S-19, and **Arm: Avoid → Verdict deferred** because I cannot defend the valuation claim without a model.

exec
/usr/bin/zsh -lc "sed -n '2140,2410p' cpu-investment-research-2/transcript/full_debate.md" in /mnt/c/Users/hyc97/workspace/Ecclesia/CPU
exec
/usr/bin/zsh -lc "sed -n '2410,2585p' cpu-investment-research-2/transcript/full_debate.md" in /mnt/c/Users/hyc97/workspace/Ecclesia/CPU
exec
/usr/bin/zsh -lc "sed -n '3650,3778p' cpu-investment-research-2/transcript/full_debate.md" in /mnt/c/Users/hyc97/workspace/Ecclesia/CPU
 succeeded in 179ms:

Timestamp: 2026-04-25T22:56:22

# Round 2 Codex Revision — Response to Critique

## 1. Changes Made To Thesis

**Thesis revised downward.** I no longer treat hyperscaler capex as a direct CPU bull signal. It is a **confirmed infrastructure-demand signal**, but CPU revenue conversion is **unproven** without rack-level CPU dollars, attach rate, architecture mix, and ASP data.

**Old conclusion:** AMD, Arm, TSMC, Dell, Wiwynn as Strong candidates.  
**New conclusion:** **No unqualified Strong candidate for a CPU-pure thesis.** AMD, Intel, Arm, TSMC, and Dell remain investable candidates only with explicit caveats. Wiwynn is downgraded.

**Core revision:** AI may raise absolute CPU demand in inference and orchestration, but accelerated rack economics can reduce CPU dollars as a percentage of capex. This weakens the CPU-specific equity thesis.

Confidence: **Medium**.

## 2. Challenges Accepted

| Challenge | Disposition | Reason |
|---|---:|---|
| F1: Capex to CPU revenue chain not demonstrated | **Accept** | Central weakness. Capex is not CPU revenue. CPU dollars per rack remain missing. |
| F2: Microsoft capex wording over-interpreted | **Accept / Revise** | Microsoft says roughly two-thirds of capex was short-lived assets, primarily GPUs and CPUs, but does not disclose CPU share. Source: [Microsoft FY26 Q2 call](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q2). |
| F4: AI-server revenue can decouple from CPU sockets | **Accept** | Gartner 2Q25 shows server revenue +89.9% while shipments declined 1.5%, implying system ASP inflation is not CPU-unit growth. Source: [Gartner](https://www.gartner.com/en/documents/6998066). |
| F5: No valuation framework | **Accept** | Any “Strong candidate” label is invalid without multiples, FCF yield, EPS/FCF scenarios, or implied IRR. |
| AMD CPU-only disclosure gap | **Accept** | AMD Data Center includes EPYC CPUs and Instinct GPUs; EPYC-only growth is not disclosed. Source: [AMD FY25 results](https://www.amd.com/en/newsroom/press-releases/2026-2-3-amd-reports-fourth-quarter-and-full-year-2025-fina.html). |
| Arm royalty economics gap | **Accept** | Neoverse core deployment does not translate cleanly into royalty dollars. |
| Wiwynn margin critique | **Accept** | Q4 GM of 7.2% is not a semiconductor-like margin profile. Source: [Wiwynn Q4 2025](https://www.wiwynn.com/news/wiwynn-reports-fourth-quarter-2025-unaudited-financial-results). |
| NVIDIA / hyperscaler Arm substitution missing | **Accept** | GB200 NVL72 uses 36 Grace CPUs and 72 Blackwell GPUs; AWS says Graviton is over half of new AWS CPU capacity. Sources: [NVIDIA GB200](https://www.nvidia.com/en-us/data-center/gb200-nvl72/), [AWS Graviton5](https://www.aboutamazon.com/news/aws/aws-graviton-5-cpu-amazon-ec2). |
| HPE Juniper omission | **Accept** | HPE is now partly a networking strategy, not just server exposure. Source: [HPE Juniper close](https://www.hpe.com/us/en/newsroom/press-release/2025/07/hewlett-packard-enterprise-closes-acquisition-of-juniper-networks-to-offer-industry-leading-comprehensive-cloud-native-ai-driven-portfolio.html). |

## 3. Challenges Rejected, With Reason

| Challenge | Disposition | Reason |
|---|---:|---|
| Dell $64B / $43B figure may be false | **Reject factual challenge; accept interpretation risk** | Dell officially disclosed >$64B AI-optimized server orders, >$25B shipped, and $43B backlog. But this is AI-server revenue/order flow, not CPU revenue. Source: [Dell FY26 results](https://investors.delltechnologies.com/news-releases/news-release-details/dell-technologies-delivers-fourth-quarter-and-full-year-fiscal-3). |
| Alphabet / Meta / Amazon capex figures unsupported | **Reject factual challenge** | Official sources confirm Alphabet $175B-$185B, Meta $115B-$135B, and Amazon about $200B 2026 capex. Sources: [Alphabet transcript](https://s206.q4cdn.com/479360582/files/doc_events/2026/Feb/04/2025_Q4_Earnings_Transcript.pdf), [Meta Q4 2025](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Fourth-Quarter-and-Full-Year-2025-Results/), [Amazon Q4 2025](https://www.aboutamazon.com/news/company-news/amazon-earnings-q4-2025-report). |
| Broadcom / Marvell should be removed entirely | **Reject** | They should not be ranked as CPU plays, but they matter as substitution and relative-return benchmarks in AI infrastructure. |

## 4. Claims Revised

| Prior Claim | Revised Claim | Confidence |
|---|---|---:|
| Hyperscaler capex supports CPU upside | Hyperscaler capex supports infrastructure demand; CPU conversion is unquantified. | **Medium** |
| Microsoft two-thirds capex was GPUs/CPUs | Two-thirds was short-lived assets, primarily GPUs and CPUs; CPU slice unknown. | **High fact / Low CPU read-through** |
| Dell backlog supports CPU thesis | Dell backlog supports AI-server demand; CPU content and margin capture unknown. | **High fact / Low CPU read-through** |
| AMD is best direct CPU candidate | AMD is a qualified CPU candidate; EPYC-only revenue and share data are missing. | **Medium** |
| Intel DCAI +22% is recovery | Intel DCAI improved YoY, but “recovery” needs two-year stack and margin/ASP evidence. | **Medium-Low** |
| Arm is strong structural candidate | Arm is structurally exposed, but royalty dollars and valuation are unresolved. | **Medium** |
| Wiwynn is Strong ODM beta | Wiwynn is downgraded; growth is real but margin quality is weak. | **Medium** |

## 5. Claims Downgraded Due To Insufficient Evidence

| Claim | New Status |
|---|---|
| AI inference lifts merchant x86 CPU revenue materially | **Needs more evidence** |
| CPU attach rate rises with AI servers | **UNSUPPORTED** |
| AMD EPYC growth remains >25% | **UNSUPPORTED** |
| Intel CPU pricing tightens structurally | **UNSUPPORTED** |
| Arm hyperscaler share near 50% is independently verified | **Downgraded to management claim / Low independent confidence** |
| Server CPU price hikes of 10%-20% are real transactions | **Market rumor; exclude from base case** |
| TSMC is unconditionally bullish across all architectures | **Revised; capacity allocation and packaging constraints matter** |
| OEM/ODM AI revenue is high-quality earnings growth | **Downgraded** |

## 6. Updated Bull / Base / Bear View

**Bull Case — Low / Medium Confidence**  
Inference, agents, and cloud refresh create enough general-purpose compute demand that absolute CPU dollars grow even as CPU share of AI rack BOM falls. AMD EPYC grows faster than Intel, Intel benefits from x86 host CPU roles such as DGX Rubin NVL8, Arm royalties compound from Graviton/Cobalt/Axion/Grace/Vera, and TSMC captures the diversified silicon and packaging layer. Needs CPU-per-rack and share data.

**Base Case — Medium Confidence**  
AI capex remains strong, but CPU captures a smaller slice than GPUs, ASICs, networking, HBM, and packaging. AMD and Intel grow CPU revenue modestly, Arm gains architecture share, and TSMC remains the best diversified exposure. OEM/ODM revenue grows faster than profit.

**Bear Case — Medium Confidence**  
Accelerated racks, internal Arm CPUs, and custom ASIC systems displace merchant x86 sockets at hyperscalers. Server-system ASP rises while CPU sockets and CPU ASP lag. OEM/ODM margins stay compressed. AMD/Intel CPU upside disappoints despite headline capex growth.

## 7. Updated Company Ranking

| Ranking | Companies | Rationale |
|---|---|---|
| **Strong candidate** | None unconditionally | Missing valuation, CPU attach, CPU ASP, and share data. |
| **Qualified candidate** | TSMC, AMD, Intel, Arm, Dell | Real exposure, but each has a gating uncertainty. |
| **Watchlist / benchmark** | Broadcom, Marvell, NVIDIA, HPE, Lenovo, Quanta, Wiwynn, Inventec, Supermicro, Foxconn, Celestica | Useful for AI infrastructure or order-flow comparison; not clean CPU plays. |
| **Avoid for CPU-pure thesis** | Qualcomm | Server CPU revenue/customer proof absent; prior Centriq attempt raises execution skepticism. Source: [Qualcomm Centriq 2017 launch](https://www.qualcomm.com/news/releases/2017/11/qualcomm-datacenter-technologies-announces-commercial-shipment-qualcomm). |

## 8. Remaining Unresolved Disputes

1. CPU dollars per rack: 2S x86, GB200/GB300, MI300X/MI350, Trainium, TPU, Maia.
2. EPYC-only and Xeon-only revenue growth.
3. Mercury / IDC / Omdia server CPU unit and revenue share through Q1 2026.
4. CPU ASP by SKU and customer class.
5. Arm royalty dollars per server CPU/core.
6. Hyperscaler internal CPU displacement of merchant x86 sockets.
7. Dell AI-server order duration, cancellation risk, and margin profile.
8. TSMC CoWoS / SoIC allocation among NVIDIA, AMD, Broadcom, hyperscalers, and Apple.
9. Valuation framework for AMD, Intel, Arm, TSMC, Dell, SMCI.

## 9. Updated Claim Register Rows

| ID | Claim | Source | Confidence | Status |
|---|---|---|---:|---|
| K3-R | Inference boosts general-purpose server demand, but this is an analyst estimate, not CPU attach proof. | [TrendForce](https://www.trendforce.com/presscenter/news/20260120-12887.html) | Low-Medium | Revised |
| K4-R | AMD FY25 Data Center revenue was $16.6B, +32%, but includes EPYC and Instinct. | [AMD](https://www.amd.com/en/newsroom/press-releases/2026-2-3-amd-reports-fourth-quarter-and-full-year-2025-fina.html) | High fact / Medium-Low CPU inference | Revised |
| K6-R | Microsoft FY26 Q2 capex was $37.5B; CPU share is not disclosed. | [Microsoft](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q2) | High fact / Low CPU read-through | Revised |
| K7-R | Dell disclosed >$64B AI-server orders and $43B backlog; CPU content unknown. | [Dell](https://investors.delltechnologies.com/news-releases/news-release-details/dell-technologies-delivers-fourth-quarter-and-full-year-fiscal-3) | High fact / Low CPU read-through | Revised |
| K8-R | Supermicro Q2 FY26 sales were $12.7B and GM 6.3%; margin risk is structural until proven otherwise. | [SMCI](https://ir.supermicro.com/news/news-details/2026/Supermicro-Announces-Second-Quarter-Fiscal-Year-2026-Financial-Results/default.aspx) | High | Revised negative |
| K11-R | Arm Neoverse >1B cores and near-50% top-hyperscaler share is management claim, not independent share data. | [Arm](https://newsroom.arm.com/news/arm-q3-fye26-results) | Medium fact / Low independent verification | Downgraded |
| K18-R | 10%-20% server CPU price hike report remains market rumor. | Prior Tom’s Hardware citation | Low | Excluded from base case |
| C19 | CPU dollars per AI rack vs traditional rack are missing. | UNSUPPORTED | Unknown | Fatal evidence gap |
| C20 | Server-system ASP inflation is not CPU ASP inflation. | [Gartner](https://www.gartner.com/en/documents/6998066) | Medium-High | Added |
| C21 | NVIDIA Grace/Vera, AWS Graviton, Azure Cobalt, and Google Axion are direct x86 substitution vectors. | [NVIDIA](https://www.nvidia.com/en-us/data-center/gb200-nvl72/), [AWS](https://www.aboutamazon.com/news/aws/aws-graviton-5-cpu-amazon-ec2), [Azure](https://azure.microsoft.com/en-us/blog/azure-cobalt-100-based-virtual-machines-are-now-generally-available/), [Google Axion](https://cloud.google.com/products/axion) | Medium | Added |
| C23 | No valuation framework means no unqualified Strong ratings. | UNSUPPORTED until valuation work completed | Unknown | Added |

--- STDERR ---

Reading prompt from stdin...
OpenAI Codex v0.125.0 (research preview)
--------
workdir: /mnt/c/Users/hyc97/workspace/Ecclesia/CPU
model: gpt-5.5
provider: openai
approval: never
sandbox: workspace-write [workdir, /tmp, $TMPDIR, /home/yucheng/.codex/memories]
reasoning effort: xhigh
reasoning summaries: none
session id: 019dc858-20b3-7063-8211-177096e4bc06
--------
user
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
- Full transcript: cpu-investment-research-2/transcript/full_debate.md
- Claim register: cpu-investment-research-2/claims/claim_register.md
- Source log: cpu-investment-research-2/sources/source_log.md

        Role:
        You are Codex. You are revising your research after receiving critique.

        Task:
        Respond to the critique from round 1.

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

 succeeded in 187ms:
@@ -2,3 +2,19 @@
 
 | ID | Claim | Company | Category | Source | Confidence | Challenged By | Status |
 |---|---|---|---|---|---|---|---|
+| CDR-01 | CPU silicon is only 3-7% of AI server BOM / <5% of GB200-class rack BOM. | Industry | BOM / pricing | Claude round 1; no primary teardown cited | Low | Codex round 1 opposition | UNSUPPORTED; fatal to bear thesis until platform-level BOM is sourced |
+| CDR-02 | 60-70% of incremental hyperscaler compute capex flows into accelerated systems. | Industry | Capex allocation | Claude round 1 assumption | Low | Codex round 1 opposition | UNSUPPORTED; needs capex-to-server architecture bridge |
+| CDR-03 | Merchant x86 competes for a shrinking slice of incremental cloud CPU capacity. | AMD / Intel | Market share | S-10, S-11, S-13, S-14 support ARM adoption directionally; no independent share series cited | Medium-Low | Codex round 1 opposition | PARTIALLY SUPPORTED; requires Mercury/IDC/Omdia unit, revenue, and core-hour share |
+| CDR-04 | Nvidia AI rack architecture means ARM CPU displacement for x86. | Nvidia / Intel / AMD / Arm | Architecture | S-12 confirms GB200/GB300 use Grace Arm; S-19 confirms Xeon 6 host CPU in DGX Rubin NVL8 | Medium | Codex round 1 opposition | OVERBROAD; split by platform rather than treating all Nvidia systems as ARM-hosted |
+| CDR-05 | Custom ASIC racks have the lowest CPU intensity and are directly subtractive to merchant CPU vendors. | Broadcom / Marvell / hyperscalers | Substitution risk | Claude round 1; no TPU/Trainium/MAIA host-CPU counts cited | Low | Codex round 1 opposition | UNSUPPORTED; needs architecture attach data |
+| CDR-06 | AMD EPYC growth is probably sub-20%, with Instinct doing the heavy lifting. | AMD | Revenue mix | S-01 confirms Data Center includes EPYC and Instinct but not the split | Low | Codex round 1 opposition | UNSUPPORTED; do not use without EPYC/Instinct triangulation |
+| CDR-07 | Intel DCAI Q1 2026 strength may be mostly Sierra Forest mix / easy comp / low ASP host CPUs. | Intel | Revenue quality / ASP | S-02 confirms DCAI +22%; mix explanation is Claude inference | Low | Codex round 1 opposition | UNSUPPORTED; needs Intel product mix, ASP, and gross margin evidence |
+| CDR-08 | Server-system ASP inflation is not CPU ASP inflation. | Industry | Pricing | S-15 confirms system ASP +92.8%; CPU ASP split unavailable | Medium-High | Codex round 1 opposition | VALID CAVEAT; needs CPU-specific price dataset before bullish or bearish pricing claims |
+| CDR-09 | 10-20% server CPU price hikes since March 2026. | Intel / AMD | Pricing | Secondary press / channel rumor; no company confirmation in register | Low | Codex round 1 opposition | MARKET RUMOR; do not model as fact |
+| CDR-10 | Arm royalty per server CPU is low single-digit percentage of CPU ASP. | Arm | Unit economics | Claude round 1; no contract / AALA / CSS economics cited | Low | Codex round 1 opposition | UNSUPPORTED; needs royalty-dollar model |
+| CDR-11 | Arm Holdings is an Avoid on valuation because the multiple is extreme. | Arm | Valuation | Claude round 1; no current multiple table or DCF cited | Unknown | Codex round 1 opposition | UNSUPPORTED; needs price, share count, forward revenue/EPS/FCF scenarios |
+| CDR-12 | TSMC is priced for AI upside. | TSMC | Valuation | Claude round 1; no valuation comp table cited | Unknown | Codex round 1 opposition | UNSUPPORTED; needs valuation and scenario analysis |
+| CDR-13 | OEM/ODM gross margins will remain 6-10% and not recover. | SMCI / Wiwynn / Dell / Quanta / Inventec | Margin | S-08 and S-09 support SMCI/Wiwynn low recent GM; Dell evidence in S-07 is more mixed | Medium-Low | Codex round 1 opposition | OVERGENERALIZED; split by company, product mix, and operating margin |
+| CDR-14 | Dell is the highest-quality OEM and the only OEM worth Watchlist status. | Dell / OEMs | Ranking / quality | S-07 supports explicit AI orders/backlog and ISG growth; no peer valuation/quality scorecard cited | Medium-Low | Codex round 1 opposition | PARTIALLY SUPPORTED; needs peer scorecard and AI-server margin disclosure |
+| CDR-15 | Broadcom and Marvell should be excluded from the CPU framework. | Broadcom / Marvell | Universe definition | S-16 and S-17 confirm AI custom silicon / data center exposure, not CPU revenue | Medium | Codex round 1 opposition | TOO NARROW; exclude from pure CPU revenue, include as substitution and relative-return benchmarks |
+| CDR-16 | Hyperscaler capex may decelerate in 2H26 and hit OEM/ODM and merchant CPU first. | Industry | Cycle risk | Claude round 1 scenario; S-03, S-04, S-05, S-06 show high 2026 capex guidance | Low | Codex round 1 opposition | UNSUPPORTED SCENARIO; retain as bear case only |
diff --git a//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/sources/source_log.md b//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/sources/source_log.md
index 01b9972c25c14dc1e786453963d3d92445d5caa6..61fbc5b1877cffb5173d17ea67b6b7cfda9d8157
--- a//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/sources/source_log.md
+++ b//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/sources/source_log.md
@@ -4,3 +4,22 @@
 
 | ID | Source | Type | Date | Used For | Reliability |
 |---|---|---|---|---|---|
+| S-01 | https://www.amd.com/en/newsroom/press-releases/2026-2-3-amd-reports-fourth-quarter-and-full-year-2025-fina.html | Company earnings release | 2026-02-03 | AMD FY2025 Data Center revenue; EPYC + Instinct disclosure issue | High |
+| S-02 | https://www.intc.com/news-events/press-releases/detail/1767/intel-reports-first-quarter-2026-financial-results | Company earnings release | 2026-04-23 | Intel Q1 2026 DCAI revenue, management CPU demand framing, DGX Rubin NVL8 business highlight | High |
+| S-03 | https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q2 | Company earnings call transcript | 2026-01-28 | Microsoft FY26 Q2 capex and GPUs/CPUs wording | High |
+| S-04 | https://abc.xyz/investor/events/event-details/2026/2025-Q4-Earnings-Call-2026-Dr_C033hS6/default.aspx | Company earnings call transcript | 2026-02-04 | Alphabet 2026 capex guide and server/data-center allocation commentary | High |
+| S-05 | https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Fourth-Quarter-Results/default.aspx | Company earnings release | 2026-02-05 | Amazon 2026 capex guide | High |
+| S-06 | https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Fourth-Quarter-and-Full-Year-2025-Results/ | Company earnings release | 2026-01-28 | Meta 2026 capex guide | High |
+| S-07 | https://investors.delltechnologies.com/news-releases/news-release-details/dell-technologies-delivers-fourth-quarter-and-full-year-fiscal-3 | Company earnings release | 2026-02-26 | Dell FY26 AI server orders, shipments, backlog, ISG revenue and operating income | High |
+| S-08 | https://ir.supermicro.com/news/news-details/2026/Supermicro-Announces-Second-Quarter-Fiscal-Year-2026-Financial-Results/default.aspx | Company earnings release | 2026-02-03 | Supermicro Q2 FY2026 revenue and gross margin | High |
+| S-09 | https://www.wiwynn.com/news/wiwynn-reports-fourth-quarter-2025-unaudited-financial-results | Company unaudited financial release | 2026-03-03 | Wiwynn Q4 2025 gross margin, FY2025 revenue growth, AI product mix | Medium-High |
+| S-10 | https://newsroom.arm.com/news/arm-q3-fye26-results | Company earnings summary | 2026-02-04 | Arm Q3 FYE26 revenue, royalty growth, Neoverse cores, top-hyperscaler share management claim | Medium-High |
+| S-11 | https://www.aboutamazon.com/news/aws/aws-graviton-5-cpu-amazon-ec2/ | Company product announcement | 2025-12-04 | AWS Graviton share of new AWS CPU capacity | High for management claim |
+| S-12 | https://www.nvidia.com/en-us/data-center/gb200-nvl72/ | Company product page | 2026 crawled | NVIDIA GB200/GB300 Grace CPU counts and Arm architecture | High |
+| S-13 | https://azure.microsoft.com/en-us/blog/azure-cobalt-100-based-virtual-machines-are-now-generally-available/ | Company product announcement | 2024-10-16 | Microsoft Cobalt 100 GA and Arm-based Azure VM details | High |
+| S-14 | https://cloud.google.com/products/axion | Company product page | 2026 crawled | Google Axion custom Arm CPU and C4A/N4A instance details | High |
+| S-15 | https://www.gartner.com/en/documents/6998066 | Market research summary | 2025-09-26 | 2Q25 server shipments, vendor revenue, server-system ASP | Medium; paywalled analyst estimate |
+| S-16 | https://investors.broadcom.com/news-releases/news-release-details/broadcom-inc-announces-fourth-quarter-and-fiscal-year-2025 | Company earnings release | 2025-12-11 | Broadcom Q4 FY2025 AI semiconductor growth and AI revenue guide | High |
+| S-17 | https://investor.marvell.com/news-events/press-releases/detail/1011/marvell-technology-inc-reports-fourth-quarter-and-fiscal-year-2026-financial-results | Company earnings release | 2026-03-05 | Marvell FY2026 revenue growth and data center share of revenue | High |
+| S-18 | https://www.sec.gov/Archives/edgar/data/0000804328/000080432825000085/qcom-20250928.htm | SEC 10-K | 2025-11-05 | Qualcomm Oryon/data center product intent and segment context | High |
+| S-19 | https://newsroom.intel.com/data-center/intel-xeon-6-used-as-host-cpus-in-nvidia-dgx-rubin-nvl8-systems | Company product announcement | 2026-03-16 | Intel Xeon 6 host CPU role in NVIDIA DGX Rubin NVL8 systems | High for Intel claim |

2026-04-26T05:48:51.857235Z ERROR codex_core::session: failed to record rollout items: thread 019dc850-e8a2-7ed2-90a3-03e264f58558 not found
tokens used
233,945


---

# claude: round_1_claude_critiques_codex

Timestamp: 2026-04-25T22:51:51

# Round 1 Adversarial Review — Opposing CPU Equity Memo

**Reviewer:** Claude (opposing analyst)
**Subject:** Codex Round 1 memo dated 2026-04-25
**Stance:** Adversarial. The memo's framing is reasonable but several headline numbers look implausibly large, the central CPU-from-capex linkage is logically weak, and key substitution risks are under-weighted.

---

## 1. Highest-Risk Errors (Fatal or Near-Fatal)

**F1. The hyperscaler capex → CPU revenue chain is asserted, not demonstrated.**
Codex stacks Microsoft $37.5B, Alphabet $175–185B, Amazon ~$200B, Meta $115–135B and treats these as a CPU bull signal. The CPU share of an AI rack BOM (e.g. GB200 NVL72) is single-digit percent. Doubling AI capex with a falling CPU/system ratio can leave merchant CPU revenue flat. **Codex never quantifies CPU $ per AI rack, which is the entire load-bearing assumption of the memo.** Severity: Fatal to the bull case as written.

**F2. Microsoft "two-thirds were GPUs and CPUs" is misread.**
Microsoft's own language is "primarily GPUs and CPUs" for short-lived asset capex — it groups them as a *category* (silicon vs. shells/land/long-lived). Codex implies a two-thirds CPU+GPU mix in a way that suggests CPU is a meaningful slice. Reality: GPU dollars dwarf CPU dollars by ~10–20x in AI builds. Restating this as a CPU-positive datapoint is rhetorical, not quantitative. Severity: Fatal to claim K6's interpretation.

**F3. Dell "$64B FY26 AI orders / $43B backlog" needs hard verification.**
That magnitude is an order of 5–6x Dell's FY25 disclosed AI orders run-rate. If accurate, it's the single biggest data point in the memo; if it conflates "orders received in period" with "cumulative book-to-ship," the entire OEM ranking shifts. The memo cites a Dell IR URL but no quote. Severity: Fatal if wrong (Dell ranking flips), Major if real (still conflates AI-server $ with CPU $).

**F4. AI-server unit shipments are decoupling from CPU socket counts.**
Codex's own Gartner citation (2Q25 revenue +89.9%, units **−1.5%**) is itself a bearish CPU-unit signal that the memo papers over. Server *systems* are getting more expensive; CPU *sockets shipped* are not necessarily growing. This contradicts the bull thesis on AMD/Intel volume. Severity: Major — undermines the "merchant CPU revenue compounds with AI capex" claim.

**F5. No valuation framework whatsoever.**
The memo ranks AMD, Arm, TSMC as "Strong candidates" without a single multiple, EPS estimate, or implied IRR. Arm trades at >70x forward earnings; AMD trades at a premium to peer DC semis; ranking without valuation is a thesis, not a recommendation. Severity: Fatal to investability.

---

## 2. Unsupported Claims

| Statement in Codex memo | Why unsupported |
|---|---|
| "Roughly two-thirds [of MSFT FY26 Q2 capex] was GPUs and CPUs" | Microsoft's stated language is "primarily" — no disclosed quantitative split. |
| "Alphabet 2026 capex $175–$185B" | Cite-only; this is ~2.3x 2025 capex. If genuine guidance, source link should be timestamped to a specific call/transcript page; the URL provided is a placeholder pattern. |
| "Amazon expects ~$200B capex in 2026" | Same issue; Amazon historically guides quarter-by-quarter, not annual. Marked High Confidence in K16 — should be Medium at best until transcript is pulled. |
| "Meta 2026 capex $115–$135B" | Same — needs literal transcript line. |
| "Dell FY26 AI orders >$64B; backlog $43B" | Magnitude not reconciled to Dell's prior disclosures. |
| "Inference workloads boosting general-purpose server demand" (K3) | Asserted by TrendForce; no causal data showing CPU-only attach uplift. |
| "Arm Neoverse may approach 50% share at top hyperscalers" (K11) | Arm management claim; no third-party verification. Codex correctly flags as Medium but uses it in main text as if directional fact. |
| "AMD gaining profitable EPYC share" (Bull case sec. 11) | Mercury share trend has been *decelerating* in late 2025 as Intel Granite Rapids/Sierra Forest ramp. UNSUPPORTED in current form. |

---

## 3. Questionable Assumptions

**Q1.** *That AI server attach drives merchant x86 CPU revenue.* AI racks use 1–2 host CPUs per 8 GPUs. Old non-AI 2S server racks were 100% CPU. Per-GPU dollar growth ≠ per-CPU dollar growth. This is the central question; Codex doesn't engage it.

**Q2.** *That Intel DCAI's +22% YoY in Q1 2026 is "recovery."* Q1 2025 base was depressed (Sapphire Rapids transition, customer destocking). Two-year stack is the relevant frame — likely flat to mildly positive, not a turnaround.

**Q3.** *That AMD pricing power in EPYC continues to expand.* Mix-up driven by Genoa/Bergamo/Turin is real, but Intel's response with Granite Rapids-AP and aggressive cloud SKU pricing in late 2025/early 2026 likely caps further mix gains.

**Q4.** *That Arm royalty growth flows proportionally to server cores.* Server royalty rates per core are higher than mobile but Arm doesn't disclose; the leap from "1B Neoverse cores" to investable royalty $ is unsupported. Royalty per Graviton core is reportedly low single-digit dollars at most.

**Q5.** *That TSMC is uniformly bullish across architectures.* Apple is still ~22–25% of TSMC revenue. CoWoS capacity, not wafer demand, is the binding constraint for AI silicon. The "broadest beneficiary" framing ignores capacity allocation tradeoffs.

**Q6.** *That Wiwynn margin pressure is "monitor and own."* 7.2% Q4 GM at peak revenue cycle is a structural problem, not transitional. ODM operating leverage is the opposite of typical semiconductor leverage — revenue growth ≠ profit growth.

**Q7.** *That OCP/hyperscaler internal builds don't cannibalize merchant CPU.* Cobalt 100, Graviton 4, Axion, and the SoftBank-acquired Ampere lineup all displace Xeon/EPYC sockets at *exactly* the customers driving capex growth.

---

## 4. Missing Evidence / Missing Companies

**Missing companies & substitution risks:**
- **NVIDIA** — Grace, Grace-Blackwell, Vera Rubin CPU. Direct displacement of merchant x86 in AI racks. Mentioned in passing in section 5 but not in company table or as an investable substitute risk.
- **Ampere Computing / SoftBank** — Acquired by SoftBank (announced March 2025). Now Arm-aligned hyperscaler CPU vendor. Should be in the substitution map.
- **MediaTek** — NVIDIA-MediaTek Arm-based CPU partnership for consumer/AI PC announced; potential server extension.
- **IBM (Power)** — Niche but real in financial services / mainframe replacement. Z17 CPU launch.
- **Foxconn / Hon Hai** — Largest AI-server ODM by some measures, only mentioned once in passing.
- **Pegatron, ASRock Rack, Gigabyte (GIGA-BYTE)** — Smaller AI-server ODMs but capturing share.
- **Celestica** — Hyperscaler AI infrastructure ODM; should at minimum be in watchlist.

**Missing supply-chain links:**
- DDR5/HBM memory controllers and the CPU-memory bandwidth wall (Samsung, SK hynix, Micron) — affects CPU pricing power because memory bandwidth, not core count, is the AI inference CPU bottleneck.
- Substrate/ABF (Ibiden, Unimicron) — capacity gates server CPU shipments.
- Advanced packaging (CoWoS, SoIC) — gates AMD MI accelerators but also Intel Clearwater Forest/Diamond Rapids.

**Missing analytical evidence:**
- A side-by-side $-per-CPU table for: 2S Genoa rack vs. 2S Granite Rapids rack vs. GB200 NVL72 vs. MI300X HGX vs. Trainium 2 rack. Without this, "AI capex helps CPUs" is a slogan.
- TCO/perf-per-watt comparison: Graviton 4 vs. EPYC Turin vs. Xeon 6. This is the single biggest driver of x86 vs. Arm switching at AWS/Azure/GCP.
- Mercury Research Q4 2025 server CPU unit and revenue share — Codex flags this as a verification task but builds the share-gain narrative without it.
- Channel-checked CPU ASP from a real distributor (ASBIS, Synnex, etc.) to validate or kill the Tom's Hardware K18 rumor.

**Missing macro / geopolitical:**
- US export controls on advanced node CPUs to China — affects Intel/AMD revenue mix.
- Arm royalty-rate dispute history with Qualcomm — relevant to whether the licensing model holds.

---

## 5. Company-Specific Objections

**AMD (objection: ranking too high without CPU-only disclosure)**
- $16.6B FY25 DC includes Instinct GPU revenue (likely $5–7B). EPYC-only growth is therefore inferred, not measured. If Instinct grew 100%+ and EPYC grew 15%, "DC +32%" tells you nothing about CPU share. Codex flags this gap but still ranks AMD "Strong" — inconsistent.
- Forward risk: MI400 ramp slippage and GB200 ASP undercutting could compress DC GM.

**Intel (objection: ranking too low / mis-framed)**
- If the bull thesis includes "DCAI recovery" plus "supply tightens DCAI pricing," then Intel is *more* leveraged to the CPU-specific upside than AMD (since AMD revenue is being diluted by Instinct GPU mix).
- Codex puts Intel on watchlist but builds the bull case partly on Intel CPU pricing power — internally inconsistent.
- Foundry losses and 18A yield are still the binding constraint, not DCAI demand.

**Arm (objection: pricing-in problem, not addressed)**
- Stock trades at extreme P/E multiples relative to revenue scale. Royalty $ per Neoverse core is undisclosed — bull case is a black box.
- Arm China governance overhang (~20% of revenue) is unaddressed.

**Qualcomm (objection: agree on Avoid for CPU thesis, but reasoning incomplete)**
- AI200/AI250 are inference accelerators, not CPUs. Codex correctly notes server CPU is in development but doesn't note Qualcomm's prior failed Centriq attempt (2017–2018). Pattern matters for option value.

**Broadcom / Marvell (objection: shouldn't be in a CPU memo at all)**
- Both are correctly described as "not clean CPU plays" — then why are they in the company universe? Either expand the thesis to "AI silicon" or remove. Including them inflates the universe.

**TSMC (objection: capacity constraint not discussed)**
- CoWoS-L is the bottleneck, not wafer starts. TSMC's CPU upside is gated by its packaging allocation between Apple, NVIDIA, AMD, Broadcom — not by aggregate server demand. Ranking "Strong" without this discussion is incomplete.

**Supermicro (objection: customer concentration / accounting overhang under-weighted)**
- Hindenburg report (Aug 2024), 10-K delay (2024), auditor change — these are not historical artifacts; SEC investigation status as of early 2026 should be stated.
- 6.3% GM at $12.7B revenue is a *structural* problem, not transitional.

**Dell (objection: $64B headline number not stress-tested)**
- If real: still a low-margin pass-through; ISG operating margin is what matters.
- If "orders" includes multi-year framework agreements with no firm delivery dates: number is largely vapor.

**HPE (objection: Juniper acquisition not mentioned)**
- HPE's strategy pivot to networking via Juniper materially changes the thesis. Memo treats HPE as a server-only story.

**Lenovo (objection: ISG margin context missing)**
- Lenovo ISG has been loss-making in some quarters. AI server revenue growth without unit economics is not investable.

**Quanta / Wiwynn / Inventec (objection: ranking is order-flow proxy, not equity thesis)**
- ODM equities track NT$ revenue announcements monthly. Investing in them is essentially a leveraged AI-capex bet with worse margins than buying NVDA directly. Codex never explains why an investor would prefer Wiwynn over NVDA exposure.

---

## 6. Revised Ranking

I disagree with Codex's ranking. My adversarial counter-ranking:

| Rank | Companies | Reasoning |
|---|---|---|
| **Strong candidate (CPU-thesis pure)** | None unconditionally. AMD if EPYC-only disclosure or strong channel checks confirm continued share gains. | Pure CPU exposure is rare; everything else is diluted. |
| **Qualified candidate** | TSMC (gated by CoWoS supply/demand discipline), Arm (only at lower multiples) | Picks-and-shovels logic survives scrutiny; valuation does not at current levels. |
| **Watchlist** | AMD, Intel, Dell, Broadcom | Each has a credible 12–18 month catalyst path. |
| **Avoid for CPU-pure thesis** | Qualcomm, HPE, Supermicro, Wiwynn, Quanta, Inventec, Lenovo, Marvell | Either not a CPU play, or quality of CPU-driven earnings is too low. |

The Codex "Strong: AMD/Arm/TSMC/Dell/Wiwynn" basket is too inclusive given the central uncertainties.

---

## 7. Claim Challenges Table

| Claim ID | Problem | Severity | Suggested Fix | Status |
|---|---|---|---|---|
| K1 | IDC Q4 2025 +52.4% revenue / +10.3% units — needs primary source URL with date; current link is a category page. | Minor | Replace with specific IDC press release. | Open |
| K2 | TrendForce 2026 forecast — number could not be verified from URL pattern; not yet primary-sourced. | Minor | Confirm specific TrendForce report and cite. | Open |
| K3 | "Inference boosts general-purpose server demand" — TrendForce assertion stated as a confidence-Medium fact. | Major | Downgrade to Low; require empirical attach data. | Open |
| K4 | AMD $16.6B DC includes Instinct GPU; EPYC-only growth not disclosed. | Major | Add EPYC-only estimate range; flag dependency. | Open |
| K5 | Intel DCAI +22% YoY off depressed Q1 2025 base. | Minor | Show 2-year stack growth instead. | Open |
| K6 | "Roughly two-thirds was GPUs and CPUs" overstates CPU portion. | Fatal to interpretation | Restate as "primarily silicon vs. real estate"; do not split GPU/CPU. | Open |
| K7 | Dell $64B AI orders / $43B backlog — magnitude requires direct transcript verification. | Fatal if wrong | Pull Dell FY26 Q4 earnings transcript and 10-K disclosure verbatim. | Open |
| K8 | SMCI 6.3% GM is structural, not noted as such. | Major | Add structural margin discussion; flag SEC/audit status. | Open |
| K9 | Wiwynn +163.7% revenue / 7.2% Q4 GM — bull/bear interpretation should be bear. | Major | Re-rank Wiwynn from Strong to Watchlist or Avoid. | Open |
| K10 | Arm Q3 FYE26 revenue figures need transcript reference, not only newsroom URL. | Minor | Add transcript citation. | Open |
| K11 | "~50% Arm share at top hyperscalers" — management claim only. | Major | Downgrade to Low until Mercury or hyperscaler disclosure confirms. | Open |
| K12 | Broadcom AI semis +74% — fact, but irrelevant to CPU thesis. | Minor | Note as orthogonal. | Open |
| K13 | Marvell DC 74% of Q4 — fact, but again orthogonal. | Minor | Note as orthogonal. | Open |
| K14 | Meta 2026 capex $115–135B — needs primary-source transcript line. | Major | Pull Q4 2025 earnings call transcript. | Open |
| K15 | Alphabet 2026 capex $175–185B — magnitude is ~2.3x 2025 baseline; high-prior verification required. | Major | Pull 4Q25 earnings call transcript. | Open |
| K16 | Amazon $200B capex 2026 — Amazon typically does not give annual capex guidance. | Major | Verify exact wording; may be analyst-derived, not company guidance. | Open |
| K17 | Qualcomm "server CPUs in development" — also true in 2017 (Centriq history). | Minor | Add prior-attempt context. | Open |
| K18 | Tom's Hardware April 2026 CPU price-rise rumor. | Major | Already flagged Low; downgrade to "Rumor — exclude from base case." | Open |
| **NEW C19** | CPU $ per AI rack vs. CPU $ per traditional 2S rack — never quantified. | Fatal | Build ratio table; this is the central missing analysis. | Open |
| **NEW C20** | Server unit shipments −1.5% YoY (Gartner 2Q25) implies CPU socket count is flat to declining. | Major | Reconcile with CPU revenue claims; downgrade volume-based bull case. | Open |
| **NEW C21** | NVIDIA Grace/Vera and SoftBank-Ampere as direct merchant-CPU substitutes are absent from Industry Map. | Major | Add to Industry Map and substitution analysis. | Open |
| **NEW C22** | TSMC CoWoS-L allocation as binding constraint not discussed. | Major | Add capacity allocation analysis to TSMC ranking. | Open |
| **NEW C23** | No valuation multiples cited for any company in Strong-candidate ranking. | Fatal | Add P/E, EV/EBITDA, FCF yield for AMD, Arm, TSMC, Dell minimum. | Open |
| **NEW C24** | Hyperscaler internal CPU programs (Cobalt, Graviton, Axion) not quantified as merchant CPU TAM headwind. | Major | Estimate displaced merchant socket count by hyperscaler. | Open |

---

## 8. Required Follow-Up Research (Round 2)

1. **CPU $-per-rack table.** Build a 5-row comparison: traditional 2S Genoa, 2S Granite Rapids, GB200 NVL72 (Grace), MI300X HGX (with Genoa host), Trainium 2 rack. Show CPU dollars and CPU as % of system BOM.
2. **Verify all four hyperscaler 2026 capex numbers** with literal transcript quotes, page numbers, and dates. Demote any unverifiable figure to "analyst aggregation."
3. **Pull Mercury Research Q4 2025 / Q1 2026 server CPU share data** (paid). Settle whether AMD share growth is continuing or plateauing.
4. **Channel-check CPU ASP** via at least two distributors (ASBIS, Synnex, Ingram Micro) and at least one OEM procurement contact. Either kill or upgrade K18.
5. **Confirm Dell $64B figure** by pulling the FY26 Q4 transcript and 10-K. Determine whether "orders" = backlog + shipped or backlog only, and what duration is implied.
6. **Estimate Arm royalty $ per Neoverse server core** using Arm's reported royalty revenue, deployed core count, and Graviton/Cobalt unit estimates.
7. **Add Ampere/SoftBank, NVIDIA Grace/Vera, IBM Power, and Foxconn** to the company universe. Re-rank.
8. **Add valuation snapshot** (P/E NTM, EV/EBITDA NTM, FCF yield) for at minimum AMD, Arm, TSMC, Intel, Dell, SMCI. The "Strong candidate" label requires a price-supported view.
9. **Quantify hyperscaler internal CPU displacement** of merchant x86: Graviton (~50% of new AWS instances per AWS), Cobalt, Axion, Ampere base.
10. **TSMC capacity allocation analysis**: CoWoS-L wafer share for Apple vs. NVIDIA vs. AMD vs. Broadcom in 2026/2027.

---

## What Would Change My Mind

- **EPYC-only revenue disclosure or credible channel estimate** showing >25% growth in 2026 → AMD upgrade to Strong.
- **Mercury data confirming AMD revenue share >35%** in server CPUs through Q1 2026 with stable ASP → AMD upgrade.
- **Verified Microsoft/Alphabet/Amazon transcript lines** confirming 2026 capex magnitudes within ±5% of Codex numbers → restores confidence in K6/K15/K16.
- **Disclosed CPU $ per AI rack ≥ 5%** of system value, with growing absolute CPU $ even at falling % → resolves F1/F4.
- **Intel 18A yield credibly above 50% by mid-2026** → Intel from Watchlist to Qualified candidate.
- **Arm valuation compression to <40x forward EPS** → Arm from Disqualified-on-price to Qualified.

If none of these materialize in Round 2, my ranking stands and the bull thesis as Codex framed it does not survive scrutiny.

---

*Note on memory: I have not written any of this round's claims to my memory store. These are working-session artifacts and belong in the round-1 transcript, not in cross-session memory. Per the project files, the actual claim register file is empty — Codex did not persist the K1–K18 table to `cpu-investment-research-2/claims/claim_register.md`. That should be fixed at the orchestrator level.*


---

# codex: round_1_codex_revision


 succeeded in 180ms:
web search: 
web search: HPE completes Juniper acquisition 2025 official HPE networking strategy
codex
# Round 2 Codex Revision — Response to Critique

## 1. Changes Made To Thesis

**Thesis revised downward.** I no longer treat hyperscaler capex as a direct CPU bull signal. It is a **confirmed infrastructure-demand signal**, but CPU revenue conversion is **unproven** without rack-level CPU dollars, attach rate, architecture mix, and ASP data.

**Old conclusion:** AMD, Arm, TSMC, Dell, Wiwynn as Strong candidates.  
**New conclusion:** **No unqualified Strong candidate for a CPU-pure thesis.** AMD, Intel, Arm, TSMC, and Dell remain investable candidates only with explicit caveats. Wiwynn is downgraded.

**Core revision:** AI may raise absolute CPU demand in inference and orchestration, but accelerated rack economics can reduce CPU dollars as a percentage of capex. This weakens the CPU-specific equity thesis.

Confidence: **Medium**.

## 2. Challenges Accepted

| Challenge | Disposition | Reason |
|---|---:|---|
| F1: Capex to CPU revenue chain not demonstrated | **Accept** | Central weakness. Capex is not CPU revenue. CPU dollars per rack remain missing. |
| F2: Microsoft capex wording over-interpreted | **Accept / Revise** | Microsoft says roughly two-thirds of capex was short-lived assets, primarily GPUs and CPUs, but does not disclose CPU share. Source: [Microsoft FY26 Q2 call](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q2). |
| F4: AI-server revenue can decouple from CPU sockets | **Accept** | Gartner 2Q25 shows server revenue +89.9% while shipments declined 1.5%, implying system ASP inflation is not CPU-unit growth. Source: [Gartner](https://www.gartner.com/en/documents/6998066). |
| F5: No valuation framework | **Accept** | Any “Strong candidate” label is invalid without multiples, FCF yield, EPS/FCF scenarios, or implied IRR. |
| AMD CPU-only disclosure gap | **Accept** | AMD Data Center includes EPYC CPUs and Instinct GPUs; EPYC-only growth is not disclosed. Source: [AMD FY25 results](https://www.amd.com/en/newsroom/press-releases/2026-2-3-amd-reports-fourth-quarter-and-full-year-2025-fina.html). |
| Arm royalty economics gap | **Accept** | Neoverse core deployment does not translate cleanly into royalty dollars. |
| Wiwynn margin critique | **Accept** | Q4 GM of 7.2% is not a semiconductor-like margin profile. Source: [Wiwynn Q4 2025](https://www.wiwynn.com/news/wiwynn-reports-fourth-quarter-2025-unaudited-financial-results). |
| NVIDIA / hyperscaler Arm substitution missing | **Accept** | GB200 NVL72 uses 36 Grace CPUs and 72 Blackwell GPUs; AWS says Graviton is over half of new AWS CPU capacity. Sources: [NVIDIA GB200](https://www.nvidia.com/en-us/data-center/gb200-nvl72/), [AWS Graviton5](https://www.aboutamazon.com/news/aws/aws-graviton-5-cpu-amazon-ec2). |
| HPE Juniper omission | **Accept** | HPE is now partly a networking strategy, not just server exposure. Source: [HPE Juniper close](https://www.hpe.com/us/en/newsroom/press-release/2025/07/hewlett-packard-enterprise-closes-acquisition-of-juniper-networks-to-offer-industry-leading-comprehensive-cloud-native-ai-driven-portfolio.html). |

## 3. Challenges Rejected, With Reason

| Challenge | Disposition | Reason |
|---|---:|---|
| Dell $64B / $43B figure may be false | **Reject factual challenge; accept interpretation risk** | Dell officially disclosed >$64B AI-optimized server orders, >$25B shipped, and $43B backlog. But this is AI-server revenue/order flow, not CPU revenue. Source: [Dell FY26 results](https://investors.delltechnologies.com/news-releases/news-release-details/dell-technologies-delivers-fourth-quarter-and-full-year-fiscal-3). |
| Alphabet / Meta / Amazon capex figures unsupported | **Reject factual challenge** | Official sources confirm Alphabet $175B-$185B, Meta $115B-$135B, and Amazon about $200B 2026 capex. Sources: [Alphabet transcript](https://s206.q4cdn.com/479360582/files/doc_events/2026/Feb/04/2025_Q4_Earnings_Transcript.pdf), [Meta Q4 2025](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Fourth-Quarter-and-Full-Year-2025-Results/), [Amazon Q4 2025](https://www.aboutamazon.com/news/company-news/amazon-earnings-q4-2025-report). |
| Broadcom / Marvell should be removed entirely | **Reject** | They should not be ranked as CPU plays, but they matter as substitution and relative-return benchmarks in AI infrastructure. |

## 4. Claims Revised

| Prior Claim | Revised Claim | Confidence |
|---|---|---:|
| Hyperscaler capex supports CPU upside | Hyperscaler capex supports infrastructure demand; CPU conversion is unquantified. | **Medium** |
| Microsoft two-thirds capex was GPUs/CPUs | Two-thirds was short-lived assets, primarily GPUs and CPUs; CPU slice unknown. | **High fact / Low CPU read-through** |
| Dell backlog supports CPU thesis | Dell backlog supports AI-server demand; CPU content and margin capture unknown. | **High fact / Low CPU read-through** |
| AMD is best direct CPU candidate | AMD is a qualified CPU candidate; EPYC-only revenue and share data are missing. | **Medium** |
| Intel DCAI +22% is recovery | Intel DCAI improved YoY, but “recovery” needs two-year stack and margin/ASP evidence. | **Medium-Low** |
| Arm is strong structural candidate | Arm is structurally exposed, but royalty dollars and valuation are unresolved. | **Medium** |
| Wiwynn is Strong ODM beta | Wiwynn is downgraded; growth is real but margin quality is weak. | **Medium** |

## 5. Claims Downgraded Due To Insufficient Evidence

| Claim | New Status |
|---|---|
| AI inference lifts merchant x86 CPU revenue materially | **Needs more evidence** |
| CPU attach rate rises with AI servers | **UNSUPPORTED** |
| AMD EPYC growth remains >25% | **UNSUPPORTED** |
| Intel CPU pricing tightens structurally | **UNSUPPORTED** |
| Arm hyperscaler share near 50% is independently verified | **Downgraded to management claim / Low independent confidence** |
| Server CPU price hikes of 10%-20% are real transactions | **Market rumor; exclude from base case** |
| TSMC is unconditionally bullish across all architectures | **Revised; capacity allocation and packaging constraints matter** |
| OEM/ODM AI revenue is high-quality earnings growth | **Downgraded** |

## 6. Updated Bull / Base / Bear View

**Bull Case — Low / Medium Confidence**  
Inference, agents, and cloud refresh create enough general-purpose compute demand that absolute CPU dollars grow even as CPU share of AI rack BOM falls. AMD EPYC grows faster than Intel, Intel benefits from x86 host CPU roles such as DGX Rubin NVL8, Arm royalties compound from Graviton/Cobalt/Axion/Grace/Vera, and TSMC captures the diversified silicon and packaging layer. Needs CPU-per-rack and share data.

**Base Case — Medium Confidence**  
AI capex remains strong, but CPU captures a smaller slice than GPUs, ASICs, networking, HBM, and packaging. AMD and Intel grow CPU revenue modestly, Arm gains architecture share, and TSMC remains the best diversified exposure. OEM/ODM revenue grows faster than profit.

**Bear Case — Medium Confidence**  
Accelerated racks, internal Arm CPUs, and custom ASIC systems displace merchant x86 sockets at hyperscalers. Server-system ASP rises while CPU sockets and CPU ASP lag. OEM/ODM margins stay compressed. AMD/Intel CPU upside disappoints despite headline capex growth.

## 7. Updated Company Ranking

| Ranking | Companies | Rationale |
|---|---|---|
| **Strong candidate** | None unconditionally | Missing valuation, CPU attach, CPU ASP, and share data. |
| **Qualified candidate** | TSMC, AMD, Intel, Arm, Dell | Real exposure, but each has a gating uncertainty. |
| **Watchlist / benchmark** | Broadcom, Marvell, NVIDIA, HPE, Lenovo, Quanta, Wiwynn, Inventec, Supermicro, Foxconn, Celestica | Useful for AI infrastructure or order-flow comparison; not clean CPU plays. |
| **Avoid for CPU-pure thesis** | Qualcomm | Server CPU revenue/customer proof absent; prior Centriq attempt raises execution skepticism. Source: [Qualcomm Centriq 2017 launch](https://www.qualcomm.com/news/releases/2017/11/qualcomm-datacenter-technologies-announces-commercial-shipment-qualcomm). |

## 8. Remaining Unresolved Disputes

1. CPU dollars per rack: 2S x86, GB200/GB300, MI300X/MI350, Trainium, TPU, Maia.
2. EPYC-only and Xeon-only revenue growth.
3. Mercury / IDC / Omdia server CPU unit and revenue share through Q1 2026.
4. CPU ASP by SKU and customer class.
5. Arm royalty dollars per server CPU/core.
6. Hyperscaler internal CPU displacement of merchant x86 sockets.
7. Dell AI-server order duration, cancellation risk, and margin profile.
8. TSMC CoWoS / SoIC allocation among NVIDIA, AMD, Broadcom, hyperscalers, and Apple.
9. Valuation framework for AMD, Intel, Arm, TSMC, Dell, SMCI.

## 9. Updated Claim Register Rows

| ID | Claim | Source | Confidence | Status |
|---|---|---|---:|---|
| K3-R | Inference boosts general-purpose server demand, but this is an analyst estimate, not CPU attach proof. | [TrendForce](https://www.trendforce.com/presscenter/news/20260120-12887.html) | Low-Medium | Revised |
| K4-R | AMD FY25 Data Center revenue was $16.6B, +32%, but includes EPYC and Instinct. | [AMD](https://www.amd.com/en/newsroom/press-releases/2026-2-3-amd-reports-fourth-quarter-and-full-year-2025-fina.html) | High fact / Medium-Low CPU inference | Revised |
| K6-R | Microsoft FY26 Q2 capex was $37.5B; CPU share is not disclosed. | [Microsoft](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q2) | High fact / Low CPU read-through | Revised |
| K7-R | Dell disclosed >$64B AI-server orders and $43B backlog; CPU content unknown. | [Dell](https://investors.delltechnologies.com/news-releases/news-release-details/dell-technologies-delivers-fourth-quarter-and-full-year-fiscal-3) | High fact / Low CPU read-through | Revised |
| K8-R | Supermicro Q2 FY26 sales were $12.7B and GM 6.3%; margin risk is structural until proven otherwise. | [SMCI](https://ir.supermicro.com/news/news-details/2026/Supermicro-Announces-Second-Quarter-Fiscal-Year-2026-Financial-Results/default.aspx) | High | Revised negative |
| K11-R | Arm Neoverse >1B cores and near-50% top-hyperscaler share is management claim, not independent share data. | [Arm](https://newsroom.arm.com/news/arm-q3-fye26-results) | Medium fact / Low independent verification | Downgraded |
| K18-R | 10%-20% server CPU price hike report remains market rumor. | Prior Tom’s Hardware citation | Low | Excluded from base case |
| C19 | CPU dollars per AI rack vs traditional rack are missing. | UNSUPPORTED | Unknown | Fatal evidence gap |
| C20 | Server-system ASP inflation is not CPU ASP inflation. | [Gartner](https://www.gartner.com/en/documents/6998066) | Medium-High | Added |
| C21 | NVIDIA Grace/Vera, AWS Graviton, Azure Cobalt, and Google Axion are direct x86 substitution vectors. | [NVIDIA](https://www.nvidia.com/en-us/data-center/gb200-nvl72/), [AWS](https://www.aboutamazon.com/news/aws/aws-graviton-5-cpu-amazon-ec2), [Azure](https://azure.microsoft.com/en-us/blog/azure-cobalt-100-based-virtual-machines-are-now-generally-available/), [Google Axion](https://cloud.google.com/products/axion) | Medium | Added |
| C23 | No valuation framework means no unqualified Strong ratings. | UNSUPPORTED until valuation work completed | Unknown | Added |
2026-04-26T05:56:22.736401Z ERROR codex_core::session: failed to record rollout items: thread 019dc858-20b3-7063-8211-177096e4bc06 not found
tokens used
218,963


---

# claude: round_1_claude_revision

Timestamp: 2026-04-25T22:58:53

(Note: write permission to `claim_register.md` was not granted, so CDR-17 through CDR-25 above are proposed rows for the next register update — the round-2 revisions remain captured in this response.)

---

**Closing**: The Codex critique correctly forced me to separate **structural bear arguments** (CPU equities trade as AI capex beta; merchant x86 faces real captive-ARM substitution at hyperscalers; OEM/ODM AI-server economics are margin-thin where confirmed) from **bear quantifications I had no source for** (3–7% BOM, sub-20% EPYC growth, Sierra Forest mix). The structural arguments survive at Medium confidence; the quantifications are withdrawn. The most material verdict change is **Intel: Avoid → Tactical Watchlist (bear bias)** on the strength of S-02 and S-19, and **Arm: Avoid → Verdict deferred** because I cannot defend the valuation claim without a model.

web search: 
web search: https://www.intc.com/news-events/press-releases/detail/1767/intel-reports-first-quarter-2026-financial-results
web search: 
web search: '1 billion Neoverse cores' in https://newsroom.arm.com/news/arm-q3-fye26-results
web search: 
web search: https://investors.delltechnologies.com/news-releases/news-release-details/dell-technologies-delivers-fourth-quarter-and-full-year-fiscal-3
web search: 
web search: 'Gross margin' in https://ir.supermicro.com/news/news-details/2026/Supermicro-Announces-Second-Quarter-Fiscal-Year-2026-Financial-Results/default.aspx
web search: 
web search: https://www.amd.com/en/newsroom/press-releases/2026-2-3-amd-reports-fourth-quarter-and-full-year-2025-fina.html
web search: 
web search: 'Data Center segment revenue' in https://www.amd.com/en/newsroom/press-releases/2026-2-3-amd-reports-fourth-quarter-and-full-year-2025-fina.html
web search: 
web search: TSMC Q4 2025 earnings call transcript CoWoS demand exceeds supply 2026 official
web search: 
web search: site:pr.tsmc.com Q1 2026 TSMC Reports First Quarter EPS NT 2026 April 16 PDF
web search: 
web search: finance: AMD
web search: 
web search: finance: AMD
web search: 
web search: https://www.qualcomm.com/news/releases/2017/11/qualcomm-datacenter-technologies-announces-commercial-shipment-qualcomm
web search: 
web search: https://investors.broadcom.com/news-releases/news-release-details/broadcom-inc-announces-fourth-quarter-and-fiscal-year-2025
web search: 
web search: 'Data center' in https://investor.marvell.com/news-events/press-releases/detail/1011/marvell-technology-inc-reports-fourth-quarter-and-fiscal-year-2026-financial-results
web search: 
web search: Super Micro Computer 2025 10-K delayed auditor resigned SEC investigation official 2026 filing
codex
I found one important update beyond the existing source log: Supermicro now has an April 2026 independent-director investigation tied to an export-control indictment, so treating SMCI’s 2024 accounting delay as the only governance issue would be stale. I’m going to add round-2 challenge rows and the incremental sources to the local register/log.
apply patch
patch: completed
/mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/sources/source_log.md
diff --git a//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/sources/source_log.md b//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/sources/source_log.md
index 61fbc5b1877cffb5173d17ea67b6b7cfda9d8157..54e92abc4492d20314734dc50a84e92902d01894
--- a//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/sources/source_log.md
+++ b//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/sources/source_log.md
@@ -23,3 +23,8 @@
 | S-17 | https://investor.marvell.com/news-events/press-releases/detail/1011/marvell-technology-inc-reports-fourth-quarter-and-fiscal-year-2026-financial-results | Company earnings release | 2026-03-05 | Marvell FY2026 revenue growth and data center share of revenue | High |
 | S-18 | https://www.sec.gov/Archives/edgar/data/0000804328/000080432825000085/qcom-20250928.htm | SEC 10-K | 2025-11-05 | Qualcomm Oryon/data center product intent and segment context | High |
 | S-19 | https://newsroom.intel.com/data-center/intel-xeon-6-used-as-host-cpus-in-nvidia-dgx-rubin-nvl8-systems | Company product announcement | 2026-03-16 | Intel Xeon 6 host CPU role in NVIDIA DGX Rubin NVL8 systems | High for Intel claim |
+| S-20 | https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-04/bd8eb0403902fdea59a2f5e390e48d010b50edc9/1Q26%20EarningsRelease_WoG.pdf | Company earnings release | 2026-04-16 | TSMC Q1 2026 revenue, margin, advanced-node revenue mix | High |
+| S-21 | https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-04/9f060092ba29ff3630cfdaefd67774026195e135/1Q26ManagementReport.pdf | Company management report | 2026-04-16 | TSMC Q1 2026 platform mix; HPC share of revenue | High |
+| S-22 | https://www.hpe.com/us/en/newsroom/press-release/2025/07/hewlett-packard-enterprise-closes-acquisition-of-juniper-networks-to-offer-industry-leading-comprehensive-cloud-native-ai-driven-portfolio.html | Company press release | 2025-07-02 | HPE Juniper close; networking-driven AI infrastructure strategy | High |
+| S-23 | https://www.qualcomm.com/news/releases/2017/11/qualcomm-datacenter-technologies-announces-commercial-shipment-qualcomm | Company product announcement | 2017-11-07 | Qualcomm prior Centriq server CPU commercialization attempt | High but stale; historical context only |
+| S-24 | https://ir.supermicro.com/news/news-details/2026/Supermicro-Provides-Update-on-Investigation-by-Independent-Board-Directors/default.aspx | Company press release | 2026-04-07 | Supermicro independent-director investigation tied to export-control indictment of former associated individuals | High for company disclosure |

diff --git a//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/sources/source_log.md b//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/sources/source_log.md
index 61fbc5b1877cffb5173d17ea67b6b7cfda9d8157..54e92abc4492d20314734dc50a84e92902d01894
--- a//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/sources/source_log.md
+++ b//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/sources/source_log.md
@@ -23,3 +23,8 @@
 | S-17 | https://investor.marvell.com/news-events/press-releases/detail/1011/marvell-technology-inc-reports-fourth-quarter-and-fiscal-year-2026-financial-results | Company earnings release | 2026-03-05 | Marvell FY2026 revenue growth and data center share of revenue | High |
 | S-18 | https://www.sec.gov/Archives/edgar/data/0000804328/000080432825000085/qcom-20250928.htm | SEC 10-K | 2025-11-05 | Qualcomm Oryon/data center product intent and segment context | High |
 | S-19 | https://newsroom.intel.com/data-center/intel-xeon-6-used-as-host-cpus-in-nvidia-dgx-rubin-nvl8-systems | Company product announcement | 2026-03-16 | Intel Xeon 6 host CPU role in NVIDIA DGX Rubin NVL8 systems | High for Intel claim |
+| S-20 | https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-04/bd8eb0403902fdea59a2f5e390e48d010b50edc9/1Q26%20EarningsRelease_WoG.pdf | Company earnings release | 2026-04-16 | TSMC Q1 2026 revenue, margin, advanced-node revenue mix | High |
+| S-21 | https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-04/9f060092ba29ff3630cfdaefd67774026195e135/1Q26ManagementReport.pdf | Company management report | 2026-04-16 | TSMC Q1 2026 platform mix; HPC share of revenue | High |
+| S-22 | https://www.hpe.com/us/en/newsroom/press-release/2025/07/hewlett-packard-enterprise-closes-acquisition-of-juniper-networks-to-offer-industry-leading-comprehensive-cloud-native-ai-driven-portfolio.html | Company press release | 2025-07-02 | HPE Juniper close; networking-driven AI infrastructure strategy | High |
+| S-23 | https://www.qualcomm.com/news/releases/2017/11/qualcomm-datacenter-technologies-announces-commercial-shipment-qualcomm | Company product announcement | 2017-11-07 | Qualcomm prior Centriq server CPU commercialization attempt | High but stale; historical context only |
+| S-24 | https://ir.supermicro.com/news/news-details/2026/Supermicro-Provides-Update-on-Investigation-by-Independent-Board-Directors/default.aspx | Company press release | 2026-04-07 | Supermicro independent-director investigation tied to export-control indictment of former associated individuals | High for company disclosure |

apply patch
patch: completed
/mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/claims/claim_register.md
diff --git a//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/claims/claim_register.md b//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/claims/claim_register.md
index b5b76759dc0441e2e535d024c765470a4d909c68..abb73018038a0b1353839f46db64bbdf12798599
--- a//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/claims/claim_register.md
+++ b//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/claims/claim_register.md
@@ -18,3 +18,14 @@
 | CDR-14 | Dell is the highest-quality OEM and the only OEM worth Watchlist status. | Dell / OEMs | Ranking / quality | S-07 supports explicit AI orders/backlog and ISG growth; no peer valuation/quality scorecard cited | Medium-Low | Codex round 1 opposition | PARTIALLY SUPPORTED; needs peer scorecard and AI-server margin disclosure |
 | CDR-15 | Broadcom and Marvell should be excluded from the CPU framework. | Broadcom / Marvell | Universe definition | S-16 and S-17 confirm AI custom silicon / data center exposure, not CPU revenue | Medium | Codex round 1 opposition | TOO NARROW; exclude from pure CPU revenue, include as substitution and relative-return benchmarks |
 | CDR-16 | Hyperscaler capex may decelerate in 2H26 and hit OEM/ODM and merchant CPU first. | Industry | Cycle risk | Claude round 1 scenario; S-03, S-04, S-05, S-06 show high 2026 capex guidance | Low | Codex round 1 opposition | UNSUPPORTED SCENARIO; retain as bear case only |
+| CDR-17 | CPU equities trade as AI capex beta. | Industry / CPU universe | Valuation / factor exposure | Claude round 2 closing; no equity-factor regression or CPU revenue bridge cited | Low | Codex round 2 opposition | UNSUPPORTED as an investment claim; test stock sensitivity, backlog conversion, and CPU revenue beta before using in valuation |
+| CDR-18 | Merchant x86 faces real captive-ARM substitution at hyperscalers. | AMD / Intel / Arm | Market share / substitution | S-11, S-13, S-14 support directionally; no independent displaced-socket or displaced-revenue estimate cited | Medium | Codex round 2 opposition | PARTIALLY SUPPORTED; requires hyperscaler-by-hyperscaler merchant socket displacement and Arm royalty-dollar impact |
+| CDR-19 | OEM/ODM AI-server economics are margin-thin where confirmed. | SMCI / Wiwynn / Dell / Quanta / Inventec | Margin / quality | S-08 and S-09 confirm low recent GM at SMCI/Wiwynn; S-07 shows Dell ISG operating margin is materially higher | Medium | Codex round 2 opposition | PARTIALLY SUPPORTED; do not generalize beyond confirmed companies; split gross margin, operating margin, and cash conversion |
+| CDR-20 | Intel should move from Avoid to Tactical Watchlist on Q1 DCAI growth and the DGX Rubin NVL8 Xeon role. | Intel | Ranking / revenue quality | S-02 confirms DCAI +22% YoY and management CPU demand framing; S-19 confirms DGX Rubin NVL8 host CPU role | Medium-Low | Codex round 2 opposition | PREMATURE; facts are confirmed but not sufficient without two-year DCAI stack, product mix, ASP, margins, design-win volume, and valuation |
+| CDR-21 | Arm verdict should be deferred because valuation cannot be defended without a model. | Arm | Valuation / process | Claude round 2 closing; S-10 confirms revenue and royalty growth but not valuation or server royalty dollars | High for process fix / Unknown for investment conclusion | Codex round 2 opposition | VALID PROCESS FIX; also requires royalty-dollar model, Arm China/customer concentration, and hyperscaler adoption economics |
+| CDR-22 | Prior bear quantifications on AI-server CPU BOM, sub-20% EPYC growth, and Sierra Forest mix are withdrawn. | Industry / AMD / Intel | Evidence hygiene | Claude round 2 closing; relates to CDR-01, CDR-06, CDR-07 | High | Codex round 2 opposition | RESOLVED AS WITHDRAWN; do not reintroduce without platform BOM, EPYC/Instinct split, and Intel mix/ASP evidence |
+| CDR-23 | CPU dollars per AI rack versus traditional 2S server rack remain the central missing evidence. | Industry | Architecture / BOM / attach rate | CDR-01, CDR-05, CDR-08; S-12 and S-19 provide platform architecture facts but not CPU dollars | High evidence gap / Unknown conclusion | Codex round 2 opposition | FATAL GAP; build rack-level CPU count, CPU SKU/ASP, host ratio, memory attach, and CPU % of system value by platform |
+| CDR-24 | TSMC remains the best diversified CPU-related AI silicon exposure. | TSMC | Ranking / substitution | S-20 confirms Q1 2026 growth and margins; S-21 confirms HPC platform share; CPU-specific revenue is not isolated | Medium-Low | Codex round 2 opposition | OVERBROAD; positive AI/HPC exposure is confirmed, but CPU-thesis inference and valuation require separate work |
+| CDR-25 | Broadcom and Marvell belong in the CPU memo as substitutes and relative-return benchmarks, not CPU longs. | Broadcom / Marvell | Universe definition / substitution | S-16 and S-17 confirm AI custom silicon and data-center exposure; neither confirms material CPU revenue | Medium-High | Codex round 2 opposition | ACCEPTED WITH LIMITS; classify as substitution/benchmark exposure and exclude from pure CPU ranking |
+| CDR-26 | Qualcomm remains Avoid for a CPU-pure thesis, but its data-center CPU option value is not zero. | Qualcomm | Ranking / optionality | S-18 confirms data-center business and custom CPU-core intent; S-23 confirms prior Centriq server CPU commercialization history | Medium | Codex round 2 opposition | PARTIALLY SUPPORTED; avoid until customer/revenue proof, but track new design wins and separate accelerator from CPU claims |
+| CDR-27 | Supermicro governance/accounting overhang is historical and closed. | Supermicro | Governance / quality | S-24 shows a current independent-director investigation; prior 2025 filing remediation does not settle 2026 export-control-related risk | Medium | Codex round 2 opposition | STALE / INCOMPLETE; update SMCI quality thesis for current investigation and distinguish company disclosure from allegation |
diff --git a//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/sources/source_log.md b//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/sources/source_log.md
index 61fbc5b1877cffb5173d17ea67b6b7cfda9d8157..54e92abc4492d20314734dc50a84e92902d01894
--- a//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/sources/source_log.md
+++ b//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/sources/source_log.md
@@ -23,3 +23,8 @@
 | S-17 | https://investor.marvell.com/news-events/press-releases/detail/1011/marvell-technology-inc-reports-fourth-quarter-and-fiscal-year-2026-financial-results | Company earnings release | 2026-03-05 | Marvell FY2026 revenue growth and data center share of revenue | High |
 | S-18 | https://www.sec.gov/Archives/edgar/data/0000804328/000080432825000085/qcom-20250928.htm | SEC 10-K | 2025-11-05 | Qualcomm Oryon/data center product intent and segment context | High |
 | S-19 | https://newsroom.intel.com/data-center/intel-xeon-6-used-as-host-cpus-in-nvidia-dgx-rubin-nvl8-systems | Company product announcement | 2026-03-16 | Intel Xeon 6 host CPU role in NVIDIA DGX Rubin NVL8 systems | High for Intel claim |
+| S-20 | https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-04/bd8eb0403902fdea59a2f5e390e48d010b50edc9/1Q26%20EarningsRelease_WoG.pdf | Company earnings release | 2026-04-16 | TSMC Q1 2026 revenue, margin, advanced-node revenue mix | High |
+| S-21 | https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-04/9f060092ba29ff3630cfdaefd67774026195e135/1Q26ManagementReport.pdf | Company management report | 2026-04-16 | TSMC Q1 2026 platform mix; HPC share of revenue | High |
+| S-22 | https://www.hpe.com/us/en/newsroom/press-release/2025/07/hewlett-packard-enterprise-closes-acquisition-of-juniper-networks-to-offer-industry-leading-comprehensive-cloud-native-ai-driven-portfolio.html | Company press release | 2025-07-02 | HPE Juniper close; networking-driven AI infrastructure strategy | High |
+| S-23 | https://www.qualcomm.com/news/releases/2017/11/qualcomm-datacenter-technologies-announces-commercial-shipment-qualcomm | Company product announcement | 2017-11-07 | Qualcomm prior Centriq server CPU commercialization attempt | High but stale; historical context only |
+| S-24 | https://ir.supermicro.com/news/news-details/2026/Supermicro-Provides-Update-on-Investigation-by-Independent-Board-Directors/default.aspx | Company press release | 2026-04-07 | Supermicro independent-director investigation tied to export-control indictment of former associated individuals | High for company disclosure |

diff --git a//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/claims/claim_register.md b//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/claims/claim_register.md
index b5b76759dc0441e2e535d024c765470a4d909c68..abb73018038a0b1353839f46db64bbdf12798599
--- a//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/claims/claim_register.md
+++ b//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/claims/claim_register.md
@@ -18,3 +18,14 @@
 | CDR-14 | Dell is the highest-quality OEM and the only OEM worth Watchlist status. | Dell / OEMs | Ranking / quality | S-07 supports explicit AI orders/backlog and ISG growth; no peer valuation/quality scorecard cited | Medium-Low | Codex round 1 opposition | PARTIALLY SUPPORTED; needs peer scorecard and AI-server margin disclosure |
 | CDR-15 | Broadcom and Marvell should be excluded from the CPU framework. | Broadcom / Marvell | Universe definition | S-16 and S-17 confirm AI custom silicon / data center exposure, not CPU revenue | Medium | Codex round 1 opposition | TOO NARROW; exclude from pure CPU revenue, include as substitution and relative-return benchmarks |
 | CDR-16 | Hyperscaler capex may decelerate in 2H26 and hit OEM/ODM and merchant CPU first. | Industry | Cycle risk | Claude round 1 scenario; S-03, S-04, S-05, S-06 show high 2026 capex guidance | Low | Codex round 1 opposition | UNSUPPORTED SCENARIO; retain as bear case only |
+| CDR-17 | CPU equities trade as AI capex beta. | Industry / CPU universe | Valuation / factor exposure | Claude round 2 closing; no equity-factor regression or CPU revenue bridge cited | Low | Codex round 2 opposition | UNSUPPORTED as an investment claim; test stock sensitivity, backlog conversion, and CPU revenue beta before using in valuation |
+| CDR-18 | Merchant x86 faces real captive-ARM substitution at hyperscalers. | AMD / Intel / Arm | Market share / substitution | S-11, S-13, S-14 support directionally; no independent displaced-socket or displaced-revenue estimate cited | Medium | Codex round 2 opposition | PARTIALLY SUPPORTED; requires hyperscaler-by-hyperscaler merchant socket displacement and Arm royalty-dollar impact |
+| CDR-19 | OEM/ODM AI-server economics are margin-thin where confirmed. | SMCI / Wiwynn / Dell / Quanta / Inventec | Margin / quality | S-08 and S-09 confirm low recent GM at SMCI/Wiwynn; S-07 shows Dell ISG operating margin is materially higher | Medium | Codex round 2 opposition | PARTIALLY SUPPORTED; do not generalize beyond confirmed companies; split gross margin, operating margin, and cash conversion |
+| CDR-20 | Intel should move from Avoid to Tactical Watchlist on Q1 DCAI growth and the DGX Rubin NVL8 Xeon role. | Intel | Ranking / revenue quality | S-02 confirms DCAI +22% YoY and management CPU demand framing; S-19 confirms DGX Rubin NVL8 host CPU role | Medium-Low | Codex round 2 opposition | PREMATURE; facts are confirmed but not sufficient without two-year DCAI stack, product mix, ASP, margins, design-win volume, and valuation |
+| CDR-21 | Arm verdict should be deferred because valuation cannot be defended without a model. | Arm | Valuation / process | Claude round 2 closing; S-10 confirms revenue and royalty growth but not valuation or server royalty dollars | High for process fix / Unknown for investment conclusion | Codex round 2 opposition | VALID PROCESS FIX; also requires royalty-dollar model, Arm China/customer concentration, and hyperscaler adoption economics |
+| CDR-22 | Prior bear quantifications on AI-server CPU BOM, sub-20% EPYC growth, and Sierra Forest mix are withdrawn. | Industry / AMD / Intel | Evidence hygiene | Claude round 2 closing; relates to CDR-01, CDR-06, CDR-07 | High | Codex round 2 opposition | RESOLVED AS WITHDRAWN; do not reintroduce without platform BOM, EPYC/Instinct split, and Intel mix/ASP evidence |
+| CDR-23 | CPU dollars per AI rack versus traditional 2S server rack remain the central missing evidence. | Industry | Architecture / BOM / attach rate | CDR-01, CDR-05, CDR-08; S-12 and S-19 provide platform architecture facts but not CPU dollars | High evidence gap / Unknown conclusion | Codex round 2 opposition | FATAL GAP; build rack-level CPU count, CPU SKU/ASP, host ratio, memory attach, and CPU % of system value by platform |
+| CDR-24 | TSMC remains the best diversified CPU-related AI silicon exposure. | TSMC | Ranking / substitution | S-20 confirms Q1 2026 growth and margins; S-21 confirms HPC platform share; CPU-specific revenue is not isolated | Medium-Low | Codex round 2 opposition | OVERBROAD; positive AI/HPC exposure is confirmed, but CPU-thesis inference and valuation require separate work |
+| CDR-25 | Broadcom and Marvell belong in the CPU memo as substitutes and relative-return benchmarks, not CPU longs. | Broadcom / Marvell | Universe definition / substitution | S-16 and S-17 confirm AI custom silicon and data-center exposure; neither confirms material CPU revenue | Medium-High | Codex round 2 opposition | ACCEPTED WITH LIMITS; classify as substitution/benchmark exposure and exclude from pure CPU ranking |
+| CDR-26 | Qualcomm remains Avoid for a CPU-pure thesis, but its data-center CPU option value is not zero. | Qualcomm | Ranking / optionality | S-18 confirms data-center business and custom CPU-core intent; S-23 confirms prior Centriq server CPU commercialization history | Medium | Codex round 2 opposition | PARTIALLY SUPPORTED; avoid until customer/revenue proof, but track new design wins and separate accelerator from CPU claims |
+| CDR-27 | Supermicro governance/accounting overhang is historical and closed. | Supermicro | Governance / quality | S-24 shows a current independent-director investigation; prior 2025 filing remediation does not settle 2026 export-control-related risk | Medium | Codex round 2 opposition | STALE / INCOMPLETE; update SMCI quality thesis for current investigation and distinguish company disclosure from allegation |
diff --git a//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/sources/source_log.md b//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/sources/source_log.md
index 61fbc5b1877cffb5173d17ea67b6b7cfda9d8157..54e92abc4492d20314734dc50a84e92902d01894
--- a//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/sources/source_log.md
+++ b//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/sources/source_log.md
@@ -23,3 +23,8 @@
 | S-17 | https://investor.marvell.com/news-events/press-releases/detail/1011/marvell-technology-inc-reports-fourth-quarter-and-fiscal-year-2026-financial-results | Company earnings release | 2026-03-05 | Marvell FY2026 revenue growth and data center share of revenue | High |
 | S-18 | https://www.sec.gov/Archives/edgar/data/0000804328/000080432825000085/qcom-20250928.htm | SEC 10-K | 2025-11-05 | Qualcomm Oryon/data center product intent and segment context | High |
 | S-19 | https://newsroom.intel.com/data-center/intel-xeon-6-used-as-host-cpus-in-nvidia-dgx-rubin-nvl8-systems | Company product announcement | 2026-03-16 | Intel Xeon 6 host CPU role in NVIDIA DGX Rubin NVL8 systems | High for Intel claim |
+| S-20 | https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-04/bd8eb0403902fdea59a2f5e390e48d010b50edc9/1Q26%20EarningsRelease_WoG.pdf | Company earnings release | 2026-04-16 | TSMC Q1 2026 revenue, margin, advanced-node revenue mix | High |
+| S-21 | https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-04/9f060092ba29ff3630cfdaefd67774026195e135/1Q26ManagementReport.pdf | Company management report | 2026-04-16 | TSMC Q1 2026 platform mix; HPC share of revenue | High |
+| S-22 | https://www.hpe.com/us/en/newsroom/press-release/2025/07/hewlett-packard-enterprise-closes-acquisition-of-juniper-networks-to-offer-industry-leading-comprehensive-cloud-native-ai-driven-portfolio.html | Company press release | 2025-07-02 | HPE Juniper close; networking-driven AI infrastructure strategy | High |
+| S-23 | https://www.qualcomm.com/news/releases/2017/11/qualcomm-datacenter-technologies-announces-commercial-shipment-qualcomm | Company product announcement | 2017-11-07 | Qualcomm prior Centriq server CPU commercialization attempt | High but stale; historical context only |
+| S-24 | https://ir.supermicro.com/news/news-details/2026/Supermicro-Provides-Update-on-Investigation-by-Independent-Board-Directors/default.aspx | Company press release | 2026-04-07 | Supermicro independent-director investigation tied to export-control indictment of former associated individuals | High for company disclosure |

codex
The register now has CDR-17 through CDR-27, covering the round-2 closing claims plus Qualcomm and SMCI stale-risk updates. I’m checking the diff and then I’ll produce the adversarial Markdown response with source-linked claim challenges.
exec
/usr/bin/zsh -lc 'git diff -- cpu-investment-research-2/claims/claim_register.md cpu-investment-research-2/sources/source_log.md' in /mnt/c/Users/hyc97/workspace/Ecclesia/CPU
exec
/usr/bin/zsh -lc "nl -ba cpu-investment-research-2/sources/source_log.md | sed -n '1,80p'" in /mnt/c/Users/hyc97/workspace/Ecclesia/CPU
exec
/usr/bin/zsh -lc "nl -ba cpu-investment-research-2/claims/claim_register.md | sed -n '1,80p'" in /mnt/c/Users/hyc97/workspace/Ecclesia/CPU
diff --git a//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/claims/claim_register.md b//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/claims/claim_register.md
index b5b76759dc0441e2e535d024c765470a4d909c68..abb73018038a0b1353839f46db64bbdf12798599
--- a//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/claims/claim_register.md
+++ b//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/claims/claim_register.md
@@ -18,3 +18,14 @@
 | CDR-14 | Dell is the highest-quality OEM and the only OEM worth Watchlist status. | Dell / OEMs | Ranking / quality | S-07 supports explicit AI orders/backlog and ISG growth; no peer valuation/quality scorecard cited | Medium-Low | Codex round 1 opposition | PARTIALLY SUPPORTED; needs peer scorecard and AI-server margin disclosure |
 | CDR-15 | Broadcom and Marvell should be excluded from the CPU framework. | Broadcom / Marvell | Universe definition | S-16 and S-17 confirm AI custom silicon / data center exposure, not CPU revenue | Medium | Codex round 1 opposition | TOO NARROW; exclude from pure CPU revenue, include as substitution and relative-return benchmarks |
 | CDR-16 | Hyperscaler capex may decelerate in 2H26 and hit OEM/ODM and merchant CPU first. | Industry | Cycle risk | Claude round 1 scenario; S-03, S-04, S-05, S-06 show high 2026 capex guidance | Low | Codex round 1 opposition | UNSUPPORTED SCENARIO; retain as bear case only |
+| CDR-17 | CPU equities trade as AI capex beta. | Industry / CPU universe | Valuation / factor exposure | Claude round 2 closing; no equity-factor regression or CPU revenue bridge cited | Low | Codex round 2 opposition | UNSUPPORTED as an investment claim; test stock sensitivity, backlog conversion, and CPU revenue beta before using in valuation |
+| CDR-18 | Merchant x86 faces real captive-ARM substitution at hyperscalers. | AMD / Intel / Arm | Market share / substitution | S-11, S-13, S-14 support directionally; no independent displaced-socket or displaced-revenue estimate cited | Medium | Codex round 2 opposition | PARTIALLY SUPPORTED; requires hyperscaler-by-hyperscaler merchant socket displacement and Arm royalty-dollar impact |
+| CDR-19 | OEM/ODM AI-server economics are margin-thin where confirmed. | SMCI / Wiwynn / Dell / Quanta / Inventec | Margin / quality | S-08 and S-09 confirm low recent GM at SMCI/Wiwynn; S-07 shows Dell ISG operating margin is materially higher | Medium | Codex round 2 opposition | PARTIALLY SUPPORTED; do not generalize beyond confirmed companies; split gross margin, operating margin, and cash conversion |
+| CDR-20 | Intel should move from Avoid to Tactical Watchlist on Q1 DCAI growth and the DGX Rubin NVL8 Xeon role. | Intel | Ranking / revenue quality | S-02 confirms DCAI +22% YoY and management CPU demand framing; S-19 confirms DGX Rubin NVL8 host CPU role | Medium-Low | Codex round 2 opposition | PREMATURE; facts are confirmed but not sufficient without two-year DCAI stack, product mix, ASP, margins, design-win volume, and valuation |
+| CDR-21 | Arm verdict should be deferred because valuation cannot be defended without a model. | Arm | Valuation / process | Claude round 2 closing; S-10 confirms revenue and royalty growth but not valuation or server royalty dollars | High for process fix / Unknown for investment conclusion | Codex round 2 opposition | VALID PROCESS FIX; also requires royalty-dollar model, Arm China/customer concentration, and hyperscaler adoption economics |
+| CDR-22 | Prior bear quantifications on AI-server CPU BOM, sub-20% EPYC growth, and Sierra Forest mix are withdrawn. | Industry / AMD / Intel | Evidence hygiene | Claude round 2 closing; relates to CDR-01, CDR-06, CDR-07 | High | Codex round 2 opposition | RESOLVED AS WITHDRAWN; do not reintroduce without platform BOM, EPYC/Instinct split, and Intel mix/ASP evidence |
+| CDR-23 | CPU dollars per AI rack versus traditional 2S server rack remain the central missing evidence. | Industry | Architecture / BOM / attach rate | CDR-01, CDR-05, CDR-08; S-12 and S-19 provide platform architecture facts but not CPU dollars | High evidence gap / Unknown conclusion | Codex round 2 opposition | FATAL GAP; build rack-level CPU count, CPU SKU/ASP, host ratio, memory attach, and CPU % of system value by platform |
+| CDR-24 | TSMC remains the best diversified CPU-related AI silicon exposure. | TSMC | Ranking / substitution | S-20 confirms Q1 2026 growth and margins; S-21 confirms HPC platform share; CPU-specific revenue is not isolated | Medium-Low | Codex round 2 opposition | OVERBROAD; positive AI/HPC exposure is confirmed, but CPU-thesis inference and valuation require separate work |
+| CDR-25 | Broadcom and Marvell belong in the CPU memo as substitutes and relative-return benchmarks, not CPU longs. | Broadcom / Marvell | Universe definition / substitution | S-16 and S-17 confirm AI custom silicon and data-center exposure; neither confirms material CPU revenue | Medium-High | Codex round 2 opposition | ACCEPTED WITH LIMITS; classify as substitution/benchmark exposure and exclude from pure CPU ranking |
+| CDR-26 | Qualcomm remains Avoid for a CPU-pure thesis, but its data-center CPU option value is not zero. | Qualcomm | Ranking / optionality | S-18 confirms data-center business and custom CPU-core intent; S-23 confirms prior Centriq server CPU commercialization history | Medium | Codex round 2 opposition | PARTIALLY SUPPORTED; avoid until customer/revenue proof, but track new design wins and separate accelerator from CPU claims |
+| CDR-27 | Supermicro governance/accounting overhang is historical and closed. | Supermicro | Governance / quality | S-24 shows a current independent-director investigation; prior 2025 filing remediation does not settle 2026 export-control-related risk | Medium | Codex round 2 opposition | STALE / INCOMPLETE; update SMCI quality thesis for current investigation and distinguish company disclosure from allegation |
diff --git a//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/sources/source_log.md b//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/sources/source_log.md
index 61fbc5b1877cffb5173d17ea67b6b7cfda9d8157..54e92abc4492d20314734dc50a84e92902d01894
--- a//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/sources/source_log.md
+++ b//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/sources/source_log.md
@@ -23,3 +23,8 @@
 | S-17 | https://investor.marvell.com/news-events/press-releases/detail/1011/marvell-technology-inc-reports-fourth-quarter-and-fiscal-year-2026-financial-results | Company earnings release | 2026-03-05 | Marvell FY2026 revenue growth and data center share of revenue | High |
 | S-18 | https://www.sec.gov/Archives/edgar/data/0000804328/000080432825000085/qcom-20250928.htm | SEC 10-K | 2025-11-05 | Qualcomm Oryon/data center product intent and segment context | High |
 | S-19 | https://newsroom.intel.com/data-center/intel-xeon-6-used-as-host-cpus-in-nvidia-dgx-rubin-nvl8-systems | Company product announcement | 2026-03-16 | Intel Xeon 6 host CPU role in NVIDIA DGX Rubin NVL8 systems | High for Intel claim |
+| S-20 | https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-04/bd8eb0403902fdea59a2f5e390e48d010b50edc9/1Q26%20EarningsRelease_WoG.pdf | Company earnings release | 2026-04-16 | TSMC Q1 2026 revenue, margin, advanced-node revenue mix | High |
+| S-21 | https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-04/9f060092ba29ff3630cfdaefd67774026195e135/1Q26ManagementReport.pdf | Company management report | 2026-04-16 | TSMC Q1 2026 platform mix; HPC share of revenue | High |
+| S-22 | https://www.hpe.com/us/en/newsroom/press-release/2025/07/hewlett-packard-enterprise-closes-acquisition-of-juniper-networks-to-offer-industry-leading-comprehensive-cloud-native-ai-driven-portfolio.html | Company press release | 2025-07-02 | HPE Juniper close; networking-driven AI infrastructure strategy | High |
+| S-23 | https://www.qualcomm.com/news/releases/2017/11/qualcomm-datacenter-technologies-announces-commercial-shipment-qualcomm | Company product announcement | 2017-11-07 | Qualcomm prior Centriq server CPU commercialization attempt | High but stale; historical context only |
+| S-24 | https://ir.supermicro.com/news/news-details/2026/Supermicro-Provides-Update-on-Investigation-by-Independent-Board-Directors/default.aspx | Company press release | 2026-04-07 | Supermicro independent-director investigation tied to export-control indictment of former associated individuals | High for company disclosure |

 succeeded in 184ms:
     1	# Source Log
     2	
     3	Use this file to track source URLs, filings, earnings calls, market data sources, and unresolved evidence gaps.
     4	
     5	| ID | Source | Type | Date | Used For | Reliability |
     6	|---|---|---|---|---|---|
     7	| S-01 | https://www.amd.com/en/newsroom/press-releases/2026-2-3-amd-reports-fourth-quarter-and-full-year-2025-fina.html | Company earnings release | 2026-02-03 | AMD FY2025 Data Center revenue; EPYC + Instinct disclosure issue | High |
     8	| S-02 | https://www.intc.com/news-events/press-releases/detail/1767/intel-reports-first-quarter-2026-financial-results | Company earnings release | 2026-04-23 | Intel Q1 2026 DCAI revenue, management CPU demand framing, DGX Rubin NVL8 business highlight | High |
     9	| S-03 | https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q2 | Company earnings call transcript | 2026-01-28 | Microsoft FY26 Q2 capex and GPUs/CPUs wording | High |
    10	| S-04 | https://abc.xyz/investor/events/event-details/2026/2025-Q4-Earnings-Call-2026-Dr_C033hS6/default.aspx | Company earnings call transcript | 2026-02-04 | Alphabet 2026 capex guide and server/data-center allocation commentary | High |
    11	| S-05 | https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Fourth-Quarter-Results/default.aspx | Company earnings release | 2026-02-05 | Amazon 2026 capex guide | High |
    12	| S-06 | https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Fourth-Quarter-and-Full-Year-2025-Results/ | Company earnings release | 2026-01-28 | Meta 2026 capex guide | High |
    13	| S-07 | https://investors.delltechnologies.com/news-releases/news-release-details/dell-technologies-delivers-fourth-quarter-and-full-year-fiscal-3 | Company earnings release | 2026-02-26 | Dell FY26 AI server orders, shipments, backlog, ISG revenue and operating income | High |
    14	| S-08 | https://ir.supermicro.com/news/news-details/2026/Supermicro-Announces-Second-Quarter-Fiscal-Year-2026-Financial-Results/default.aspx | Company earnings release | 2026-02-03 | Supermicro Q2 FY2026 revenue and gross margin | High |
    15	| S-09 | https://www.wiwynn.com/news/wiwynn-reports-fourth-quarter-2025-unaudited-financial-results | Company unaudited financial release | 2026-03-03 | Wiwynn Q4 2025 gross margin, FY2025 revenue growth, AI product mix | Medium-High |
    16	| S-10 | https://newsroom.arm.com/news/arm-q3-fye26-results | Company earnings summary | 2026-02-04 | Arm Q3 FYE26 revenue, royalty growth, Neoverse cores, top-hyperscaler share management claim | Medium-High |
    17	| S-11 | https://www.aboutamazon.com/news/aws/aws-graviton-5-cpu-amazon-ec2/ | Company product announcement | 2025-12-04 | AWS Graviton share of new AWS CPU capacity | High for management claim |
    18	| S-12 | https://www.nvidia.com/en-us/data-center/gb200-nvl72/ | Company product page | 2026 crawled | NVIDIA GB200/GB300 Grace CPU counts and Arm architecture | High |
    19	| S-13 | https://azure.microsoft.com/en-us/blog/azure-cobalt-100-based-virtual-machines-are-now-generally-available/ | Company product announcement | 2024-10-16 | Microsoft Cobalt 100 GA and Arm-based Azure VM details | High |
    20	| S-14 | https://cloud.google.com/products/axion | Company product page | 2026 crawled | Google Axion custom Arm CPU and C4A/N4A instance details | High |
    21	| S-15 | https://www.gartner.com/en/documents/6998066 | Market research summary | 2025-09-26 | 2Q25 server shipments, vendor revenue, server-system ASP | Medium; paywalled analyst estimate |
    22	| S-16 | https://investors.broadcom.com/news-releases/news-release-details/broadcom-inc-announces-fourth-quarter-and-fiscal-year-2025 | Company earnings release | 2025-12-11 | Broadcom Q4 FY2025 AI semiconductor growth and AI revenue guide | High |
    23	| S-17 | https://investor.marvell.com/news-events/press-releases/detail/1011/marvell-technology-inc-reports-fourth-quarter-and-fiscal-year-2026-financial-results | Company earnings release | 2026-03-05 | Marvell FY2026 revenue growth and data center share of revenue | High |
    24	| S-18 | https://www.sec.gov/Archives/edgar/data/0000804328/000080432825000085/qcom-20250928.htm | SEC 10-K | 2025-11-05 | Qualcomm Oryon/data center product intent and segment context | High |
    25	| S-19 | https://newsroom.intel.com/data-center/intel-xeon-6-used-as-host-cpus-in-nvidia-dgx-rubin-nvl8-systems | Company product announcement | 2026-03-16 | Intel Xeon 6 host CPU role in NVIDIA DGX Rubin NVL8 systems | High for Intel claim |
    26	| S-20 | https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-04/bd8eb0403902fdea59a2f5e390e48d010b50edc9/1Q26%20EarningsRelease_WoG.pdf | Company earnings release | 2026-04-16 | TSMC Q1 2026 revenue, margin, advanced-node revenue mix | High |
    27	| S-21 | https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-04/9f060092ba29ff3630cfdaefd67774026195e135/1Q26ManagementReport.pdf | Company management report | 2026-04-16 | TSMC Q1 2026 platform mix; HPC share of revenue | High |
    28	| S-22 | https://www.hpe.com/us/en/newsroom/press-release/2025/07/hewlett-packard-enterprise-closes-acquisition-of-juniper-networks-to-offer-industry-leading-comprehensive-cloud-native-ai-driven-portfolio.html | Company press release | 2025-07-02 | HPE Juniper close; networking-driven AI infrastructure strategy | High |
    29	| S-23 | https://www.qualcomm.com/news/releases/2017/11/qualcomm-datacenter-technologies-announces-commercial-shipment-qualcomm | Company product announcement | 2017-11-07 | Qualcomm prior Centriq server CPU commercialization attempt | High but stale; historical context only |
    30	| S-24 | https://ir.supermicro.com/news/news-details/2026/Supermicro-Provides-Update-on-Investigation-by-Independent-Board-Directors/default.aspx | Company press release | 2026-04-07 | Supermicro independent-director investigation tied to export-control indictment of former associated individuals | High for company disclosure |

 succeeded in 189ms:
     1	# Claim Register
     2	
     3	| ID | Claim | Company | Category | Source | Confidence | Challenged By | Status |
     4	|---|---|---|---|---|---|---|---|
     5	| CDR-01 | CPU silicon is only 3-7% of AI server BOM / <5% of GB200-class rack BOM. | Industry | BOM / pricing | Claude round 1; no primary teardown cited | Low | Codex round 1 opposition | UNSUPPORTED; fatal to bear thesis until platform-level BOM is sourced |
     6	| CDR-02 | 60-70% of incremental hyperscaler compute capex flows into accelerated systems. | Industry | Capex allocation | Claude round 1 assumption | Low | Codex round 1 opposition | UNSUPPORTED; needs capex-to-server architecture bridge |
     7	| CDR-03 | Merchant x86 competes for a shrinking slice of incremental cloud CPU capacity. | AMD / Intel | Market share | S-10, S-11, S-13, S-14 support ARM adoption directionally; no independent share series cited | Medium-Low | Codex round 1 opposition | PARTIALLY SUPPORTED; requires Mercury/IDC/Omdia unit, revenue, and core-hour share |
     8	| CDR-04 | Nvidia AI rack architecture means ARM CPU displacement for x86. | Nvidia / Intel / AMD / Arm | Architecture | S-12 confirms GB200/GB300 use Grace Arm; S-19 confirms Xeon 6 host CPU in DGX Rubin NVL8 | Medium | Codex round 1 opposition | OVERBROAD; split by platform rather than treating all Nvidia systems as ARM-hosted |
     9	| CDR-05 | Custom ASIC racks have the lowest CPU intensity and are directly subtractive to merchant CPU vendors. | Broadcom / Marvell / hyperscalers | Substitution risk | Claude round 1; no TPU/Trainium/MAIA host-CPU counts cited | Low | Codex round 1 opposition | UNSUPPORTED; needs architecture attach data |
    10	| CDR-06 | AMD EPYC growth is probably sub-20%, with Instinct doing the heavy lifting. | AMD | Revenue mix | S-01 confirms Data Center includes EPYC and Instinct but not the split | Low | Codex round 1 opposition | UNSUPPORTED; do not use without EPYC/Instinct triangulation |
    11	| CDR-07 | Intel DCAI Q1 2026 strength may be mostly Sierra Forest mix / easy comp / low ASP host CPUs. | Intel | Revenue quality / ASP | S-02 confirms DCAI +22%; mix explanation is Claude inference | Low | Codex round 1 opposition | UNSUPPORTED; needs Intel product mix, ASP, and gross margin evidence |
    12	| CDR-08 | Server-system ASP inflation is not CPU ASP inflation. | Industry | Pricing | S-15 confirms system ASP +92.8%; CPU ASP split unavailable | Medium-High | Codex round 1 opposition | VALID CAVEAT; needs CPU-specific price dataset before bullish or bearish pricing claims |
    13	| CDR-09 | 10-20% server CPU price hikes since March 2026. | Intel / AMD | Pricing | Secondary press / channel rumor; no company confirmation in register | Low | Codex round 1 opposition | MARKET RUMOR; do not model as fact |
    14	| CDR-10 | Arm royalty per server CPU is low single-digit percentage of CPU ASP. | Arm | Unit economics | Claude round 1; no contract / AALA / CSS economics cited | Low | Codex round 1 opposition | UNSUPPORTED; needs royalty-dollar model |
    15	| CDR-11 | Arm Holdings is an Avoid on valuation because the multiple is extreme. | Arm | Valuation | Claude round 1; no current multiple table or DCF cited | Unknown | Codex round 1 opposition | UNSUPPORTED; needs price, share count, forward revenue/EPS/FCF scenarios |
    16	| CDR-12 | TSMC is priced for AI upside. | TSMC | Valuation | Claude round 1; no valuation comp table cited | Unknown | Codex round 1 opposition | UNSUPPORTED; needs valuation and scenario analysis |
    17	| CDR-13 | OEM/ODM gross margins will remain 6-10% and not recover. | SMCI / Wiwynn / Dell / Quanta / Inventec | Margin | S-08 and S-09 support SMCI/Wiwynn low recent GM; Dell evidence in S-07 is more mixed | Medium-Low | Codex round 1 opposition | OVERGENERALIZED; split by company, product mix, and operating margin |
    18	| CDR-14 | Dell is the highest-quality OEM and the only OEM worth Watchlist status. | Dell / OEMs | Ranking / quality | S-07 supports explicit AI orders/backlog and ISG growth; no peer valuation/quality scorecard cited | Medium-Low | Codex round 1 opposition | PARTIALLY SUPPORTED; needs peer scorecard and AI-server margin disclosure |
    19	| CDR-15 | Broadcom and Marvell should be excluded from the CPU framework. | Broadcom / Marvell | Universe definition | S-16 and S-17 confirm AI custom silicon / data center exposure, not CPU revenue | Medium | Codex round 1 opposition | TOO NARROW; exclude from pure CPU revenue, include as substitution and relative-return benchmarks |
    20	| CDR-16 | Hyperscaler capex may decelerate in 2H26 and hit OEM/ODM and merchant CPU first. | Industry | Cycle risk | Claude round 1 scenario; S-03, S-04, S-05, S-06 show high 2026 capex guidance | Low | Codex round 1 opposition | UNSUPPORTED SCENARIO; retain as bear case only |
    21	| CDR-17 | CPU equities trade as AI capex beta. | Industry / CPU universe | Valuation / factor exposure | Claude round 2 closing; no equity-factor regression or CPU revenue bridge cited | Low | Codex round 2 opposition | UNSUPPORTED as an investment claim; test stock sensitivity, backlog conversion, and CPU revenue beta before using in valuation |
    22	| CDR-18 | Merchant x86 faces real captive-ARM substitution at hyperscalers. | AMD / Intel / Arm | Market share / substitution | S-11, S-13, S-14 support directionally; no independent displaced-socket or displaced-revenue estimate cited | Medium | Codex round 2 opposition | PARTIALLY SUPPORTED; requires hyperscaler-by-hyperscaler merchant socket displacement and Arm royalty-dollar impact |
    23	| CDR-19 | OEM/ODM AI-server economics are margin-thin where confirmed. | SMCI / Wiwynn / Dell / Quanta / Inventec | Margin / quality | S-08 and S-09 confirm low recent GM at SMCI/Wiwynn; S-07 shows Dell ISG operating margin is materially higher | Medium | Codex round 2 opposition | PARTIALLY SUPPORTED; do not generalize beyond confirmed companies; split gross margin, operating margin, and cash conversion |
    24	| CDR-20 | Intel should move from Avoid to Tactical Watchlist on Q1 DCAI growth and the DGX Rubin NVL8 Xeon role. | Intel | Ranking / revenue quality | S-02 confirms DCAI +22% YoY and management CPU demand framing; S-19 confirms DGX Rubin NVL8 host CPU role | Medium-Low | Codex round 2 opposition | PREMATURE; facts are confirmed but not sufficient without two-year DCAI stack, product mix, ASP, margins, design-win volume, and valuation |
    25	| CDR-21 | Arm verdict should be deferred because valuation cannot be defended without a model. | Arm | Valuation / process | Claude round 2 closing; S-10 confirms revenue and royalty growth but not valuation or server royalty dollars | High for process fix / Unknown for investment conclusion | Codex round 2 opposition | VALID PROCESS FIX; also requires royalty-dollar model, Arm China/customer concentration, and hyperscaler adoption economics |
    26	| CDR-22 | Prior bear quantifications on AI-server CPU BOM, sub-20% EPYC growth, and Sierra Forest mix are withdrawn. | Industry / AMD / Intel | Evidence hygiene | Claude round 2 closing; relates to CDR-01, CDR-06, CDR-07 | High | Codex round 2 opposition | RESOLVED AS WITHDRAWN; do not reintroduce without platform BOM, EPYC/Instinct split, and Intel mix/ASP evidence |
    27	| CDR-23 | CPU dollars per AI rack versus traditional 2S server rack remain the central missing evidence. | Industry | Architecture / BOM / attach rate | CDR-01, CDR-05, CDR-08; S-12 and S-19 provide platform architecture facts but not CPU dollars | High evidence gap / Unknown conclusion | Codex round 2 opposition | FATAL GAP; build rack-level CPU count, CPU SKU/ASP, host ratio, memory attach, and CPU % of system value by platform |
    28	| CDR-24 | TSMC remains the best diversified CPU-related AI silicon exposure. | TSMC | Ranking / substitution | S-20 confirms Q1 2026 growth and margins; S-21 confirms HPC platform share; CPU-specific revenue is not isolated | Medium-Low | Codex round 2 opposition | OVERBROAD; positive AI/HPC exposure is confirmed, but CPU-thesis inference and valuation require separate work |
    29	| CDR-25 | Broadcom and Marvell belong in the CPU memo as substitutes and relative-return benchmarks, not CPU longs. | Broadcom / Marvell | Universe definition / substitution | S-16 and S-17 confirm AI custom silicon and data-center exposure; neither confirms material CPU revenue | Medium-High | Codex round 2 opposition | ACCEPTED WITH LIMITS; classify as substitution/benchmark exposure and exclude from pure CPU ranking |
    30	| CDR-26 | Qualcomm remains Avoid for a CPU-pure thesis, but its data-center CPU option value is not zero. | Qualcomm | Ranking / optionality | S-18 confirms data-center business and custom CPU-core intent; S-23 confirms prior Centriq server CPU commercialization history | Medium | Codex round 2 opposition | PARTIALLY SUPPORTED; avoid until customer/revenue proof, but track new design wins and separate accelerator from CPU claims |
    31	| CDR-27 | Supermicro governance/accounting overhang is historical and closed. | Supermicro | Governance / quality | S-24 shows a current independent-director investigation; prior 2025 filing remediation does not settle 2026 export-control-related risk | Medium | Codex round 2 opposition | STALE / INCOMPLETE; update SMCI quality thesis for current investigation and distinguish company disclosure from allegation |

 exited 1 in 243ms:
diff --git a/cpu-investment-research-2/claims/claim_register.md b/cpu-investment-research-2/sources/source_log.md
index abb7301..54e92ab 100755
--- a/cpu-investment-research-2/claims/claim_register.md
+++ b/cpu-investment-research-2/sources/source_log.md
@@ -1,31 +1,30 @@
-# Claim Register
+# Source Log
 
-| ID | Claim | Company | Category | Source | Confidence | Challenged By | Status |
-|---|---|---|---|---|---|---|---|
-| CDR-01 | CPU silicon is only 3-7% of AI server BOM / <5% of GB200-class rack BOM. | Industry | BOM / pricing | Claude round 1; no primary teardown cited | Low | Codex round 1 opposition | UNSUPPORTED; fatal to bear thesis until platform-level BOM is sourced |
-| CDR-02 | 60-70% of incremental hyperscaler compute capex flows into accelerated systems. | Industry | Capex allocation | Claude round 1 assumption | Low | Codex round 1 opposition | UNSUPPORTED; needs capex-to-server architecture bridge |
-| CDR-03 | Merchant x86 competes for a shrinking slice of incremental cloud CPU capacity. | AMD / Intel | Market share | S-10, S-11, S-13, S-14 support ARM adoption directionally; no independent share series cited | Medium-Low | Codex round 1 opposition | PARTIALLY SUPPORTED; requires Mercury/IDC/Omdia unit, revenue, and core-hour share |
-| CDR-04 | Nvidia AI rack architecture means ARM CPU displacement for x86. | Nvidia / Intel / AMD / Arm | Architecture | S-12 confirms GB200/GB300 use Grace Arm; S-19 confirms Xeon 6 host CPU in DGX Rubin NVL8 | Medium | Codex round 1 opposition | OVERBROAD; split by platform rather than treating all Nvidia systems as ARM-hosted |
-| CDR-05 | Custom ASIC racks have the lowest CPU intensity and are directly subtractive to merchant CPU vendors. | Broadcom / Marvell / hyperscalers | Substitution risk | Claude round 1; no TPU/Trainium/MAIA host-CPU counts cited | Low | Codex round 1 opposition | UNSUPPORTED; needs architecture attach data |
-| CDR-06 | AMD EPYC growth is probably sub-20%, with Instinct doing the heavy lifting. | AMD | Revenue mix | S-01 confirms Data Center includes EPYC and Instinct but not the split | Low | Codex round 1 opposition | UNSUPPORTED; do not use without EPYC/Instinct triangulation |
-| CDR-07 | Intel DCAI Q1 2026 strength may be mostly Sierra Forest mix / easy comp / low ASP host CPUs. | Intel | Revenue quality / ASP | S-02 confirms DCAI +22%; mix explanation is Claude inference | Low | Codex round 1 opposition | UNSUPPORTED; needs Intel product mix, ASP, and gross margin evidence |
-| CDR-08 | Server-system ASP inflation is not CPU ASP inflation. | Industry | Pricing | S-15 confirms system ASP +92.8%; CPU ASP split unavailable | Medium-High | Codex round 1 opposition | VALID CAVEAT; needs CPU-specific price dataset before bullish or bearish pricing claims |
-| CDR-09 | 10-20% server CPU price hikes since March 2026. | Intel / AMD | Pricing | Secondary press / channel rumor; no company confirmation in register | Low | Codex round 1 opposition | MARKET RUMOR; do not model as fact |
-| CDR-10 | Arm royalty per server CPU is low single-digit percentage of CPU ASP. | Arm | Unit economics | Claude round 1; no contract / AALA / CSS economics cited | Low | Codex round 1 opposition | UNSUPPORTED; needs royalty-dollar model |
-| CDR-11 | Arm Holdings is an Avoid on valuation because the multiple is extreme. | Arm | Valuation | Claude round 1; no current multiple table or DCF cited | Unknown | Codex round 1 opposition | UNSUPPORTED; needs price, share count, forward revenue/EPS/FCF scenarios |
-| CDR-12 | TSMC is priced for AI upside. | TSMC | Valuation | Claude round 1; no valuation comp table cited | Unknown | Codex round 1 opposition | UNSUPPORTED; needs valuation and scenario analysis |
-| CDR-13 | OEM/ODM gross margins will remain 6-10% and not recover. | SMCI / Wiwynn / Dell / Quanta / Inventec | Margin | S-08 and S-09 support SMCI/Wiwynn low recent GM; Dell evidence in S-07 is more mixed | Medium-Low | Codex round 1 opposition | OVERGENERALIZED; split by company, product mix, and operating margin |
-| CDR-14 | Dell is the highest-quality OEM and the only OEM worth Watchlist status. | Dell / OEMs | Ranking / quality | S-07 supports explicit AI orders/backlog and ISG growth; no peer valuation/quality scorecard cited | Medium-Low | Codex round 1 opposition | PARTIALLY SUPPORTED; needs peer scorecard and AI-server margin disclosure |
-| CDR-15 | Broadcom and Marvell should be excluded from the CPU framework. | Broadcom / Marvell | Universe definition | S-16 and S-17 confirm AI custom silicon / data center exposure, not CPU revenue | Medium | Codex round 1 opposition | TOO NARROW; exclude from pure CPU revenue, include as substitution and relative-return benchmarks |
-| CDR-16 | Hyperscaler capex may decelerate in 2H26 and hit OEM/ODM and merchant CPU first. | Industry | Cycle risk | Claude round 1 scenario; S-03, S-04, S-05, S-06 show high 2026 capex guidance | Low | Codex round 1 opposition | UNSUPPORTED SCENARIO; retain as bear case only |
-| CDR-17 | CPU equities trade as AI capex beta. | Industry / CPU universe | Valuation / factor exposure | Claude round 2 closing; no equity-factor regression or CPU revenue bridge cited | Low | Codex round 2 opposition | UNSUPPORTED as an investment claim; test stock sensitivity, backlog conversion, and CPU revenue beta before using in valuation |
-| CDR-18 | Merchant x86 faces real captive-ARM substitution at hyperscalers. | AMD / Intel / Arm | Market share / substitution | S-11, S-13, S-14 support directionally; no independent displaced-socket or displaced-revenue estimate cited | Medium | Codex round 2 opposition | PARTIALLY SUPPORTED; requires hyperscaler-by-hyperscaler merchant socket displacement and Arm royalty-dollar impact |
-| CDR-19 | OEM/ODM AI-server economics are margin-thin where confirmed. | SMCI / Wiwynn / Dell / Quanta / Inventec | Margin / quality | S-08 and S-09 confirm low recent GM at SMCI/Wiwynn; S-07 shows Dell ISG operating margin is materially higher | Medium | Codex round 2 opposition | PARTIALLY SUPPORTED; do not generalize beyond confirmed companies; split gross margin, operating margin, and cash conversion |
-| CDR-20 | Intel should move from Avoid to Tactical Watchlist on Q1 DCAI growth and the DGX Rubin NVL8 Xeon role. | Intel | Ranking / revenue quality | S-02 confirms DCAI +22% YoY and management CPU demand framing; S-19 confirms DGX Rubin NVL8 host CPU role | Medium-Low | Codex round 2 opposition | PREMATURE; facts are confirmed but not sufficient without two-year DCAI stack, product mix, ASP, margins, design-win volume, and valuation |
-| CDR-21 | Arm verdict should be deferred because valuation cannot be defended without a model. | Arm | Valuation / process | Claude round 2 closing; S-10 confirms revenue and royalty growth but not valuation or server royalty dollars | High for process fix / Unknown for investment conclusion | Codex round 2 opposition | VALID PROCESS FIX; also requires royalty-dollar model, Arm China/customer concentration, and hyperscaler adoption economics |
-| CDR-22 | Prior bear quantifications on AI-server CPU BOM, sub-20% EPYC growth, and Sierra Forest mix are withdrawn. | Industry / AMD / Intel | Evidence hygiene | Claude round 2 closing; relates to CDR-01, CDR-06, CDR-07 | High | Codex round 2 opposition | RESOLVED AS WITHDRAWN; do not reintroduce without platform BOM, EPYC/Instinct split, and Intel mix/ASP evidence |
-| CDR-23 | CPU dollars per AI rack versus traditional 2S server rack remain the central missing evidence. | Industry | Architecture / BOM / attach rate | CDR-01, CDR-05, CDR-08; S-12 and S-19 provide platform architecture facts but not CPU dollars | High evidence gap / Unknown conclusion | Codex round 2 opposition | FATAL GAP; build rack-level CPU count, CPU SKU/ASP, host ratio, memory attach, and CPU % of system value by platform |
-| CDR-24 | TSMC remains the best diversified CPU-related AI silicon exposure. | TSMC | Ranking / substitution | S-20 confirms Q1 2026 growth and margins; S-21 confirms HPC platform share; CPU-specific revenue is not isolated | Medium-Low | Codex round 2 opposition | OVERBROAD; positive AI/HPC exposure is confirmed, but CPU-thesis inference and valuation require separate work |
-| CDR-25 | Broadcom and Marvell belong in the CPU memo as substitutes and relative-return benchmarks, not CPU longs. | Broadcom / Marvell | Universe definition / substitution | S-16 and S-17 confirm AI custom silicon and data-center exposure; neither confirms material CPU revenue | Medium-High | Codex round 2 opposition | ACCEPTED WITH LIMITS; classify as substitution/benchmark exposure and exclude from pure CPU ranking |
-| CDR-26 | Qualcomm remains Avoid for a CPU-pure thesis, but its data-center CPU option value is not zero. | Qualcomm | Ranking / optionality | S-18 confirms data-center business and custom CPU-core intent; S-23 confirms prior Centriq server CPU commercialization history | Medium | Codex round 2 opposition | PARTIALLY SUPPORTED; avoid until customer/revenue proof, but track new design wins and separate accelerator from CPU claims |
-| CDR-27 | Supermicro governance/accounting overhang is historical and closed. | Supermicro | Governance / quality | S-24 shows a current independent-director investigation; prior 2025 filing remediation does not settle 2026 export-control-related risk | Medium | Codex round 2 opposition | STALE / INCOMPLETE; update SMCI quality thesis for current investigation and distinguish company disclosure from allegation |
+Use this file to track source URLs, filings, earnings calls, market data sources, and unresolved evidence gaps.
+
+| ID | Source | Type | Date | Used For | Reliability |
+|---|---|---|---|---|---|
+| S-01 | https://www.amd.com/en/newsroom/press-releases/2026-2-3-amd-reports-fourth-quarter-and-full-year-2025-fina.html | Company earnings release | 2026-02-03 | AMD FY2025 Data Center revenue; EPYC + Instinct disclosure issue | High |
+| S-02 | https://www.intc.com/news-events/press-releases/detail/1767/intel-reports-first-quarter-2026-financial-results | Company earnings release | 2026-04-23 | Intel Q1 2026 DCAI revenue, management CPU demand framing, DGX Rubin NVL8 business highlight | High |
+| S-03 | https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q2 | Company earnings call transcript | 2026-01-28 | Microsoft FY26 Q2 capex and GPUs/CPUs wording | High |
+| S-04 | https://abc.xyz/investor/events/event-details/2026/2025-Q4-Earnings-Call-2026-Dr_C033hS6/default.aspx | Company earnings call transcript | 2026-02-04 | Alphabet 2026 capex guide and server/data-center allocation commentary | High |
+| S-05 | https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Fourth-Quarter-Results/default.aspx | Company earnings release | 2026-02-05 | Amazon 2026 capex guide | High |
+| S-06 | https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Fourth-Quarter-and-Full-Year-2025-Results/ | Company earnings release | 2026-01-28 | Meta 2026 capex guide | High |
+| S-07 | https://investors.delltechnologies.com/news-releases/news-release-details/dell-technologies-delivers-fourth-quarter-and-full-year-fiscal-3 | Company earnings release | 2026-02-26 | Dell FY26 AI server orders, shipments, backlog, ISG revenue and operating income | High |
+| S-08 | https://ir.supermicro.com/news/news-details/2026/Supermicro-Announces-Second-Quarter-Fiscal-Year-2026-Financial-Results/default.aspx | Company earnings release | 2026-02-03 | Supermicro Q2 FY2026 revenue and gross margin | High |
+| S-09 | https://www.wiwynn.com/news/wiwynn-reports-fourth-quarter-2025-unaudited-financial-results | Company unaudited financial release | 2026-03-03 | Wiwynn Q4 2025 gross margin, FY2025 revenue growth, AI product mix | Medium-High |
+| S-10 | https://newsroom.arm.com/news/arm-q3-fye26-results | Company earnings summary | 2026-02-04 | Arm Q3 FYE26 revenue, royalty growth, Neoverse cores, top-hyperscaler share management claim | Medium-High |
+| S-11 | https://www.aboutamazon.com/news/aws/aws-graviton-5-cpu-amazon-ec2/ | Company product announcement | 2025-12-04 | AWS Graviton share of new AWS CPU capacity | High for management claim |
+| S-12 | https://www.nvidia.com/en-us/data-center/gb200-nvl72/ | Company product page | 2026 crawled | NVIDIA GB200/GB300 Grace CPU counts and Arm architecture | High |
+| S-13 | https://azure.microsoft.com/en-us/blog/azure-cobalt-100-based-virtual-machines-are-now-generally-available/ | Company product announcement | 2024-10-16 | Microsoft Cobalt 100 GA and Arm-based Azure VM details | High |
+| S-14 | https://cloud.google.com/products/axion | Company product page | 2026 crawled | Google Axion custom Arm CPU and C4A/N4A instance details | High |
+| S-15 | https://www.gartner.com/en/documents/6998066 | Market research summary | 2025-09-26 | 2Q25 server shipments, vendor revenue, server-system ASP | Medium; paywalled analyst estimate |
+| S-16 | https://investors.broadcom.com/news-releases/news-release-details/broadcom-inc-announces-fourth-quarter-and-fiscal-year-2025 | Company earnings release | 2025-12-11 | Broadcom Q4 FY2025 AI semiconductor growth and AI revenue guide | High |
+| S-17 | https://investor.marvell.com/news-events/press-releases/detail/1011/marvell-technology-inc-reports-fourth-quarter-and-fiscal-year-2026-financial-results | Company earnings release | 2026-03-05 | Marvell FY2026 revenue growth and data center share of revenue | High |
+| S-18 | https://www.sec.gov/Archives/edgar/data/0000804328/000080432825000085/qcom-20250928.htm | SEC 10-K | 2025-11-05 | Qualcomm Oryon/data center product intent and segment context | High |
+| S-19 | https://newsroom.intel.com/data-center/intel-xeon-6-used-as-host-cpus-in-nvidia-dgx-rubin-nvl8-systems | Company product announcement | 2026-03-16 | Intel Xeon 6 host CPU role in NVIDIA DGX Rubin NVL8 systems | High for Intel claim |
+| S-20 | https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-04/bd8eb0403902fdea59a2f5e390e48d010b50edc9/1Q26%20EarningsRelease_WoG.pdf | Company earnings release | 2026-04-16 | TSMC Q1 2026 revenue, margin, advanced-node revenue mix | High |
+| S-21 | https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-04/9f060092ba29ff3630cfdaefd67774026195e135/1Q26ManagementReport.pdf | Company management report | 2026-04-16 | TSMC Q1 2026 platform mix; HPC share of revenue | High |
+| S-22 | https://www.hpe.com/us/en/newsroom/press-release/2025/07/hewlett-packard-enterprise-closes-acquisition-of-juniper-networks-to-offer-industry-leading-comprehensive-cloud-native-ai-driven-portfolio.html | Company press release | 2025-07-02 | HPE Juniper close; networking-driven AI infrastructure strategy | High |
+| S-23 | https://www.qualcomm.com/news/releases/2017/11/qualcomm-datacenter-technologies-announces-commercial-shipment-qualcomm | Company product announcement | 2017-11-07 | Qualcomm prior Centriq server CPU commercialization attempt | High but stale; historical context only |
+| S-24 | https://ir.supermicro.com/news/news-details/2026/Supermicro-Provides-Update-on-Investigation-by-Independent-Board-Directors/default.aspx | Company press release | 2026-04-07 | Supermicro independent-director investigation tied to export-control indictment of former associated individuals | High for company disclosure |

exec
/usr/bin/zsh -lc 'git status --short' in /mnt/c/Users/hyc97/workspace/Ecclesia/CPU
diff --git a//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/claims/claim_register.md b//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/claims/claim_register.md
index b5b76759dc0441e2e535d024c765470a4d909c68..abb73018038a0b1353839f46db64bbdf12798599
--- a//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/claims/claim_register.md
+++ b//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/claims/claim_register.md
@@ -18,3 +18,14 @@
 | CDR-14 | Dell is the highest-quality OEM and the only OEM worth Watchlist status. | Dell / OEMs | Ranking / quality | S-07 supports explicit AI orders/backlog and ISG growth; no peer valuation/quality scorecard cited | Medium-Low | Codex round 1 opposition | PARTIALLY SUPPORTED; needs peer scorecard and AI-server margin disclosure |
 | CDR-15 | Broadcom and Marvell should be excluded from the CPU framework. | Broadcom / Marvell | Universe definition | S-16 and S-17 confirm AI custom silicon / data center exposure, not CPU revenue | Medium | Codex round 1 opposition | TOO NARROW; exclude from pure CPU revenue, include as substitution and relative-return benchmarks |
 | CDR-16 | Hyperscaler capex may decelerate in 2H26 and hit OEM/ODM and merchant CPU first. | Industry | Cycle risk | Claude round 1 scenario; S-03, S-04, S-05, S-06 show high 2026 capex guidance | Low | Codex round 1 opposition | UNSUPPORTED SCENARIO; retain as bear case only |
+| CDR-17 | CPU equities trade as AI capex beta. | Industry / CPU universe | Valuation / factor exposure | Claude round 2 closing; no equity-factor regression or CPU revenue bridge cited | Low | Codex round 2 opposition | UNSUPPORTED as an investment claim; test stock sensitivity, backlog conversion, and CPU revenue beta before using in valuation |
+| CDR-18 | Merchant x86 faces real captive-ARM substitution at hyperscalers. | AMD / Intel / Arm | Market share / substitution | S-11, S-13, S-14 support directionally; no independent displaced-socket or displaced-revenue estimate cited | Medium | Codex round 2 opposition | PARTIALLY SUPPORTED; requires hyperscaler-by-hyperscaler merchant socket displacement and Arm royalty-dollar impact |
+| CDR-19 | OEM/ODM AI-server economics are margin-thin where confirmed. | SMCI / Wiwynn / Dell / Quanta / Inventec | Margin / quality | S-08 and S-09 confirm low recent GM at SMCI/Wiwynn; S-07 shows Dell ISG operating margin is materially higher | Medium | Codex round 2 opposition | PARTIALLY SUPPORTED; do not generalize beyond confirmed companies; split gross margin, operating margin, and cash conversion |
+| CDR-20 | Intel should move from Avoid to Tactical Watchlist on Q1 DCAI growth and the DGX Rubin NVL8 Xeon role. | Intel | Ranking / revenue quality | S-02 confirms DCAI +22% YoY and management CPU demand framing; S-19 confirms DGX Rubin NVL8 host CPU role | Medium-Low | Codex round 2 opposition | PREMATURE; facts are confirmed but not sufficient without two-year DCAI stack, product mix, ASP, margins, design-win volume, and valuation |
+| CDR-21 | Arm verdict should be deferred because valuation cannot be defended without a model. | Arm | Valuation / process | Claude round 2 closing; S-10 confirms revenue and royalty growth but not valuation or server royalty dollars | High for process fix / Unknown for investment conclusion | Codex round 2 opposition | VALID PROCESS FIX; also requires royalty-dollar model, Arm China/customer concentration, and hyperscaler adoption economics |
+| CDR-22 | Prior bear quantifications on AI-server CPU BOM, sub-20% EPYC growth, and Sierra Forest mix are withdrawn. | Industry / AMD / Intel | Evidence hygiene | Claude round 2 closing; relates to CDR-01, CDR-06, CDR-07 | High | Codex round 2 opposition | RESOLVED AS WITHDRAWN; do not reintroduce without platform BOM, EPYC/Instinct split, and Intel mix/ASP evidence |
+| CDR-23 | CPU dollars per AI rack versus traditional 2S server rack remain the central missing evidence. | Industry | Architecture / BOM / attach rate | CDR-01, CDR-05, CDR-08; S-12 and S-19 provide platform architecture facts but not CPU dollars | High evidence gap / Unknown conclusion | Codex round 2 opposition | FATAL GAP; build rack-level CPU count, CPU SKU/ASP, host ratio, memory attach, and CPU % of system value by platform |
+| CDR-24 | TSMC remains the best diversified CPU-related AI silicon exposure. | TSMC | Ranking / substitution | S-20 confirms Q1 2026 growth and margins; S-21 confirms HPC platform share; CPU-specific revenue is not isolated | Medium-Low | Codex round 2 opposition | OVERBROAD; positive AI/HPC exposure is confirmed, but CPU-thesis inference and valuation require separate work |
+| CDR-25 | Broadcom and Marvell belong in the CPU memo as substitutes and relative-return benchmarks, not CPU longs. | Broadcom / Marvell | Universe definition / substitution | S-16 and S-17 confirm AI custom silicon and data-center exposure; neither confirms material CPU revenue | Medium-High | Codex round 2 opposition | ACCEPTED WITH LIMITS; classify as substitution/benchmark exposure and exclude from pure CPU ranking |
+| CDR-26 | Qualcomm remains Avoid for a CPU-pure thesis, but its data-center CPU option value is not zero. | Qualcomm | Ranking / optionality | S-18 confirms data-center business and custom CPU-core intent; S-23 confirms prior Centriq server CPU commercialization history | Medium | Codex round 2 opposition | PARTIALLY SUPPORTED; avoid until customer/revenue proof, but track new design wins and separate accelerator from CPU claims |
+| CDR-27 | Supermicro governance/accounting overhang is historical and closed. | Supermicro | Governance / quality | S-24 shows a current independent-director investigation; prior 2025 filing remediation does not settle 2026 export-control-related risk | Medium | Codex round 2 opposition | STALE / INCOMPLETE; update SMCI quality thesis for current investigation and distinguish company disclosure from allegation |
diff --git a//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/sources/source_log.md b//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/sources/source_log.md
index 61fbc5b1877cffb5173d17ea67b6b7cfda9d8157..54e92abc4492d20314734dc50a84e92902d01894
--- a//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/sources/source_log.md
+++ b//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/sources/source_log.md
@@ -23,3 +23,8 @@
 | S-17 | https://investor.marvell.com/news-events/press-releases/detail/1011/marvell-technology-inc-reports-fourth-quarter-and-fiscal-year-2026-financial-results | Company earnings release | 2026-03-05 | Marvell FY2026 revenue growth and data center share of revenue | High |
 | S-18 | https://www.sec.gov/Archives/edgar/data/0000804328/000080432825000085/qcom-20250928.htm | SEC 10-K | 2025-11-05 | Qualcomm Oryon/data center product intent and segment context | High |
 | S-19 | https://newsroom.intel.com/data-center/intel-xeon-6-used-as-host-cpus-in-nvidia-dgx-rubin-nvl8-systems | Company product announcement | 2026-03-16 | Intel Xeon 6 host CPU role in NVIDIA DGX Rubin NVL8 systems | High for Intel claim |
+| S-20 | https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-04/bd8eb0403902fdea59a2f5e390e48d010b50edc9/1Q26%20EarningsRelease_WoG.pdf | Company earnings release | 2026-04-16 | TSMC Q1 2026 revenue, margin, advanced-node revenue mix | High |
+| S-21 | https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-04/9f060092ba29ff3630cfdaefd67774026195e135/1Q26ManagementReport.pdf | Company management report | 2026-04-16 | TSMC Q1 2026 platform mix; HPC share of revenue | High |
+| S-22 | https://www.hpe.com/us/en/newsroom/press-release/2025/07/hewlett-packard-enterprise-closes-acquisition-of-juniper-networks-to-offer-industry-leading-comprehensive-cloud-native-ai-driven-portfolio.html | Company press release | 2025-07-02 | HPE Juniper close; networking-driven AI infrastructure strategy | High |
+| S-23 | https://www.qualcomm.com/news/releases/2017/11/qualcomm-datacenter-technologies-announces-commercial-shipment-qualcomm | Company product announcement | 2017-11-07 | Qualcomm prior Centriq server CPU commercialization attempt | High but stale; historical context only |
+| S-24 | https://ir.supermicro.com/news/news-details/2026/Supermicro-Provides-Update-on-Investigation-by-Independent-Board-Directors/default.aspx | Company press release | 2026-04-07 | Supermicro independent-director investigation tied to export-control indictment of former associated individuals | High for company disclosure |

 exited 128 in 167ms:
fatal: not a git repository (or any parent up to mount point /mnt)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).

codex
Updated the register and source log:
- [claim_register.md](/mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/claims/claim_register.md:21): added `CDR-17` through `CDR-27`.
- [source_log.md](/mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/sources/source_log.md:26): added `S-20` through `S-24`.

**1. Highest-Risk Errors**
1. **Intel upgrade is premature.** Confirmed fact: Intel DCAI was `$5.1B`, `+22% YoY`, and Intel says Xeon 6 is used as DGX Rubin NVL8 host CPU. Sources: [Intel Q1 2026](https://www.intc.com/news-events/press-releases/detail/1767/intel-reports-first-quarter-2026-financial-results), [Intel Rubin NVL8](https://newsroom.intel.com/data-center/intel-xeon-6-used-as-host-cpus-in-nvidia-dgx-rubin-nvl8-systems). Investment conclusion still needs volume, ASP, margin, and valuation. Confidence: **Medium-High**.
2. **“CPU equities trade as AI capex beta” is UNSUPPORTED.** That is a market-factor claim, not a business-model fact. No regression, CPU revenue bridge, or capex-to-CPU conversion model is cited. Confidence: **Low**.
3. **Claude’s “structural arguments survive at Medium confidence” bundles unlike claims.** Captive Arm substitution is directionally supported by AWS Graviton, Azure Cobalt, and Google Axion disclosures; OEM margin thinness is confirmed mainly for SMCI/Wiwynn; CPU equity beta is not confirmed. Sources: [AWS Graviton5](https://www.aboutamazon.com/news/aws/aws-graviton-5-cpu-amazon-ec2), `S-13`, `S-14`, [SMCI](https://ir.supermicro.com/news/news-details/2026/Supermicro-Announces-Second-Quarter-Fiscal-Year-2026-Financial-Results/default.aspx), [Wiwynn](https://www.wiwynn.com/news/wiwynn-reports-fourth-quarter-2025-unaudited-financial-results). Confidence: **Medium**.
4. **SMCI risk framing is stale if treated as only a 2024 accounting issue.** Supermicro disclosed an April 2026 independent-director investigation tied to an export-control indictment of former associated individuals. Source: [SMCI April 2026 update](https://ir.supermicro.com/news/news-details/2026/Supermicro-Provides-Update-on-Investigation-by-Independent-Board-Directors/default.aspx). Confidence: **High for disclosure, Unknown for financial impact**.

**2. Unsupported Claims**
| Claim | Problem | Confidence |
|---|---|---:|
| CPU equities are AI capex beta | No equity-factor evidence or CPU revenue bridge. | Low |
| Intel merits Tactical Watchlist on S-02/S-19 alone | Facts are real; investment conclusion is under-modeled. | Medium-Low |
| OEM/ODM economics are broadly margin-thin | Supported for SMCI/Wiwynn; Dell ISG operating margin is materially different. Source: [Dell FY26](https://investors.delltechnologies.com/news-releases/news-release-details/dell-technologies-delivers-fourth-quarter-and-full-year-fiscal-3). | Medium |
| Arm valuation can only be deferred | Correct process step, but incomplete without royalty dollars, Arm China, and customer concentration. Source: [Arm Q3 FYE26](https://newsroom.arm.com/news/arm-q3-fye26-results). | Medium |

**3. Questionable Assumptions**
- ARM substitution is real directionally, but displaced merchant x86 revenue is still unquantified. AWS says Graviton was more than half of new AWS CPU capacity, but that is a management claim, not a full market-share dataset. Confidence: **Medium**.
- AI server CPU attach may be lower than legacy CPU racks, but the actual CPU dollars per rack remain missing. This is still the central fatal gap. Confidence: **Unknown**.
- TSMC is confirmed as a strong AI/HPC beneficiary, but not specifically a CPU equity thesis. TSMC Q1 2026 results and management report show strong advanced-node/HPC exposure, not CPU-only revenue. Sources: [TSMC Q1 release](https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-04/bd8eb0403902fdea59a2f5e390e48d010b50edc9/1Q26%20EarningsRelease_WoG.pdf), [TSMC Q1 management report](https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-04/9f060092ba29ff3630cfdaefd67774026195e135/1Q26ManagementReport.pdf). Confidence: **Medium**.

**4. Missing Evidence**
- CPU dollars per rack: legacy 2S x86, GB200/GB300, DGX Rubin NVL8, MI300/MI350/MI400, Trainium, TPU, Maia.
- AMD EPYC-only revenue and growth; AMD Data Center includes EPYC and Instinct. Source: [AMD FY2025](https://www.amd.com/en/newsroom/press-releases/2026-2-3-amd-reports-fourth-quarter-and-full-year-2025-fina.html).
- Xeon product mix, ASP, and DCAI operating margin.
- Independent server CPU unit/revenue share from Mercury, IDC, Omdia, or Gartner.
- Arm royalty dollars per server CPU/core.
- OEM/ODM AI server backlog terms, cancellation risk, and margin by configuration.
- Full valuation model for AMD, Intel, Arm, TSMC, Dell, SMCI.

**5. Company-Specific Objections**
- **AMD:** Data Center growth is not EPYC-only; CPU thesis still needs EPYC/Instinct split. Confidence: **High fact / Medium-Low inference**.
- **Intel:** Better than “Avoid,” but Tactical Watchlist needs proof that DCAI growth is durable and profitable. Confidence: **Medium-Low**.
- **Arm:** Deferring valuation is right, but adoption share without royalty economics is not investable. Confidence: **Medium**.
- **Qualcomm:** Avoid for CPU-pure thesis is reasonable, but option value is not zero; 10-K confirms data-center intent and custom CPU cores, while Centriq shows prior execution risk. Sources: [Qualcomm 10-K](https://www.sec.gov/Archives/edgar/data/0000804328/000080432825000085/qcom-20250928.htm), [Centriq launch](https://www.qualcomm.com/news/releases/2017/11/qualcomm-datacenter-technologies-announces-commercial-shipment-qualcomm).
- **SMCI/Wiwynn:** Margin evidence is bearish, not neutral. SMCI Q2 FY26 GM was 6.3%; Wiwynn Q4 2025 GM was 7.2%. Sources: `S-08`, `S-09`.
- **Broadcom/Marvell:** Keep as substitution and relative-return benchmarks, not CPU longs. Sources: [Broadcom FY25](https://investors.broadcom.com/news-releases/news-release-details/broadcom-inc-announces-fourth-quarter-and-fiscal-year-2025), [Marvell FY26](https://investor.marvell.com/news-events/press-releases/detail/1011/marvell-technology-inc-reports-fourth-quarter-and-fiscal-year-2026-financial-results).

**6. Revised Ranking**
| Rank | Companies | View |
|---|---|---|
| Strong CPU-pure candidate | None | Fatal evidence gaps remain. |
| Qualified / needs model | TSMC, AMD, Dell, Intel | Real exposure, but CPU conversion or valuation unresolved. |
| Deferred | Arm | Technology exposure confirmed; valuation and royalty model absent. |
| Benchmark / substitution | Broadcom, Marvell, NVIDIA | Useful comparables, not CPU-pure longs. |
| Avoid for CPU-pure thesis | Qualcomm, HPE, SMCI, Wiwynn, Quanta, Inventec, Lenovo | Either indirect, low-margin, or insufficient CPU economics. |

**7. Claim Challenges Table**
| Claim ID | Problem | Severity | Suggested Fix | Status |
|---|---|---|---|---|
| CDR-17 | AI capex beta claim lacks evidence. | Fatal | Run factor regression and CPU revenue bridge. | Added / Open |
| CDR-18 | Arm substitution not quantified. | Major | Estimate displaced sockets and revenue by hyperscaler. | Added / Open |
| CDR-19 | OEM margin claim overgeneralized. | Major | Split SMCI, Wiwynn, Dell, Quanta, Inventec. | Added / Open |
| CDR-20 | Intel upgrade under-modeled. | Major | Add DCAI 2-year stack, ASP, mix, margin, valuation. | Added / Open |
| CDR-21 | Arm deferral incomplete. | Major | Add royalty-dollar and valuation model. | Added / Open |
| CDR-23 | CPU dollars per rack missing. | Fatal | Build rack BOM/attach table. | Added / Open |
| CDR-24 | TSMC CPU read-through overbroad. | Major | Separate AI/HPC foundry thesis from CPU thesis. | Added / Open |
| CDR-27 | SMCI risk framing stale. | Major | Update for April 2026 investigation. | Added / Open |

**8. Required Follow-Up Research**
1. Build CPU-dollar-per-rack table; this is the evidence that would most change my view.
2. Pull Mercury/IDC/Omdia server CPU share through Q1 2026.
3. Build AMD EPYC-only and Intel Xeon-only revenue estimates.
4. Channel-check server CPU ASPs; keep price-hike rumors out of base case until verified.
5. Build valuation snapshots for AMD, Intel, Arm, TSMC, Dell, SMCI.
6. Quantify Graviton/Cobalt/Axion displacement of merchant x86.
7. Update SMCI governance/export-control risk status before any quality ranking.
diff --git a//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/claims/claim_register.md b//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/claims/claim_register.md
index b5b76759dc0441e2e535d024c765470a4d909c68..abb73018038a0b1353839f46db64bbdf12798599
--- a//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/claims/claim_register.md
+++ b//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/claims/claim_register.md
@@ -18,3 +18,14 @@
 | CDR-14 | Dell is the highest-quality OEM and the only OEM worth Watchlist status. | Dell / OEMs | Ranking / quality | S-07 supports explicit AI orders/backlog and ISG growth; no peer valuation/quality scorecard cited | Medium-Low | Codex round 1 opposition | PARTIALLY SUPPORTED; needs peer scorecard and AI-server margin disclosure |
 | CDR-15 | Broadcom and Marvell should be excluded from the CPU framework. | Broadcom / Marvell | Universe definition | S-16 and S-17 confirm AI custom silicon / data center exposure, not CPU revenue | Medium | Codex round 1 opposition | TOO NARROW; exclude from pure CPU revenue, include as substitution and relative-return benchmarks |
 | CDR-16 | Hyperscaler capex may decelerate in 2H26 and hit OEM/ODM and merchant CPU first. | Industry | Cycle risk | Claude round 1 scenario; S-03, S-04, S-05, S-06 show high 2026 capex guidance | Low | Codex round 1 opposition | UNSUPPORTED SCENARIO; retain as bear case only |
+| CDR-17 | CPU equities trade as AI capex beta. | Industry / CPU universe | Valuation / factor exposure | Claude round 2 closing; no equity-factor regression or CPU revenue bridge cited | Low | Codex round 2 opposition | UNSUPPORTED as an investment claim; test stock sensitivity, backlog conversion, and CPU revenue beta before using in valuation |
+| CDR-18 | Merchant x86 faces real captive-ARM substitution at hyperscalers. | AMD / Intel / Arm | Market share / substitution | S-11, S-13, S-14 support directionally; no independent displaced-socket or displaced-revenue estimate cited | Medium | Codex round 2 opposition | PARTIALLY SUPPORTED; requires hyperscaler-by-hyperscaler merchant socket displacement and Arm royalty-dollar impact |
+| CDR-19 | OEM/ODM AI-server economics are margin-thin where confirmed. | SMCI / Wiwynn / Dell / Quanta / Inventec | Margin / quality | S-08 and S-09 confirm low recent GM at SMCI/Wiwynn; S-07 shows Dell ISG operating margin is materially higher | Medium | Codex round 2 opposition | PARTIALLY SUPPORTED; do not generalize beyond confirmed companies; split gross margin, operating margin, and cash conversion |
+| CDR-20 | Intel should move from Avoid to Tactical Watchlist on Q1 DCAI growth and the DGX Rubin NVL8 Xeon role. | Intel | Ranking / revenue quality | S-02 confirms DCAI +22% YoY and management CPU demand framing; S-19 confirms DGX Rubin NVL8 host CPU role | Medium-Low | Codex round 2 opposition | PREMATURE; facts are confirmed but not sufficient without two-year DCAI stack, product mix, ASP, margins, design-win volume, and valuation |
+| CDR-21 | Arm verdict should be deferred because valuation cannot be defended without a model. | Arm | Valuation / process | Claude round 2 closing; S-10 confirms revenue and royalty growth but not valuation or server royalty dollars | High for process fix / Unknown for investment conclusion | Codex round 2 opposition | VALID PROCESS FIX; also requires royalty-dollar model, Arm China/customer concentration, and hyperscaler adoption economics |
+| CDR-22 | Prior bear quantifications on AI-server CPU BOM, sub-20% EPYC growth, and Sierra Forest mix are withdrawn. | Industry / AMD / Intel | Evidence hygiene | Claude round 2 closing; relates to CDR-01, CDR-06, CDR-07 | High | Codex round 2 opposition | RESOLVED AS WITHDRAWN; do not reintroduce without platform BOM, EPYC/Instinct split, and Intel mix/ASP evidence |
+| CDR-23 | CPU dollars per AI rack versus traditional 2S server rack remain the central missing evidence. | Industry | Architecture / BOM / attach rate | CDR-01, CDR-05, CDR-08; S-12 and S-19 provide platform architecture facts but not CPU dollars | High evidence gap / Unknown conclusion | Codex round 2 opposition | FATAL GAP; build rack-level CPU count, CPU SKU/ASP, host ratio, memory attach, and CPU % of system value by platform |
+| CDR-24 | TSMC remains the best diversified CPU-related AI silicon exposure. | TSMC | Ranking / substitution | S-20 confirms Q1 2026 growth and margins; S-21 confirms HPC platform share; CPU-specific revenue is not isolated | Medium-Low | Codex round 2 opposition | OVERBROAD; positive AI/HPC exposure is confirmed, but CPU-thesis inference and valuation require separate work |
+| CDR-25 | Broadcom and Marvell belong in the CPU memo as substitutes and relative-return benchmarks, not CPU longs. | Broadcom / Marvell | Universe definition / substitution | S-16 and S-17 confirm AI custom silicon and data-center exposure; neither confirms material CPU revenue | Medium-High | Codex round 2 opposition | ACCEPTED WITH LIMITS; classify as substitution/benchmark exposure and exclude from pure CPU ranking |
+| CDR-26 | Qualcomm remains Avoid for a CPU-pure thesis, but its data-center CPU option value is not zero. | Qualcomm | Ranking / optionality | S-18 confirms data-center business and custom CPU-core intent; S-23 confirms prior Centriq server CPU commercialization history | Medium | Codex round 2 opposition | PARTIALLY SUPPORTED; avoid until customer/revenue proof, but track new design wins and separate accelerator from CPU claims |
+| CDR-27 | Supermicro governance/accounting overhang is historical and closed. | Supermicro | Governance / quality | S-24 shows a current independent-director investigation; prior 2025 filing remediation does not settle 2026 export-control-related risk | Medium | Codex round 2 opposition | STALE / INCOMPLETE; update SMCI quality thesis for current investigation and distinguish company disclosure from allegation |
diff --git a//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/sources/source_log.md b//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/sources/source_log.md
index 61fbc5b1877cffb5173d17ea67b6b7cfda9d8157..54e92abc4492d20314734dc50a84e92902d01894
--- a//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/sources/source_log.md
+++ b//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/sources/source_log.md
@@ -23,3 +23,8 @@
 | S-17 | https://investor.marvell.com/news-events/press-releases/detail/1011/marvell-technology-inc-reports-fourth-quarter-and-fiscal-year-2026-financial-results | Company earnings release | 2026-03-05 | Marvell FY2026 revenue growth and data center share of revenue | High |
 | S-18 | https://www.sec.gov/Archives/edgar/data/0000804328/000080432825000085/qcom-20250928.htm | SEC 10-K | 2025-11-05 | Qualcomm Oryon/data center product intent and segment context | High |
 | S-19 | https://newsroom.intel.com/data-center/intel-xeon-6-used-as-host-cpus-in-nvidia-dgx-rubin-nvl8-systems | Company product announcement | 2026-03-16 | Intel Xeon 6 host CPU role in NVIDIA DGX Rubin NVL8 systems | High for Intel claim |
+| S-20 | https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-04/bd8eb0403902fdea59a2f5e390e48d010b50edc9/1Q26%20EarningsRelease_WoG.pdf | Company earnings release | 2026-04-16 | TSMC Q1 2026 revenue, margin, advanced-node revenue mix | High |
+| S-21 | https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-04/9f060092ba29ff3630cfdaefd67774026195e135/1Q26ManagementReport.pdf | Company management report | 2026-04-16 | TSMC Q1 2026 platform mix; HPC share of revenue | High |
+| S-22 | https://www.hpe.com/us/en/newsroom/press-release/2025/07/hewlett-packard-enterprise-closes-acquisition-of-juniper-networks-to-offer-industry-leading-comprehensive-cloud-native-ai-driven-portfolio.html | Company press release | 2025-07-02 | HPE Juniper close; networking-driven AI infrastructure strategy | High |
+| S-23 | https://www.qualcomm.com/news/releases/2017/11/qualcomm-datacenter-technologies-announces-commercial-shipment-qualcomm | Company product announcement | 2017-11-07 | Qualcomm prior Centriq server CPU commercialization attempt | High but stale; historical context only |
+| S-24 | https://ir.supermicro.com/news/news-details/2026/Supermicro-Provides-Update-on-Investigation-by-Independent-Board-Directors/default.aspx | Company press release | 2026-04-07 | Supermicro independent-director investigation tied to export-control indictment of former associated individuals | High for company disclosure |

2026-04-26T06:03:36.316088Z ERROR codex_core::session: failed to record rollout items: thread 019dc85e-8fd5-75c3-9f06-071c7cbb07de not found
tokens used
204,410