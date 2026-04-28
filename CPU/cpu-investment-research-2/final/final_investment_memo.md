# Final Investment Memo — CPU-Related Public Equities

**Prepared by:** Investment Committee Chair
**Date:** 2026-04-25
**Status:** Watchlist-level research. **Not actionable** as a CPU-pure long basket at current evidence quality.
**Inputs:** Full debate transcript (Claude bear-leaning analyst, Codex revisionist), claim register CDR-01 through CDR-40, source log S-01 through S-29.

---

## 1. Executive Summary

After two adversarial rounds, the committee finds **no CPU-pure equity that clears both an evidence bar and a valuation bar** for a Strong long recommendation in the current set-up. AI infrastructure demand is real and well-sourced (hyperscaler capex), but the CPU read-through of that capex is **not established** — the central piece of evidence (CPU dollars per AI rack vs traditional 2S rack) does not exist in any source consulted in this debate.

- **One Qualified candidate:** **TSMC**, but explicitly as **diversified AI/HPC foundry exposure**, not as a CPU-pure thesis. Confidence: Medium.
- **Watchlist (gating items specified):** AMD, Intel, Arm, Dell.
- **Avoid for CPU-pure thesis:** Qualcomm, HPE, SMCI, Wiwynn, Quanta, Inventec, Lenovo.
- **Substitution / benchmark only (not CPU longs):** Broadcom, Marvell, NVIDIA.
- **Substitution map (not investable in this framework):** AWS Graviton, Azure Cobalt, Google Axion, NVIDIA Grace/Vera, Ampere/SoftBank, IBM Power/Z.

The bear case (CPU as a shrinking share of AI rack BOM, with captive-ARM displacement at hyperscalers) is **directionally supported at Medium confidence**. The bull case (absolute CPU dollars grow despite share compression) is **plausible but Low confidence** because it requires per-rack BOM data that is not disclosed.

---

## 2. Final Investment Conclusion

**Do not initiate a CPU-pure long basket at this time.** The committee's verdict is to:

1. **Open one Qualified position** in TSMC sized as diversified AI/HPC foundry exposure, with explicit recognition that this is not a CPU-pure expression. Gated on CoWoS/SoIC allocation work and geopolitical risk sizing.
2. **Build models — not positions — for AMD, Intel, Arm, and Dell.** Each has a specific, named gating item (see §11). None can be sized today without that work.
3. **Decline all other names for a CPU-pure thesis.** This includes the Taiwanese ODMs and U.S. AI-server OEMs that the consensus narrative groups with the AI capex trade.
4. **Treat hyperscaler capex as demand backdrop and capital-cycle risk, not as a CPU revenue forecast** (CDR-29, CDR-37).

This is **watchlist-level research**. It is not actionable as a basket trade today. Individual position sizing on TSMC requires the additional gating work below.

---

## 3. Consensus Findings

After both rounds, both analysts converged on:

| # | Finding | Confidence |
|---|---|---|
| 1 | Hyperscaler 2026 capex is large and confirmed at the company level (S-03 MSFT, S-04 GOOG, S-05 AMZN, S-06 META). | High for capex; Low for direct CPU read-through. |
| 2 | CPU dollars per AI rack vs traditional 2S rack is the central missing evidence. Without it, no rigorous bull or bear case can be modeled. (CDR-23, CDR-28) | High for the gap itself. |
| 3 | Captive-ARM at hyperscalers is real and directionally negative for merchant x86, but displacement magnitude is not quantified. (CDR-18, CDR-33) | Medium directional / Unknown magnitude. |
| 4 | Dell has confirmed AI-server orders and backlog (S-07), but order duration, cancellation provisions, CPU content, and AI-server margin are not disclosed. (CDR-32) | High fact / Low CPU read-through. |
| 5 | SMCI (S-08) and Wiwynn (S-09) have confirmed low gross margins; SMCI carries a current independent-director investigation (S-24). | Medium-High. |
| 6 | TSMC is well-positioned as AI/HPC foundry exposure but CPU-only revenue is not isolable from S-20/S-21. (CDR-31) | Medium. |
| 7 | Broadcom and Marvell are substitution/benchmark exposure, not CPU longs. (CDR-25) | Medium-High. |
| 8 | Qualcomm has no shipping server CPU revenue today; Centriq history supports execution skepticism. (CDR-26, CDR-35) | Medium. |
| 9 | Bear quantifications on AI-server CPU BOM, sub-20% EPYC growth, and Sierra Forest mix were withdrawn for lack of evidence. (CDR-22) | High (resolved as withdrawn). |
| 10 | Intel's prior "Avoid" label is retracted on S-02 (DCAI +22% YoY) and S-19 (Rubin NVL8 host CPU role); but the upgrade to Watchlist is not yet earned. | Medium-Low for the retraction. |

---

## 4. Remaining Disputes

| # | Dispute | Claude position | Codex position | Committee disposition |
|---|---|---|---|---|
| 1 | Intel verdict | **Needs More Evidence** (retracts Avoid but does not earn Watchlist) | **Watchlist** | **Side with Claude.** Watchlist requires DCAI two-year stack, mix/ASP, gross margin attribution, and valuation. Codex's facts (S-02, S-19) are sufficient to remove Avoid but not to earn Watchlist on their own. |
| 2 | "CPU equities trade as AI capex beta" (CDR-17) | **UNSUPPORTED working hypothesis (Low)** | Accepts as untested | **Resolved as UNSUPPORTED.** Cannot be used in valuation. |
| 3 | Bundled vs unbundled "structural bear argument" | Argues for unbundling into three claims with separate confidence | Did not contest in Round 3 | **Side with Claude.** Adopt the three-claim split (CDR-38). |
| 4 | TSMC bucket placement | Reclassify out of "Qualified CPU-pure" into "diversified AI/HPC, not CPU-pure" | Same | **Resolved.** TSMC is Qualified as AI/HPC foundry, not as CPU-pure. |
| 5 | SMCI ranking | **Avoid** with explicit investigation flag (S-24) | **Avoid** | **Resolved as Avoid.** |
| 6 | Whether the rack-economics sensitivity (CDR-28) rescues the bull case | No, even with sensitivity table the BOM data is missing | Built sensitivity, agrees it does not rescue bull case | **Resolved.** Sensitivity is useful, not load-bearing. |

No remaining dispute material to the final ranking.

---

## 5. Unknowns / Data Gaps

Ranked by importance for the investment decision:

1. **Fatal:** CPU dollars and CPU % of BOM by AI rack platform (GB200/GB300 NVL72, DGX Rubin NVL8, MI300X/MI350 HGX, Trainium 2/3, TPU v5/v6, Maia). (CDR-23, CDR-28)
2. **High:** EPYC-only revenue/share split for AMD; Xeon-only mix/ASP/margin attribution for Intel.
3. **High:** Independent 2026 server CPU unit and revenue share data (Mercury / IDC / Omdia). All current share claims are management-sourced or stale (CDR-33).
4. **High:** Arm royalty $/server CPU/core; Arm China governance; customer concentration. (CDR-21-R)
5. **Medium-High:** Captive-ARM displacement quantified per hyperscaler in sockets and dollars, not capacity-mix language.
6. **Medium-High:** Dell AI-server order duration, cancellation provisions, and AI-server-specific gross margin. (CDR-32)
7. **Medium:** Valuation framework — P/E NTM, EV/EBITDA, FCF yield, implied IRR — built on primary filings, not third-party aggregators (S-25 is Medium quality only).
8. **Medium:** TSMC CoWoS/SoIC allocation by customer, with geopolitical risk sizing.
9. **Medium:** SMCI investigation (S-24) financial/legal exposure.
10. **Medium:** CPU-equity factor structure — does CPU-vendor stock variance load on AI capex beta, semis cycle beta, or company-specific revenue? (CDR-17-R)
11. **Low:** Server CPU price hike rumors (10–20%); excluded from base case.

---

## 6. Market Structure

**Confirmed:**
- Two-vendor merchant x86 server CPU market (AMD, Intel) with active captive Arm encroachment at the top three U.S. hyperscalers.
- AWS Graviton, Azure Cobalt, and Google Axion are deployed; NVIDIA Grace ships in GB200 NVL72 racks at 36 Grace CPUs per rack (S-12).
- Arm-architecture server adoption is broadening (S-10, S-11, S-13, S-14), but **independent share data is missing**; AWS's "majority of new CPU capacity" (S-11) is a dated management claim from the Graviton5 launch (CDR-33).
- ODM/OEM stack: Supermicro, Dell, HPE, Lenovo, Quanta, Wiwynn, Inventec all participate in AI-server build, but margin profiles diverge sharply (Dell ISG > SMCI/Wiwynn).
- Foundry is dominated by TSMC for advanced node CPU/GPU/ASIC silicon (S-20, S-21).

**Unsupported / consensus-narrative-only:**
- "Merchant CPU benefits proportionally from AI capex." Not established.
- "x86 duopoly is structurally protected." Captive-ARM evidence (S-11, S-13, S-14) directionally contradicts this.

---

## 7. Demand Outlook

**Confirmed (High):**
- Microsoft Q2 FY26 capex of $37.5B (S-03); Alphabet 2026 capex range $175B–$185B (S-04); Amazon ~$200B 2026 capex (S-05); Meta confirmed elevated 2026 capex (S-06).
- Aggregate is large but the sum is a Codex aggregation (CDR-37) and should be treated as scenario context, not a forecast.

**Read-through to CPU revenue: Low.** Capex is split across GPUs, ASICs, networking, HBM, packaging, land/buildings, power infrastructure, and software. CPU's share of incremental capex in AI builds is **undisclosed** (CDR-29).

**Demand by segment:**
- AI-server CPU attach rate: **Unknown** in dollar terms; per-rack CPU count is known for some platforms (GB200 NVL72: 36 Grace; DGX Rubin NVL8: Xeon 6 host) but per-rack CPU dollars are not.
- General-purpose cloud / enterprise refresh: assumed to provide continued merchant CPU demand; not separately sourced in this debate.
- Edge / telco / sovereign AI: not analyzed.

**Confidence:** Medium that CPU demand grows in absolute dollars; Low that it grows fast enough to justify CPU-equity multiples.

---

## 8. Server Configuration and CPU Attach-Rate Analysis

**Rack-economics sensitivity (CDR-28; Low-Medium confidence):**

| Platform | Confirmed facts | CPU-dollar estimate | Confidence |
|---|---|---|---|
| Traditional 40-node 2S EPYC 9654 rack | 80 CPUs; AMD 1kU price $8,452 (S-27) | ~$0.68M | Low-Medium; assumes 40 servers/rack |
| Traditional 40-node 2S Xeon 6980P rack | 80 CPUs; Intel RCP $12,460 (S-27) | ~$1.00M | Low-Medium |
| GB200 NVL72 | 36 Grace CPUs / 72 Blackwell GPUs (S-12) | Undisclosed; proxy $0.31M–$0.50M if priced like high-end merchant CPU | Low |
| DGX Rubin NVL8 | Xeon 6 host CPU role confirmed (S-19) | Not disclosed | Unknown |
| MI300X / MI350 HGX | Host CPU count varies by OEM | Not disclosed | Unknown |
| Trainium 2 / TPU v5p | Accelerator counts disclosed (S-28) | Host CPU dollars not disclosed | Unknown |

**Interpretation:** The traditional rack is the only platform where CPU dollars are calculable from public list/RCP prices, and even there the price-per-server count is an analyst assumption. AI-rack CPU economics are not modelable at current disclosure. The committee therefore **declines to make any directional claim about CPU $/rack** for AI platforms (CDR-23 remains a fatal gap).

**Attach rate in unit terms:** AI racks have *fewer* CPUs per accelerator than traditional 2S racks (e.g., 36 Grace : 72 Blackwell in GB200 NVL72, or 1 Xeon : 8 GPUs in DGX Rubin NVL8). Whether unit decline is offset by ASP increase (Grace, Xeon 6 high-SKU) is **Unknown**.

---

## 9. OEM/ODM Shipment Implications

**Confirmed:**
- Dell ISG growth and AI-server orders/backlog (S-07); operating margin materially higher than SMCI/Wiwynn at the segment level.
- SMCI Q2 FY26 GM 6.3% (S-08) — structurally low.
- Wiwynn Q4 GM 7.2% (S-09) — structurally low.
- HPE has materially shifted toward networking via the Juniper acquisition (S-22); CPU-pure exposure has diluted.
- SMCI carries a current independent-director investigation tied to export-control matters (S-24).

**Not confirmed (required before generalizing):**
- Quanta, Inventec, Lenovo normalized AI-server margins.
- Dell AI-server-specific gross margin (segment-level ISG margin includes traditional servers).
- Order duration, cancellation provisions, and BOM mix at any of the AI-server OEMs/ODMs.

**Investment read-through:**
- AI-server unit and revenue growth is **not synonymous with profit growth** for OEM/ODMs. SMCI and Wiwynn are confirmed margin-thin; Dell is the only OEM with confirmed strong segment-level economics, but its CPU-attributable margin is not isolated.
- Pure unit-shipment exposure (Quanta, Wiwynn, Inventec) trades increasingly on hyperscaler ODM allocation, not on CPU economics — which makes them poor vehicles for a CPU-pure thesis.

---

## 10. CPU Pricing / ASP / Margin Implications

**Confirmed:**
- Server-system ASP is rising sharply: S-15 cited +92.8% YoY with units −1.5%, indicating mix/system-richness, not necessarily CPU-ASP-driven.
- AMD EPYC and Intel Xeon list/RCP prices have ratcheted higher at the top of the SKU stack (S-27).

**Not confirmed:**
- Whether hyperscaler transaction prices follow list/RCP. (List prices are a proxy only — CDR-28 / S-27.)
- Whether Sierra Forest E-core mix is dilutive to Intel CPU ASP (bear quantification withdrawn — CDR-22).
- Server CPU price hike rumors (10–20%) — excluded from base case until distributor/OEM channel checks confirm.

**Margin read-through:**
- AMD: confirmed Data Center growth (S-01); EPYC-only margin attribution unknown.
- Intel: DCAI +22% YoY (S-02); standalone Xeon margin attribution unknown; foundry/18A drag remains.
- Arm: revenue and royalty growth confirmed (S-10); royalty $/server core unknown.

**Verdict:** CPU pricing is directionally supportive at the top of the SKU stack, but the margin translation is undisclosed. **Do not model CPU ASP as a positive surprise** in the base case.

---

## 11. Company-by-Company Thesis

| Company | Verdict | Thesis (one sentence) | Gating evidence | Key sources |
|---|---|---|---|---|
| **TSMC** | **Qualified (AI/HPC foundry, not CPU-pure)** | Diversified silicon and packaging exposure to AI/HPC, with CPU as one of several beneficiaries. | CoWoS/SoIC allocation by customer; geopolitical risk sizing. | S-20, S-21 |
| **AMD** | **Watchlist** | EPYC share gains likely continue, but the EPYC-vs-Instinct revenue split is not disclosed and valuation is high. | EPYC-only revenue / share; valuation framework on primary data. | S-01, S-25, S-26 |
| **Intel** | **Needs More Evidence** (Avoid label retracted; Watchlist not earned) | DCAI +22% (S-02) and Rubin NVL8 host-CPU role (S-19) remove the prior bear bias, but mix/ASP/margin/valuation are required before a directional view. | DCAI two-year stack; Sierra Forest vs Granite Rapids mix; foundry/18A trajectory. | S-02, S-19, S-25 |
| **Arm** | **Deferred** | Server adoption is broadening, but valuation, royalty $/core, Arm China, and customer concentration are all unresolved. | Royalty model; valuation defense; Arm China governance. | S-10, S-25, S-26 |
| **Dell** | **Watchlist** | Confirmed AI-server orders (S-07), but CPU-attributable content, AI-server margin, and order duration are undisclosed. | AI-server-specific GM; backlog duration and cancellation terms. | S-07 |
| **SMCI** | **Avoid (CPU-pure)** | Structural low GM (S-08) and current independent-director investigation (S-24). Valuation alone does not offset. | Investigation outcome; sustainable GM normalization. | S-08, S-24 |
| **Wiwynn** | **Avoid (CPU-pure)** | Confirmed low GM (S-09); pure pass-through ODM economics. | N/A for CPU-pure. | S-09 |
| **HPE** | **Avoid (CPU-pure)** | Materially networking-weighted post-Juniper (S-22); CPU exposure dilutes. | N/A for CPU-pure. | S-22 |
| **Qualcomm** | **Avoid (CPU-pure)** | No shipping server CPU revenue; Centriq precedent (S-23) supports execution skepticism; option value is non-zero but not investable today. | Customer wins and revenue proof; separate accelerator from CPU narrative. | S-18, S-23 |
| **Quanta / Inventec / Lenovo** | **Avoid (CPU-pure)** | Insufficient CPU-attributable margin disclosure; pure shipment exposure. | Per-company normalized margin. | — |
| **Broadcom / Marvell** | **Substitution / benchmark only** | Custom AI silicon and ASIC racks are CPU substitutes, not CPU longs. | N/A for CPU-pure. | S-16, S-17 |
| **NVIDIA** | **Substitution / benchmark only** | The accelerator exposure that CPU revenue is being substituted by; benchmark only. | N/A for CPU-pure. | S-12, S-19, S-25 |

---

## 12. Final Ranking

| Bucket | Names |
|---|---|
| **Strong candidate** | None. |
| **Qualified candidate** | TSMC (as diversified AI/HPC foundry exposure, not CPU-pure). |
| **Watchlist** | AMD, Intel (Needs More Evidence flag), Dell. |
| **Deferred** | Arm. |
| **Avoid for CPU-pure thesis** | Qualcomm, HPE, SMCI, Wiwynn, Quanta, Inventec, Lenovo. |
| **Substitution / benchmark only (not longs)** | Broadcom, Marvell, NVIDIA. |
| **Substitution map (not investable here)** | AWS Graviton, Azure Cobalt, Google Axion, NVIDIA Grace/Vera, Ampere/SoftBank, IBM Power/Z. |

**Important framing (CDR-40):** "Avoid" labels apply to the **CPU-pure investment thesis** only. They are not whole-company Avoid recommendations. HPE, SMCI, Wiwynn, Qualcomm, Quanta, Inventec, Lenovo each have non-CPU drivers that may justify separate, non-CPU-thesis evaluation outside this memo's scope.

---

## 13. Bull / Base / Bear Scenarios

**Bull — Low confidence.** Inference workloads, agentic AI, sovereign AI, and a delayed enterprise refresh deliver enough general-purpose compute demand that absolute CPU dollars grow even as CPU share of AI rack BOM compresses. AMD EPYC continues to take revenue share; Intel Xeon 6 host-CPU wins anchor a price/mix recovery; Arm royalties scale with hyperscaler captive deployment; TSMC captures the diversified silicon and packaging layer regardless of architecture. **Required to validate:** CPU $/rack table, EPYC-only and Xeon-only revenue, independent server CPU share, and valuation framework. None exist today.

**Base — Medium confidence.** AI capex remains the dominant 2026 demand signal, but CPU dollars are a smaller and slower-growing slice than GPU/ASIC/HBM/networking/packaging. Merchant x86 grows mid-single to low-double digits in revenue. Captive ARM continues to take new-capacity share at the top three U.S. hyperscalers. AMD beats Intel on share; neither EPYC nor Xeon individually justifies current CPU-equity multiples without per-rack CPU economics confirmation. OEM/ODM revenue grows faster than profit.

**Bear — Medium confidence.** Accelerated racks, captive ARM at AWS/Azure/GCP, and ASIC racks (Broadcom-built TPU/Trainium/Maia) absorb the marginal new compute slot. Server-system ASP rises while CPU sockets and CPU ASP lag (S-15 directionally supportive). OEM/ODM margins stay compressed at SMCI and Wiwynn; Dell margins hold up only via mix shift away from low-margin AI orders. Hyperscaler 2H26 capex digestion (CDR-37) hits OEM/ODM and merchant CPU first.

All three cases share the same fatal evidence gap (CDR-23). Until CPU $/rack exists, no case is rigorously model-supported.

---

## 14. Key Risks

| # | Risk | Hits | Confidence |
|---|---|---|---|
| 1 | Captive-ARM displacement of merchant x86 accelerates beyond current management language. | AMD, Intel | Medium |
| 2 | AI rack CPU $/BOM is materially lower than legacy 2S rack, and the gap widens with NVL72-style architectures. | AMD, Intel | Medium |
| 3 | Hyperscaler 2H26 capex digestion / capital-cycle reversal. | All CPU and OEM/ODM names | Medium |
| 4 | TSMC geopolitical risk (Taiwan / China) and CoWoS/SoIC bottleneck reallocation. | TSMC | Medium |
| 5 | SMCI investigation escalates into financial/legal liability or delisting risk. | SMCI | Medium |
| 6 | Intel 18A / foundry execution slips; DCAI ASP/margin disappoints. | Intel | Medium-High |
| 7 | Arm China governance, customer concentration, or royalty-rate disputes. | Arm | Medium |
| 8 | Dell AI-server orders carry softer-than-disclosed cancellation terms; backlog quality deteriorates. | Dell | Medium-Low |
| 9 | Valuation reset across high-multiple AI-adjacent equities (AMD, Arm in particular). | AMD, Arm | Medium |
| 10 | Server CPU price-hike rumors do not materialize; ASP support fades. | AMD, Intel | Low-Medium |

---

## 15. What Would Change The Thesis

**Upgrade triggers (any name from Watchlist → Qualified, or Qualified → Strong):**

| Trigger | Affects | Required source |
|---|---|---|
| Disclosure of CPU dollars and CPU % BOM by AI rack platform | All | NVIDIA, AMD, hyperscaler BOM, or sell-side teardown |
| AMD EPYC-only revenue and share data | AMD | AMD segment disclosure or Mercury/IDC |
| Intel DCAI two-year stack with mix/ASP/margin | Intel | Intel disclosure |
| Arm royalty $/server CPU/core | Arm | Arm disclosure or analyst-day update |
| Dell AI-server-specific gross margin and order duration | Dell | Dell disclosure |
| Independent 2026 server CPU share (Mercury/IDC/Omdia) | AMD, Intel, Arm | Third-party |
| Valuation reset of AMD / Arm (multiples compress on growth) | AMD, Arm | Market |
| TSMC CoWoS allocation by customer + geopolitical risk update | TSMC | TSMC disclosure or sell-side |

**Downgrade triggers (any name from Watchlist → Avoid):**

| Trigger | Affects |
|---|---|
| Mercury/IDC confirms captive-ARM share at hyperscalers crossed 30%+ of new capacity | AMD, Intel |
| GB300 / Rubin / Vera roadmap reduces host-CPU count further | AMD, Intel |
| Hyperscaler capex guidance cut for 2H26 | All |
| SMCI investigation produces material restatement or delisting threat | SMCI |
| Dell AI backlog cancellations become material | Dell |

---

## 16. Claim Register Summary

The full register has 40 claims (CDR-01 through CDR-40 with revisions). Highest-importance entries for the final memo:

| ID | Claim | Confidence | Status |
|---|---|---|---|
| CDR-17-R | "CPU equities trade as AI capex beta" | Low | UNSUPPORTED working hypothesis |
| CDR-18 | Captive-ARM substitution at hyperscalers is real | Medium | Directional only |
| CDR-19-R | OEM/ODM margin thinness confined to SMCI and Wiwynn | Medium / Unknown for others | Revised, do not generalize |
| CDR-20-R | Intel verdict: Avoid retracted; Watchlist not earned | Medium-Low / Unknown | Needs More Evidence |
| CDR-21-R | Arm deferred on valuation, royalty model, Arm China, customer concentration | Unknown | Revised |
| CDR-22 | Prior bear quantifications withdrawn | High | Resolved |
| CDR-23 | CPU $/rack is the central missing evidence | High evidence gap | FATAL GAP |
| CDR-24-R | TSMC reclassified to AI/HPC foundry, not CPU-pure | Medium | Revised |
| CDR-27-R | SMCI Avoid retained on margin + investigation | Medium-High | Revised |
| CDR-28 | Rack CPU-dollar table is sensitivity only | Low-Medium | Useful only as bounds |
| CDR-29 | Hyperscaler capex is not CPU demand evidence | High fact / Low read-through | Revised |
| CDR-30 | Valuation prevents AMD / Intel / Arm upgrades | Medium | Added |
| CDR-32 | Dell orders confirmed; CPU/margin/duration unknown | High fact / Low read-through | Revised |
| CDR-33 | Graviton "majority of new capacity" is dated mgmt claim | Medium directional / Unknown magnitude | Revised |
| CDR-37 | Hyperscaler capex scale is also a capital-cycle risk | Medium | Added |
| CDR-38 | Bear arguments unbundled into three claims with separate confidence | Per-claim | Added (this round) |
| CDR-39 | Intel Rubin NVL8 win does not reverse Arm-host trend in NVL72 | High facts / Medium read-through | Added (this round) |
| CDR-40 | "Avoid" applies to CPU-pure thesis, not whole company | High | Added (this round) |

---

## 17. Source Quality Assessment

| Tier | Sources | Notes |
|---|---|---|
| **High (primary, current)** | S-01 (AMD), S-02 (Intel), S-03 (MSFT), S-04 (GOOG), S-05 (AMZN), S-06 (META), S-07 (Dell), S-08 (SMCI), S-09 (Wiwynn), S-10 (Arm), S-12 (NVIDIA GB200), S-15 (server ASP), S-16 (Broadcom), S-17 (Marvell), S-18 (Qualcomm), S-19 (NVIDIA DGX Rubin NVL8), S-20 (TSMC Q1 26 release), S-21 (TSMC Q1 26 mgmt report), S-22 (HPE Juniper close), S-24 (SMCI investigation), S-28 (AI platform pages) | Company-issued earnings releases, transcripts, product/architecture pages. |
| **Medium (third-party, useful as proxy)** | S-25 (StockAnalysis statistics), S-27 (CPU list/RCP product pages — not transaction prices) | Use as bounds, not as primary facts. |
| **Medium-Low (consensus / aggregator)** | S-26 (StockAnalysis forecast pages, citing Finnhub/Benzinga) | Consensus estimates; flagged as estimate, not fact. |
| **High but stale** | S-11 (AWS Graviton5 launch — "majority of new CPU capacity" is a management claim, dated; CDR-33), S-23 (Qualcomm Centriq 2017) | Useful as direction; not as 2026 share data. |
| **High existence / Low displacement-magnitude** | S-29 (Ampere/SoftBank, IBM z17, Telum II) | Confirms substitution map participants exist; does not size displacement. |

**Independent server CPU share data (Mercury / IDC / Omdia) is the single most important missing source category.** All current share claims in this memo lean on management language or third-party aggregators.

**No paid-data feeds were consulted.** This memo is built entirely from primary company materials and one third-party market-data aggregator (StockAnalysis). Conclusions should be re-tested when paid data is available.

---

## Final note on actionability

This memo is **watchlist-level research, not actionable**, with one narrow exception: TSMC may be sized as diversified AI/HPC foundry exposure following completion of the CoWoS/SoIC allocation and geopolitical risk work cited in §11. All other names require the specific gating disclosures listed before any directional position can be built. The committee explicitly resists the consensus narrative that "CPU equities are the AI trade" — the evidence does not support it, and the central piece of evidence required to support or refute it (CPU $/rack by platform) does not exist in any source consulted.