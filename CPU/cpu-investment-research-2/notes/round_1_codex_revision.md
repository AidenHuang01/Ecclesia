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
        6. Updated bull/base/bear view
        7. Updated company ranking
        8. Remaining unresolved disputes
        9. Updated claim register rows

        Do not pretend uncertainty is resolved.

        Your prior report:
        ```markdown
        # Initial Independent CPU Equity Memo

## 1. Executive Thesis

The bullish CPU thesis is investable, but only if framed narrowly: AI does not eliminate CPU demand; it increases demand for orchestration, inference serving, storage, networking, and general-purpose cloud refresh. The strongest evidence is not a generic “AI needs CPUs” narrative, but the combination of hyperscaler capex, OEM AI-server backlog, AMD EPYC share gains, Intel DCAI recovery, and Arm server penetration.

Base conclusion: **own CPU upside through AMD, Arm, and TSMC first; treat OEM/ODM names as execution and margin trades; treat Intel as a turnaround watchlist name; avoid Qualcomm as a server CPU thesis until products/customers are proven.**

## 2. Industry Map

- **CPU vendors:** AMD and Intel dominate merchant x86 server CPUs.
- **Architecture/IP:** Arm benefits from hyperscaler and Nvidia Arm CPU adoption through royalties and licensing.
- **Custom silicon / AI infrastructure:** Broadcom and Marvell benefit from custom AI accelerators, networking, SerDes, and ASIC programs, but are not clean CPU plays.
- **Foundry:** TSMC is the broadest beneficiary across AMD, Arm-based custom silicon, AI ASICs, and networking silicon.
- **OEM/ODM:** Dell, Supermicro, HPE, Lenovo, Quanta, Wiwynn, Inventec convert AI/server demand into revenue, but margins are structurally pressured by pass-through GPU/BOM economics.

## 3. Company Universe

| Group | Companies | CPU Thesis Relevance |
|---|---|---|
| Direct CPU | AMD, Intel | Highest direct exposure |
| Architecture/IP | Arm | High exposure to Arm substitution and hyperscaler custom CPUs |
| Prospective CPU | Qualcomm | Option value only; server CPU not proven |
| Custom/AI silicon | Broadcom, Marvell | Benefits from custom AI infrastructure, may compete with merchant CPU/GPU architectures |
| Foundry | TSMC | Broadest picks-and-shovels exposure |
| OEM/ODM | Dell, SMCI, HPE, Lenovo, Quanta, Wiwynn, Inventec | Demand signal; lower-quality margin capture |

## 4. Demand Drivers

Confirmed demand signals are strong. Dell closed **more than $64B of FY26 AI-optimized server orders**, shipped **more than $25B**, and entered FY27 with **$43B backlog**. Microsoft reported FY26 Q2 capex of **$37.5B**, with roughly two-thirds on short-lived assets, “primarily GPUs and CPUs,” and said demand exceeds supply. Alphabet guided 2026 capex to **$175B-$185B**. Amazon said it expects about **$200B** of 2026 capex.

Analyst estimates are also supportive: TrendForce forecasts 2026 total server shipments +12.8% YoY and AI server shipments +28%+ YoY. This is still an estimate, not fact.

## 5. Server CPU Market Structure

The market is bifurcating:

- **Merchant x86:** AMD gaining share and richer mix; Intel still large and showing recent DCAI recovery.
- **Captive/custom Arm:** AWS Graviton, Microsoft Cobalt, Nvidia Grace/Vera, and other hyperscaler CPUs pressure x86 over time.
- **AI rack systems:** GPU/ASIC platform choice increasingly dictates CPU attach, cooling, networking, and server architecture.

Important caveat: IDC “non-x86 server” growth is not the same as Arm CPU share. Accelerated systems, proprietary architectures, and high-value AI racks can distort revenue share.

## 6. Hyperscaler And Data Center Order Signals

Confirmed:
- Microsoft FY26 Q2 capex: **$37.5B**, roughly two-thirds short-lived assets, primarily GPUs and CPUs.
- Alphabet 2026 capex guide: **$175B-$185B**.
- Amazon 2026 capex expectation: about **$200B**.
- Meta 2026 capex guide: **$115B-$135B**.
- Oracle Q3 FY26 RPO: **$553B**, up 325% YoY, with large-scale AI contracts.

Interpretation: these numbers support server demand, but not a precise CPU ASP or CPU-unit forecast. Confidence in broad infrastructure demand is High; confidence in CPU-specific revenue conversion is Medium.

## 7. OEM/ODM Server Configuration And Shipment Implications

Dell and Supermicro show extreme AI-server revenue conversion, but margin quality differs. Supermicro Q2 FY26 net sales reached **$12.7B**, but gross margin fell to **6.3%**, showing how AI server growth can be BOM-heavy and margin-thin. Wiwynn’s FY25 revenue rose **163.7% YoY**, with AI-related products over half of revenue, but Q4 gross margin fell to **7.2%** due to product mix.

Conclusion: OEM/ODM revenue is a good demand signal, not automatically a high-quality equity signal.

## 8. CPU Pricing / ASP / Margin Discussion

Confirmed data supports **server-system ASP inflation**, not clean CPU ASP inflation. Gartner estimated 2Q25 server vendor revenue +89.9% YoY while shipments declined 1.5%, driven by a 92.8% ASP increase from AI-optimized server demand. Mercury data reported by Tom’s Hardware shows AMD x86 server revenue share above unit share, consistent with richer mix.

Market rumor: Tom’s Hardware reported in April 2026 that server CPU prices rose 10%-20% since March 2026 due to AI/inference demand. Treat as **rumor / Low confidence** until checked against OEM quotes, distributor pricing, and Intel/AMD disclosures.

## 9. x86 Vs Arm Substitution Risk

Arm risk is real and investable. Arm reported Q3 FYE26 revenue +26% YoY and royalty revenue +27% YoY; management also said Neoverse CPUs surpassed 1B deployed cores and expects Arm share among top hyperscalers to reach nearly 50%. That is management guidance/claim, not independent market share.

For AMD/Intel, Arm is both a threat and a market validator: total server CPU demand can grow while x86 share declines.

## 10. Company-By-Company Analysis

- **AMD:** Best direct CPU candidate. FY25 Data Center revenue was **$16.6B, +32% YoY**, driven by EPYC CPUs and Instinct GPUs. Key risk: AMD does not disclose EPYC-only revenue, so CPU-specific growth must be inferred.
- **Intel:** Watchlist turnaround. Q1 2026 DCAI revenue was **$5.1B, +22% YoY**. Bullish CPU signal, but AMD share loss and foundry execution remain unresolved.
- **Arm:** Strong structural candidate. Benefits from hyperscaler custom CPUs and Nvidia Arm CPU platforms. Risk is valuation and indirect royalty capture.
- **Qualcomm:** Avoid for CPU thesis. Data center CPUs are “in development”; AI200/AI250 and Alphawave add optionality, but server CPU revenue/customer proof is absent.
- **Broadcom:** Strong AI infrastructure name, not a clean CPU play. FY25 Q4 AI semiconductor revenue +74% YoY; custom accelerators and Ethernet are the story.
- **Marvell:** Watchlist. FY26 revenue +42% YoY; data center was 74% of Q4 revenue. Strong AI custom silicon exposure, weak CPU purity.
- **TSMC:** Strong candidate. Broad beneficiary of advanced compute regardless of x86 vs Arm vs ASIC winner.
- **Supermicro:** Watchlist. Exceptional revenue growth, but margin compression and customer concentration risk are central.
- **Dell:** Stronger OEM candidate. AI orders/backlog are unusually explicit; watch ISG margin and working capital.
- **HPE:** Watchlist. Server revenue was down in Q1 FY26, while networking improved; not the cleanest CPU demand vehicle.
- **Lenovo:** Watchlist. AI revenue mix is rising, but server-specific disclosure is insufficient.
- **Quanta:** Watchlist/Strong ODM beta. 2025 monthly sales total rose 50.5% YoY; AI server attribution needs verification.
- **Wiwynn:** Strong ODM beta. AI products over half of FY25 revenue; margin pressure must be monitored.
- **Inventec:** Watchlist. FY25 revenue grew only 6.95%; recent AI server momentum needs more evidence.

## 11. Bull Case

AI inference and agentic workloads lift CPU attach, general-purpose server refresh, and x86/Arm server CPU demand simultaneously. AMD keeps gaining profitable EPYC share, Intel supply tightens DCAI pricing, Arm royalties compound from hyperscaler CPUs, and TSMC captures advanced-node volume across all winners.

## 12. Bear Case

AI rack architectures integrate more Arm/custom CPUs, reducing merchant x86 attach. CPU ASP rumors fade, AI capex pauses, OEM/ODM backlogs prove low-margin, and server CPU value is captured by hyperscalers, Nvidia, custom ASIC vendors, and TSMC rather than Intel/AMD.

## 13. Base Case

Server CPU demand grows, but less explosively than GPU/ASIC demand. AMD and Arm are the cleanest equity expressions; Intel improves but remains execution-heavy; OEM/ODM revenue grows faster than profit; TSMC remains the best diversified beneficiary.

## 14. Key Claims Table

| ID | Claim | Company | Category | Source | Confidence | Status |
|---|---|---|---|---|---|---|
| K1 | Worldwide server spending grew 52.4% YoY in Q4 2025; units +10.3%. | Industry | Server demand | [IDC](https://www.idc.com/promo/servers/) | High | Analyst estimate |
| K2 | 2026 server shipments forecast +12.8%; AI server shipments +28%+. | Industry | Demand | [TrendForce](https://www.trendforce.com/presscenter/news/20260120-12887.html) | Medium | Analyst estimate |
| K3 | Inference workloads are boosting general-purpose server demand. | Industry | Demand | [TrendForce](https://www.trendforce.com/presscenter/news/20260120-12887.html) | Medium | Analyst estimate |
| K4 | AMD FY25 Data Center revenue was $16.6B, +32% YoY. | AMD | Revenue | [AMD](https://ir.amd.com/news-events/press-releases/detail/1276/amd-reports-fourth-quarter-and-full-year-2025-financial-results) | High | Confirmed fact |
| K5 | Intel Q1 2026 DCAI revenue was $5.1B, +22% YoY. | Intel | Revenue | [Intel](https://www.intc.com/news-events/press-releases/detail/1767/intel-reports-first-quarter-2026-financial-results) | High | Confirmed fact |
| K6 | Microsoft FY26 Q2 capex was $37.5B; roughly two-thirds was GPUs/CPUs. | Microsoft | Capex | [Microsoft](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q2) | High | Confirmed fact |
| K7 | Dell FY26 AI server orders exceeded $64B; backlog $43B. | Dell | Orders | [Dell](https://investors.delltechnologies.com/news-releases/news-release-details/dell-technologies-delivers-fourth-quarter-and-full-year-fiscal-3) | High | Confirmed fact |
| K8 | Supermicro Q2 FY26 sales were $12.7B; gross margin 6.3%. | SMCI | OEM margin | [Supermicro](https://ir.supermicro.com/news/news-details/2026/Supermicro-Announces-Second-Quarter-Fiscal-Year-2026-Financial-Results/default.aspx) | High | Confirmed fact |
| K9 | Wiwynn FY25 revenue +163.7%; AI products over 50% of revenue. | Wiwynn | ODM demand | [Wiwynn](https://www.wiwynn.com/news/wiwynn-reports-fourth-quarter-2025-financial-results) | High | Confirmed fact |
| K10 | Arm Q3 FYE26 revenue +26%; royalty revenue +27%. | Arm | Revenue | [Arm](https://newsroom.arm.com/news/arm-q3-fye26-results) | High | Confirmed fact |
| K11 | Arm says Neoverse surpassed 1B deployed cores and may approach 50% share at top hyperscalers. | Arm | ARM adoption | [Arm](https://newsroom.arm.com/news/arm-q3-fye26-results) | Medium | Management claim |
| K12 | Broadcom Q4 FY25 AI semiconductor revenue +74% YoY. | Broadcom | AI silicon | [Broadcom](https://investors.broadcom.com/news-releases/news-release-details/broadcom-inc-announces-fourth-quarter-and-fiscal-year-2025) | High | Confirmed fact |
| K13 | Marvell FY26 revenue was $8.195B, +42% YoY; Q4 data center was 74% of revenue. | Marvell | AI silicon | [Marvell](https://investor.marvell.com/news-events/press-releases/detail/1011/marvell-technology-inc-reports-fourth-quarter-and-fiscal-year-2026-financial-results) | High | Confirmed fact |
| K14 | Meta guides 2026 capex to $115B-$135B. | Meta | Capex | [Meta](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Fourth-Quarter-and-Full-Year-2025-Results/) | High | Management guidance |
| K15 | Alphabet guides 2026 capex to $175B-$185B. | Alphabet | Capex | [Alphabet](https://abc.xyz/investor/events/event-details/2026/2025-Q4-Earnings-Call-2026-Dr_C033hS6/default.aspx) | High | Management guidance |
| K16 | Amazon expects about $200B capex in 2026. | Amazon | Capex | [Amazon](https://www.aboutamazon.com/news/company-news/amazon-earnings-q4-2025-report) | High | Management guidance |
| K17 | Qualcomm says server CPUs are in development. | Qualcomm | Product status | [Qualcomm](https://www.qualcomm.com/artificial-intelligence/data-center) | High | Confirmed fact |
| K18 | Server CPU prices reportedly rose 10%-20% since March 2026. | Intel/AMD | Pricing | [Tom’s Hardware](https://www.tomshardware.com/pc-components/cpus/shifting-need-for-cpus-in-ai-workloads-drives-intensifying-shortages-price-hikes) | Low | Market rumor |

## 15. Evidence Gaps

- EPYC-only revenue and Intel Xeon-only revenue.
- Server CPU ASP by SKU and customer class.
- CPU attach rate by architecture: HGX, GB200/GB300, MI300/MI350, Trainium, TPU, custom ASIC.
- OEM/ODM gross margin by AI server type.
- Arm royalty dollars per Neoverse server CPU.
- Hyperscaler order split across Dell, SMCI, Quanta, Wiwynn, Inventec, Foxconn, and internal builds.
- Whether reported CPU price increases are real transactions or channel noise.

## 16. Initial Ranking

| Ranking | Companies |
|---|---|
| Strong candidate | AMD, Arm, TSMC, Dell, Wiwynn |
| Watchlist | Intel, Broadcom, Marvell, Supermicro, Lenovo, Quanta, HPE, Inventec |
| Avoid for CPU thesis | Qualcomm |

## 17. What Must Be Verified Next

1. Build an architecture-level CPU attach table for Nvidia GB200/GB300, AMD MI300/MI350/MI400, AWS Trainium, Google TPU, and major ASIC racks.
2. Pull Mercury/IDC paid data for AMD, Intel, and Arm server CPU unit and revenue share.
3. Verify CPU pricing with OEM quotes, distributor checks, and hyperscaler procurement commentary.
4. Split AMD Data Center into EPYC vs Instinct using management commentary and channel estimates.
5. Track Q1/Q2 2026 capex updates from Microsoft, Amazon, Alphabet, Meta, Oracle, and major neoclouds.

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

 succeeded in 175ms:
# Claim Register

| ID | Claim | Company | Category | Source | Confidence | Challenged By | Status |
|---|---|---|---|---|---|---|---|

 succeeded in 181ms:
# Source Log

Use this file to track source URLs, filings, earnings calls, market data sources, and unresolved evidence gaps.

| ID | Source | Type | Date | Used For | Reliability |
|---|---|---|---|---|---|

codex
The local project is essentially a blank scaffold: the transcript has only two lines, and the claim/source tables have headers only. I’m treating this as a fresh independent memo rather than a response to prior claims.
exec
/usr/bin/zsh -lc "sed -n '1,200p' cpu-investment-research-2/state.json" in /mnt/c/Users/hyc97/workspace/Ecclesia/CPU
exec
/usr/bin/zsh -lc "sed -n '1,120p' cpu-investment-research-2/transcript/full_debate.md" in /mnt/c/Users/hyc97/workspace/Ecclesia/CPU
 succeeded in 159ms:
# CPU Investment Research Debate Transcript


 succeeded in 167ms:
{
  "started_at": "2026-04-25T22:34:33",
  "rounds": 2,
  "codex_command": [
    "codex",
    "exec",
    "--skip-git-repo-check"
  ],
  "claude_command": [
    "claude",
    "-p"
  ]
}
web search: 
web search: 2025 AMD annual report data center revenue EPYC server CPU 2025 10-K
web search: 
web search: site:ir.amd.com 2026 Q4 2025 AMD data center revenue EPYC annual results 2025
web search: 
web search: site:hpe.com investor relations FY 2025 AI server orders backlog 2025 results HPE
web search: 
web search: site:investor.qualcomm.com 2025 annual report data center CPU Qualcomm Oryon fiscal 2025
web search: 
web search: site:investor.qualcomm.com fiscal 2025 results data center CPU Qualcomm Oryon AI data center
web search: 
web search: Qualcomm reports fourth quarter fiscal 2025 results November 5 2025 QCT revenue automotive IoT handset
web search: 
web search: IDC worldwide server market 2025 revenue shipments AI servers 2025
web search: 
web search: Mercury Research server CPU market share AMD Intel Arm 2025 Q4 server CPU share
web search: 
web search: Alphabet 2025 capital expenditures AI infrastructure full year 2025 earnings release
web search: 
web search: Amazon Q4 2025 earnings capital expenditures AI infrastructure 2026 AWS capex official
web search: 
web search: site:abc.xyz investor 2025 Q4 results capital expenditures 2026 AI infrastructure Alphabet capex 2025
web search: 
web search: Meta investor relations Q4 2025 results capital expenditures 2026 115 135 billion official
web search: 
web search: Quanta Computer 2025 annual revenue AI server 2026 outlook official investor relations
web search: 
web search: Quanta Computer 2025 Q4 financial results AI server revenue official
web search: 
web search: Inventec monthly revenue 2025 server AI server official investor relations
web search: 
web search: Supermicro fiscal 2026 Q2 results AI server revenue liquid cooling backlog official
web search: 
web search: Arm Holdings fiscal 2025 annual report Neoverse data center royalty revenue server official
web search: 
web search: Intel reports first quarter 2026 financial results Data Center AI revenue Xeon official April 2026
codex
# Initial Independent CPU Equity Memo

## 1. Executive Thesis

The bullish CPU thesis is investable, but only if framed narrowly: AI does not eliminate CPU demand; it increases demand for orchestration, inference serving, storage, networking, and general-purpose cloud refresh. The strongest evidence is not a generic “AI needs CPUs” narrative, but the combination of hyperscaler capex, OEM AI-server backlog, AMD EPYC share gains, Intel DCAI recovery, and Arm server penetration.

Base conclusion: **own CPU upside through AMD, Arm, and TSMC first; treat OEM/ODM names as execution and margin trades; treat Intel as a turnaround watchlist name; avoid Qualcomm as a server CPU thesis until products/customers are proven.**

## 2. Industry Map

- **CPU vendors:** AMD and Intel dominate merchant x86 server CPUs.
- **Architecture/IP:** Arm benefits from hyperscaler and Nvidia Arm CPU adoption through royalties and licensing.
- **Custom silicon / AI infrastructure:** Broadcom and Marvell benefit from custom AI accelerators, networking, SerDes, and ASIC programs, but are not clean CPU plays.
- **Foundry:** TSMC is the broadest beneficiary across AMD, Arm-based custom silicon, AI ASICs, and networking silicon.
- **OEM/ODM:** Dell, Supermicro, HPE, Lenovo, Quanta, Wiwynn, Inventec convert AI/server demand into revenue, but margins are structurally pressured by pass-through GPU/BOM economics.

## 3. Company Universe

| Group | Companies | CPU Thesis Relevance |
|---|---|---|
| Direct CPU | AMD, Intel | Highest direct exposure |
| Architecture/IP | Arm | High exposure to Arm substitution and hyperscaler custom CPUs |
| Prospective CPU | Qualcomm | Option value only; server CPU not proven |
| Custom/AI silicon | Broadcom, Marvell | Benefits from custom AI infrastructure, may compete with merchant CPU/GPU architectures |
| Foundry | TSMC | Broadest picks-and-shovels exposure |
| OEM/ODM | Dell, SMCI, HPE, Lenovo, Quanta, Wiwynn, Inventec | Demand signal; lower-quality margin capture |

## 4. Demand Drivers

Confirmed demand signals are strong. Dell closed **more than $64B of FY26 AI-optimized server orders**, shipped **more than $25B**, and entered FY27 with **$43B backlog**. Microsoft reported FY26 Q2 capex of **$37.5B**, with roughly two-thirds on short-lived assets, “primarily GPUs and CPUs,” and said demand exceeds supply. Alphabet guided 2026 capex to **$175B-$185B**. Amazon said it expects about **$200B** of 2026 capex.

Analyst estimates are also supportive: TrendForce forecasts 2026 total server shipments +12.8% YoY and AI server shipments +28%+ YoY. This is still an estimate, not fact.

## 5. Server CPU Market Structure

The market is bifurcating:

- **Merchant x86:** AMD gaining share and richer mix; Intel still large and showing recent DCAI recovery.
- **Captive/custom Arm:** AWS Graviton, Microsoft Cobalt, Nvidia Grace/Vera, and other hyperscaler CPUs pressure x86 over time.
- **AI rack systems:** GPU/ASIC platform choice increasingly dictates CPU attach, cooling, networking, and server architecture.

Important caveat: IDC “non-x86 server” growth is not the same as Arm CPU share. Accelerated systems, proprietary architectures, and high-value AI racks can distort revenue share.

## 6. Hyperscaler And Data Center Order Signals

Confirmed:
- Microsoft FY26 Q2 capex: **$37.5B**, roughly two-thirds short-lived assets, primarily GPUs and CPUs.
- Alphabet 2026 capex guide: **$175B-$185B**.
- Amazon 2026 capex expectation: about **$200B**.
- Meta 2026 capex guide: **$115B-$135B**.
- Oracle Q3 FY26 RPO: **$553B**, up 325% YoY, with large-scale AI contracts.

Interpretation: these numbers support server demand, but not a precise CPU ASP or CPU-unit forecast. Confidence in broad infrastructure demand is High; confidence in CPU-specific revenue conversion is Medium.

## 7. OEM/ODM Server Configuration And Shipment Implications

Dell and Supermicro show extreme AI-server revenue conversion, but margin quality differs. Supermicro Q2 FY26 net sales reached **$12.7B**, but gross margin fell to **6.3%**, showing how AI server growth can be BOM-heavy and margin-thin. Wiwynn’s FY25 revenue rose **163.7% YoY**, with AI-related products over half of revenue, but Q4 gross margin fell to **7.2%** due to product mix.

Conclusion: OEM/ODM revenue is a good demand signal, not automatically a high-quality equity signal.

## 8. CPU Pricing / ASP / Margin Discussion

Confirmed data supports **server-system ASP inflation**, not clean CPU ASP inflation. Gartner estimated 2Q25 server vendor revenue +89.9% YoY while shipments declined 1.5%, driven by a 92.8% ASP increase from AI-optimized server demand. Mercury data reported by Tom’s Hardware shows AMD x86 server revenue share above unit share, consistent with richer mix.

Market rumor: Tom’s Hardware reported in April 2026 that server CPU prices rose 10%-20% since March 2026 due to AI/inference demand. Treat as **rumor / Low confidence** until checked against OEM quotes, distributor pricing, and Intel/AMD disclosures.

## 9. x86 Vs Arm Substitution Risk

Arm risk is real and investable. Arm reported Q3 FYE26 revenue +26% YoY and royalty revenue +27% YoY; management also said Neoverse CPUs surpassed 1B deployed cores and expects Arm share among top hyperscalers to reach nearly 50%. That is management guidance/claim, not independent market share.

For AMD/Intel, Arm is both a threat and a market validator: total server CPU demand can grow while x86 share declines.

## 10. Company-By-Company Analysis

- **AMD:** Best direct CPU candidate. FY25 Data Center revenue was **$16.6B, +32% YoY**, driven by EPYC CPUs and Instinct GPUs. Key risk: AMD does not disclose EPYC-only revenue, so CPU-specific growth must be inferred.
- **Intel:** Watchlist turnaround. Q1 2026 DCAI revenue was **$5.1B, +22% YoY**. Bullish CPU signal, but AMD share loss and foundry execution remain unresolved.
- **Arm:** Strong structural candidate. Benefits from hyperscaler custom CPUs and Nvidia Arm CPU platforms. Risk is valuation and indirect royalty capture.
- **Qualcomm:** Avoid for CPU thesis. Data center CPUs are “in development”; AI200/AI250 and Alphawave add optionality, but server CPU revenue/customer proof is absent.
- **Broadcom:** Strong AI infrastructure name, not a clean CPU play. FY25 Q4 AI semiconductor revenue +74% YoY; custom accelerators and Ethernet are the story.
- **Marvell:** Watchlist. FY26 revenue +42% YoY; data center was 74% of Q4 revenue. Strong AI custom silicon exposure, weak CPU purity.
- **TSMC:** Strong candidate. Broad beneficiary of advanced compute regardless of x86 vs Arm vs ASIC winner.
- **Supermicro:** Watchlist. Exceptional revenue growth, but margin compression and customer concentration risk are central.
- **Dell:** Stronger OEM candidate. AI orders/backlog are unusually explicit; watch ISG margin and working capital.
- **HPE:** Watchlist. Server revenue was down in Q1 FY26, while networking improved; not the cleanest CPU demand vehicle.
- **Lenovo:** Watchlist. AI revenue mix is rising, but server-specific disclosure is insufficient.
- **Quanta:** Watchlist/Strong ODM beta. 2025 monthly sales total rose 50.5% YoY; AI server attribution needs verification.
- **Wiwynn:** Strong ODM beta. AI products over half of FY25 revenue; margin pressure must be monitored.
- **Inventec:** Watchlist. FY25 revenue grew only 6.95%; recent AI server momentum needs more evidence.

## 11. Bull Case

AI inference and agentic workloads lift CPU attach, general-purpose server refresh, and x86/Arm server CPU demand simultaneously. AMD keeps gaining profitable EPYC share, Intel supply tightens DCAI pricing, Arm royalties compound from hyperscaler CPUs, and TSMC captures advanced-node volume across all winners.

## 12. Bear Case

AI rack architectures integrate more Arm/custom CPUs, reducing merchant x86 attach. CPU ASP rumors fade, AI capex pauses, OEM/ODM backlogs prove low-margin, and server CPU value is captured by hyperscalers, Nvidia, custom ASIC vendors, and TSMC rather than Intel/AMD.

## 13. Base Case

Server CPU demand grows, but less explosively than GPU/ASIC demand. AMD and Arm are the cleanest equity expressions; Intel improves but remains execution-heavy; OEM/ODM revenue grows faster than profit; TSMC remains the best diversified beneficiary.

## 14. Key Claims Table

| ID | Claim | Company | Category | Source | Confidence | Status |
|---|---|---|---|---|---|---|
| K1 | Worldwide server spending grew 52.4% YoY in Q4 2025; units +10.3%. | Industry | Server demand | [IDC](https://www.idc.com/promo/servers/) | High | Analyst estimate |
| K2 | 2026 server shipments forecast +12.8%; AI server shipments +28%+. | Industry | Demand | [TrendForce](https://www.trendforce.com/presscenter/news/20260120-12887.html) | Medium | Analyst estimate |
| K3 | Inference workloads are boosting general-purpose server demand. | Industry | Demand | [TrendForce](https://www.trendforce.com/presscenter/news/20260120-12887.html) | Medium | Analyst estimate |
| K4 | AMD FY25 Data Center revenue was $16.6B, +32% YoY. | AMD | Revenue | [AMD](https://ir.amd.com/news-events/press-releases/detail/1276/amd-reports-fourth-quarter-and-full-year-2025-financial-results) | High | Confirmed fact |
| K5 | Intel Q1 2026 DCAI revenue was $5.1B, +22% YoY. | Intel | Revenue | [Intel](https://www.intc.com/news-events/press-releases/detail/1767/intel-reports-first-quarter-2026-financial-results) | High | Confirmed fact |
| K6 | Microsoft FY26 Q2 capex was $37.5B; roughly two-thirds was GPUs/CPUs. | Microsoft | Capex | [Microsoft](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q2) | High | Confirmed fact |
| K7 | Dell FY26 AI server orders exceeded $64B; backlog $43B. | Dell | Orders | [Dell](https://investors.delltechnologies.com/news-releases/news-release-details/dell-technologies-delivers-fourth-quarter-and-full-year-fiscal-3) | High | Confirmed fact |
| K8 | Supermicro Q2 FY26 sales were $12.7B; gross margin 6.3%. | SMCI | OEM margin | [Supermicro](https://ir.supermicro.com/news/news-details/2026/Supermicro-Announces-Second-Quarter-Fiscal-Year-2026-Financial-Results/default.aspx) | High | Confirmed fact |
| K9 | Wiwynn FY25 revenue +163.7%; AI products over 50% of revenue. | Wiwynn | ODM demand | [Wiwynn](https://www.wiwynn.com/news/wiwynn-reports-fourth-quarter-2025-financial-results) | High | Confirmed fact |
| K10 | Arm Q3 FYE26 revenue +26%; royalty revenue +27%. | Arm | Revenue | [Arm](https://newsroom.arm.com/news/arm-q3-fye26-results) | High | Confirmed fact |
| K11 | Arm says Neoverse surpassed 1B deployed cores and may approach 50% share at top hyperscalers. | Arm | ARM adoption | [Arm](https://newsroom.arm.com/news/arm-q3-fye26-results) | Medium | Management claim |
| K12 | Broadcom Q4 FY25 AI semiconductor revenue +74% YoY. | Broadcom | AI silicon | [Broadcom](https://investors.broadcom.com/news-releases/news-release-details/broadcom-inc-announces-fourth-quarter-and-fiscal-year-2025) | High | Confirmed fact |
| K13 | Marvell FY26 revenue was $8.195B, +42% YoY; Q4 data center was 74% of revenue. | Marvell | AI silicon | [Marvell](https://investor.marvell.com/news-events/press-releases/detail/1011/marvell-technology-inc-reports-fourth-quarter-and-fiscal-year-2026-financial-results) | High | Confirmed fact |
| K14 | Meta guides 2026 capex to $115B-$135B. | Meta | Capex | [Meta](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Fourth-Quarter-and-Full-Year-2025-Results/) | High | Management guidance |
| K15 | Alphabet guides 2026 capex to $175B-$185B. | Alphabet | Capex | [Alphabet](https://abc.xyz/investor/events/event-details/2026/2025-Q4-Earnings-Call-2026-Dr_C033hS6/default.aspx) | High | Management guidance |
| K16 | Amazon expects about $200B capex in 2026. | Amazon | Capex | [Amazon](https://www.aboutamazon.com/news/company-news/amazon-earnings-q4-2025-report) | High | Management guidance |
| K17 | Qualcomm says server CPUs are in development. | Qualcomm | Product status | [Qualcomm](https://www.qualcomm.com/artificial-intelligence/data-center) | High | Confirmed fact |
| K18 | Server CPU prices reportedly rose 10%-20% since March 2026. | Intel/AMD | Pricing | [Tom’s Hardware](https://www.tomshardware.com/pc-components/cpus/shifting-need-for-cpus-in-ai-workloads-drives-intensifying-shortages-price-hikes) | Low | Market rumor |

## 15. Evidence Gaps

- EPYC-only revenue and Intel Xeon-only revenue.
- Server CPU ASP by SKU and customer class.
- CPU attach rate by architecture: HGX, GB200/GB300, MI300/MI350, Trainium, TPU, custom ASIC.
- OEM/ODM gross margin by AI server type.
- Arm royalty dollars per Neoverse server CPU.
- Hyperscaler order split across Dell, SMCI, Quanta, Wiwynn, Inventec, Foxconn, and internal builds.
- Whether reported CPU price increases are real transactions or channel noise.

## 16. Initial Ranking

| Ranking | Companies |
|---|---|
| Strong candidate | AMD, Arm, TSMC, Dell, Wiwynn |
| Watchlist | Intel, Broadcom, Marvell, Supermicro, Lenovo, Quanta, HPE, Inventec |
| Avoid for CPU thesis | Qualcomm |

## 17. What Must Be Verified Next

1. Build an architecture-level CPU attach table for Nvidia GB200/GB300, AMD MI300/MI350/MI400, AWS Trainium, Google TPU, and major ASIC racks.
2. Pull Mercury/IDC paid data for AMD, Intel, and Arm server CPU unit and revenue share.
3. Verify CPU pricing with OEM quotes, distributor checks, and hyperscaler procurement commentary.
4. Split AMD Data Center into EPYC vs Instinct using management commentary and channel estimates.
5. Track Q1/Q2 2026 capex updates from Microsoft, Amazon, Alphabet, Meta, Oracle, and major neoclouds.
2026-04-26T05:39:39.072993Z ERROR codex_core::session: failed to record rollout items: thread 019dc848-47d1-72e1-a202-8ff372f21a0b not found
tokens used
123,221
        ```

        Critique received:
        ```markdown
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
        ```

codex
I’ll verify the challenged, time-sensitive claims before revising the thesis, especially the capex and Dell order figures. The local files were called out as project artifacts, but the requested deliverable is a structured response, so I’m focusing on a clean revision memo unless file edits become necessary.
web search: 
web search: site:microsoft.com/en-us/investor/events FY 2026 Q2 earnings capital expenditures GPUs CPUs short-lived assets Microsoft 37.5 billion
web search: 
web search: Dell Technologies Delivers Fourth Quarter and Full Year Fiscal 2026 results AI optimized server orders 64 billion backlog 43 billion
web search: 
web search: Alphabet Q4 2025 earnings call 2026 capital expenditures 175 185 billion Ruth Porat
web search: 
web search: Meta Reports Fourth Quarter and Full Year 2025 Results 2026 capital expenditures 115 135 billion official
web search: 
web search: Amazon Q4 2025 earnings call 2026 capital expenditures 200 billion official transcript Andy Jassy Brian Olsavsky
web search: 
web search: Gartner 2Q25 server revenue shipments ASP AI optimized server 89.9 1.5 92.8 press release
codex
The key challenged facts are partly real: Microsoft, Dell, Alphabet, Meta, and Amazon have official 2026-era disclosures matching the headline capex/order figures. The critique still lands on interpretation: those are infrastructure or AI-server dollars, not CPU revenue dollars.
exec
/usr/bin/zsh -lc "sed -n '1,220p' cpu-investment-research-2/claims/claim_register.md" in /mnt/c/Users/hyc97/workspace/Ecclesia/CPU
exec
/usr/bin/zsh -lc "sed -n '1,260p' cpu-investment-research-2/transcript/full_debate.md" in /mnt/c/Users/hyc97/workspace/Ecclesia/CPU
exec
/usr/bin/zsh -lc "sed -n '1,260p' cpu-investment-research-2/sources/source_log.md" in /mnt/c/Users/hyc97/workspace/Ecclesia/CPU
 succeeded in 198ms:
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

 succeeded in 174ms:
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

 succeeded in 192ms:
# CPU Investment Research Debate Transcript



---

# codex: codex_initial

Timestamp: 2026-04-25T22:39:39

# Initial Independent CPU Equity Memo

## 1. Executive Thesis

The bullish CPU thesis is investable, but only if framed narrowly: AI does not eliminate CPU demand; it increases demand for orchestration, inference serving, storage, networking, and general-purpose cloud refresh. The strongest evidence is not a generic “AI needs CPUs” narrative, but the combination of hyperscaler capex, OEM AI-server backlog, AMD EPYC share gains, Intel DCAI recovery, and Arm server penetration.

Base conclusion: **own CPU upside through AMD, Arm, and TSMC first; treat OEM/ODM names as execution and margin trades; treat Intel as a turnaround watchlist name; avoid Qualcomm as a server CPU thesis until products/customers are proven.**

## 2. Industry Map

- **CPU vendors:** AMD and Intel dominate merchant x86 server CPUs.
- **Architecture/IP:** Arm benefits from hyperscaler and Nvidia Arm CPU adoption through royalties and licensing.
- **Custom silicon / AI infrastructure:** Broadcom and Marvell benefit from custom AI accelerators, networking, SerDes, and ASIC programs, but are not clean CPU plays.
- **Foundry:** TSMC is the broadest beneficiary across AMD, Arm-based custom silicon, AI ASICs, and networking silicon.
- **OEM/ODM:** Dell, Supermicro, HPE, Lenovo, Quanta, Wiwynn, Inventec convert AI/server demand into revenue, but margins are structurally pressured by pass-through GPU/BOM economics.

## 3. Company Universe

| Group | Companies | CPU Thesis Relevance |
|---|---|---|
| Direct CPU | AMD, Intel | Highest direct exposure |
| Architecture/IP | Arm | High exposure to Arm substitution and hyperscaler custom CPUs |
| Prospective CPU | Qualcomm | Option value only; server CPU not proven |
| Custom/AI silicon | Broadcom, Marvell | Benefits from custom AI infrastructure, may compete with merchant CPU/GPU architectures |
| Foundry | TSMC | Broadest picks-and-shovels exposure |
| OEM/ODM | Dell, SMCI, HPE, Lenovo, Quanta, Wiwynn, Inventec | Demand signal; lower-quality margin capture |

## 4. Demand Drivers

Confirmed demand signals are strong. Dell closed **more than $64B of FY26 AI-optimized server orders**, shipped **more than $25B**, and entered FY27 with **$43B backlog**. Microsoft reported FY26 Q2 capex of **$37.5B**, with roughly two-thirds on short-lived assets, “primarily GPUs and CPUs,” and said demand exceeds supply. Alphabet guided 2026 capex to **$175B-$185B**. Amazon said it expects about **$200B** of 2026 capex.

Analyst estimates are also supportive: TrendForce forecasts 2026 total server shipments +12.8% YoY and AI server shipments +28%+ YoY. This is still an estimate, not fact.

## 5. Server CPU Market Structure

The market is bifurcating:

- **Merchant x86:** AMD gaining share and richer mix; Intel still large and showing recent DCAI recovery.
- **Captive/custom Arm:** AWS Graviton, Microsoft Cobalt, Nvidia Grace/Vera, and other hyperscaler CPUs pressure x86 over time.
- **AI rack systems:** GPU/ASIC platform choice increasingly dictates CPU attach, cooling, networking, and server architecture.

Important caveat: IDC “non-x86 server” growth is not the same as Arm CPU share. Accelerated systems, proprietary architectures, and high-value AI racks can distort revenue share.

## 6. Hyperscaler And Data Center Order Signals

Confirmed:
- Microsoft FY26 Q2 capex: **$37.5B**, roughly two-thirds short-lived assets, primarily GPUs and CPUs.
- Alphabet 2026 capex guide: **$175B-$185B**.
- Amazon 2026 capex expectation: about **$200B**.
- Meta 2026 capex guide: **$115B-$135B**.
- Oracle Q3 FY26 RPO: **$553B**, up 325% YoY, with large-scale AI contracts.

Interpretation: these numbers support server demand, but not a precise CPU ASP or CPU-unit forecast. Confidence in broad infrastructure demand is High; confidence in CPU-specific revenue conversion is Medium.

## 7. OEM/ODM Server Configuration And Shipment Implications

Dell and Supermicro show extreme AI-server revenue conversion, but margin quality differs. Supermicro Q2 FY26 net sales reached **$12.7B**, but gross margin fell to **6.3%**, showing how AI server growth can be BOM-heavy and margin-thin. Wiwynn’s FY25 revenue rose **163.7% YoY**, with AI-related products over half of revenue, but Q4 gross margin fell to **7.2%** due to product mix.

Conclusion: OEM/ODM revenue is a good demand signal, not automatically a high-quality equity signal.

## 8. CPU Pricing / ASP / Margin Discussion

Confirmed data supports **server-system ASP inflation**, not clean CPU ASP inflation. Gartner estimated 2Q25 server vendor revenue +89.9% YoY while shipments declined 1.5%, driven by a 92.8% ASP increase from AI-optimized server demand. Mercury data reported by Tom’s Hardware shows AMD x86 server revenue share above unit share, consistent with richer mix.

Market rumor: Tom’s Hardware reported in April 2026 that server CPU prices rose 10%-20% since March 2026 due to AI/inference demand. Treat as **rumor / Low confidence** until checked against OEM quotes, distributor pricing, and Intel/AMD disclosures.

## 9. x86 Vs Arm Substitution Risk

Arm risk is real and investable. Arm reported Q3 FYE26 revenue +26% YoY and royalty revenue +27% YoY; management also said Neoverse CPUs surpassed 1B deployed cores and expects Arm share among top hyperscalers to reach nearly 50%. That is management guidance/claim, not independent market share.

For AMD/Intel, Arm is both a threat and a market validator: total server CPU demand can grow while x86 share declines.

## 10. Company-By-Company Analysis

- **AMD:** Best direct CPU candidate. FY25 Data Center revenue was **$16.6B, +32% YoY**, driven by EPYC CPUs and Instinct GPUs. Key risk: AMD does not disclose EPYC-only revenue, so CPU-specific growth must be inferred.
- **Intel:** Watchlist turnaround. Q1 2026 DCAI revenue was **$5.1B, +22% YoY**. Bullish CPU signal, but AMD share loss and foundry execution remain unresolved.
- **Arm:** Strong structural candidate. Benefits from hyperscaler custom CPUs and Nvidia Arm CPU platforms. Risk is valuation and indirect royalty capture.
- **Qualcomm:** Avoid for CPU thesis. Data center CPUs are “in development”; AI200/AI250 and Alphawave add optionality, but server CPU revenue/customer proof is absent.
- **Broadcom:** Strong AI infrastructure name, not a clean CPU play. FY25 Q4 AI semiconductor revenue +74% YoY; custom accelerators and Ethernet are the story.
- **Marvell:** Watchlist. FY26 revenue +42% YoY; data center was 74% of Q4 revenue. Strong AI custom silicon exposure, weak CPU purity.
- **TSMC:** Strong candidate. Broad beneficiary of advanced compute regardless of x86 vs Arm vs ASIC winner.
- **Supermicro:** Watchlist. Exceptional revenue growth, but margin compression and customer concentration risk are central.
- **Dell:** Stronger OEM candidate. AI orders/backlog are unusually explicit; watch ISG margin and working capital.
- **HPE:** Watchlist. Server revenue was down in Q1 FY26, while networking improved; not the cleanest CPU demand vehicle.
- **Lenovo:** Watchlist. AI revenue mix is rising, but server-specific disclosure is insufficient.
- **Quanta:** Watchlist/Strong ODM beta. 2025 monthly sales total rose 50.5% YoY; AI server attribution needs verification.
- **Wiwynn:** Strong ODM beta. AI products over half of FY25 revenue; margin pressure must be monitored.
- **Inventec:** Watchlist. FY25 revenue grew only 6.95%; recent AI server momentum needs more evidence.

## 11. Bull Case

AI inference and agentic workloads lift CPU attach, general-purpose server refresh, and x86/Arm server CPU demand simultaneously. AMD keeps gaining profitable EPYC share, Intel supply tightens DCAI pricing, Arm royalties compound from hyperscaler CPUs, and TSMC captures advanced-node volume across all winners.

## 12. Bear Case

AI rack architectures integrate more Arm/custom CPUs, reducing merchant x86 attach. CPU ASP rumors fade, AI capex pauses, OEM/ODM backlogs prove low-margin, and server CPU value is captured by hyperscalers, Nvidia, custom ASIC vendors, and TSMC rather than Intel/AMD.

## 13. Base Case

Server CPU demand grows, but less explosively than GPU/ASIC demand. AMD and Arm are the cleanest equity expressions; Intel improves but remains execution-heavy; OEM/ODM revenue grows faster than profit; TSMC remains the best diversified beneficiary.

## 14. Key Claims Table

| ID | Claim | Company | Category | Source | Confidence | Status |
|---|---|---|---|---|---|---|
| K1 | Worldwide server spending grew 52.4% YoY in Q4 2025; units +10.3%. | Industry | Server demand | [IDC](https://www.idc.com/promo/servers/) | High | Analyst estimate |
| K2 | 2026 server shipments forecast +12.8%; AI server shipments +28%+. | Industry | Demand | [TrendForce](https://www.trendforce.com/presscenter/news/20260120-12887.html) | Medium | Analyst estimate |
| K3 | Inference workloads are boosting general-purpose server demand. | Industry | Demand | [TrendForce](https://www.trendforce.com/presscenter/news/20260120-12887.html) | Medium | Analyst estimate |
| K4 | AMD FY25 Data Center revenue was $16.6B, +32% YoY. | AMD | Revenue | [AMD](https://ir.amd.com/news-events/press-releases/detail/1276/amd-reports-fourth-quarter-and-full-year-2025-financial-results) | High | Confirmed fact |
| K5 | Intel Q1 2026 DCAI revenue was $5.1B, +22% YoY. | Intel | Revenue | [Intel](https://www.intc.com/news-events/press-releases/detail/1767/intel-reports-first-quarter-2026-financial-results) | High | Confirmed fact |
| K6 | Microsoft FY26 Q2 capex was $37.5B; roughly two-thirds was GPUs/CPUs. | Microsoft | Capex | [Microsoft](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q2) | High | Confirmed fact |
| K7 | Dell FY26 AI server orders exceeded $64B; backlog $43B. | Dell | Orders | [Dell](https://investors.delltechnologies.com/news-releases/news-release-details/dell-technologies-delivers-fourth-quarter-and-full-year-fiscal-3) | High | Confirmed fact |
| K8 | Supermicro Q2 FY26 sales were $12.7B; gross margin 6.3%. | SMCI | OEM margin | [Supermicro](https://ir.supermicro.com/news/news-details/2026/Supermicro-Announces-Second-Quarter-Fiscal-Year-2026-Financial-Results/default.aspx) | High | Confirmed fact |
| K9 | Wiwynn FY25 revenue +163.7%; AI products over 50% of revenue. | Wiwynn | ODM demand | [Wiwynn](https://www.wiwynn.com/news/wiwynn-reports-fourth-quarter-2025-financial-results) | High | Confirmed fact |
| K10 | Arm Q3 FYE26 revenue +26%; royalty revenue +27%. | Arm | Revenue | [Arm](https://newsroom.arm.com/news/arm-q3-fye26-results) | High | Confirmed fact |
| K11 | Arm says Neoverse surpassed 1B deployed cores and may approach 50% share at top hyperscalers. | Arm | ARM adoption | [Arm](https://newsroom.arm.com/news/arm-q3-fye26-results) | Medium | Management claim |
| K12 | Broadcom Q4 FY25 AI semiconductor revenue +74% YoY. | Broadcom | AI silicon | [Broadcom](https://investors.broadcom.com/news-releases/news-release-details/broadcom-inc-announces-fourth-quarter-and-fiscal-year-2025) | High | Confirmed fact |
| K13 | Marvell FY26 revenue was $8.195B, +42% YoY; Q4 data center was 74% of revenue. | Marvell | AI silicon | [Marvell](https://investor.marvell.com/news-events/press-releases/detail/1011/marvell-technology-inc-reports-fourth-quarter-and-fiscal-year-2026-financial-results) | High | Confirmed fact |
| K14 | Meta guides 2026 capex to $115B-$135B. | Meta | Capex | [Meta](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Fourth-Quarter-and-Full-Year-2025-Results/) | High | Management guidance |
| K15 | Alphabet guides 2026 capex to $175B-$185B. | Alphabet | Capex | [Alphabet](https://abc.xyz/investor/events/event-details/2026/2025-Q4-Earnings-Call-2026-Dr_C033hS6/default.aspx) | High | Management guidance |
| K16 | Amazon expects about $200B capex in 2026. | Amazon | Capex | [Amazon](https://www.aboutamazon.com/news/company-news/amazon-earnings-q4-2025-report) | High | Management guidance |
| K17 | Qualcomm says server CPUs are in development. | Qualcomm | Product status | [Qualcomm](https://www.qualcomm.com/artificial-intelligence/data-center) | High | Confirmed fact |
| K18 | Server CPU prices reportedly rose 10%-20% since March 2026. | Intel/AMD | Pricing | [Tom’s Hardware](https://www.tomshardware.com/pc-components/cpus/shifting-need-for-cpus-in-ai-workloads-drives-intensifying-shortages-price-hikes) | Low | Market rumor |

## 15. Evidence Gaps

- EPYC-only revenue and Intel Xeon-only revenue.
- Server CPU ASP by SKU and customer class.
- CPU attach rate by architecture: HGX, GB200/GB300, MI300/MI350, Trainium, TPU, custom ASIC.
- OEM/ODM gross margin by AI server type.
- Arm royalty dollars per Neoverse server CPU.
- Hyperscaler order split across Dell, SMCI, Quanta, Wiwynn, Inventec, Foxconn, and internal builds.
- Whether reported CPU price increases are real transactions or channel noise.

## 16. Initial Ranking

| Ranking | Companies |
|---|---|
| Strong candidate | AMD, Arm, TSMC, Dell, Wiwynn |
| Watchlist | Intel, Broadcom, Marvell, Supermicro, Lenovo, Quanta, HPE, Inventec |
| Avoid for CPU thesis | Qualcomm |

## 17. What Must Be Verified Next

1. Build an architecture-level CPU attach table for Nvidia GB200/GB300, AMD MI300/MI350/MI400, AWS Trainium, Google TPU, and major ASIC racks.
2. Pull Mercury/IDC paid data for AMD, Intel, and Arm server CPU unit and revenue share.
3. Verify CPU pricing with OEM quotes, distributor checks, and hyperscaler procurement commentary.
4. Split AMD Data Center into EPYC vs Instinct using management commentary and channel estimates.
5. Track Q1/Q2 2026 capex updates from Microsoft, Amazon, Alphabet, Meta, Oracle, and major neoclouds.

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