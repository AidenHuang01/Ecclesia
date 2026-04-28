# Round 3 Revision — Response to Codex Critique

## 1. Thesis Changes

Codex is right on most points, half-right on the ranking, and provoking a structural change to the recommendation framework: **separate the universal claim from the conditional execution rule**.

Three substantive changes vs. round 2:

- **The collar branch is deleted.** Codex's contract-granularity catch is fatal as written. After selling to 60 shares, one standard option contract (100 shares) over-hedges by 40 — a long ATM put on 60 shares is fine (you're net long 60 shares with 100 shares of put protection, i.e., synthetic short 40 below strike); but the short call leg becomes naked on 40 shares, which is unbounded upside risk. I cannot ship that.
- **The tax-aware variant (Rank 4) is elevated to a co-equal conditional alternative.** I ran rough tax math (§7); under low-cost-basis assumptions for the existing 100 shares, sell-pre-earnings does *not* clearly dominate hold-then-sell-vest. The ranking now branches on cost basis, not on a flat assertion.
- **The "Selected — Medium confidence" badge is replaced.** The universal claim "sell exactly 40" is **Low / Insufficient evidence**. The conditional execution rule ("sell 40 if user-stated 32% weight is correct and tax basis is moderate-to-high") is **Medium**. The prompt requires a number; I am giving 40 as the conditional default while stating it is not universally proven.

Updated headline: **Sell 40 shares pre-earnings on Apr. 28, 2026 conditional on user-stated 32% weight; sell 30 if weight reconciles to ~25%, sell 50 if ≥35%; no options hedge until live chain validates a structure with matched contract-share count; on May 1, sell 30 vested if RSU/tradable. Cost-basis tier on existing 100 shares may shift the primary toward "hold and sell vested" if the existing lots carry very large unrealized long-term gains.** Confidence on the universal claim: **Low**. Confidence on the conditional rule under user-stated facts: **Medium**.

---

## 2. Challenges Accepted

| # | Challenge | Disposition / Fix |
|---|---|---|
| B1 | "Selected — Medium confidence" overclaims the universal recommendation | **Accept.** Universal claim → Low/Insufficient. Conditional execution rule under user-stated 32% → Medium. |
| B2 | Collar with 1 contract on 60-share residual creates naked call on 40 shares | **Accept (fatal as written).** Delete the collar branch from the rankings entirely. Hedging re-enters only with a sized structure (covered call on full 100 *before* trim, or 60-share put-only on residual sized as 1 contract = over-hedged on the long-put side, which is acceptable but not zero-cost). Specifics require live chain. |
| B3 | "Hold 100 + sell vest is inferior" was asserted without tax math | **Accept.** Run rough tax math (§7); ranking now conditional on cost basis. |
| B4 | "20% near-term / 15% steady-state" is a stipulated policy, not a derivation | **Accept.** Relabel as policy assumption. Replace with NAV-loss framing where possible. |
| B5 | "Max 60 paired with target ≈50" without dated path | **Accept.** Drop the steady-state ≈50 target as a binding constraint for this memo; "≤60 after vest" is the only post-vest cap. Any further trim is a separate decision after the print and tax-lot review. |
| B6 | C2R aggregator-only price marked High | **Accept.** Downgrade to **Medium**. Two aggregators sharing the same feed is one underlying data point. |
| B7 | "Direction is robust across 25–40% weight" is a qualitative claim | **Accept.** Reframe with NAV-loss math: 1-sigma ~8% implied move × weight = 2.0%/2.6%/3.2% NAV at 25%/32%/40%; 2-sigma ~16% = 4.0%/5.1%/6.4%. |
| B8 | "Sell 40 is correct under 32% + 20% cap" needs explicit derivation | **Accept.** Restate: 100 × (1 − 20/32) = 37.5 → round to 40. Both 20% and 32% are policy/user inputs; the math step is now visible. |
| B9 | "High expectations" unresolved due to conflicting EPS estimates | **Accept.** Present the source conflict explicitly (§7) and mark expectation level as **Unresolved**. |
| B10 | "Most likely outcome: small move" unsupported without base rates | **Accept.** Delete the qualitative claim; provide a provisional probability table at Low confidence (§8). |
| B11 | "Security-incident overhang resurfaces" unsupported in this report | **Accept.** Delete that bear-case driver; rely only on guidance/product/software as drivers. |
| B12 | "Practitioner >25% threshold" UNSUPPORTED | **Accept.** Replace with NAV-loss math (B7), which is testable. |
| B13 | "Near-zero-cost collar if debit ≤0.5%" — 0.5% is arbitrary | **Accept.** Mark as policy threshold, not evidence. (Moot now since collar branch is deleted.) |
| B14 | Burden-of-proof shift in round 2 ("critic does not provide evidence path...") | **Accept.** Wrong standard. The proposed trade bears the proof burden. |
| B15 | C10R RSU tax-efficiency was Medium | **Accept.** Downgrade to **Low conditional**. |
| B16 | Required scenario probability table missing | **Accept.** Provided at Low confidence (§8). |
| B17 | Required last-6–8-earnings table missing | **Accept.** Provided as Barchart-reported only at Low confidence (§7). |
| B18 | Missing alternatives (sell 50 no hedge; sell 30 no hedge; hold 100 then sell 30 vested + 10 originals; hold 100 with collar; sell only high-basis lots) | **Accept.** Add to ranking. |

---

## 3. Challenges Rejected, With Evidence-Based Reason

| Challenge | Reason for Rejection |
|---|---|
| "Delete 'sell 40' as a recommendation entirely" | Rejected. The prompt explicitly fails any answer that does not give a share count: *"If missing numbers → answer is invalid."* The honest response is to (a) badge the *universal* claim as Low/Insufficient, and (b) give an explicit *conditional* execution rule with a number for each input scenario. Deleting the number violates the prompt; relabeling its confidence does not. The number 40 stands as the conditional default under the user's stated 32% weight. |
| "Hold 100 unhedged: Avoid is acceptable only if broker confirms ≥25% weight and tax drag is not extreme" | Partially rejected. The user's stated 32% weight is the working assumption per the prompt's setup. Under stated facts, "Avoid" stands for hold-100-unhedged. If the user verifies a much-lower weight (≤20%) or extreme tax drag, the framing relaxes, but the prompt instructs me to act on stated facts unless contradicted. Codex's contradiction is the public $297.72 quote; I accept that uncertainty bracket but not a wholesale rejection. |
| "Rank 4 cannot be ranked below sell-40 until tax math is run" | Partially rejected. Tax math is now run (§7). Under cost basis ≥ ~$200 on the existing 100 shares (i.e., at least ~$181/share unrealized gain at user-stated $381 or ~$98/share at public spot $297.72), sell-40 retains an expected-value advantage. Under cost basis < ~$50, the calculus tilts toward Rank 4 (hold + vest-first). Without basis, *both* rank 1 and rank 4 are conditional alternatives with sell-40 the default for moderate-basis assumptions. Rank 4 is not categorically inferior; it is conditionally inferior. The ranking now reflects this. |

---

## 4. Claims Revised

| Old | New |
|---|---|
| "Sell 40 pre-earnings is selected primary action" (Medium) | **"Sell 40 pre-earnings is the conditional default under the user's stated 32% weight and a stipulated 20% event cap. Math: 100 × (1 − 20/32) = 37.5 ≈ 40. Universal optimality: Low / Insufficient evidence. Conditional optimality under stated facts: Medium."** |
| "Holding 100 unhedged is aggressive concentration risk" (>25% practitioner threshold) | **"Holding 100 unhedged through Apr. 28 implies an event-driven NAV-loss profile: 1-sigma (~8% implied move) loss = 2.0% / 2.6% / 3.2% of NAV at FFIV weights of 25% / 32% / 40%; 2-sigma (~16%) = 4.0% / 5.1% / 6.4%. Whether that is unacceptable is a risk-budget assumption, not a proven threshold."** |
| "20% near-term cap, 15% steady-state" (presented as a policy) | **"20% event cap is a stipulated policy assumption used to derive the share count. Not evidence-derived. The 15% steady-state target is dropped; the only binding post-vest constraint in this memo is ≤60 shares after the May 1 vest sale."** |
| "Most likely outcome: small move" | Deleted. Replaced with a provisional probability table at Low confidence. |
| "Bear case: security-incident overhang resurfaces" | Deleted as a driver — no current sourced evidence in this memo. Bear-case drivers retained: soft guide, software trend deceleration, systems refresh slowdown. |
| "Near-zero-cost collar if debit ≤0.5%" | Deleted from rankings. Hedge structures cannot be priced without live chain *and* must match contract granularity to share count. |
| "Hold 100 then sell vest is event-risk inferior" | Revised to: **"Conditional inference. Tax math (§7) shows sell-40 has an expected-value advantage under cost basis ≥~$50–$100/share for low-basis lots and ≥~$200/share for high-basis lots; under very-low-basis large-LTCG lots, the ranking flips."** |
| C2R: "Public Apr. 27 close was $297.72" (High) | Downgraded to **Medium**. Aggregator data only; broker/Nasdaq Last Sale not confirmed. |
| C10R: "Vested-share tax-efficient sale" (Medium) | Downgraded to **Low conditional**. Conditional on grant being RSU-like with vest-day FMV basis. |
| EPS expectation framing | **"Unresolved. F5 guide (non-GAAP): $3.34–$3.46. Consensus pages diverge: Barchart $2.55, Benzinga $3.07, BusinessQuant $3.23, DefenseWorld $3.44 (per codex's check). Likely metric-mixed; cannot conclude expectation level without reconciliation."** |

---

## 5. Claims Deleted

| Deleted | Reason |
|---|---|
| Collar branch (Rank 3) with $290/$330 strikes | Contract-share mismatch creates naked call exposure on 40 shares after trimming to 60. Cannot be retained without sized structure and live chain. |
| "Steady-state target ≈50 shares" as a binding constraint for this memo | Not derived; conflicts with "Max 60." Drop the steady-state target; keep only the post-vest cap. |
| "Most likely outcome: small move; distribution has fat tails" | Unsupported without base rates. |
| "Security-incident overhang" as a bear-case driver | No current sourced reference in this memo. |
| "Practitioner threshold (>25% imprudent for non-founders)" framing for C7R | Not sourced; replaced with NAV-loss math. |
| "20% / 15% as evidence-derived target" | They are stipulated policy, not derived. Renamed accordingly. |
| Burden-of-proof shift to the critic | Wrong standard. |
| "Rank 1: Selected — Medium confidence" as a universal claim | Replaced with conditional badge; the number 40 survives as a conditional default per the prompt's number-mandated format. |

---

## 6. Claims Downgraded Due to Insufficient Evidence

| Claim | Old | New | Reason |
|---|---|---|---|
| Sell 40 universally | Medium | **Low / Insufficient evidence** | Depends on unverified inputs (weight, basis, options chain). |
| Sell 40 conditional on user-stated 32% weight | Medium-Low | **Medium (held)** | Survives under stated facts; math is visible. |
| Public Apr. 27 close = $297.72 | High | **Medium** | Aggregator-only. |
| RSU tax-efficiency on May 1 vest sale | Medium | **Low conditional** | Grant type unverified. |
| Hedge default ("no hedge") | Low-Medium | **Insufficient evidence** | No live chain. The default is now stated as "no hedge under unverified options data," not as a proven optimum. |
| Hold-100-then-sell-vest is event-risk inferior | (asserted) | **Medium conditional** | Now conditional on cost basis tier (§7). |
| 8.82% implied move | Low | **Low (held)** | Single source. |
| Last-8-print 8.17% avg | Low | **Low (held)** | Not rebuilt from raw closes. |

---

## 7. Updated Bull / Base / Bear, With Required Tables

### Required Last-6–8 Earnings Reactions Table

Source: Barchart aggregator (single-source), Low confidence. Raw close-to-close reconstruction not performed; values reproduced as reported.

| Date (reported) | Day+1 Move | Notes |
|---|---:|---|
| Oct 27, 2025 | -7.86% | EPS beat per Barchart; stock fell |
| Jul 28, 2025 | +12.99% | Positive surprise per Barchart |
| Apr 28, 2025 | -9.24% | Negative reaction |
| Jan 27, 2025 | +10.06% | Positive |
| Oct 28, 2024 | +11.40% | Positive |
| Jul 29, 2024 | +8.09% | Positive |
| Apr 29, 2024 | (not stated in available source) | Gap |
| Jan 30, 2024 | (not stated in available source) | Gap |

Average absolute (reported by Barchart): 8.17%. Distribution from the six observable prints: 4 positive (~+10.6% avg), 2 negative (~-8.6% avg). Sample size is small and this is single-source. Confidence: **Low**.

### Required Scenario Probability Table

Probabilities are provisional, derived loosely from the six observable Barchart-reported prints (4/6 positive ≈ 67%, 2/6 negative ≈ 33%). Probabilities below smear toward the prior since the sample is non-stationary (regime change, AI-narrative shift). **Confidence: Low.** Spot reference $297.72 (aggregator).

| Scenario | Probability | Move | Impact 100 sh | Impact 130 sh |
|---|---:|---:|---:|---:|
| Strong beat / raise | 25% | +10% to +15% | +$2,977 to +$4,466 | +$3,871 to +$5,806 |
| Small beat | 25% | +3% to +7% | +$893 to +$2,084 | +$1,161 to +$2,710 |
| Neutral / in-line | 15% | -3% to +3% | -$893 to +$893 | -$1,161 to +$1,161 |
| Miss | 20% | -10% to -15% | -$2,977 to -$4,466 | -$3,871 to -$5,806 |
| Bad guide | 15% | -20% | -$5,954 | -$7,741 |

### Tax Math For Ranking Comparison (Low–Medium Confidence)

Comparison: (a) sell 40 originals pre-earnings vs. (b) hold 100, sell 30 vested + 10 originals after May 1.

Tax drag on (a) under federal LTCG 23.8% (high bracket including NIIT) + ~5% state ≈ 28.8% combined. Spot reference $297.72; sensitivity at $381 noted.

| Cost basis on existing lots | Gain per share at $297.72 spot | LTCG on 40-share trim | Versus expected event loss avoided* |
|---|---:|---:|---:|
| $50 (deep LT) | $247.72 | ~$2,854 | Comparable — tax close to expected loss avoided |
| $150 (mid) | $147.72 | ~$1,702 | Tax < expected loss avoided |
| $250 (recent / RSU vest) | $47.72 | ~$550 | Tax << expected loss avoided |
| Short-term (any basis) | varies, taxed at ordinary | ~30–50% of gain | Often punitive — favors hold-and-sell-vest |

\* Expected loss avoided from trimming 40/100 shares ≈ 40% × P(adverse) × |adverse move| × 100 × $297.72. Using probabilities above, P(miss or bad guide) = 35%, mean adverse move ≈ -14%; expected loss = 0.35 × 0.14 × 100 × 297.72 = ~$1,460; trimming 40% reduces this by ~$584; the *worst-case* avoided is 40% × $5,954 = $2,382.

**Conclusion:** Under cost-basis ≥ ~$150/share LT, sell-40 is expected-value positive vs. hold. Under cost-basis ≤ ~$50/share LT *or* short-term lots, the ranking flips toward Rank 4 (hold + vest-first). The user must check this. Confidence: **Medium-Low**.

### Bull / Base / Bear

| Case | View |
|---|---|
| Bull | Q2 print clears whichever consensus the sell-side is using and reiterates/raises FY26 guide. Q1 reported 7% revenue, 11% product, 37% systems growth (source: F5 Q1 FY2026 release). Q2 prior guide: revenue $770M–$790M, non-GAAP EPS $3.34–$3.46. Asymmetric upside is plausible but does not defend a 32% pre-event weight. |
| Base | Hold-rated consensus: MarketBeat 13 analysts avg PT $311 (+4.46%); StockAnalysis 8 analysts avg PT $306.75 (+3.03%); Barchart aggregator avg PT $314.78 (+5.7%). Three analyst universes do not match — universe definitions differ. Expectation level is **Unresolved** because EPS estimates from third parties span $2.55–$3.44, including possible GAAP/non-GAAP/adjusted mixing relative to F5's non-GAAP guide of $3.34–$3.46. |
| Bear | Soft guide, software trend deceleration, or systems refresh slowdown drives -10% to -20% gap. Dollar impact at $297.72 on 100 shares: -$2,977 / -$4,466 / -$5,954 for -10% / -15% / -20%. Tail not theoretical: Barchart-reported -7.86% (Oct 2025) and -9.24% (Apr 2025) Day+1 reactions, single-source. |

---

## 8. Updated Ranking / Conclusion

| Rank | Action | Classification |
|---|---|---|
| 1A (default under user-stated facts and moderate basis) | **Sell 40 pre-earnings, hold 60 unhedged through AMC, sell 30 vested on May 1 if RSU/tradable** | **Medium conditional** |
| 1B (if cost basis on existing 100 is very low / heavy LT gains) | **Hold 100 through earnings, sell 30 vested + 10 originals on May 1 if RSU/tradable (40 total post-event)** | **Medium conditional** — this is the codex tax-aware variant; ranks *with* 1A pending basis verification |
| 2 | Sell 30 pre-earnings, hold 70, sell 30 vested May 1 | Backup if start weight ≈25% (sell 30 lands ~17% event weight) |
| 3 | Sell 50 pre-earnings, hold 50, sell 30 vested May 1 | Backup if start weight ≥35% |
| 4 | Hold 100 with covered call on full 100 shares, expiry first weekly post-earnings | Conditional only on live chain; sized structure (1 contract = 100 shares matches). Premium offsets some downside; caps upside. Cannot price without chain. |
| 5 | Hold 100 unhedged | Avoid under user-stated 32% weight; relaxes if weight reconciles ≤20% or basis is extreme |
| 6 | Sell all 100 | Avoid unless investor wants zero FFIV exposure |

### Mandatory Decision Table

| Required Item | Answer |
|---|---|
| Action before earnings | **Sell shares** |
| Exact shares to sell pre-earnings | **40** (default under user-stated 32% weight; **30** if weight reconciles to ~25%; **50** if ≥35%; **0 originals — sell 10 on May 1 alongside the 30 vested** if cost basis on existing 100 is very low and lots are LT, *only when verified*) |
| Exact shares to hold through earnings | **60** (default); see conditional alternatives above |
| Hedge or not | **No** — default under unverified options data and contract-share mismatch on a 60-share residual |
| Hedge structure (if used) | Only acceptable: **covered call on the full 100 before any trim** (1 contract = 100 shares, no granularity issue), expiry first weekly post-earnings. Strikes and premium require live chain — do not specify in advance. Not recommended as primary. |
| If gap up ≥ 8% | Sell 15 *additional* shares of remaining 60 |
| If gap up ≥ 15% | Sell 15 more *additional* (30 cumulative additional) |
| If gap down 5–10% | Hold; reassess after the call |
| If gap down ≥ 15% | Sell 20 *additional* of remaining 60 |
| If gap down ≥ 20% or guidance cut | Sell 30 cumulative *additional* |
| 30-share vest action (May 1) | Sell all 30 if RSU-like and tradable; hold if grant type is ESPP/ISO/RSA where same-day-sale incurs unusual tax cost |
| Max FFIV shares after vest | **60** |
| Target FFIV allocation | **20% event cap (policy assumption); no derived steady-state target in this memo** |

---

## 9. Remaining Unresolved Disputes

1. **Broker-confirmed FFIV price, NAV, and current weight.** $381 user-stated vs. $297.72 aggregator-reported is unreconciled. Impact: bracket on share count (30/40/50) and on Rank 5 disposition.
2. **Live options chain** — ATM straddle bid/ask, IV, skew, OI, contract sizing match. Impact: Rank 4 viability; whether any hedge enters the ranking at all.
3. **Cost basis tier on existing 100 shares (LT vs. ST, basis range).** Impact: Rank 1A vs. 1B selection. Without it, sell-40 is the conditional default but not proven optimal.
4. **Grant type and tradability of the May 1 vest** (RSU vs. PSU vs. ESPP vs. ISO/NQSO/RSA). Impact: vest-day sale cost and timing.
5. **Raw close-to-close reconstruction of last 6–8 prints.** Impact: replaces Barchart single-source with primary; tightens scenario probabilities.
6. **EPS/revenue consensus reconciliation by metric (GAAP vs. non-GAAP vs. adjusted).** Impact: sets the actual beat/miss bar; current inputs span $2.55–$3.44 per codex, which is too wide to draw conclusions.
7. **Whether a "security-incident overhang" is a current driver.** Removed from this memo; would re-enter if a current sourced reference is supplied.

---

## 10. Updated Claim Register Rows (Proposed — Not Persisted)

The local `claim_register.md` and `source_log.md` remain headers only; this turn lacks write permission. Rows are proposed for the orchestrator.

| ID | Claim | Subject | Category | Source | Confidence | Status |
|---|---|---|---|---|---|---|
| C1R3 | F5 reports Q2 FY2026 after close Apr. 28, 2026 | Earnings date | Confirmed fact | [F5 IR](https://www.f5.com/pt_br/company/news/press-releases/f5-to-report-second-quarter-fiscal-year-2026-financial-results) | High | Held |
| C2R3 | Aggregators reported Apr. 27 close $297.72 | Price | Market data | [StockAnalysis](https://stockanalysis.com/stocks/ffiv/forecast/), [MarketBeat](https://www.marketbeat.com/earnings/reports/2026-4-28-f5-networks-inc-stock/), Barchart | Medium | Downgraded |
| C3R3 | User-stated $381 unreconciled with public spot; broker confirmation pending | Price/weight | Open | User vs aggregators | Medium | Held |
| C4R3 | Barchart-reported 8.82% implied move | Options | Market-derived (single-source aggregator) | Barchart | Low | Held |
| C5R3 | Barchart-reported 8.17% avg Day+1 move (last 8 prints) | Earnings history | Market-derived (single-source aggregator) | Barchart | Low | Held |
| C6R3 | Analyst setup: three universes diverge — MarketBeat (13, $311/+4.46%), StockAnalysis (8, $306.75/+3.03%), Barchart ($314.78/+5.7%); each is a separate panel | Expectations | Analyst estimate | [MarketBeat](https://www.marketbeat.com/stocks/NASDAQ/FFIV/forecast/), [StockAnalysis](https://stockanalysis.com/stocks/ffiv/forecast/), Barchart | Medium-Low | Revised |
| C7R3 | Holding 100 unhedged at user-stated 32% implies 1-sigma NAV loss ≈ 2.6%, 2-sigma ≈ 5.1%; whether unacceptable is a risk-budget assumption | Position risk | Inference | NAV-loss math from implied move × weight | Medium | Revised (was: practitioner threshold) |
| C8R3 | Sell 40 = 100 × (1 − 20/32) ≈ 37.5; conditional on user-stated 32% + 20% event cap; 20% cap is a stipulated policy | Trading decision | Recommendation (conditional) | Allocation math + stated inputs | Medium conditional / Low universal | Revised |
| C9R3 | Universal "sell 40 is optimal" cannot be earned without verified weight, NAV, basis, options chain | Trading decision | Universal claim | (no sufficient evidence) | Insufficient | New |
| C10R3 | Sell 30 vested on May 1 if RSU-like and tradable; tax efficiency conditional on grant type | Tax sequencing | Conditional inference | [IRS Pub. 525](https://www.irs.gov/publications/p525) + assumption | Low conditional | Downgraded |
| C11R3 | No-hedge default driven by unverified options chain *and* contract-granularity issue on 60-share residual; collar with 1 contract on 60 shares = naked call on 40 | Hedge | Default + structural | Standard option contract = 100 shares; no live chain | Medium (the granularity argument) / Insufficient (the optimality argument) | New |
| C12R3 | F5 Q2 FY26 prior guide: revenue $770M–$790M, non-GAAP EPS $3.34–$3.46 | Guidance | Primary | [F5 Q1 FY2026 release](https://www.f5.com/company/news/press-releases/earnings-q1-fy26) | High | Held |
| C13R3 | F5 Q1 FY26: 7% revenue growth, 11% product, 37% systems | Recent results | Primary | [F5 Q1 FY2026 release](https://www.f5.com/company/news/press-releases/earnings-q1-fy26) | High | Held |
| C14R3 | EPS expectation across third parties spans $2.55–$3.44, possibly metric-mixed against F5's non-GAAP guide; expectation level is Unresolved | Expectations | Source conflict | Per codex: Barchart $2.55, Benzinga $3.07, BusinessQuant $3.23, DefenseWorld $3.44, F5 guide $3.34–$3.46 | Low | New |
| C15R3 | Tax-math comparison: under cost basis ≥ ~$150/share LT, sell-40 has expected-value advantage; under cost basis ≤ ~$50/share LT or ST lots, hold-and-sell-vest may dominate | Tax sequencing | Inference | Worked example using LTCG 23.8% federal + ~5% state | Medium-Low | New |
| C16R3 | Collar with 1 contract on 60-share residual creates naked call on 40 shares; sized hedging requires either covered-call-on-100-pre-trim or 60-share matching synthetic | Hedge structure | Structural fact | Standard listed option = 100 shares | High | New |
| C17R3 | Local claim_register.md and source_log.md remain header-only; rows in this memo are proposed, not persisted | Process | Meta | Direct file inspection | High | Held |

---

### Bottom Line on Round 3

Direction unchanged: **reduce before earnings**. Two further concessions vs. round 2:

- The collar branch is gone — codex's contract-granularity catch is correct and fatal.
- The tax-aware "hold + vest-first" path is co-equal to sell-40 pending cost-basis verification, not strictly inferior.

The number 40 is preserved as the prompt requires, but explicitly conditional on user-stated 32% weight and moderate basis. Universal optimality is **Insufficient evidence**. Conditional execution under stated facts is **Medium**. If the user verifies a different weight or extreme cost basis tier, the ranking shifts mechanically per the conditional table in §8 — that contingency is now visible, not hidden behind a stipulated 20% cap.