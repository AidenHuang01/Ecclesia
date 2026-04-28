# Round 2 Adversarial Review — Opposing CPU Equity Memo

**Reviewer:** Claude (opposing analyst)
**Subject:** Codex Round 2 revision dated 2026-04-25
**Stance:** Codex accepted most Round 1 critiques. Good. But several Round 1 fatal flaws remain unfixed, the relabeling from "Strong" to "Qualified" is rhetorical not analytical, and new issues have crept in. The thesis is now *more honest* but still not *investable*.

---

## 1. Highest-Risk Errors

**F1-R (still fatal). The CPU $-per-rack table was deferred again.**
Codex listed it as Round 1 follow-up, accepted the critique, listed it as "Unresolved Dispute #1" in Round 2, and *still did not build it*. This was the single most load-bearing missing analysis. Without it, "Bull / Base / Bear" cases are narrative not quantitative. Severity: **Fatal**, repeat offense.

**F2-R (still fatal). No valuation framework, despite Accept on F5.**
Codex accepted the no-valuation critique and then ranked TSMC, AMD, Intel, Arm, and Dell as "Qualified candidates." A "Qualified candidate" without a P/E, EV/EBITDA, FCF yield, or implied IRR is the same epistemic object as a "Strong candidate" — a thesis without a price. Acceptance ≠ remediation. Severity: **Fatal to the rating system itself**.

**F3-R (new). The "Strong → Qualified" relabel is rhetorical, not analytical.**
Round 1 ranked five names "Strong." Round 2 ranks the same companies (minus Wiwynn, plus Intel) as "Qualified." Same number, same names, weaker label. No claim was actually disqualified — Codex just lowered the heading. Severity: **Major** — gives the appearance of epistemic update without one.

**F4-R (still major). Microsoft "primarily GPUs and CPUs" framing persists.**
Round 1 critique: stop splitting GPU/CPU; Microsoft groups them as a *category* (silicon vs. real estate). Round 2 still writes: "two-thirds was short-lived assets, primarily GPUs and CPUs." That phrasing still anchors the reader on a CPU+GPU mix that's irrelevant — the GPU:CPU dollar ratio is ~10–20:1 in AI builds. The fix is to drop GPU/CPU language entirely and say "silicon and short-lived equipment." Severity: **Major**, half-fixed.

**F5-R (new). Bull and Bear cases both labeled "Medium Confidence" — epistemically incoherent.**
Mutually exclusive scenarios cannot share the same confidence. Either the bull case is Low (which the evidence supports) or the bear case is Higher than Medium. As written, the framework collapses. Severity: **Major**.

**F6-R (still major). Amazon "$200B" still not source-checked verbatim.**
Codex cites a press-release URL but did not paste the literal sentence. Amazon historically annualizes Q4 capex run-rate or gives directional language ("higher than 2025"); a precise $200B *full-year guide* is unusual. Without the literal quote, K16 should not carry "High Confidence." Severity: **Major**.

---

## 2. Unsupported Claims (Round 2 specific)

| Statement in Codex Round 2 | Why unsupported |
|---|---|
| "AWS says Graviton is over half of new AWS CPU capacity" | This was an Adam Selipsky / Peter DeSantis remark in 2024–2025. Not verified for 2026. May be stale. Codex cites a 2025-12-04 Graviton 5 launch URL — not the same claim. |
| "Intel benefits from x86 host CPU roles such as DGX Rubin NVL8" (Bull case) | DGX Rubin NVL8 is announced; revenue contribution is unmodeled. Treating it as a bull driver without unit economics is hand-waving. |
| "AMD EPYC grows faster than Intel" (Bull case) | After Round 1's accept-with-revision on EPYC-only disclosure gap, this claim has *no underlying data* to support it. Inconsistent with Codex's own downgrade of "AMD EPYC growth >25% → UNSUPPORTED." |
| "TSMC captures the diversified silicon and packaging layer" (Bull case) | Round 1 critique on CoWoS-L allocation accepted, but Round 2 didn't add the allocation analysis. The bull case still leans on the un-analyzed claim. |
| "Qualcomm prior Centriq attempt raises execution skepticism" (Avoid rationale) | Codex linked the 2017 Centriq launch — but the relevant fact is the *2018 cancellation*, not the launch. Citation supports the wrong half of the argument. |
| Alphabet $175B–$185B 2026 capex | URL provided, but no literal quote pasted. Magnitude is ~2.3x 2025 baseline — base-rate-implausible enough to require verbatim verification. |

---

## 3. Questionable Assumptions

**Q1-R.** *That Intel belongs in the same "Qualified" bucket as AMD, Arm, and TSMC.*
Round 1 noted that Intel is *more* leveraged to merchant CPU upside than AMD (because AMD's DC revenue is diluted by Instinct). Codex accepted this implicitly but didn't restructure the bucket. Intel and AMD have inverted risk profiles (Intel: execution risk, CPU-pure; AMD: CPU-mix risk, GPU-diluted) and shouldn't be lumped together.

**Q2-R.** *That moving Wiwynn, SMCI, Quanta, Inventec to "Watchlist / benchmark" addresses Round 1's margin critique.*
Round 1 challenge was that ODMs at 6–8% GM at peak revenue are *structurally* low-quality earnings, not transitional. "Watchlist / benchmark" is not a sell signal; for a CPU-pure thesis they should be in **Avoid**.

**Q3-R.** *That "Qualified" without a valuation cap is meaningfully different from "Strong" without one.*
At current Arm forward multiples (~70–90x depending on date), the company can be a "Qualified candidate" only if *price-insensitive* upside exists. Codex doesn't say what price disqualifies it.

**Q4-R.** *That Dell's $64B / $43B figure is high-confidence.*
Codex confirmed the figure exists in Dell's IR materials. Fine. But the **interpretation question** — orders vs. backlog vs. multi-year framework agreement, duration, cancellation provisions — was not resolved. Round 1 flagged this; Round 2 listed it as Unresolved Dispute #7. Same issue: accepted, not addressed.

**Q5-R.** *That "primarily GPUs and CPUs" Microsoft language has any CPU read-through at all.*
Codex labels this "High fact / Low CPU read-through." If CPU read-through is Low, the claim should not appear in Demand Drivers at all — it's misleadingly placed in section 6 of the original memo and the same wording survives.

**Q6-R.** *That Bull case "needs CPU-per-rack and share data" is sufficient as a caveat.*
A bull case predicated on missing data is an aspiration, not a case. Either Codex builds the data or removes the bull case.

**Q7-R.** *That capex at the disclosed magnitudes is risk-symmetric.*
Aggregate hyperscaler 2026 capex of ~$675B+ (MSFT + GOOG + AMZN + META) is itself a *bear* signal for capital cycle risk: this magnitude has no historical precedent in tech infra and increases the probability of 2H26 / 2027 air-pocket. Codex's bear case acknowledges this only weakly ("AI capex pauses").

---

## 4. Missing Evidence (Round 2 specific)

**Still missing from Round 1 list — not added in Round 2:**
- CPU $-per-rack comparison table (the central analysis).
- Valuation snapshot for any company.
- Channel-checked CPU ASP from real distributors (kill or upgrade K18).
- Mercury / IDC / Omdia paid Q4 2025 / Q1 2026 server CPU unit + revenue share data.
- Arm royalty $-per-Neoverse-server-core estimate.
- Memory bandwidth / HBM constraints on CPU pricing power.
- ABF substrate / packaging gating for server CPUs.
- US export controls' CPU revenue impact (Intel/AMD China).

**Companies still missing or under-discussed:**
- **Ampere Computing / SoftBank** — Acquired by SoftBank, now Arm-aligned hyperscaler CPU vendor. Round 1 flagged. Round 2 ignored.
- **IBM Power / Z17** — Niche but real. Round 1 flagged. Round 2 ignored.
- **MediaTek** — NVIDIA partnership for Arm-based CPUs; potential server extension. Round 1 flagged. Round 2 ignored.
- **Memory ecosystem**: Samsung, SK hynix, Micron — HBM bandwidth gates AI CPU value-add. Not in industry map.
- **Substrate/packaging**: Ibiden, Unimicron — supply constraint for server CPUs. Not in industry map.

**Codex did add to the universe** (Foxconn, Celestica), but only at "Watchlist / benchmark" level without analysis. Adding names without evidence does not address Round 1.

---

## 5. Company-Specific Objections (Round 2)

**AMD.** Codex now correctly downgrades "EPYC growth >25%" to UNSUPPORTED but *still* writes "AMD EPYC grows faster than Intel" in the bull case. Internally inconsistent.

**Intel.** Wrong bucket. Either Intel is the *cleanest* CPU-pure expression (and should be ranked above AMD for a pure thesis), or it's gated by 18A foundry execution (and belongs lower). Putting it in the same "Qualified" bucket as AMD avoids the choice.

**Arm.** "Qualified candidate" without an explicit price-disqualification level is a punt. Round 1 critique on royalty-$/core was accepted, but Round 2 didn't model it. The valuation question is unanswered.

**Qualcomm.** Citation supports the wrong half (2017 launch URL, not 2018 cancellation). Argument intent is correct; evidence is sloppy.

**TSMC.** Round 1 critique on CoWoS-L allocation was accepted; Round 2 didn't add the analysis. "Qualified candidate" is unsupported by the work that was supposed to back it up.

**Dell.** Order figure verified ✓. But ISG operating margin, AI-server unit economics, and order-duration analysis are still missing. Round 1 said "if real, still a low-margin pass-through" — Round 2 didn't address.

**Supermicro.** Round 1 flagged SEC investigation, auditor change, 10-K delay. Round 2 marked margin "Revised negative" but did not acknowledge the accounting/governance overhang. Material omission.

**HPE.** Juniper now mentioned ✓. But the implication — HPE is no longer a server-led story — should disqualify it from the CPU framework, not put it on the watchlist.

**Wiwynn / Quanta / Inventec.** Margin critique accepted ✓ for Wiwynn only. Quanta and Inventec carry the same structural margin profile and should be downgraded for the same reason. Inconsistent application.

**NVIDIA.** Added to "Watchlist / benchmark." Wrong category. NVIDIA Grace/Vera is a *direct merchant-CPU substitute* sold inside NVIDIA's own AI rack systems — it belongs in the **substitution map** (alongside Graviton, Cobalt, Axion), not in a benchmark bucket.

**Broadcom / Marvell.** Codex defends keeping them as "substitution and relative-return benchmarks." Acceptable, but if so, the company-by-company section should not carry CPU-thesis ratings for them. Currently still mixed.

---

## 6. Revised Ranking

| Rank | Companies | Reasoning |
|---|---|---|
| **Strong candidate (CPU-thesis pure)** | None. Same as Codex Round 2. | Agreed. |
| **Qualified candidate** | Intel (CPU-purest expression), TSMC (only at price discipline; CoWoS allocation pending) | Narrowed from Codex's five. |
| **Watchlist** | AMD (pending EPYC-only disclosure), Arm (pending price compression), Dell (pending ISG margin / order-duration) | Each has a specific gating event. |
| **Avoid for CPU-pure thesis** | Qualcomm, HPE, Supermicro, Wiwynn, Quanta, Inventec, Lenovo, Broadcom, Marvell, NVIDIA (as CPU bet, not as company) | Either non-CPU, or low-quality CPU earnings, or both. |
| **Substitution-risk map (not investable on this thesis)** | NVIDIA Grace/Vera, AWS Graviton, Azure Cobalt, Google Axion, Ampere/SoftBank, IBM Power | Direct merchant-CPU TAM headwinds. |

The disagreement with Codex Round 2: Intel deserves a higher tier than AMD for a *CPU-pure* thesis (because AMD's data center revenue is GPU-diluted), and the Avoid list should be longer.

---

## 7. Claim Challenges Table

| Claim ID | Problem | Severity | Suggested Fix | Status |
|---|---|---|---|---|
| K6-R | "Primarily GPUs and CPUs" wording survives — still anchors reader on CPU mix that doesn't exist. | Major | Restate as "silicon vs. real estate"; remove GPU/CPU split language entirely. | Open |
| K7-R | Dell figure verified, but order-duration / cancellation / margin still unaddressed. | Major | Pull Dell FY26 Q4 transcript verbatim; segment "orders" by duration. | Open |
| K15 | Alphabet $175–185B 2026 capex — verbatim quote not pasted; magnitude is ~2.3x 2025 baseline. | Major | Quote literal sentence from 4Q25 transcript with page reference. | Open |
| K16 | Amazon $200B 2026 capex — Amazon historically does not give annual capex guidance. | Major | Quote exact wording; if it's a Q4 annualized run-rate vs. full-year guide, restate. | Open |
| K17 | Qualcomm Centriq citation supports 2017 launch, not 2018 cancellation. | Minor | Replace with the cancellation announcement source. | Open |
| **C19** | CPU $-per-rack table still not built. | **Fatal, repeat** | Round 2 deferred this; Round 3 must deliver it or drop the bull case. | Open |
| **C23** | No valuation framework still — accepted but not built. | **Fatal, repeat** | Add P/E NTM, EV/EBITDA NTM, FCF yield for AMD, Intel, Arm, TSMC, Dell, SMCI; specify disqualifying multiple. | Open |
| **C25 (new)** | Bull and Bear scenarios both labeled "Medium Confidence" — incoherent. | Major | Bull → Low; Base → Medium; Bear → Medium-High. Or rebuild with explicit probability weights. | Open |
| **C26 (new)** | "Strong → Qualified" relabel without analytical change. | Major | Either disqualify a name with evidence or revert label. | Open |
| **C27 (new)** | Graviton "over half of new CPU capacity" claim — possibly stale 2024-2025 wording. | Minor | Verify with current AWS leadership statement (2026); date-stamp the source. | Open |
| **C28 (new)** | Bull case still asserts "AMD EPYC grows faster than Intel" while Codex's own downgrade list marks "EPYC growth >25%" UNSUPPORTED. Internal contradiction. | Major | Remove from bull case, or back with a channel estimate. | Open |
| **C29 (new)** | Wiwynn margin critique accepted; Quanta and Inventec carry same structural issue but were not downgraded consistently. | Minor | Apply margin downgrade across all Taiwan ODMs or articulate why they differ. | Open |
| **C30 (new)** | Ampere/SoftBank, IBM Power, MediaTek still missing from universe. | Major | Add to substitution map at minimum. | Open |
| **C31 (new)** | Memory bandwidth / HBM constraint on CPU value-add not modeled. | Major | Add to industry map; cite Samsung/SK hynix/Micron HBM3e/HBM4 capacity. | Open |
| **C32 (new)** | TSMC CoWoS-L allocation analysis accepted Round 1, not delivered Round 2. | Major | Build wafer-share table for Apple / NVIDIA / AMD / Broadcom / hyperscalers in 2026–2027. | Open |
| **C33 (new)** | Supermicro accounting/governance overhang (Hindenburg, auditor change, 10-K delay, SEC) not stated. | Major | Add governance section; flag SEC status as of latest filing. | Open |
| **C34 (new)** | Aggregate $675B+ hyperscaler capex is itself a *bear* signal (capital cycle risk); Codex treats it only as bull demand. | Major | Add capital cycle / digestion-risk discussion to bear case. | Open |

---

## 8. Required Follow-Up Research

1. **Build the CPU $-per-rack table.** Round 3 must deliver: 2S Genoa baseline, 2S Granite Rapids, GB200 NVL72, MI300X HGX (Genoa host), Trainium 2 rack, TPU v5p pod. Without this, the entire memo is qualitative.
2. **Build the valuation snapshot.** P/E NTM, EV/EBITDA NTM, FCF yield, 2026/2027 consensus EPS for AMD, Intel, Arm, TSMC, Dell, SMCI, NVIDIA. Specify a disqualifying multiple for each.
3. **Paste verbatim transcript quotes** for Microsoft, Alphabet, Amazon, Meta 2026 capex. Cite page numbers.
4. **Estimate Arm royalty $ per server core** using disclosed royalty revenue, deployed core count, and Graviton/Cobalt unit estimates. Round 1 asked; Round 2 still pending.
5. **Add Ampere/SoftBank, IBM Power, MediaTek** to industry map and substitution analysis.
6. **TSMC CoWoS-L allocation analysis** for 2026 and 2027.
7. **Mercury Research Q4 2025 / Q1 2026 paid data** for AMD/Intel/Arm server CPU unit and revenue share. Settle whether AMD share gain is continuing or plateauing.
8. **Channel checks on K18** (CPU price hike rumor) via at least two distributors — kill or upgrade.
9. **Supermicro governance status** as of latest filing — SEC, auditor, 10-K timeliness.
10. **Capital cycle / digestion-risk model**: at $675B+ aggregate hyperscaler capex, what's the historical base rate for an air-pocket within 18 months?

---

## What Would Change My Mind (Round 3)

- **Quantified CPU $-per-rack table** showing absolute CPU $ rises across rack types → resolves F1, restores bull case viability.
- **Valuation snapshot with disqualifying levels specified** → makes "Qualified candidate" mean something.
- **Verbatim transcript quotes** for all four hyperscaler capex figures → upgrades K6/K15/K16 to truly High.
- **Mercury Q4 2025 share data** showing AMD share continuing >35% with stable ASP → AMD upgrade.
- **Arm royalty $/core within ±50% of a credible model** → Arm bull case becomes evaluable.
- **Intel 18A yield disclosure** → Intel from Qualified to Watchlist with a thesis.

If Round 3 fails to deliver the CPU $-per-rack table and a valuation framework, my position is that the bull thesis as currently constructed is **unfalsifiable** and should not be acted on as an investment recommendation regardless of how the labels are rearranged.

---

*Note on persistence: the local claim register file `cpu-investment-research-2/claims/claim_register.md` contains CDR-01 through CDR-16 from prior rounds, but Codex's K1–K18 and C19–C23 rows have not been written there. The orchestrator is failing to persist Codex's claim tables to the registry file. Same issue I flagged in Round 1 — still unfixed.*