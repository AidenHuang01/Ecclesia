# Independent Research Memo — FFIV Pre-Earnings Decision (Skeptical Track)

**Author role:** Skeptical researcher (correction-seeking)
**Date of memo:** April 27, 2026 (per prompt context)
**Critical caveat up front:** My training cutoff is January 2026. I cannot verify late-April 2026 primary-source data (live FFIV price, current IV, the April 28, 2026 earnings date, analyst consensus, recent prints). Every datum from the prompt — $381 price, ~32% weight, the April 28 AMC release, the 30-share May 1 vest — is treated as **input assumption from the user, UNSUPPORTED by my own primary verification**. I will still produce a concrete recommendation because the concentration math forces it independent of the unverifiable data points.

---

## 1. Executive Thesis

**Sell 40 shares pre-earnings tomorrow morning. Hedge the remaining 60 with a single ATM/slightly-OTM protective put expiring 5/15 (or nearest weekly post-earnings). After the 5/1 vest, sell ~40 of the newly-vested 30 + remaining inventory down to a 50-share core. Target allocation: 12–15% of portfolio.**

The decision is driven by **concentration risk**, not by an earnings forecast. Anyone who tells you to hold 32% (going to ~40%) of a portfolio in a single mid-cap tech name through a binary catalyst is wrong on risk-management grounds, regardless of how bullish the thesis is. The "default bias" in the prompt is correct, and the burden of proof for holding has not been met by anything verifiable.

**Classification: Avoid (the act of holding the full position through earnings).**

---

## 2. Scope and Definitions

- **Decision horizon:** ~16 trading hours (open April 28 → close April 28 before AMC release).
- **Action set:** sell, hedge, hold, partial combinations.
- **What this memo is not:** a fundamental view on F5 Inc. (FFIV). I take no strong stance on whether FFIV is a good 3-year hold. I take a strong stance against the *position structure* through this specific event.
- **Portfolio math (derived):** If $38,108 = 32%, total portfolio ≈ **$119,100**. Post-vest, FFIV ≈ $49,538 of ~$130,500 total ≈ **38%** (prompt says 40%+, close enough — likely rounding or assumes some appreciation).

---

## 3. Research Universe / Options Considered

| Option | Description | Considered? |
|---|---|---|
| A. Hold all 100 | Do nothing | Yes — rejected |
| B. Sell 10–20 | Token trim | Yes — rejected as insufficient |
| C. Sell 25–40 | Meaningful de-risk | **Selected** |
| D. Sell 50+ | Aggressive cut | Yes — viable backup |
| E. Sell 100 (full exit pre-earnings) | Maximally defensive | Considered — rejected (gives up upside entirely with no hedge cost) |
| F. Buy puts only, hold all 100 | Pure hedge | Considered — too expensive at high IV |
| G. Collar (sell calls + buy puts) | Cost-reduced hedge | Considered — viable secondary |
| H. Sell + partial hedge | Combo (selected) | **Selected** |
| I. Wait until after earnings | Defer decision | Rejected — this is "do nothing" rebranded |

---

## 4. Evidence Map

| Evidence Category | Available to me? | Quality |
|---|---|---|
| Concentration math | Yes (from prompt inputs) | High — arithmetic |
| FFIV historical earnings behavior (long-run) | Partial — pre-2026 only | Medium |
| FFIV ~April 2026 price action | **No** | None — flag as gap |
| Current IV / implied move | **No** | None — flag as gap |
| Analyst consensus for this print | **No** | None — flag as gap |
| FFIV business fundamentals (general) | Yes — through cutoff | Medium |
| Behavioral / risk-management theory on concentration | Yes | High |

The evidence base is **lopsided**: strong for the structural argument (concentration), weak for the tactical argument (whether this specific print is bullish or bearish). That asymmetry is itself an argument for a structural rather than tactical action.

---

## 5. Key Facts and Sources

| # | Fact | Source | Confidence |
|---|---|---|---|
| F1 | FFIV is F5 Inc., application delivery / app-security vendor, mid-cap | General knowledge through Jan 2026 | High |
| F2 | FFIV historically has had volatile earnings reactions; single-day moves of 5–15% are not unusual | Historical pattern through cutoff | Medium |
| F3 | FFIV reports quarterly; fiscal year ends September; "April 2026" report would be Q2 FY26 | General | Medium |
| F4 | Current price $381, position 100 shares, ~32% weight | **Prompt — UNSUPPORTED by independent source** | Treat as given |
| F5 | Earnings April 28, 2026 AMC | **Prompt — UNSUPPORTED** | Treat as given |
| F6 | 30-share vest May 1, 2026 | **Prompt — UNSUPPORTED** | Treat as given |
| F7 | No insider-trading restrictions on user | **Prompt — user assertion** | Accept per instructions |
| F8 | Standard wealth-management guidance: single-stock concentration over 10–15% is high-risk; over 25% is widely considered imprudent for non-founders | Common practitioner guidance (e.g., Vanguard, Fidelity educational materials, generally) | High as norm, not law |

I do **not** have verified data on:
- Current 1-week / 1-month / 3-month price moves
- Pre-earnings run-up magnitude
- Implied move from straddle pricing
- Put/call skew
- Analyst revisions in the last 30 days

These are flagged in §12.

---

## 6. Main Drivers / Causal Mechanisms

**The decision turns on three things, in this order of importance:**

1. **Concentration × binary event = unacceptable variance.** A 32% single-name position experiencing a 1-sigma earnings move (call it ±8% as a placeholder for a name with FFIV's profile) implies portfolio volatility of ~2.6% in a single overnight session. A 2-sigma adverse move (~-15%) implies ~-4.8% portfolio drawdown from one stock, one event. This is the dominant mechanism.

2. **Asymmetry of regret.** If you sell 40 shares and stock rips +15%, opportunity cost ≈ $2,290 (~1.9% of portfolio). If you hold all 100 and stock drops -15%, realized loss ≈ $5,720 (~4.8% of portfolio). The pain-of-loss vs forgone-gain asymmetry favors trimming, even at 50/50 odds — and especially because **employment income is also FFIV-correlated** (the user is an FFIV employee).

3. **Vest amplifies, doesn't dilute, the problem.** The 30-share vest 3 days after earnings is *additional FFIV exposure landing into an already-overweight book.* It is not a reason to hold; it is a reason to sell more, sooner, since you'll be re-loaded automatically.

---

## 7. Counterarguments and Disconfirming Evidence

I am required to look for what would invalidate the "trim" recommendation. Honest list:

- **Counter 1: "FFIV has guided conservatively recently and beat handily."** If true, IV may underprice the upside. *Response:* I don't have the data to confirm, and even a beat doesn't always rally the stock if the run-up has already priced it in. This counter cannot overcome concentration math.
- **Counter 2: "Tax cost of selling lots is high."** Plausible — if shares were acquired cheaply (likely for an employee via ESPP/RSU), capital gains tax could materially erode the trim. *Response:* Real, but quantifiable separately. A 20% federal LTCG + state on a $381 - $X cost basis × 40 shares is at most a few thousand dollars; concentration drawdown risk dwarfs this. Still, it is the **strongest single counterargument** and I flag it as a gap (§12).
- **Counter 3: "Implied move is small (e.g., 4%) so risk is low."** *Response:* Implied move is the market's *expected* move; realized moves break above implied ~30–40% of the time historically across single-name earnings. Cannot rely on small implied move to justify carrying 32%.
- **Counter 4: "Stock has been weak into print, sentiment washed out."** Possible. *Response:* I can't verify, but even a "washed out" setup is not a reason to carry 32%. It might shift the trim from 40 shares to 30, not eliminate it.
- **Counter 5: "Selling employer stock signals lack of confidence."** Irrelevant for a lower-level employee with no public disclosure obligation.

**None of these counters touch the concentration math, which is the load-bearing argument.**

---

## 8. Bull Case / Strongest Positive Interpretation

The cleanest pro-hold argument:

> FFIV is in an AI-infrastructure-adjacent product cycle (application delivery + security for AI workloads). If management raises guidance materially, the stock can re-rate. A 32% position rallying 15% adds ~4.8% to the portfolio. If the user has high conviction in management and product, taking a path with 50%+ asymmetric upside justifies the variance.

**Why I don't buy this as decisive:** "High conviction" is exactly the rationalization that destroys concentrated portfolios. Employees of public companies systematically overweight conviction in their employer (familiarity bias, halo effect). The bull case is *plausible*; it does not overcome the variance objection. It justifies *holding some*, not *holding 100*.

---

## 9. Bear Case / Strongest Negative Interpretation

> FFIV is a legacy hardware vendor in slow transition to software/subscription. Networking/security has had several recent disappointments in the broader peer set. A guide-down or soft Q3 outlook could produce a -15 to -20% gap. At 32% weight, that is a -5% to -6.5% portfolio hit in one session, plus pressure on RSU compensation value, plus possible secondary effects on employment outlook. Concentration risk and human-capital risk compound.

**This is the case I weight more heavily** because it captures the joint distribution of stock and employment outcomes — which the bull case typically ignores.

---

## 10. Base Case / Most Likely Interpretation

Without verifiable IV or analyst data, my base case must be probability-weighted broadly:

| Scenario | Prob (my prior) | Stock Move | P&L on 100 sh | P&L on 130 sh |
|---|---|---|---|---|
| Strong beat + raise | 20% | +10% | +$3,810 | +$4,953 |
| Modest beat, in-line guide | 30% | +3% | +$1,143 | +$1,486 |
| Neutral / mixed | 20% | 0% | $0 | $0 |
| Soft guide | 20% | -8% | -$3,048 | -$3,963 |
| Miss + bad guide | 10% | -18% | -$6,858 | -$8,917 |

Expected value: ~+0.4% on the position. Standard deviation: ~7.5%. **The expected value is small, the variance is large, the position is huge** — textbook case for risk reduction. These probabilities are my own priors and should be treated as **Low confidence**, but the *shape* (low EV, high variance) is robust to reasonable reweighting.

I deliberately included a -10% / -15% / -20% leg per the prompt's requirement: a -15% move on 100 shares = -$5,715; on 130 shares = -$7,430; -20% on 130 = -$9,906 (~7.6% of total portfolio from one event).

---

## 11. Key Claims Table

| ID | Claim | Subject | Category | Source | Confidence | Status |
|---|---|---|---|---|---|---|
| C1 | Holding 32% in a single name through earnings is imprudent risk management | Risk theory | Assumption + practitioner consensus | General financial guidance | High | Open |
| C2 | Post-vest weight rises to ~38–40% absent action | Portfolio math | Confirmed (arithmetic) | Prompt inputs | High | Confirmed (given inputs) |
| C3 | FFIV typically moves 5–15% on earnings | FFIV history | Historical | Pre-2026 record | Medium | Open — needs latest 6–8 quarters verified |
| C4 | Current price ≈ $381 | Market data | Primary fact | Prompt | Unknown to me | UNSUPPORTED by independent source |
| C5 | Implied move (straddle) is X% | Options market | Market data | Not available | Unknown | **GAP — must verify** |
| C6 | Analyst consensus is Y EPS / Z revenue | Expectations | Estimate | Not available | Unknown | **GAP — must verify** |
| C7 | Pre-earnings run-up has occurred | Price action | Estimate | Not available | Unknown | **GAP — must verify** |
| C8 | Tax cost of trimming is material | User-specific | Assumption | Unknown cost basis | Unknown | **GAP — must verify** |
| C9 | Employee status correlates personal income with FFIV | Human capital | Logical | User input | High | Confirmed |
| C10 | Default action should be reduce | Decision rule | Reasoned | Prompt + analysis | High | Confirmed |
| C11 | Average single-day FFIV earnings reaction has historically been < 10% | FFIV history | Historical | Pre-2026 record | Medium | Open |
| C12 | Hedging via puts is more expensive than usual into print | Options pricing | General | Standard IV term-structure behavior | High as norm | Open |

---

## 12. Evidence Gaps (What I'd Need to Tighten This)

1. **Current FFIV implied move from ATM straddle pricing for the closest weekly expiry post-earnings.** This is the single most important missing datapoint. If implied move is <4%, hedging is cheap and changes the recommendation toward "hold + buy puts" with smaller share sale. If >7%, hedging is expensive and the recommendation tilts further toward outright selling.
2. **Last 6–8 quarters of FFIV next-day reactions** with EPS/rev/guidance details.
3. **30-day analyst revision trend.** Are estimates rising or falling into the print?
4. **1-month and 3-month price action** to assess pre-earnings run-up.
5. **User's cost basis** to estimate tax drag on the sell decision.
6. **Total portfolio composition** to determine target allocation precisely (currently I'm assuming a generalist diversified book).
7. **Whether the 30 vesting shares are RSUs (taxed as ordinary income at vest, basis = vest-day price) or ISOs/NQSOs.** This affects whether selling vested shares immediately incurs incremental tax.

---

## 13. Initial Classification / Ranking

| Action | Rank | Verdict |
|---|---|---|
| Hold all 100 through earnings | Worst | **Avoid** |
| Sell 10–20 (token trim) | 2nd worst | Insufficient |
| Sell 25–40 + light hedge on remainder | **Best** | **Selected** |
| Sell 50+ outright | 2nd best | Backup |
| Buy puts only, hold all 100 | Mid | Too expensive at typical pre-print IV |
| Wait until after earnings | Equivalent to "hold all 100" | Avoid |

---

## 14. Mandatory Trading Recommendation

| Required Item | Answer |
|---|---|
| Action before earnings | **Sell 40 shares + buy 1 protective put on remaining 60** |
| Exact shares to sell pre-earnings | **40** |
| Exact shares to hold through earnings | **60** |
| Hedge or not | **Yes** |
| Hedge structure | **Buy 1 contract of FFIV $375 put (or nearest strike ~1–2% OTM), expiry first weekly post-earnings (≈May 1 or May 8). If IV makes premium > $9 (~2.4% of spot), substitute a $370/$340 put spread instead.** |
| If gap up > +6%: action | **Sell 20 more shares at the open. If > +12%, sell 30 more.** |
| If gap down: action | **If -6% to -12%: hold remaining 60 (do not panic; the put offsets). If > -15%: do not sell more, let the put work; reassess after the day's range settles. The put is precisely there to prevent forced selling at the worst price.** |
| What to do with 30-share vest | **Sell 25 of the 30 vested shares within 1 trading day of vest (5/1 or 5/4), regardless of post-earnings price (subject to a same-day-sale tax wash if RSU). Keep 5.** |
| Max acceptable shares after vest | **65 shares** (60 held through + 5 from vest). |
| Target FFIV allocation | **12–15% of portfolio** (≈$15K–$18K, ≈40–47 shares at $381). The 65-share target is a near-term landing; further trimming to ~45 shares over the next 1–2 months is the steady-state goal. |

---

## Post-Earnings Plan

| Scenario | Action | Reason |
|---|---|---|
| Gap up > +12% | Sell 30 of remaining 60 at open. Let put expire. | Lock in windfall; concentration math doesn't change just because the stock went up. |
| Gap up +6% to +12% | Sell 20 of 60. | Trim the gain; reduce concentration. |
| Gap up 0% to +6% | Sell 10 of 60. | Modest de-risk; protect against post-earnings drift lower. |
| Flat to -6% | Hold 60. Sell put if it has retained value. | Move on; resume scheduled trim post-vest. |
| -6% to -15% | Hold 60. Put offsets most of the loss. | Don't sell into weakness without the hedge having paid out. |
| Worse than -15% | Hold 60, exercise/sell put for max value. Reassess after 24 hours. | Avoid forced selling at the gap-low; the put was bought for exactly this. |

---

## Adversarial Self-Audit (Required by Debate Rules)

I am required to attack weak reasoning, including my own. Things I am attacking:

- **"Just hold and see"** — rejected. There is no information arriving overnight that the user will have but the market won't. "Wait and see" is a euphemism for "I'm scared to choose."
- **"Company is good so hold"** — rejected. Quality of company is a long-horizon argument; binary event risk is short-horizon. They are different problems.
- **"32% is fine because it's grown there organically"** — rejected. Path-dependent rationalization. If you wouldn't *buy* 32% today, you shouldn't *hold* 32% today.
- **"Vest is small relative to position"** — rejected. 30 shares at $381 = $11,430 = ~9% of portfolio incoming. That's not small.
- **My own recommendation's weakest point:** I am recommending a specific put strike and expiry without verified IV data. The structure is *directionally correct* (sell some + hedge some) but the exact strike/expiry must be sized against actual quoted premiums tomorrow morning. If the put costs more than ~2.5% of spot, switch to a put spread or simply sell more shares (an additional 10–15) instead of paying for the hedge.

---

## Final Classification

**Avoid** — referring to the action of *holding the full 100-share position unhedged through the April 28 print*.

The selected action (sell 40 + hedge 60, then trim post-vest to ~65, then to ~45) is the recommendation. The recommendation's directional structure is **High confidence**. The exact share counts are **Medium confidence** (could reasonably range from sell-30 to sell-50 depending on verified tax basis and IV). The post-earnings triggers are **Medium confidence**.

The recommendation's robustness comes from the fact that **even if every unverifiable claim in the prompt is wrong by a moderate amount, the concentration argument still selects the same action.** That is the tell that this is a structural decision masquerading as a tactical one — and structural decisions deserve structural answers, not "wait and see."