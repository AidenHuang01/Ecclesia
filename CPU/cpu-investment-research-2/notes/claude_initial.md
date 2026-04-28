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