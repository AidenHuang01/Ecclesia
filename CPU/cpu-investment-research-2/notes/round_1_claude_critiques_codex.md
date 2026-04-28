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