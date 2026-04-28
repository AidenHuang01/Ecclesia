Updated:
[claim_register.md](/mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/claims/claim_register.md) and [source_log.md](/mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/sources/source_log.md).

## 1. Highest-Risk Errors

1. **Fatal: CPU-BOM share is asserted, not proven.** The bear thesis depends on CPU silicon being a small and shrinking share of AI rack value, but the 3-7% / <5% BOM claim has no teardown or platform quote. Confidence: Low. Status: UNSUPPORTED.

2. **High: “Nvidia = Arm displacement” is overbroad.** Nvidia GB200/GB300 do use Grace Arm CPUs, confirmed by Nvidia. But Intel says Xeon 6 is used as host CPU in NVIDIA DGX Rubin NVL8 systems, so Nvidia architecture is not uniformly x86-negative. Confidence: Medium. Sources: [Nvidia GB200/GB300](https://www.nvidia.com/en-us/data-center/gb200-nvl72/), [Intel/NVIDIA DGX Rubin NVL8](https://newsroom.intel.com/data-center/intel-xeon-6-used-as-host-cpus-in-nvidia-dgx-rubin-nvl8-systems).

3. **High: AMD CPU conclusion is built on a missing split.** AMD confirms FY2025 Data Center revenue was $16.6B, up 32%, from both EPYC CPUs and Instinct GPUs, but Claude’s “EPYC probably sub-20%” is unsupported. Source: [AMD FY2025 results](https://www.amd.com/en/newsroom/press-releases/2026-2-3-amd-reports-fourth-quarter-and-full-year-2025-fina.html).

## 2. Unsupported Claims

- CPU share of AI server BOM is 3-7%: UNSUPPORTED.
- 60-70% of incremental hyperscaler compute capex flows to accelerated systems: UNSUPPORTED.
- Custom ASIC racks have the lowest CPU intensity: UNSUPPORTED.
- Intel DCAI strength is mostly Sierra Forest / easy comp / lower ASP: UNSUPPORTED. Intel reported DCAI revenue of $5.1B, up 22%, but mix is not disclosed. Source: [Intel Q1 2026](https://www.intc.com/news-events/press-releases/detail/1767/intel-reports-first-quarter-2026-financial-results).
- Arm royalty per server CPU is low single-digit % of CPU ASP: UNSUPPORTED without contract or royalty-dollar model.
- Arm and TSMC are “priced for it”: UNSUPPORTED without valuation tables.

## 3. Questionable Assumptions

- **Share of BOM down does not mean CPU revenue down.** CPU value share can fall while CPU sockets, cores, and dollars rise.
- **Arm adoption is real, but not quantified enough.** AWS says Graviton is more than half of new AWS CPU capacity, and Microsoft/Google have Cobalt/Axion, but this is not the same as global server CPU revenue share. Sources: [AWS Graviton](https://www.aboutamazon.com/news/aws/aws-graviton-5-cpu-amazon-ec2/), [Azure Cobalt](https://azure.microsoft.com/en-us/blog/azure-cobalt-100-based-virtual-machines-are-now-generally-available/), [Google Axion](https://cloud.google.com/products/axion).
- **OEM margin conclusion is too broad.** SMCI and Wiwynn have low gross margins, but Dell’s AI backlog and ISG scale need separate treatment. Sources: [SMCI](https://ir.supermicro.com/news/news-details/2026/Supermicro-Announces-Second-Quarter-Fiscal-Year-2026-Financial-Results/default.aspx), [Wiwynn](https://www.wiwynn.com/news/wiwynn-reports-fourth-quarter-2025-unaudited-financial-results), [Dell](https://investors.delltechnologies.com/news-releases/news-release-details/dell-technologies-delivers-fourth-quarter-and-full-year-fiscal-3).

## 4. Missing Evidence

- Platform BOMs for GB200, GB300, DGX Rubin NVL8, MI300X/MI350, Trainium, TPU, MAIA.
- CPU attach rate by system architecture, not just capex headline.
- AMD EPYC vs Instinct revenue split.
- Intel Xeon mix, ASP, and DCAI margin bridge.
- Arm Neoverse royalty dollars per chip.
- Mercury/IDC/Omdia server CPU unit and revenue share.
- OEM/ODM AI server gross margin by customer and product.
- Current valuation tables for AMD, Intel, Arm, TSMC, Dell, SMCI, Broadcom, Marvell.

## 5. Company-Specific Objections

- **AMD:** Watchlist is reasonable, but the bear case cannot assume EPYC weakness without evidence.
- **Intel:** Avoid is too harsh if Q1 DCAI strength and disclosed Nvidia Rubin NVL8 host-CPU role persist. Still execution-heavy.
- **Arm:** Technology thesis is supported; valuation objection is not yet evidenced.
- **Qualcomm:** Avoid as CPU thesis remains reasonable; its 10-K says it intends to use custom CPU cores for data center products, but no material server CPU revenue is shown. Source: [Qualcomm 10-K](https://www.sec.gov/Archives/edgar/data/0000804328/000080432825000085/qcom-20250928.htm).
- **Broadcom / Marvell:** Not CPU pure plays, but excluding them entirely weakens substitution-risk analysis. Sources: [Broadcom](https://investors.broadcom.com/news-releases/news-release-details/broadcom-inc-announces-fourth-quarter-and-fiscal-year-2025), [Marvell](https://investor.marvell.com/news-events/press-releases/detail/1011/marvell-technology-inc-reports-fourth-quarter-and-fiscal-year-2026-financial-results).
- **Dell / SMCI / Wiwynn:** Treat separately; SMCI/Wiwynn margin pressure is confirmed, Dell quality claim needs peer scorecard.

## 6. Revised Ranking

| Tier | Revised View |
|---|---|
| Strong candidate | None yet |
| Watchlist | AMD, Intel, Arm, TSMC, Dell |
| Tactical / cyclical | SMCI, Quanta, Wiwynn, Lenovo, HPE, Inventec |
| Avoid as CPU thesis | Qualcomm |
| Include as substitution benchmark | Broadcom, Marvell |

Main change: upgrade **Intel from Avoid to Watchlist / tactical CPU beta** pending Q2 confirmation.

## 7. Claim Challenges Table

| Claim ID | Problem | Severity | Suggested Fix | Status |
|---|---|---|---|---|
| CDR-01 | CPU BOM share unsupported | Fatal | Source platform teardown / BOM | Added |
| CDR-02 | 60-70% capex allocation unsupported | High | Build capex-to-architecture model | Added |
| CDR-03 | x86 share-loss claim lacks independent share data | High | Pull Mercury/IDC/Omdia | Added |
| CDR-04 | Nvidia ARM displacement overbroad | High | Split GB200/GB300 vs DGX Rubin NVL8 | Added |
| CDR-05 | Custom ASIC CPU intensity unsupported | High | Map TPU/Trainium/MAIA host CPUs | Added |
| CDR-06 | AMD EPYC sub-20% unsupported | High | Triangulate EPYC/Instinct split | Added |
| CDR-07 | Intel mix explanation unsupported | Medium | Get DCAI product mix / ASP | Added |
| CDR-08 | System ASP not CPU ASP | Medium | Obtain CPU-specific pricing | Added |
| CDR-09 | CPU price hike is market rumor | Medium | Verify with OEM/distributor data | Added |
| CDR-10 | Arm royalty economics unsupported | High | Build royalty-dollar model | Added |
| CDR-11 | Arm valuation claim unsupported | Medium | Add valuation table | Added |
| CDR-12 | TSMC valuation claim unsupported | Medium | Add valuation table | Added |
| CDR-13 | OEM/ODM margin conclusion overgeneralized | Medium | Split by company and margin type | Added |
| CDR-15 | Broadcom/Marvell exclusion too narrow | Medium | Include as substitutes / comps | Added |

## 8. Required Follow-Up Research

Evidence that would change my mind: a sourced platform BOM showing CPUs consistently below 5% of AI rack value, Mercury/IDC data proving merchant x86 revenue share is falling despite AI demand, and AMD/Intel disclosures showing weak CPU ASP or margin.

Near-term work: build the architecture attach table, pull paid server CPU share data, verify CPU pricing, split AMD EPYC vs Instinct, and create valuation scenarios before making a public-equity ranking with conviction.

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
session id: 019dc850-e8a2-7ed2-90a3-03e264f58558
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

        You are reviewing Claude's research from round 1.

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
        I'll write my independent bearish CPU equity memo. The Codex bullish memo is saved at `notes/codex_initial.md`; my role here is the bearish but evidence-disciplined counterpart, so I'll reason from first principles rather than echo or rebut Codex point-by-point.

# Initial Independent CPU Equity Memo — Bear Side

## 1. Executive Thesis

**The "AI lifts CPUs" framing conflates three different things and obscures a weak equity thesis for merchant CPU vendors.** The accurate decomposition is:

1. **Compute TAM is up sharply** (High confidence) — driven by GPU/HBM/networking, not CPU silicon.
2. **CPU unit demand is up modestly** (Medium) — but the marginal CPU is increasingly a captive ARM design from a hyperscaler, not a merchant Xeon/EPYC.
3. **Merchant CPU pricing power is weak** (Medium-High bear conviction) — server-system ASP inflation is a GPU/BOM story; the rumored "CPU price hikes" remain unverified.

Net: CPU equities trade as a derivative of the AI capex narrative, but the cash flows the narrative implies accrue mostly to **TSMC, Nvidia, custom-ASIC vendors, and hyperscaler internal silicon programs** — not to Intel, AMD's CPU line, or Arm Holdings on a risk-adjusted basis at current valuations.

**Base bearish conclusion:**
- **AMD**: Watchlist, not Strong. The "AMD CPU" thesis is largely an Instinct/MI thesis, and Instinct is a distant #2 to Nvidia. EPYC growth is real but unquantified; segment disclosure hides it.
- **Intel**: Avoid as a CPU thesis. Foundry losses, structural share loss, and unproven 18A ramp dominate any DCAI green shoot.
- **Arm Holdings**: Avoid on valuation, not on technology. Royalty per server CPU is small; multiple is extreme.
- **Qualcomm**: Avoid as CPU thesis (agree with bull side here).
- **Broadcom / Marvell**: Not CPU plays — exclude from CPU equity universe.
- **TSMC**: Watchlist. Best clean exposure, but priced for it; geopolitical tail.
- **OEM/ODM (SMCI, Wiwynn, Quanta, Inventec, HPE, Lenovo, Dell)**: Treat as cyclical capex pass-throughs. Single-digit gross margins on AI servers do not compound. **Dell** is the highest-quality of the group and the only OEM I'd consider for Watchlist.

## 2. Industry Map

| Layer | Players | Bear-side framing |
|---|---|---|
| **Merchant x86 CPU** | Intel, AMD | Shrinking share of AI rack BOM; captive ARM displaces at the demand frontier |
| **Captive ARM CPU (no merchant equity)** | AWS Graviton, Microsoft Cobalt, Google Axion, Nvidia Grace/Vera | Structural TAM-eroder for x86 |
| **CPU IP licensor** | Arm Holdings | Captures TAM economics indirectly via royalty; small $/CPU |
| **AI accelerators** | Nvidia (GPU), AMD Instinct, custom ASICs (Broadcom, Marvell, Alchip) | Capture the marginal capex dollar; reduce CPU share of BOM |
| **Foundry** | TSMC | Wins regardless of x86/ARM/ASIC; already priced |
| **OEM** | Dell, HPE, Lenovo, Supermicro | BOM pass-through; margin compresses as AI mix rises |
| **ODM** | Quanta, Wiwynn, Inventec, Foxconn (not in scope) | Even lower margin than OEM; concentrated customer risk |
| **Prospective entrant** | Qualcomm | Server CPU is a roadmap item, not a revenue line |

## 3. Company Universe

| Ticker | Name | Bear-relevant risk vector |
|---|---|---|
| AMD | Advanced Micro Devices | EPYC vs Instinct disclosure opacity; Nvidia GPU dominance caps Instinct upside |
| INTC | Intel | Share loss, foundry losses, 18A execution risk, capital structure |
| ARM | Arm Holdings | Valuation, royalty rate ceiling, China exposure |
| QCOM | Qualcomm | No proven server CPU revenue; handset cyclical core |
| AVGO | Broadcom | Not a CPU; concentration in 3 ASIC customers (rumored) |
| MRVL | Marvell | Not a CPU; lumpy ASIC ramp timing |
| TSM | TSMC | Geopolitical tail, capex intensity, customer concentration in Apple/Nvidia/AMD |
| SMCI | Supermicro | 6.3% gross margin, accounting overhang history, customer concentration |
| DELL | Dell Technologies | ISG margin compression as AI mix grows; working-capital strain on backlog |
| HPE | HPE | Server segment weak; Juniper integration distraction |
| 992 HK | Lenovo | Disclosure granularity; PC cyclical drag |
| 2382 TT | Quanta | AI server attribution opacity |
| 6669 TT | Wiwynn | Customer concentration; Q4 GM 7.2% |
| 2356 TT | Inventec | Late to AI server cycle; modest growth |

## 4. Demand Drivers — Reframed

Hyperscaler capex is real (see §6) but the bear question is **what fraction of capex becomes merchant CPU revenue**.

**Decomposition assumption (mine, UNSUPPORTED but defensible)**: In a GB200 NVL72 rack costing ~$3M, the CPU silicon (Grace, ARM, captive Nvidia) is <5% of BOM. In an AMD MI300X system, the host CPU (one or two EPYC) may be ~3–6% of BOM. In a TPU/Trainium pod, host CPUs (often custom ARM) are similarly <5%.

If 60–70% of incremental hyperscaler compute capex flows into accelerated systems, then **CPU silicon's share of capex declines** even as CPU unit demand rises. This is the structural fact bulls under-weight.

**General-purpose refresh** is a separate, healthier driver — but it's a 3–5 year cycle, and merchant CPU vendors face share loss from Graviton/Cobalt at exactly the cloud customers where refresh dollars concentrate.

| Driver | Direction | Confidence | Bear caveat |
|---|---|---|---|
| Hyperscaler capex | Up sharply | High | Mostly GPU/HBM/networking |
| AI server unit demand | Up | High | Captive ARM share rising |
| General-purpose refresh | Up modestly | Medium | x86 share losing to Graviton/Cobalt |
| Inference workloads on CPU | Mixed | Low-Medium | Inference increasingly runs on accelerators or specialized inference ASICs (Groq, Cerebras, Inferentia) |
| Edge / sovereign AI | Up | Low | Not a near-term P&L driver |

## 5. Server CPU Market Structure

Three market structure observations the bear side should hold:

1. **Bifurcation is also a TAM split.** Merchant x86 (Intel + AMD) competes for a shrinking slice of incremental cloud CPU capacity. Independent verification needed (Mercury Research paid data) but Arm's own management commentary that Neoverse is "approaching 50%" of top-hyperscaler deployments is a *bear* signal for x86, not a neutral market data point.

2. **AI rack architecture dictates CPU choice, and Nvidia is choosing ARM.** Grace-Hopper, Grace-Blackwell GB200/GB300, and the 2026 Vera platform all use Nvidia's own ARM CPU. Each rack sold is a unit of x86 displacement. The merchant-CPU "AI attach" thesis assumes Nvidia loses platform share or that GB-series volumes underperform — neither is supported by current evidence.

3. **Custom ASIC racks have lowest CPU intensity.** TPU, Trainium, MAIA pods are vertically integrated; the host CPU is often a captive ARM SoC. Hyperscaler ASIC TAM growth is **directly subtractive** to merchant CPU vendors.

## 6. Hyperscaler / Data Center Order Signals

I accept the same headline capex numbers the bull side cited (Microsoft $37.5B FY26 Q2; Alphabet $175–185B; Amazon ~$200B; Meta $115–135B 2026; Oracle RPO $553B). I treat these as **High confidence** but **non-diagnostic for CPU vendor revenue**.

Bear-relevant overlays not in the bull memo:
- **Microsoft FY26 Q2 commentary** that capex skews to "short-lived assets, primarily GPUs and CPUs" is a verbal pairing — quantitative split is not disclosed. The sentence is consistent with a 90/10 GPU/CPU dollar split. (UNSUPPORTED specific ratio; Confidence: Low on the CPU $ share.)
- **Hyperscaler internal silicon programs are accelerating, not stable.** AWS publicly stated Graviton is the majority of new EC2 CPU capacity (rough management framing, needs exact citation; Confidence Medium). Microsoft Cobalt 100 GA in 2024; Azure has Cobalt-backed VM SKUs in production. Google Axion launched 2024. Each new generation chips at merchant CPU unit growth at the cloud frontier.
- **Capex peak risk.** Aggregate 2026 hyperscaler capex of ~$700B+ is unprecedented. Bear thesis: any 2H26 deceleration whips OEM/ODM and merchant CPU first, before GPU. (My assumption; Confidence Low.)

## 7. OEM/ODM — Revenue Up, Quality Down

Confirmed (and bear-flag) data:
- **Supermicro Q2 FY26: $12.7B revenue, gross margin 6.3%** [Supermicro IR]. This is a brutal mix-driven margin print: revenue scaling does not protect operating income at single-digit gross margins.
- **Wiwynn Q4 2025 GM 7.2%, FY25 revenue +163.7%** [Wiwynn IR]. Same pattern.
- **Dell ISG margin** trajectory needs scrutiny. $43B backlog at low ISG margin is *less valuable* than $20B at historical margin — backlog $ is a vanity metric without margin disclosure. (Bear caveat; Confidence Medium on margin pressure.)

**Bear conclusion**: OEM/ODM are AI capex *barometers*, not investments. The right way to play them is tactical, with stops on ASP-deflation prints. Wiwynn and SMCI have shown how quickly the margin print resets. They are **not** quality compounders.

## 8. CPU Pricing / ASP / Margin

This section is where the bull narrative is weakest.

**What is confirmed:** Server-system ASP +92.8% YoY in 2Q25 (Gartner) [Gartner via secondary press]. This is dominated by GPU, HBM, NIC, PSU, and liquid-cooling content — **not CPU silicon**.

**What is NOT confirmed:** Tom's Hardware's April 2026 reporting of 10–20% server CPU price hikes. Treat as **rumor / Low confidence**. Channel checks have not been corroborated by Intel or AMD price disclosures or by Mercury Research transaction data.

**Bear interpretation:**
- AMD's apparent revenue-share-above-unit-share at Mercury is **mix shift**, not pricing power. Higher core count Genoa/Bergamo/Turin SKUs at higher price points pull blended ASP up; that is share gain via product, not the same as industry CPU price inflation.
- Intel's DCAI revenue recovery (Q1 2026 $5.1B, +22% YoY) is real but plausibly comes from (a) AI host-CPU attach to GPU systems at lower margin, (b) Sierra Forest E-core SKUs that are lower price/socket, and (c) easier comp base. **None of these support sustained merchant CPU pricing power.** [Verification gap.]
- The CPU's share of AI server BOM is structurally declining as accelerator content rises. Even with stable CPU $ per server, accelerator $ per server is up 5–10x.

**Net**: CPU ASP/margin is the weakest link in the bull thesis and the most actionable bear angle.

## 9. x86 vs ARM Substitution Risk

This is real, accelerating, and largely captured by **Arm Holdings as a stock with a problem**: it captures the substitution narratively but **the royalty rate per CPU is small** (typically low single-digit %). ARM's enterprise valuation appears to discount substantial royalty rate expansion, which is contested.

| Architecture/Vendor | Status | Bear implication |
|---|---|---|
| x86 (Intel/AMD) | Loses share at hyperscaler frontier | Negative for INTC, mildly negative for AMD CPU line |
| AWS Graviton (custom Neoverse) | 4th gen, majority of new EC2 CPU capacity (mgmt framing) | Negative x86, neutral-to-positive ARM royalties (small $) |
| Microsoft Cobalt | GA, Azure SKUs ramping | Negative x86 |
| Google Axion | GA 2024 | Negative x86 |
| Nvidia Grace/Vera | Standard CPU in GB200/GB300/Vera Rubin | Negative x86 |
| Ampere | Independent merchant ARM (acquired by SoftBank 2025) | Limited cloud share; not investable |
| Qualcomm Oryon datacenter | Not yet shipping at scale | Not material |

**Bear thesis on ARM stock**: ARM benefits from substitution, but at a low fixed royalty rate, with rising hyperscaler bargaining power on royalty terms (custom-design license structures). Stock has historically traded at extreme P/E multiples that require both volume *and* royalty rate expansion.

## 10. Company-By-Company

### AMD — Watchlist (not Strong)
- FY25 Data Center revenue $16.6B, +32% YoY [AMD IR — Confirmed]. **Critical disclosure issue**: this segment includes both EPYC and Instinct. Instinct is a GPU. The "AMD CPU thesis" cannot be cleanly read from this number. Bear estimate (UNSUPPORTED): EPYC growth probably sub-20% with Instinct doing the heavy lifting; needs management disaggregation.
- EPYC continues to gain share against Intel (Confirmed directionally; specific numbers require Mercury data).
- Bear risk: Instinct competes against Nvidia, where AMD is far behind on software (CUDA moat) and roadmap cadence. Bull case requires both EPYC share gains and Instinct traction — two compounded probabilities.
- **Verdict**: AMD is the cleanest CPU equity but is increasingly priced as a GPU equity. Confidence in EPYC tailwind: Medium. Confidence in Instinct closing the Nvidia gap: Low.

### Intel — Avoid (CPU thesis only)
- Q1 2026 DCAI $5.1B, +22% YoY [Intel IR — Confirmed]. Bear caveat: read against an easy comp; Sierra Forest E-core SKU mix may flatter unit count at lower ASP/socket.
- Foundry losses ongoing; 18A ramp is unproven at volume. Even successful 18A doesn't necessarily restore DCAI margin if AMD continues taking share.
- Capital structure includes large foundry capex commitments and government funding tied to deliverables.
- **Verdict**: Turnaround optionality only. Not investable as a clean CPU growth name.

### Arm Holdings — Avoid (valuation)
- Q3 FYE26 revenue +26% YoY, royalty +27% YoY [Arm IR — Confirmed]. 1B Neoverse cores cumulative deployment [Arm IR — Confirmed but cumulative ≠ annual].
- "Approaching 50% share at top hyperscalers" — **management claim, not independent data** (Medium confidence as directional indicator).
- Royalty $/server CPU is low; revenue scaling is paced by hyperscaler design timelines.
- Stock multiple has been persistently high. Bear: pricing requires both unit growth AND royalty rate expansion AND no hyperscaler pushback on AALA terms.
- **Verdict**: Right side of substitution; wrong price.

### Qualcomm — Avoid (CPU thesis)
- Server CPUs "in development"; no revenue line. AI200/AI250 inference cards and Alphawave acquisition are option value, not P&L.
- **Verdict**: Agree with bull side. Not a CPU equity.

### Broadcom — Excluded from CPU framework
- Q4 FY25 AI semis +74% YoY [Broadcom IR — Confirmed]. Custom AI ASIC and Ethernet networking driver.
- Note: customer concentration in three hyperscaler ASIC programs is a tail risk that does not show up in headlines.
- **Verdict**: Not a CPU thesis. Strong AI silicon name but outside scope.

### Marvell — Excluded from CPU framework
- FY26 revenue +42%, Q4 data center 74% of revenue [Marvell IR — Confirmed].
- Concentrated in custom ASIC programs (AWS Trainium tail; rumored loss of Microsoft program is a recurring overhang — needs verification).
- **Verdict**: Not a CPU thesis.

### TSMC — Watchlist
- Wins on substantially every CPU/GPU/ASIC architecture.
- Bear risks: capex intensity, geopolitical (Taiwan), customer concentration, currency.
- Multiple has expanded to reflect AI tailwind; not the asymmetric trade it was in 2023.
- **Verdict**: Best clean exposure, but mature thesis at current valuation. Watchlist.

### Supermicro — Avoid as long, possible tactical
- Q2 FY26 $12.7B sales, GM 6.3% [SMCI IR — Confirmed]. Operating leverage at 6.3% GM is poor.
- Customer concentration risk; prior accounting overhang (10-K filing delays in 2024-2025) is a residual governance risk.
- **Verdict**: Avoid as quality holding. Trade only with tight risk management.

### Dell — Watchlist (highest-quality OEM)
- FY26 AI orders >$64B, shipped >$25B, FY27 backlog $43B [Dell IR — Confirmed].
- Bear caveats: ISG margin trajectory; working capital expansion to fund inventory; backlog $/profit ratio undisclosed.
- **Verdict**: Best-of-the-OEMs by disclosure quality and balance sheet. Watchlist if ISG margin holds.

### HPE — Avoid (CPU thesis)
- Q1 FY26 server revenue weak; Juniper integration ongoing [HPE IR — Confirmed directionally].
- Less clean AI server growth profile than Dell.
- **Verdict**: Not a CPU vehicle.

### Lenovo — Watchlist (with caveats)
- Server segment growing; granularity insufficient.
- PC cycle drag and FX exposure.
- **Verdict**: Diversified hardware, not a clean CPU play.

### Quanta — Watchlist (cyclical)
- 2025 monthly sales +50.5% YoY [aggregated company filings — Confirmed directionally].
- AI server attribution and customer concentration need verification.
- **Verdict**: Tactical AI server beta, not a high-quality compounder.

### Wiwynn — Avoid as quality holding
- FY25 revenue +163.7%, AI products >50% of mix; Q4 GM 7.2% [Wiwynn IR — Confirmed].
- Customer concentration (heavy single-customer exposure suspected; needs verification).
- **Verdict**: Sharp cyclical print; margin compression evidence is canonical bear data point.

### Inventec — Watchlist
- FY25 revenue +6.95%; AI server growth claims need verification.
- Late to the cycle compared with Quanta/Wiwynn.
- **Verdict**: Late mover; insufficient AI exposure to be a clean trade.

## 11. Bull Case (briefly, for completeness)

AI inference shifts to CPU-native runtimes; general-purpose refresh accelerates; AMD compounds EPYC share + Instinct ramp; Intel DCAI re-rates on 18A success; Arm royalty expansion; OEM/ODM margin stabilizes as supply normalizes; capex broadens beyond hyperscalers to enterprise/sovereign.

## 12. Bear Case (my base view)

CPU silicon is a small and shrinking share of AI server BOM. Captive ARM displaces merchant x86 at hyperscalers. AMD's CPU growth is masked by Instinct in segment reporting and is sub-20% on a clean basis. Intel's DCAI green shoot fades as Sierra Forest mix and AMD share loss reassert. Arm's stock is right-thesis-wrong-price. OEM/ODM margins remain single-digit and earnings disappoint as capex pull-forward unwinds in 2H26. Hyperscaler capex peaks in 2026 and decelerates in 2027, exposing the cyclical nature of "AI server" earnings. The cleanest beneficiary is TSMC, but its multiple already prices that.

## 13. Base Case

CPU unit demand grows mid-single-digits; merchant x86 share declines 200–400 bps to ARM by 2027; CPU $ share of AI server BOM stays in the 3–7% range; OEM/ODM gross margins remain in the 6–10% range and don't recover; AMD outperforms Intel at the equity level but underperforms a "GPU first" portfolio; Arm and TSMC roughly track index-level returns from current levels. Risk-reward across the CPU-equity universe is **mediocre vs the AI accelerator universe**.

## 14. Key Claims Table

| ID | Claim | Company | Category | Source | Confidence | Status |
|---|---|---|---|---|---|---|
| C1 | AMD FY25 Data Center segment was $16.6B, +32% YoY (includes EPYC + Instinct) | AMD | Revenue | AMD Q4 2025 release [ir.amd.com] | High | Confirmed fact — but segment commingles CPU + GPU |
| C2 | EPYC-only revenue is not separately disclosed by AMD | AMD | Disclosure | AMD 10-K — segment footnotes | High | Confirmed fact |
| C3 | Intel Q1 2026 DCAI $5.1B, +22% YoY | Intel | Revenue | Intel Q1 2026 release [intc.com] | High | Confirmed fact |
| C4 | Intel DCAI Q1 strength may reflect Sierra Forest E-core mix and easy comp | Intel | Margin | Bear assumption | Low | UNSUPPORTED — analyst inference |
| C5 | Microsoft FY26 Q2 capex $37.5B, "primarily GPUs and CPUs" — quantitative split not disclosed | Microsoft | Capex | MSFT FY26 Q2 release | High on figure / Low on CPU $ share | Confirmed fact + management framing |
| C6 | Alphabet 2026 capex guide $175–185B | Alphabet | Capex | Alphabet Q4 2025 release | High | Management guidance |
| C7 | Amazon expects ~$200B 2026 capex | Amazon | Capex | Amazon Q4 2025 release | High | Management guidance |
| C8 | Meta 2026 capex guide $115–135B | Meta | Capex | Meta Q4 2025 release | High | Management guidance |
| C9 | Server-system ASP +92.8% YoY in 2Q25 | Industry | Pricing | Gartner via secondary press | Medium | Analyst estimate — system, not CPU |
| C10 | Tom's Hardware reports 10–20% server CPU price hikes since March 2026 | INTC/AMD | Pricing | tomshardware.com | Low | Market rumor — UNVERIFIED |
| C11 | Arm Q3 FYE26 revenue +26%, royalty +27% YoY | Arm | Revenue | Arm IR | High | Confirmed fact |
| C12 | Arm Neoverse "approaching 50%" share at top hyperscalers | Arm | Share | Arm management commentary | Medium | Management claim — not independent data |
| C13 | AWS Graviton is the majority of new EC2 CPU capacity | AWS | Share | AWS public framing (re:Invent 2024) | Medium | Management framing — needs primary citation |
| C14 | Microsoft Cobalt and Google Axion are GA in production VM SKUs | MSFT/GOOG | Architecture | Azure/GCP product pages | High | Confirmed fact |
| C15 | Nvidia GB200/GB300 racks use ARM-based Grace CPU as host | Nvidia | Architecture | Nvidia product spec | High | Confirmed fact — implies x86 displacement |
| C16 | Supermicro Q2 FY26 revenue $12.7B, GM 6.3% | SMCI | Margin | Supermicro IR | High | Confirmed fact |
| C17 | Wiwynn FY25 revenue +163.7%, Q4 GM 7.2% | Wiwynn | Margin | Wiwynn IR | High | Confirmed fact |
| C18 | Dell FY26 AI orders >$64B; FY27 backlog $43B | Dell | Orders | Dell Q4 FY26 release | High | Confirmed fact — margin not disclosed by AI mix |
| C19 | Qualcomm has no shipping server CPU revenue line | QCOM | Product | Qualcomm 10-K segment disclosure | High | Confirmed fact |
| C20 | Broadcom Q4 FY25 AI semis +74% YoY | Broadcom | Revenue | Broadcom IR | High | Confirmed fact — not a CPU |
| C21 | Marvell FY26 revenue +42%, Q4 DC 74% of revenue | Marvell | Revenue | Marvell IR | High | Confirmed fact — not a CPU |
| C22 | CPU $ share of AI server BOM is 3–7% range | Industry | BOM | Industry teardowns + analyst estimates | Low-Medium | Analyst estimate — needs primary teardown |
| C23 | Aggregate 2026 hyperscaler capex (top 4 + Oracle) >$700B | Industry | Capex | Sum of company guidance | High | Derived from guidance |
| C24 | 2026 hyperscaler capex may decelerate in 2H26 | Industry | Capex | Bear assumption | Low | UNSUPPORTED — scenario |
| C25 | ARM Holdings royalty per server CPU is low single-digit % of CPU ASP | Arm | Economics | Industry research, ARM filings | Medium | Inference from disclosed royalty pool |

## 15. Evidence Gaps

Beyond the bull-side gaps, bear-priority verification:

1. **EPYC vs Instinct revenue split** at AMD — without this, "AMD CPU growth" cannot be assessed.
2. **CPU $ share of GB200/MI300/TPU/Trainium rack BOM** — primary teardown or hyperscaler disclosure needed.
3. **Mercury Research paid data** for AMD/Intel/Arm server CPU unit and revenue share by quarter, including blended ASP.
4. **Graviton share of AWS EC2 CPU capacity** — quantitative disclosure, not management framing.
5. **Cobalt/Axion deployment scale** — VM-instance-week or core-week metrics, not just product launch.
6. **Verification of the Tom's Hardware CPU price hike claim** via channel checks, distributor pricing, OEM commentary on FY26 Q2 calls.
7. **Dell ISG operating margin trajectory** by AI server mix; same for Lenovo ISG and HPE Server.
8. **Wiwynn / SMCI customer concentration** disclosures.
9. **Arm Holdings royalty rate per Neoverse compute subsystem (CSS)** vs traditional architectural license.
10. **Sierra Forest revenue mix** within Intel DCAI Q1 2026 — to test the "easy comp + low ASP mix" bear hypothesis.
11. **Whether OpenAI, xAI, Anthropic, and major neoclouds are buying ARM- or x86-host AI servers** (proxies for non-hyperscaler accelerator-rack CPU mix).
12. **Used/refurb server market signals** — early-cycle hyperscaler retirement of x86 fleets would be a leading bear indicator.

## 16. Initial Bear-Tilted Ranking

| Tier | Companies | Reasoning |
|---|---|---|
| **Strong candidate (CPU thesis)** | *(none with conviction)* | The cleanest CPU equity — AMD — is increasingly a GPU equity; thesis is dilute |
| **Watchlist** | AMD, TSMC, Dell | Highest-quality names, but priced or impure |
| **Avoid** | Intel, Arm Holdings (valuation), Supermicro, Wiwynn, HPE, Inventec, Qualcomm | Each fails the risk-reward bar for distinct reasons |
| **Excluded from CPU framework** | Broadcom, Marvell | Strong AI names, but not CPU equities |
| **Tactical only** | Quanta, Lenovo | Cyclical AI capex trades, not investments |

This ranking will tighten or loosen as evidence resolves the gaps in §15.

## 17. What Must Be Verified Next (bear priorities)

1. **Pull Mercury Research server CPU share data** (paid) — settle x86 vs ARM and AMD vs Intel quantitatively.
2. **Quantify EPYC-only revenue** at AMD via management commentary, channel checks, and supply-chain triangulation.
3. **Build CPU-$ share of BOM** for GB200, GB300, MI300X, Trainium2, TPU v5/v6, MAIA — primary teardown sources or hyperscaler disclosures.
4. **Verify or kill the Tom's Hardware "10–20% CPU price hike" rumor** via OEM, distributor, and Intel/AMD price-list checks.
5. **Track Q1 / Q2 2026 capex revision direction** at Microsoft, Amazon, Alphabet, Meta, Oracle, Coreweave, Nebius — direction matters more than level for cyclical risk.
6. **Test bear scenario for Intel** in which DCAI growth decelerates as Sierra Forest comps lap and AMD share loss continues.
7. **Stress-test ARM Holdings model** for royalty rate compression scenarios as hyperscaler bargaining power rises.
8. **Map customer concentration** at SMCI, Wiwynn, Quanta, Inventec — concentration breaks faster than backlog fills.
9. **Watch for Nvidia/AMD margin guidance shifts in 2H26** — first sign of capex peak.
10. **Track Qualcomm data center revenue line emergence** — if it emerges, re-rate.

---

**Closing note**: I do not dispute most of the bull-side facts. I dispute their investment implication. The same data set — large hyperscaler capex, growing AI server units, share gains in select x86 designs, ARM royalty growth — is consistent with a **mediocre risk-reward in CPU equities at current valuations** when accelerator and foundry equities offer cleaner exposure to the same underlying compute demand. The bear thesis is not "AI is overhyped"; it is "the CPU is the wrong layer of the stack to express AI conviction."
        ```

codex
I’ll read the existing transcript, claim register, and source log first so the critique fits the project’s current evidence structure, then I’ll verify the highest-risk financial and product claims against primary sources where possible.
exec
/usr/bin/zsh -lc "sed -n '1,220p' cpu-investment-research-2/claims/claim_register.md" in /mnt/c/Users/hyc97/workspace/Ecclesia/CPU
exec
/usr/bin/zsh -lc "rg -n \"Claude|bear|bull|C[0-9]+|AMD|Intel|Arm|Supermicro|Dell|Wiwynn|Gartner|Tom's Hardware|Graviton|Cobalt|Axion|GB200|GB300|Grace|hyperscaler|capex\" cpu-investment-research-2/transcript/full_debate.md" in /mnt/c/Users/hyc97/workspace/Ecclesia/CPU
exec
/usr/bin/zsh -lc "sed -n '1,220p' cpu-investment-research-2/sources/source_log.md" in /mnt/c/Users/hyc97/workspace/Ecclesia/CPU
 succeeded in 176ms:
# Claim Register

| ID | Claim | Company | Category | Source | Confidence | Challenged By | Status |
|---|---|---|---|---|---|---|---|

 succeeded in 176ms:
15:The bullish CPU thesis is investable, but only if framed narrowly: AI does not eliminate CPU demand; it increases demand for orchestration, inference serving, storage, networking, and general-purpose cloud refresh. The strongest evidence is not a generic “AI needs CPUs” narrative, but the combination of hyperscaler capex, OEM AI-server backlog, AMD EPYC share gains, Intel DCAI recovery, and Arm server penetration.
17:Base conclusion: **own CPU upside through AMD, Arm, and TSMC first; treat OEM/ODM names as execution and margin trades; treat Intel as a turnaround watchlist name; avoid Qualcomm as a server CPU thesis until products/customers are proven.**
21:- **CPU vendors:** AMD and Intel dominate merchant x86 server CPUs.
22:- **Architecture/IP:** Arm benefits from hyperscaler and Nvidia Arm CPU adoption through royalties and licensing.
24:- **Foundry:** TSMC is the broadest beneficiary across AMD, Arm-based custom silicon, AI ASICs, and networking silicon.
25:- **OEM/ODM:** Dell, Supermicro, HPE, Lenovo, Quanta, Wiwynn, Inventec convert AI/server demand into revenue, but margins are structurally pressured by pass-through GPU/BOM economics.
31:| Direct CPU | AMD, Intel | Highest direct exposure |
32:| Architecture/IP | Arm | High exposure to Arm substitution and hyperscaler custom CPUs |
36:| OEM/ODM | Dell, SMCI, HPE, Lenovo, Quanta, Wiwynn, Inventec | Demand signal; lower-quality margin capture |
40:Confirmed demand signals are strong. Dell closed **more than $64B of FY26 AI-optimized server orders**, shipped **more than $25B**, and entered FY27 with **$43B backlog**. Microsoft reported FY26 Q2 capex of **$37.5B**, with roughly two-thirds on short-lived assets, “primarily GPUs and CPUs,” and said demand exceeds supply. Alphabet guided 2026 capex to **$175B-$185B**. Amazon said it expects about **$200B** of 2026 capex.
48:- **Merchant x86:** AMD gaining share and richer mix; Intel still large and showing recent DCAI recovery.
49:- **Captive/custom Arm:** AWS Graviton, Microsoft Cobalt, Nvidia Grace/Vera, and other hyperscaler CPUs pressure x86 over time.
52:Important caveat: IDC “non-x86 server” growth is not the same as Arm CPU share. Accelerated systems, proprietary architectures, and high-value AI racks can distort revenue share.
57:- Microsoft FY26 Q2 capex: **$37.5B**, roughly two-thirds short-lived assets, primarily GPUs and CPUs.
58:- Alphabet 2026 capex guide: **$175B-$185B**.
59:- Amazon 2026 capex expectation: about **$200B**.
60:- Meta 2026 capex guide: **$115B-$135B**.
67:Dell and Supermicro show extreme AI-server revenue conversion, but margin quality differs. Supermicro Q2 FY26 net sales reached **$12.7B**, but gross margin fell to **6.3%**, showing how AI server growth can be BOM-heavy and margin-thin. Wiwynn’s FY25 revenue rose **163.7% YoY**, with AI-related products over half of revenue, but Q4 gross margin fell to **7.2%** due to product mix.
73:Confirmed data supports **server-system ASP inflation**, not clean CPU ASP inflation. Gartner estimated 2Q25 server vendor revenue +89.9% YoY while shipments declined 1.5%, driven by a 92.8% ASP increase from AI-optimized server demand. Mercury data reported by Tom’s Hardware shows AMD x86 server revenue share above unit share, consistent with richer mix.
75:Market rumor: Tom’s Hardware reported in April 2026 that server CPU prices rose 10%-20% since March 2026 due to AI/inference demand. Treat as **rumor / Low confidence** until checked against OEM quotes, distributor pricing, and Intel/AMD disclosures.
77:## 9. x86 Vs Arm Substitution Risk
79:Arm risk is real and investable. Arm reported Q3 FYE26 revenue +26% YoY and royalty revenue +27% YoY; management also said Neoverse CPUs surpassed 1B deployed cores and expects Arm share among top hyperscalers to reach nearly 50%. That is management guidance/claim, not independent market share.
81:For AMD/Intel, Arm is both a threat and a market validator: total server CPU demand can grow while x86 share declines.
85:- **AMD:** Best direct CPU candidate. FY25 Data Center revenue was **$16.6B, +32% YoY**, driven by EPYC CPUs and Instinct GPUs. Key risk: AMD does not disclose EPYC-only revenue, so CPU-specific growth must be inferred.
86:- **Intel:** Watchlist turnaround. Q1 2026 DCAI revenue was **$5.1B, +22% YoY**. Bullish CPU signal, but AMD share loss and foundry execution remain unresolved.
87:- **Arm:** Strong structural candidate. Benefits from hyperscaler custom CPUs and Nvidia Arm CPU platforms. Risk is valuation and indirect royalty capture.
91:- **TSMC:** Strong candidate. Broad beneficiary of advanced compute regardless of x86 vs Arm vs ASIC winner.
92:- **Supermicro:** Watchlist. Exceptional revenue growth, but margin compression and customer concentration risk are central.
93:- **Dell:** Stronger OEM candidate. AI orders/backlog are unusually explicit; watch ISG margin and working capital.
97:- **Wiwynn:** Strong ODM beta. AI products over half of FY25 revenue; margin pressure must be monitored.
102:AI inference and agentic workloads lift CPU attach, general-purpose server refresh, and x86/Arm server CPU demand simultaneously. AMD keeps gaining profitable EPYC share, Intel supply tightens DCAI pricing, Arm royalties compound from hyperscaler CPUs, and TSMC captures advanced-node volume across all winners.
106:AI rack architectures integrate more Arm/custom CPUs, reducing merchant x86 attach. CPU ASP rumors fade, AI capex pauses, OEM/ODM backlogs prove low-margin, and server CPU value is captured by hyperscalers, Nvidia, custom ASIC vendors, and TSMC rather than Intel/AMD.
110:Server CPU demand grows, but less explosively than GPU/ASIC demand. AMD and Arm are the cleanest equity expressions; Intel improves but remains execution-heavy; OEM/ODM revenue grows faster than profit; TSMC remains the best diversified beneficiary.
119:| K4 | AMD FY25 Data Center revenue was $16.6B, +32% YoY. | AMD | Revenue | [AMD](https://ir.amd.com/news-events/press-releases/detail/1276/amd-reports-fourth-quarter-and-full-year-2025-financial-results) | High | Confirmed fact |
120:| K5 | Intel Q1 2026 DCAI revenue was $5.1B, +22% YoY. | Intel | Revenue | [Intel](https://www.intc.com/news-events/press-releases/detail/1767/intel-reports-first-quarter-2026-financial-results) | High | Confirmed fact |
121:| K6 | Microsoft FY26 Q2 capex was $37.5B; roughly two-thirds was GPUs/CPUs. | Microsoft | Capex | [Microsoft](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q2) | High | Confirmed fact |
122:| K7 | Dell FY26 AI server orders exceeded $64B; backlog $43B. | Dell | Orders | [Dell](https://investors.delltechnologies.com/news-releases/news-release-details/dell-technologies-delivers-fourth-quarter-and-full-year-fiscal-3) | High | Confirmed fact |
123:| K8 | Supermicro Q2 FY26 sales were $12.7B; gross margin 6.3%. | SMCI | OEM margin | [Supermicro](https://ir.supermicro.com/news/news-details/2026/Supermicro-Announces-Second-Quarter-Fiscal-Year-2026-Financial-Results/default.aspx) | High | Confirmed fact |
124:| K9 | Wiwynn FY25 revenue +163.7%; AI products over 50% of revenue. | Wiwynn | ODM demand | [Wiwynn](https://www.wiwynn.com/news/wiwynn-reports-fourth-quarter-2025-financial-results) | High | Confirmed fact |
125:| K10 | Arm Q3 FYE26 revenue +26%; royalty revenue +27%. | Arm | Revenue | [Arm](https://newsroom.arm.com/news/arm-q3-fye26-results) | High | Confirmed fact |
126:| K11 | Arm says Neoverse surpassed 1B deployed cores and may approach 50% share at top hyperscalers. | Arm | ARM adoption | [Arm](https://newsroom.arm.com/news/arm-q3-fye26-results) | Medium | Management claim |
129:| K14 | Meta guides 2026 capex to $115B-$135B. | Meta | Capex | [Meta](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Fourth-Quarter-and-Full-Year-2025-Results/) | High | Management guidance |
130:| K15 | Alphabet guides 2026 capex to $175B-$185B. | Alphabet | Capex | [Alphabet](https://abc.xyz/investor/events/event-details/2026/2025-Q4-Earnings-Call-2026-Dr_C033hS6/default.aspx) | High | Management guidance |
131:| K16 | Amazon expects about $200B capex in 2026. | Amazon | Capex | [Amazon](https://www.aboutamazon.com/news/company-news/amazon-earnings-q4-2025-report) | High | Management guidance |
133:| K18 | Server CPU prices reportedly rose 10%-20% since March 2026. | Intel/AMD | Pricing | [Tom’s Hardware](https://www.tomshardware.com/pc-components/cpus/shifting-need-for-cpus-in-ai-workloads-drives-intensifying-shortages-price-hikes) | Low | Market rumor |
137:- EPYC-only revenue and Intel Xeon-only revenue.
139:- CPU attach rate by architecture: HGX, GB200/GB300, MI300/MI350, Trainium, TPU, custom ASIC.
141:- Arm royalty dollars per Neoverse server CPU.
142:- Hyperscaler order split across Dell, SMCI, Quanta, Wiwynn, Inventec, Foxconn, and internal builds.
149:| Strong candidate | AMD, Arm, TSMC, Dell, Wiwynn |
150:| Watchlist | Intel, Broadcom, Marvell, Supermicro, Lenovo, Quanta, HPE, Inventec |
155:1. Build an architecture-level CPU attach table for Nvidia GB200/GB300, AMD MI300/MI350/MI400, AWS Trainium, Google TPU, and major ASIC racks.
156:2. Pull Mercury/IDC paid data for AMD, Intel, and Arm server CPU unit and revenue share.
157:3. Verify CPU pricing with OEM quotes, distributor checks, and hyperscaler procurement commentary.
158:4. Split AMD Data Center into EPYC vs Instinct using management commentary and channel estimates.
159:5. Track Q1/Q2 2026 capex updates from Microsoft, Amazon, Alphabet, Meta, Oracle, and major neoclouds.
185:- Hyperscaler capex and server architecture
189:- AMD, Intel, ARM Holdings, Qualcomm, Broadcom, Marvell, TSMC, Supermicro, Dell, HPE, Lenovo, Quanta, Wiwynn, Inventec
209:You are Codex, acting as a bullish but evidence-disciplined CPU equity researcher.
301:web search: 2025 AMD annual report data center revenue EPYC server CPU 2025 10-K
303:web search: site:ir.amd.com 2026 Q4 2025 AMD data center revenue EPYC annual results 2025
315:web search: Mercury Research server CPU market share AMD Intel Arm 2025 Q4 server CPU share
319:web search: Amazon Q4 2025 earnings capital expenditures AI infrastructure 2026 AWS capex official
321:web search: site:abc.xyz investor 2025 Q4 results capital expenditures 2026 AI infrastructure Alphabet capex 2025
331:web search: Supermicro fiscal 2026 Q2 results AI server revenue liquid cooling backlog official
333:web search: Arm Holdings fiscal 2025 annual report Neoverse data center royalty revenue server official
335:web search: Intel reports first quarter 2026 financial results Data Center AI revenue Xeon official April 2026
341:The bullish CPU thesis is investable, but only if framed narrowly: AI does not eliminate CPU demand; it increases demand for orchestration, inference serving, storage, networking, and general-purpose cloud refresh. The strongest evidence is not a generic “AI needs CPUs” narrative, but the combination of hyperscaler capex, OEM AI-server backlog, AMD EPYC share gains, Intel DCAI recovery, and Arm server penetration.
343:Base conclusion: **own CPU upside through AMD, Arm, and TSMC first; treat OEM/ODM names as execution and margin trades; treat Intel as a turnaround watchlist name; avoid Qualcomm as a server CPU thesis until products/customers are proven.**
347:- **CPU vendors:** AMD and Intel dominate merchant x86 server CPUs.
348:- **Architecture/IP:** Arm benefits from hyperscaler and Nvidia Arm CPU adoption through royalties and licensing.
350:- **Foundry:** TSMC is the broadest beneficiary across AMD, Arm-based custom silicon, AI ASICs, and networking silicon.
351:- **OEM/ODM:** Dell, Supermicro, HPE, Lenovo, Quanta, Wiwynn, Inventec convert AI/server demand into revenue, but margins are structurally pressured by pass-through GPU/BOM economics.
357:| Direct CPU | AMD, Intel | Highest direct exposure |
358:| Architecture/IP | Arm | High exposure to Arm substitution and hyperscaler custom CPUs |
362:| OEM/ODM | Dell, SMCI, HPE, Lenovo, Quanta, Wiwynn, Inventec | Demand signal; lower-quality margin capture |
366:Confirmed demand signals are strong. Dell closed **more than $64B of FY26 AI-optimized server orders**, shipped **more than $25B**, and entered FY27 with **$43B backlog**. Microsoft reported FY26 Q2 capex of **$37.5B**, with roughly two-thirds on short-lived assets, “primarily GPUs and CPUs,” and said demand exceeds supply. Alphabet guided 2026 capex to **$175B-$185B**. Amazon said it expects about **$200B** of 2026 capex.
374:- **Merchant x86:** AMD gaining share and richer mix; Intel still large and showing recent DCAI recovery.
375:- **Captive/custom Arm:** AWS Graviton, Microsoft Cobalt, Nvidia Grace/Vera, and other hyperscaler CPUs pressure x86 over time.
378:Important caveat: IDC “non-x86 server” growth is not the same as Arm CPU share. Accelerated systems, proprietary architectures, and high-value AI racks can distort revenue share.
383:- Microsoft FY26 Q2 capex: **$37.5B**, roughly two-thirds short-lived assets, primarily GPUs and CPUs.
384:- Alphabet 2026 capex guide: **$175B-$185B**.
385:- Amazon 2026 capex expectation: about **$200B**.
386:- Meta 2026 capex guide: **$115B-$135B**.
393:Dell and Supermicro show extreme AI-server revenue conversion, but margin quality differs. Supermicro Q2 FY26 net sales reached **$12.7B**, but gross margin fell to **6.3%**, showing how AI server growth can be BOM-heavy and margin-thin. Wiwynn’s FY25 revenue rose **163.7% YoY**, with AI-related products over half of revenue, but Q4 gross margin fell to **7.2%** due to product mix.
399:Confirmed data supports **server-system ASP inflation**, not clean CPU ASP inflation. Gartner estimated 2Q25 server vendor revenue +89.9% YoY while shipments declined 1.5%, driven by a 92.8% ASP increase from AI-optimized server demand. Mercury data reported by Tom’s Hardware shows AMD x86 server revenue share above unit share, consistent with richer mix.
401:Market rumor: Tom’s Hardware reported in April 2026 that server CPU prices rose 10%-20% since March 2026 due to AI/inference demand. Treat as **rumor / Low confidence** until checked against OEM quotes, distributor pricing, and Intel/AMD disclosures.
403:## 9. x86 Vs Arm Substitution Risk
405:Arm risk is real and investable. Arm reported Q3 FYE26 revenue +26% YoY and royalty revenue +27% YoY; management also said Neoverse CPUs surpassed 1B deployed cores and expects Arm share among top hyperscalers to reach nearly 50%. That is management guidance/claim, not independent market share.
407:For AMD/Intel, Arm is both a threat and a market validator: total server CPU demand can grow while x86 share declines.
411:- **AMD:** Best direct CPU candidate. FY25 Data Center revenue was **$16.6B, +32% YoY**, driven by EPYC CPUs and Instinct GPUs. Key risk: AMD does not disclose EPYC-only revenue, so CPU-specific growth must be inferred.
412:- **Intel:** Watchlist turnaround. Q1 2026 DCAI revenue was **$5.1B, +22% YoY**. Bullish CPU signal, but AMD share loss and foundry execution remain unresolved.
413:- **Arm:** Strong structural candidate. Benefits from hyperscaler custom CPUs and Nvidia Arm CPU platforms. Risk is valuation and indirect royalty capture.
417:- **TSMC:** Strong candidate. Broad beneficiary of advanced compute regardless of x86 vs Arm vs ASIC winner.
418:- **Supermicro:** Watchlist. Exceptional revenue growth, but margin compression and customer concentration risk are central.
419:- **Dell:** Stronger OEM candidate. AI orders/backlog are unusually explicit; watch ISG margin and working capital.
423:- **Wiwynn:** Strong ODM beta. AI products over half of FY25 revenue; margin pressure must be monitored.
428:AI inference and agentic workloads lift CPU attach, general-purpose server refresh, and x86/Arm server CPU demand simultaneously. AMD keeps gaining profitable EPYC share, Intel supply tightens DCAI pricing, Arm royalties compound from hyperscaler CPUs, and TSMC captures advanced-node volume across all winners.
432:AI rack architectures integrate more Arm/custom CPUs, reducing merchant x86 attach. CPU ASP rumors fade, AI capex pauses, OEM/ODM backlogs prove low-margin, and server CPU value is captured by hyperscalers, Nvidia, custom ASIC vendors, and TSMC rather than Intel/AMD.
436:Server CPU demand grows, but less explosively than GPU/ASIC demand. AMD and Arm are the cleanest equity expressions; Intel improves but remains execution-heavy; OEM/ODM revenue grows faster than profit; TSMC remains the best diversified beneficiary.
445:| K4 | AMD FY25 Data Center revenue was $16.6B, +32% YoY. | AMD | Revenue | [AMD](https://ir.amd.com/news-events/press-releases/detail/1276/amd-reports-fourth-quarter-and-full-year-2025-financial-results) | High | Confirmed fact |
446:| K5 | Intel Q1 2026 DCAI revenue was $5.1B, +22% YoY. | Intel | Revenue | [Intel](https://www.intc.com/news-events/press-releases/detail/1767/intel-reports-first-quarter-2026-financial-results) | High | Confirmed fact |
447:| K6 | Microsoft FY26 Q2 capex was $37.5B; roughly two-thirds was GPUs/CPUs. | Microsoft | Capex | [Microsoft](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q2) | High | Confirmed fact |
448:| K7 | Dell FY26 AI server orders exceeded $64B; backlog $43B. | Dell | Orders | [Dell](https://investors.delltechnologies.com/news-releases/news-release-details/dell-technologies-delivers-fourth-quarter-and-full-year-fiscal-3) | High | Confirmed fact |
449:| K8 | Supermicro Q2 FY26 sales were $12.7B; gross margin 6.3%. | SMCI | OEM margin | [Supermicro](https://ir.supermicro.com/news/news-details/2026/Supermicro-Announces-Second-Quarter-Fiscal-Year-2026-Financial-Results/default.aspx) | High | Confirmed fact |
450:| K9 | Wiwynn FY25 revenue +163.7%; AI products over 50% of revenue. | Wiwynn | ODM demand | [Wiwynn](https://www.wiwynn.com/news/wiwynn-reports-fourth-quarter-2025-financial-results) | High | Confirmed fact |
451:| K10 | Arm Q3 FYE26 revenue +26%; royalty revenue +27%. | Arm | Revenue | [Arm](https://newsroom.arm.com/news/arm-q3-fye26-results) | High | Confirmed fact |
452:| K11 | Arm says Neoverse surpassed 1B deployed cores and may approach 50% share at top hyperscalers. | Arm | ARM adoption | [Arm](https://newsroom.arm.com/news/arm-q3-fye26-results) | Medium | Management claim |
455:| K14 | Meta guides 2026 capex to $115B-$135B. | Meta | Capex | [Meta](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Fourth-Quarter-and-Full-Year-2025-Results/) | High | Management guidance |
456:| K15 | Alphabet guides 2026 capex to $175B-$185B. | Alphabet | Capex | [Alphabet](https://abc.xyz/investor/events/event-details/2026/2025-Q4-Earnings-Call-2026-Dr_C033hS6/default.aspx) | High | Management guidance |
457:| K16 | Amazon expects about $200B capex in 2026. | Amazon | Capex | [Amazon](https://www.aboutamazon.com/news/company-news/amazon-earnings-q4-2025-report) | High | Management guidance |
459:| K18 | Server CPU prices reportedly rose 10%-20% since March 2026. | Intel/AMD | Pricing | [Tom’s Hardware](https://www.tomshardware.com/pc-components/cpus/shifting-need-for-cpus-in-ai-workloads-drives-intensifying-shortages-price-hikes) | Low | Market rumor |
463:- EPYC-only revenue and Intel Xeon-only revenue.
465:- CPU attach rate by architecture: HGX, GB200/GB300, MI300/MI350, Trainium, TPU, custom ASIC.
467:- Arm royalty dollars per Neoverse server CPU.
468:- Hyperscaler order split across Dell, SMCI, Quanta, Wiwynn, Inventec, Foxconn, and internal builds.
475:| Strong candidate | AMD, Arm, TSMC, Dell, Wiwynn |
476:| Watchlist | Intel, Broadcom, Marvell, Supermicro, Lenovo, Quanta, HPE, Inventec |
481:1. Build an architecture-level CPU attach table for Nvidia GB200/GB300, AMD MI300/MI350/MI400, AWS Trainium, Google TPU, and major ASIC racks.
482:2. Pull Mercury/IDC paid data for AMD, Intel, and Arm server CPU unit and revenue share.
483:3. Verify CPU pricing with OEM quotes, distributor checks, and hyperscaler procurement commentary.
484:4. Split AMD Data Center into EPYC vs Instinct using management commentary and channel estimates.
485:5. Track Q1/Q2 2026 capex updates from Microsoft, Amazon, Alphabet, Meta, Oracle, and major neoclouds.
497:I'll write my independent bearish CPU equity memo. The Codex bullish memo is saved at `notes/codex_initial.md`; my role here is the bearish but evidence-disciplined counterpart, so I'll reason from first principles rather than echo or rebut Codex point-by-point.
506:2. **CPU unit demand is up modestly** (Medium) — but the marginal CPU is increasingly a captive ARM design from a hyperscaler, not a merchant Xeon/EPYC.
507:3. **Merchant CPU pricing power is weak** (Medium-High bear conviction) — server-system ASP inflation is a GPU/BOM story; the rumored "CPU price hikes" remain unverified.
509:Net: CPU equities trade as a derivative of the AI capex narrative, but the cash flows the narrative implies accrue mostly to **TSMC, Nvidia, custom-ASIC vendors, and hyperscaler internal silicon programs** — not to Intel, AMD's CPU line, or Arm Holdings on a risk-adjusted basis at current valuations.
511:**Base bearish conclusion:**
512:- **AMD**: Watchlist, not Strong. The "AMD CPU" thesis is largely an Instinct/MI thesis, and Instinct is a distant #2 to Nvidia. EPYC growth is real but unquantified; segment disclosure hides it.
513:- **Intel**: Avoid as a CPU thesis. Foundry losses, structural share loss, and unproven 18A ramp dominate any DCAI green shoot.
514:- **Arm Holdings**: Avoid on valuation, not on technology. Royalty per server CPU is small; multiple is extreme.
515:- **Qualcomm**: Avoid as CPU thesis (agree with bull side here).
518:- **OEM/ODM (SMCI, Wiwynn, Quanta, Inventec, HPE, Lenovo, Dell)**: Treat as cyclical capex pass-throughs. Single-digit gross margins on AI servers do not compound. **Dell** is the highest-quality of the group and the only OEM I'd consider for Watchlist.
524:| **Merchant x86 CPU** | Intel, AMD | Shrinking share of AI rack BOM; captive ARM displaces at the demand frontier |
525:| **Captive ARM CPU (no merchant equity)** | AWS Graviton, Microsoft Cobalt, Google Axion, Nvidia Grace/Vera | Structural TAM-eroder for x86 |
526:| **CPU IP licensor** | Arm Holdings | Captures TAM economics indirectly via royalty; small $/CPU |
527:| **AI accelerators** | Nvidia (GPU), AMD Instinct, custom ASICs (Broadcom, Marvell, Alchip) | Capture the marginal capex dollar; reduce CPU share of BOM |
529:| **OEM** | Dell, HPE, Lenovo, Supermicro | BOM pass-through; margin compresses as AI mix rises |
530:| **ODM** | Quanta, Wiwynn, Inventec, Foxconn (not in scope) | Even lower margin than OEM; concentrated customer risk |
537:| AMD | Advanced Micro Devices | EPYC vs Instinct disclosure opacity; Nvidia GPU dominance caps Instinct upside |
538:| INTC | Intel | Share loss, foundry losses, 18A execution risk, capital structure |
539:| ARM | Arm Holdings | Valuation, royalty rate ceiling, China exposure |
543:| TSM | TSMC | Geopolitical tail, capex intensity, customer concentration in Apple/Nvidia/AMD |
544:| SMCI | Supermicro | 6.3% gross margin, accounting overhang history, customer concentration |
545:| DELL | Dell Technologies | ISG margin compression as AI mix grows; working-capital strain on backlog |
549:| 6669 TT | Wiwynn | Customer concentration; Q4 GM 7.2% |
554:Hyperscaler capex is real (see §6) but the bear question is **what fraction of capex becomes merchant CPU revenue**.
556:**Decomposition assumption (mine, UNSUPPORTED but defensible)**: In a GB200 NVL72 rack costing ~$3M, the CPU silicon (Grace, ARM, captive Nvidia) is <5% of BOM. In an AMD MI300X system, the host CPU (one or two EPYC) may be ~3–6% of BOM. In a TPU/Trainium pod, host CPUs (often custom ARM) are similarly <5%.
558:If 60–70% of incremental hyperscaler compute capex flows into accelerated systems, then **CPU silicon's share of capex declines** even as CPU unit demand rises. This is the structural fact bulls under-weight.
560:**General-purpose refresh** is a separate, healthier driver — but it's a 3–5 year cycle, and merchant CPU vendors face share loss from Graviton/Cobalt at exactly the cloud customers where refresh dollars concentrate.
564:| Hyperscaler capex | Up sharply | High | Mostly GPU/HBM/networking |
566:| General-purpose refresh | Up modestly | Medium | x86 share losing to Graviton/Cobalt |
572:Three market structure observations the bear side should hold:
574:1. **Bifurcation is also a TAM split.** Merchant x86 (Intel + AMD) competes for a shrinking slice of incremental cloud CPU capacity. Independent verification needed (Mercury Research paid data) but Arm's own management commentary that Neoverse is "approaching 50%" of top-hyperscaler deployments is a *bear* signal for x86, not a neutral market data point.
576:2. **AI rack architecture dictates CPU choice, and Nvidia is choosing ARM.** Grace-Hopper, Grace-Blackwell GB200/GB300, and the 2026 Vera platform all use Nvidia's own ARM CPU. Each rack sold is a unit of x86 displacement. The merchant-CPU "AI attach" thesis assumes Nvidia loses platform share or that GB-series volumes underperform — neither is supported by current evidence.
582:I accept the same headline capex numbers the bull side cited (Microsoft $37.5B FY26 Q2; Alphabet $175–185B; Amazon ~$200B; Meta $115–135B 2026; Oracle RPO $553B). I treat these as **High confidence** but **non-diagnostic for CPU vendor revenue**.
584:Bear-relevant overlays not in the bull memo:
585:- **Microsoft FY26 Q2 commentary** that capex skews to "short-lived assets, primarily GPUs and CPUs" is a verbal pairing — quantitative split is not disclosed. The sentence is consistent with a 90/10 GPU/CPU dollar split. (UNSUPPORTED specific ratio; Confidence: Low on the CPU $ share.)
586:- **Hyperscaler internal silicon programs are accelerating, not stable.** AWS publicly stated Graviton is the majority of new EC2 CPU capacity (rough management framing, needs exact citation; Confidence Medium). Microsoft Cobalt 100 GA in 2024; Azure has Cobalt-backed VM SKUs in production. Google Axion launched 2024. Each new generation chips at merchant CPU unit growth at the cloud frontier.
587:- **Capex peak risk.** Aggregate 2026 hyperscaler capex of ~$700B+ is unprecedented. Bear thesis: any 2H26 deceleration whips OEM/ODM and merchant CPU first, before GPU. (My assumption; Confidence Low.)
591:Confirmed (and bear-flag) data:
592:- **Supermicro Q2 FY26: $12.7B revenue, gross margin 6.3%** [Supermicro IR]. This is a brutal mix-driven margin print: revenue scaling does not protect operating income at single-digit gross margins.
593:- **Wiwynn Q4 2025 GM 7.2%, FY25 revenue +163.7%** [Wiwynn IR]. Same pattern.
594:- **Dell ISG margin** trajectory needs scrutiny. $43B backlog at low ISG margin is *less valuable* than $20B at historical margin — backlog $ is a vanity metric without margin disclosure. (Bear caveat; Confidence Medium on margin pressure.)
596:**Bear conclusion**: OEM/ODM are AI capex *barometers*, not investments. The right way to play them is tactical, with stops on ASP-deflation prints. Wiwynn and SMCI have shown how quickly the margin print resets. They are **not** quality compounders.
600:This section is where the bull narrative is weakest.
602:**What is confirmed:** Server-system ASP +92.8% YoY in 2Q25 (Gartner) [Gartner via secondary press]. This is dominated by GPU, HBM, NIC, PSU, and liquid-cooling content — **not CPU silicon**.
604:**What is NOT confirmed:** Tom's Hardware's April 2026 reporting of 10–20% server CPU price hikes. Treat as **rumor / Low confidence**. Channel checks have not been corroborated by Intel or AMD price disclosures or by Mercury Research transaction data.
607:- AMD's apparent revenue-share-above-unit-share at Mercury is **mix shift**, not pricing power. Higher core count Genoa/Bergamo/Turin SKUs at higher price points pull blended ASP up; that is share gain via product, not the same as industry CPU price inflation.
608:- Intel's DCAI revenue recovery (Q1 2026 $5.1B, +22% YoY) is real but plausibly comes from (a) AI host-CPU attach to GPU systems at lower margin, (b) Sierra Forest E-core SKUs that are lower price/socket, and (c) easier comp base. **None of these support sustained merchant CPU pricing power.** [Verification gap.]
611:**Net**: CPU ASP/margin is the weakest link in the bull thesis and the most actionable bear angle.
615:This is real, accelerating, and largely captured by **Arm Holdings as a stock with a problem**: it captures the substitution narratively but **the royalty rate per CPU is small** (typically low single-digit %). ARM's enterprise valuation appears to discount substantial royalty rate expansion, which is contested.
619:| x86 (Intel/AMD) | Loses share at hyperscaler frontier | Negative for INTC, mildly negative for AMD CPU line |
620:| AWS Graviton (custom Neoverse) | 4th gen, majority of new EC2 CPU capacity (mgmt framing) | Negative x86, neutral-to-positive ARM royalties (small $) |
621:| Microsoft Cobalt | GA, Azure SKUs ramping | Negative x86 |
622:| Google Axion | GA 2024 | Negative x86 |
623:| Nvidia Grace/Vera | Standard CPU in GB200/GB300/Vera Rubin | Negative x86 |
627:**Bear thesis on ARM stock**: ARM benefits from substitution, but at a low fixed royalty rate, with rising hyperscaler bargaining power on royalty terms (custom-design license structures). Stock has historically traded at extreme P/E multiples that require both volume *and* royalty rate expansion.
631:### AMD — Watchlist (not Strong)
632:- FY25 Data Center revenue $16.6B, +32% YoY [AMD IR — Confirmed]. **Critical disclosure issue**: this segment includes both EPYC and Instinct. Instinct is a GPU. The "AMD CPU thesis" cannot be cleanly read from this number. Bear estimate (UNSUPPORTED): EPYC growth probably sub-20% with Instinct doing the heavy lifting; needs management disaggregation.
633:- EPYC continues to gain share against Intel (Confirmed directionally; specific numbers require Mercury data).
634:- Bear risk: Instinct competes against Nvidia, where AMD is far behind on software (CUDA moat) and roadmap cadence. Bull case requires both EPYC share gains and Instinct traction — two compounded probabilities.
635:- **Verdict**: AMD is the cleanest CPU equity but is increasingly priced as a GPU equity. Confidence in EPYC tailwind: Medium. Confidence in Instinct closing the Nvidia gap: Low.
637:### Intel — Avoid (CPU thesis only)
638:- Q1 2026 DCAI $5.1B, +22% YoY [Intel IR — Confirmed]. Bear caveat: read against an easy comp; Sierra Forest E-core SKU mix may flatter unit count at lower ASP/socket.
639:- Foundry losses ongoing; 18A ramp is unproven at volume. Even successful 18A doesn't necessarily restore DCAI margin if AMD continues taking share.
640:- Capital structure includes large foundry capex commitments and government funding tied to deliverables.
643:### Arm Holdings — Avoid (valuation)
644:- Q3 FYE26 revenue +26% YoY, royalty +27% YoY [Arm IR — Confirmed]. 1B Neoverse cores cumulative deployment [Arm IR — Confirmed but cumulative ≠ annual].
645:- "Approaching 50% share at top hyperscalers" — **management claim, not independent data** (Medium confidence as directional indicator).
646:- Royalty $/server CPU is low; revenue scaling is paced by hyperscaler design timelines.
647:- Stock multiple has been persistently high. Bear: pricing requires both unit growth AND royalty rate expansion AND no hyperscaler pushback on AALA terms.
652:- **Verdict**: Agree with bull side. Not a CPU equity.
656:- Note: customer concentration in three hyperscaler ASIC programs is a tail risk that does not show up in headlines.
666:- Bear risks: capex intensity, geopolitical (Taiwan), customer concentration, currency.
670:### Supermicro — Avoid as long, possible tactical
675:### Dell — Watchlist (highest-quality OEM)
676:- FY26 AI orders >$64B, shipped >$25B, FY27 backlog $43B [Dell IR — Confirmed].
682:- Less clean AI server growth profile than Dell.
695:### Wiwynn — Avoid as quality holding
696:- FY25 revenue +163.7%, AI products >50% of mix; Q4 GM 7.2% [Wiwynn IR — Confirmed].
698:- **Verdict**: Sharp cyclical print; margin compression evidence is canonical bear data point.
702:- Late to the cycle compared with Quanta/Wiwynn.
707:AI inference shifts to CPU-native runtimes; general-purpose refresh accelerates; AMD compounds EPYC share + Instinct ramp; Intel DCAI re-rates on 18A success; Arm royalty expansion; OEM/ODM margin stabilizes as supply normalizes; capex broadens beyond hyperscalers to enterprise/sovereign.
711:CPU silicon is a small and shrinking share of AI server BOM. Captive ARM displaces merchant x86 at hyperscalers. AMD's CPU growth is masked by Instinct in segment reporting and is sub-20% on a clean basis. Intel's DCAI green shoot fades as Sierra Forest mix and AMD share loss reassert. Arm's stock is right-thesis-wrong-price. OEM/ODM margins remain single-digit and earnings disappoint as capex pull-forward unwinds in 2H26. Hyperscaler capex peaks in 2026 and decelerates in 2027, exposing the cyclical nature of "AI server" earnings. The cleanest beneficiary is TSMC, but its multiple already prices that.
715:CPU unit demand grows mid-single-digits; merchant x86 share declines 200–400 bps to ARM by 2027; CPU $ share of AI server BOM stays in the 3–7% range; OEM/ODM gross margins remain in the 6–10% range and don't recover; AMD outperforms Intel at the equity level but underperforms a "GPU first" portfolio; Arm and TSMC roughly track index-level returns from current levels. Risk-reward across the CPU-equity universe is **mediocre vs the AI accelerator universe**.
721:| C1 | AMD FY25 Data Center segment was $16.6B, +32% YoY (includes EPYC + Instinct) | AMD | Revenue | AMD Q4 2025 release [ir.amd.com] | High | Confirmed fact — but segment commingles CPU + GPU |
722:| C2 | EPYC-only revenue is not separately disclosed by AMD | AMD | Disclosure | AMD 10-K — segment footnotes | High | Confirmed fact |
723:| C3 | Intel Q1 2026 DCAI $5.1B, +22% YoY | Intel | Revenue | Intel Q1 2026 release [intc.com] | High | Confirmed fact |
724:| C4 | Intel DCAI Q1 strength may reflect Sierra Forest E-core mix and easy comp | Intel | Margin | Bear assumption | Low | UNSUPPORTED — analyst inference |
725:| C5 | Microsoft FY26 Q2 capex $37.5B, "primarily GPUs and CPUs" — quantitative split not disclosed | Microsoft | Capex | MSFT FY26 Q2 release | High on figure / Low on CPU $ share | Confirmed fact + management framing |
726:| C6 | Alphabet 2026 capex guide $175–185B | Alphabet | Capex | Alphabet Q4 2025 release | High | Management guidance |
727:| C7 | Amazon expects ~$200B 2026 capex | Amazon | Capex | Amazon Q4 2025 release | High | Management guidance |
728:| C8 | Meta 2026 capex guide $115–135B | Meta | Capex | Meta Q4 2025 release | High | Management guidance |
729:| C9 | Server-system ASP +92.8% YoY in 2Q25 | Industry | Pricing | Gartner via secondary press | Medium | Analyst estimate — system, not CPU |
730:| C10 | Tom's Hardware reports 10–20% server CPU price hikes since March 2026 | INTC/AMD | Pricing | tomshardware.com | Low | Market rumor — UNVERIFIED |
731:| C11 | Arm Q3 FYE26 revenue +26%, royalty +27% YoY | Arm | Revenue | Arm IR | High | Confirmed fact |
732:| C12 | Arm Neoverse "approaching 50%" share at top hyperscalers | Arm | Share | Arm management commentary | Medium | Management claim — not independent data |
733:| C13 | AWS Graviton is the majority of new EC2 CPU capacity | AWS | Share | AWS public framing (re:Invent 2024) | Medium | Management framing — needs primary citation |
734:| C14 | Microsoft Cobalt and Google Axion are GA in production VM SKUs | MSFT/GOOG | Architecture | Azure/GCP product pages | High | Confirmed fact |
735:| C15 | Nvidia GB200/GB300 racks use ARM-based Grace CPU as host | Nvidia | Architecture | Nvidia product spec | High | Confirmed fact — implies x86 displacement |
736:| C16 | Supermicro Q2 FY26 revenue $12.7B, GM 6.3% | SMCI | Margin | Supermicro IR | High | Confirmed fact |
737:| C17 | Wiwynn FY25 revenue +163.7%, Q4 GM 7.2% | Wiwynn | Margin | Wiwynn IR | High | Confirmed fact |
738:| C18 | Dell FY26 AI orders >$64B; FY27 backlog $43B | Dell | Orders | Dell Q4 FY26 release | High | Confirmed fact — margin not disclosed by AI mix |
739:| C19 | Qualcomm has no shipping server CPU revenue line | QCOM | Product | Qualcomm 10-K segment disclosure | High | Confirmed fact |
740:| C20 | Broadcom Q4 FY25 AI semis +74% YoY | Broadcom | Revenue | Broadcom IR | High | Confirmed fact — not a CPU |
741:| C21 | Marvell FY26 revenue +42%, Q4 DC 74% of revenue | Marvell | Revenue | Marvell IR | High | Confirmed fact — not a CPU |
742:| C22 | CPU $ share of AI server BOM is 3–7% range | Industry | BOM | Industry teardowns + analyst estimates | Low-Medium | Analyst estimate — needs primary teardown |
743:| C23 | Aggregate 2026 hyperscaler capex (top 4 + Oracle) >$700B | Industry | Capex | Sum of company guidance | High | Derived from guidance |
744:| C24 | 2026 hyperscaler capex may decelerate in 2H26 | Industry | Capex | Bear assumption | Low | UNSUPPORTED — scenario |
745:| C25 | ARM Holdings royalty per server CPU is low single-digit % of CPU ASP | Arm | Economics | Industry research, ARM filings | Medium | Inference from disclosed royalty pool |
749:Beyond the bull-side gaps, bear-priority verification:
751:1. **EPYC vs Instinct revenue split** at AMD — without this, "AMD CPU growth" cannot be assessed.
752:2. **CPU $ share of GB200/MI300/TPU/Trainium rack BOM** — primary teardown or hyperscaler disclosure needed.
753:3. **Mercury Research paid data** for AMD/Intel/Arm server CPU unit and revenue share by quarter, including blended ASP.
754:4. **Graviton share of AWS EC2 CPU capacity** — quantitative disclosure, not management framing.
755:5. **Cobalt/Axion deployment scale** — VM-instance-week or core-week metrics, not just product launch.
756:6. **Verification of the Tom's Hardware CPU price hike claim** via channel checks, distributor pricing, OEM commentary on FY26 Q2 calls.
757:7. **Dell ISG operating margin trajectory** by AI server mix; same for Lenovo ISG and HPE Server.
758:8. **Wiwynn / SMCI customer concentration** disclosures.
759:9. **Arm Holdings royalty rate per Neoverse compute subsystem (CSS)** vs traditional architectural license.
760:10. **Sierra Forest revenue mix** within Intel DCAI Q1 2026 — to test the "easy comp + low ASP mix" bear hypothesis.
761:11. **Whether OpenAI, xAI, Anthropic, and major neoclouds are buying ARM- or x86-host AI servers** (proxies for non-hyperscaler accelerator-rack CPU mix).
762:12. **Used/refurb server market signals** — early-cycle hyperscaler retirement of x86 fleets would be a leading bear indicator.
768:| **Strong candidate (CPU thesis)** | *(none with conviction)* | The cleanest CPU equity — AMD — is increasingly a GPU equity; thesis is dilute |
769:| **Watchlist** | AMD, TSMC, Dell | Highest-quality names, but priced or impure |
770:| **Avoid** | Intel, Arm Holdings (valuation), Supermicro, Wiwynn, HPE, Inventec, Qualcomm | Each fails the risk-reward bar for distinct reasons |
772:| **Tactical only** | Quanta, Lenovo | Cyclical AI capex trades, not investments |
776:## 17. What Must Be Verified Next (bear priorities)
778:1. **Pull Mercury Research server CPU share data** (paid) — settle x86 vs ARM and AMD vs Intel quantitatively.
779:2. **Quantify EPYC-only revenue** at AMD via management commentary, channel checks, and supply-chain triangulation.
780:3. **Build CPU-$ share of BOM** for GB200, GB300, MI300X, Trainium2, TPU v5/v6, MAIA — primary teardown sources or hyperscaler disclosures.
781:4. **Verify or kill the Tom's Hardware "10–20% CPU price hike" rumor** via OEM, distributor, and Intel/AMD price-list checks.
782:5. **Track Q1 / Q2 2026 capex revision direction** at Microsoft, Amazon, Alphabet, Meta, Oracle, Coreweave, Nebius — direction matters more than level for cyclical risk.
783:6. **Test bear scenario for Intel** in which DCAI growth decelerates as Sierra Forest comps lap and AMD share loss continues.
784:7. **Stress-test ARM Holdings model** for royalty rate compression scenarios as hyperscaler bargaining power rises.
785:8. **Map customer concentration** at SMCI, Wiwynn, Quanta, Inventec — concentration breaks faster than backlog fills.
786:9. **Watch for Nvidia/AMD margin guidance shifts in 2H26** — first sign of capex peak.
791:**Closing note**: I do not dispute most of the bull-side facts. I dispute their investment implication. The same data set — large hyperscaler capex, growing AI server units, share gains in select x86 designs, ARM royalty growth — is consistent with a **mediocre risk-reward in CPU equities at current valuations** when accelerator and foundry equities offer cleaner exposure to the same underlying compute demand. The bear thesis is not "AI is overhyped"; it is "the CPU is the wrong layer of the stack to express AI conviction."

 succeeded in 179ms:
# Source Log

Use this file to track source URLs, filings, earnings calls, market data sources, and unresolved evidence gaps.

| ID | Source | Type | Date | Used For | Reliability |
|---|---|---|---|---|---|

web search: 
web search: AMD reports fourth quarter full year 2025 financial results Data Center revenue 16.6 billion EPYC Instinct
web search: 
web search: Dell Technologies fourth quarter fiscal 2026 AI server orders 64 billion backlog 43 billion
web search: 
web search: Alphabet Q4 2025 2026 capex 175 185 billion official earnings
web search: 
web search: site:abc.xyz/investor "175" "185" "2026 CapEx" Alphabet Q4 2025
web search: 
web search: NVIDIA GB200 NVL72 Grace CPU Arm architecture product specifications 36 Grace CPUs 72 Blackwell GPUs
web search: 
web search: AWS Graviton majority of new EC2 CPU capacity re:Invent 2024 quote
web search: 
web search: Microsoft Cobalt 100 Azure virtual machines generally available official Arm CPU 2024
web search: 
web search: https://www.amd.com/en/newsroom/press-releases/2026-2-3-amd-reports-fourth-quarter-and-full-year-2025-fina.html
web search: 
web search: 'Data Center segment revenue' in https://www.amd.com/en/newsroom/press-releases/2026-2-3-amd-reports-fourth-quarter-and-full-year-2025-fina.html
web search: 
web search: 'FY 2025' in https://www.wiwynn.com/news/wiwynn-reports-fourth-quarter-2025-unaudited-financial-results
web search: 
web search: site:intc.com/news-events/press-releases/detail/1767 Intel Reports First Quarter 2026 Financial Results DCAI 5.1
web search: 
web search: https://www.intc.com/news-events/press-releases/detail/1767/intel-reports-first-quarter-2026-financial-results
web search: 
web search: NVIDIA DGX Rubin NVL8 Intel Xeon 6 host CPU official
web search: 
web search: Broadcom Q4 fiscal 2025 AI semiconductor revenue 74% official
web search: 
web search: finance: ARM
web search: 
web search: finance: ARM
web search: 
web search: finance: AMD
web search: 
web search: https://newsroom.arm.com/news/arm-q3-fye26-results
web search: 
web search: Qualcomm 2025 annual report revenue segments QCT handsets automotive IoT QTL no server CPU
codex
The first pass shows several headline facts are valid, but Claude’s report turns them into broader conclusions without enough bridge evidence. The most important nuance I found so far is that Nvidia’s GB200/GB300 racks support the Arm-displacement point, while Intel also has a disclosed Xeon host-CPU role in NVIDIA DGX Rubin NVL8 systems, so the “Nvidia equals ARM CPU displacement” claim is too broad.
codex
I’m going to update the project registers now: the claim register will mark the challenged claims and severity, and the source log will add the primary sources used for the verification pass.
apply patch
patch: completed
/mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/claims/claim_register.md
/mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/sources/source_log.md
diff --git a//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/claims/claim_register.md b//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/claims/claim_register.md
index e3143944e26ebee642687d770d70a3808f589435..b5b76759dc0441e2e535d024c765470a4d909c68
--- a//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/claims/claim_register.md
+++ b//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/claims/claim_register.md
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

diff --git a//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/claims/claim_register.md b//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/claims/claim_register.md
index e3143944e26ebee642687d770d70a3808f589435..b5b76759dc0441e2e535d024c765470a4d909c68
--- a//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/claims/claim_register.md
+++ b//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/claims/claim_register.md
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

exec
/usr/bin/zsh -lc "sed -n '1,80p' cpu-investment-research-2/claims/claim_register.md" in /mnt/c/Users/hyc97/workspace/Ecclesia/CPU
exec
/usr/bin/zsh -lc "sed -n '1,120p' cpu-investment-research-2/sources/source_log.md" in /mnt/c/Users/hyc97/workspace/Ecclesia/CPU
exec
/usr/bin/zsh -lc 'git diff -- cpu-investment-research-2/claims/claim_register.md cpu-investment-research-2/sources/source_log.md' in /mnt/c/Users/hyc97/workspace/Ecclesia/CPU
 succeeded in 176ms:
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

 succeeded in 175ms:
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

diff --git a//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/claims/claim_register.md b//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/claims/claim_register.md
index e3143944e26ebee642687d770d70a3808f589435..b5b76759dc0441e2e535d024c765470a4d909c68
--- a//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/claims/claim_register.md
+++ b//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/claims/claim_register.md
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

 exited 1 in 194ms:
diff --git a/cpu-investment-research-2/claims/claim_register.md b/cpu-investment-research-2/sources/source_log.md
index b5b7675..61fbc5b 100755
--- a/cpu-investment-research-2/claims/claim_register.md
+++ b/cpu-investment-research-2/sources/source_log.md
@@ -1,20 +1,25 @@
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

codex
The register updates are in place. I’m doing a quick consistency check now because the project files were initially empty, so I want the final response to cite the exact register rows I added rather than implying the earlier table already existed.
exec
/usr/bin/zsh -lc 'git status --short' in /mnt/c/Users/hyc97/workspace/Ecclesia/CPU
exec
/usr/bin/zsh -lc pwd in /mnt/c/Users/hyc97/workspace/Ecclesia/CPU
exec
/usr/bin/zsh -lc 'git diff --stat' in /mnt/c/Users/hyc97/workspace/Ecclesia/CPU
diff --git a//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/claims/claim_register.md b//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/claims/claim_register.md
index e3143944e26ebee642687d770d70a3808f589435..b5b76759dc0441e2e535d024c765470a4d909c68
--- a//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/claims/claim_register.md
+++ b//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/claims/claim_register.md
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

 exited 128 in 182ms:
fatal: not a git repository (or any parent up to mount point /mnt)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).

 exited 129 in 165ms:
warning: Not a git repository. Use --no-index to compare two paths outside a working tree
usage: git diff --no-index [<options>] <path> <path>

Diff output format options
    -p, --patch           generate patch
    -s, --no-patch        suppress diff output
    -u                    generate patch
    -U, --unified[=<n>]   generate diffs with <n> lines context
    -W, --[no-]function-context
                          generate diffs with <n> lines context
    --raw                 generate the diff in raw format
    --patch-with-raw      synonym for '-p --raw'
    --patch-with-stat     synonym for '-p --stat'
    --numstat             machine friendly --stat
    --shortstat           output only the last line of --stat
    -X, --dirstat[=<param1,param2>...]
                          output the distribution of relative amount of changes for each sub-directory
    --cumulative          synonym for --dirstat=cumulative
    --dirstat-by-file[=<param1,param2>...]
                          synonym for --dirstat=files,param1,param2...
    --check               warn if changes introduce conflict markers or whitespace errors
    --summary             condensed summary such as creations, renames and mode changes
    --name-only           show only names of changed files
    --name-status         show only names and status of changed files
    --stat[=<width>[,<name-width>[,<count>]]]
                          generate diffstat
    --stat-width <width>  generate diffstat with a given width
    --stat-name-width <width>
                          generate diffstat with a given name width
    --stat-graph-width <width>
                          generate diffstat with a given graph width
    --stat-count <count>  generate diffstat with limited lines
    --[no-]compact-summary
                          generate compact summary in diffstat
    --binary              output a binary diff that can be applied
    --[no-]full-index     show full pre- and post-image object names on the "index" lines
    --[no-]color[=<when>] show colored diff
    --ws-error-highlight <kind>
                          highlight whitespace errors in the 'context', 'old' or 'new' lines in the diff
    -z                    do not munge pathnames and use NULs as output field terminators in --raw or --numstat
    --[no-]abbrev[=<n>]   use <n> digits to display object names
    --src-prefix <prefix> show the given source prefix instead of "a/"
    --dst-prefix <prefix> show the given destination prefix instead of "b/"
    --line-prefix <prefix>
                          prepend an additional prefix to every line of output
    --no-prefix           do not show any source or destination prefix
    --default-prefix      use default prefixes a/ and b/
    --inter-hunk-context <n>
                          show context between diff hunks up to the specified number of lines
    --output-indicator-new <char>
                          specify the character to indicate a new line instead of '+'
    --output-indicator-old <char>
                          specify the character to indicate an old line instead of '-'
    --output-indicator-context <char>
                          specify the character to indicate a context instead of ' '

Diff rename options
    -B, --break-rewrites[=<n>[/<m>]]
                          break complete rewrite changes into pairs of delete and create
    -M, --find-renames[=<n>]
                          detect renames
    -D, --irreversible-delete
                          omit the preimage for deletes
    -C, --find-copies[=<n>]
                          detect copies
    --[no-]find-copies-harder
                          use unmodified files as source to find copies
    --no-renames          disable rename detection
    --[no-]rename-empty   use empty blobs as rename source
    --[no-]follow         continue listing the history of a file beyond renames
    -l <n>                prevent rename/copy detection if the number of rename/copy targets exceeds given limit

Diff algorithm options
    --minimal             produce the smallest possible diff
    -w, --ignore-all-space
                          ignore whitespace when comparing lines
    -b, --ignore-space-change
                          ignore changes in amount of whitespace
    --ignore-space-at-eol ignore changes in whitespace at EOL
    --ignore-cr-at-eol    ignore carrier-return at the end of line
    --ignore-blank-lines  ignore changes whose lines are all blank
    -I, --[no-]ignore-matching-lines <regex>
                          ignore changes whose all lines match <regex>
    --[no-]indent-heuristic
                          heuristic to shift diff hunk boundaries for easy reading
    --patience            generate diff using the "patience diff" algorithm
    --histogram           generate diff using the "histogram diff" algorithm
    --diff-algorithm <algorithm>
                          choose a diff algorithm
    --anchored <text>     generate diff using the "anchored diff" algorithm
    --word-diff[=<mode>]  show word diff, using <mode> to delimit changed words
    --word-diff-regex <regex>
                          use <regex> to decide what a word is
    --color-words[=<regex>]
                          equivalent to --word-diff=color --word-diff-regex=<regex>
    --[no-]color-moved[=<mode>]
                          moved lines of code are colored differently
    --[no-]color-moved-ws <mode>
                          how white spaces are ignored in --color-moved

Other diff options
    --[no-]relative[=<prefix>]
                          when run from subdir, exclude changes outside and show relative paths
    -a, --[no-]text       treat all files as text
    -R                    swap two inputs, reverse the diff
    --[no-]exit-code      exit with 1 if there were differences, 0 otherwise
    --[no-]quiet          disable all output of the program
    --[no-]ext-diff       allow an external diff helper to be executed
    --[no-]textconv       run external text conversion filters when comparing binary files
    --ignore-submodules[=<when>]
                          ignore changes to submodules in the diff generation
    --submodule[=<format>]
                          specify how differences in submodules are shown
    --ita-invisible-in-index
                          hide 'git add -N' entries from the index
    --ita-visible-in-index
                          treat 'git add -N' entries as real in the index
    -S <string>           look for differences that change the number of occurrences of the specified string
    -G <regex>            look for differences that change the number of occurrences of the specified regex
    --pickaxe-all         show all changes in the changeset with -S or -G
    --pickaxe-regex       treat <string> in -S as extended POSIX regular expression
    -O <file>             control the order in which files appear in the output
    --rotate-to <path>    show the change in the specified path first
    --skip-to <path>      skip the output to the specified path
    --find-object <object-id>
                          look for differences that change the number of occurrences of the specified object
    --diff-filter [(A|C|D|M|R|T|U|X|B)...[*]]
                          select files by diff type
    --output <file>       output to a specific file


 succeeded in 166ms:
/mnt/c/Users/hyc97/workspace/Ecclesia/CPU

codex
Updated:
[claim_register.md](/mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/claims/claim_register.md) and [source_log.md](/mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/sources/source_log.md).

## 1. Highest-Risk Errors

1. **Fatal: CPU-BOM share is asserted, not proven.** The bear thesis depends on CPU silicon being a small and shrinking share of AI rack value, but the 3-7% / <5% BOM claim has no teardown or platform quote. Confidence: Low. Status: UNSUPPORTED.

2. **High: “Nvidia = Arm displacement” is overbroad.** Nvidia GB200/GB300 do use Grace Arm CPUs, confirmed by Nvidia. But Intel says Xeon 6 is used as host CPU in NVIDIA DGX Rubin NVL8 systems, so Nvidia architecture is not uniformly x86-negative. Confidence: Medium. Sources: [Nvidia GB200/GB300](https://www.nvidia.com/en-us/data-center/gb200-nvl72/), [Intel/NVIDIA DGX Rubin NVL8](https://newsroom.intel.com/data-center/intel-xeon-6-used-as-host-cpus-in-nvidia-dgx-rubin-nvl8-systems).

3. **High: AMD CPU conclusion is built on a missing split.** AMD confirms FY2025 Data Center revenue was $16.6B, up 32%, from both EPYC CPUs and Instinct GPUs, but Claude’s “EPYC probably sub-20%” is unsupported. Source: [AMD FY2025 results](https://www.amd.com/en/newsroom/press-releases/2026-2-3-amd-reports-fourth-quarter-and-full-year-2025-fina.html).

## 2. Unsupported Claims

- CPU share of AI server BOM is 3-7%: UNSUPPORTED.
- 60-70% of incremental hyperscaler compute capex flows to accelerated systems: UNSUPPORTED.
- Custom ASIC racks have the lowest CPU intensity: UNSUPPORTED.
- Intel DCAI strength is mostly Sierra Forest / easy comp / lower ASP: UNSUPPORTED. Intel reported DCAI revenue of $5.1B, up 22%, but mix is not disclosed. Source: [Intel Q1 2026](https://www.intc.com/news-events/press-releases/detail/1767/intel-reports-first-quarter-2026-financial-results).
- Arm royalty per server CPU is low single-digit % of CPU ASP: UNSUPPORTED without contract or royalty-dollar model.
- Arm and TSMC are “priced for it”: UNSUPPORTED without valuation tables.

## 3. Questionable Assumptions

- **Share of BOM down does not mean CPU revenue down.** CPU value share can fall while CPU sockets, cores, and dollars rise.
- **Arm adoption is real, but not quantified enough.** AWS says Graviton is more than half of new AWS CPU capacity, and Microsoft/Google have Cobalt/Axion, but this is not the same as global server CPU revenue share. Sources: [AWS Graviton](https://www.aboutamazon.com/news/aws/aws-graviton-5-cpu-amazon-ec2/), [Azure Cobalt](https://azure.microsoft.com/en-us/blog/azure-cobalt-100-based-virtual-machines-are-now-generally-available/), [Google Axion](https://cloud.google.com/products/axion).
- **OEM margin conclusion is too broad.** SMCI and Wiwynn have low gross margins, but Dell’s AI backlog and ISG scale need separate treatment. Sources: [SMCI](https://ir.supermicro.com/news/news-details/2026/Supermicro-Announces-Second-Quarter-Fiscal-Year-2026-Financial-Results/default.aspx), [Wiwynn](https://www.wiwynn.com/news/wiwynn-reports-fourth-quarter-2025-unaudited-financial-results), [Dell](https://investors.delltechnologies.com/news-releases/news-release-details/dell-technologies-delivers-fourth-quarter-and-full-year-fiscal-3).

## 4. Missing Evidence

- Platform BOMs for GB200, GB300, DGX Rubin NVL8, MI300X/MI350, Trainium, TPU, MAIA.
- CPU attach rate by system architecture, not just capex headline.
- AMD EPYC vs Instinct revenue split.
- Intel Xeon mix, ASP, and DCAI margin bridge.
- Arm Neoverse royalty dollars per chip.
- Mercury/IDC/Omdia server CPU unit and revenue share.
- OEM/ODM AI server gross margin by customer and product.
- Current valuation tables for AMD, Intel, Arm, TSMC, Dell, SMCI, Broadcom, Marvell.

## 5. Company-Specific Objections

- **AMD:** Watchlist is reasonable, but the bear case cannot assume EPYC weakness without evidence.
- **Intel:** Avoid is too harsh if Q1 DCAI strength and disclosed Nvidia Rubin NVL8 host-CPU role persist. Still execution-heavy.
- **Arm:** Technology thesis is supported; valuation objection is not yet evidenced.
- **Qualcomm:** Avoid as CPU thesis remains reasonable; its 10-K says it intends to use custom CPU cores for data center products, but no material server CPU revenue is shown. Source: [Qualcomm 10-K](https://www.sec.gov/Archives/edgar/data/0000804328/000080432825000085/qcom-20250928.htm).
- **Broadcom / Marvell:** Not CPU pure plays, but excluding them entirely weakens substitution-risk analysis. Sources: [Broadcom](https://investors.broadcom.com/news-releases/news-release-details/broadcom-inc-announces-fourth-quarter-and-fiscal-year-2025), [Marvell](https://investor.marvell.com/news-events/press-releases/detail/1011/marvell-technology-inc-reports-fourth-quarter-and-fiscal-year-2026-financial-results).
- **Dell / SMCI / Wiwynn:** Treat separately; SMCI/Wiwynn margin pressure is confirmed, Dell quality claim needs peer scorecard.

## 6. Revised Ranking

| Tier | Revised View |
|---|---|
| Strong candidate | None yet |
| Watchlist | AMD, Intel, Arm, TSMC, Dell |
| Tactical / cyclical | SMCI, Quanta, Wiwynn, Lenovo, HPE, Inventec |
| Avoid as CPU thesis | Qualcomm |
| Include as substitution benchmark | Broadcom, Marvell |

Main change: upgrade **Intel from Avoid to Watchlist / tactical CPU beta** pending Q2 confirmation.

## 7. Claim Challenges Table

| Claim ID | Problem | Severity | Suggested Fix | Status |
|---|---|---|---|---|
| CDR-01 | CPU BOM share unsupported | Fatal | Source platform teardown / BOM | Added |
| CDR-02 | 60-70% capex allocation unsupported | High | Build capex-to-architecture model | Added |
| CDR-03 | x86 share-loss claim lacks independent share data | High | Pull Mercury/IDC/Omdia | Added |
| CDR-04 | Nvidia ARM displacement overbroad | High | Split GB200/GB300 vs DGX Rubin NVL8 | Added |
| CDR-05 | Custom ASIC CPU intensity unsupported | High | Map TPU/Trainium/MAIA host CPUs | Added |
| CDR-06 | AMD EPYC sub-20% unsupported | High | Triangulate EPYC/Instinct split | Added |
| CDR-07 | Intel mix explanation unsupported | Medium | Get DCAI product mix / ASP | Added |
| CDR-08 | System ASP not CPU ASP | Medium | Obtain CPU-specific pricing | Added |
| CDR-09 | CPU price hike is market rumor | Medium | Verify with OEM/distributor data | Added |
| CDR-10 | Arm royalty economics unsupported | High | Build royalty-dollar model | Added |
| CDR-11 | Arm valuation claim unsupported | Medium | Add valuation table | Added |
| CDR-12 | TSMC valuation claim unsupported | Medium | Add valuation table | Added |
| CDR-13 | OEM/ODM margin conclusion overgeneralized | Medium | Split by company and margin type | Added |
| CDR-15 | Broadcom/Marvell exclusion too narrow | Medium | Include as substitutes / comps | Added |

## 8. Required Follow-Up Research

Evidence that would change my mind: a sourced platform BOM showing CPUs consistently below 5% of AI rack value, Mercury/IDC data proving merchant x86 revenue share is falling despite AI demand, and AMD/Intel disclosures showing weak CPU ASP or margin.

Near-term work: build the architecture attach table, pull paid server CPU share data, verify CPU pricing, split AMD EPYC vs Instinct, and create valuation scenarios before making a public-equity ranking with conviction.
diff --git a//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/claims/claim_register.md b//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/claims/claim_register.md
index e3143944e26ebee642687d770d70a3808f589435..b5b76759dc0441e2e535d024c765470a4d909c68
--- a//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/claims/claim_register.md
+++ b//mnt/c/Users/hyc97/workspace/Ecclesia/CPU/cpu-investment-research-2/claims/claim_register.md
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