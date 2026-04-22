# Experiment: Is the "Higher Tier = Better AVP" Pattern Universal?
**Status**: 🧪 draft
**Date**: 2026-04-22
**Module**: 5 (Trait Breakpoints — follow-up)

## The Question

The [[experiments/2026-04-22-trait-breakpoint-multi-comp]] experiment found that 3 traits (N.O.V.A., Dark Star, Summon) all showed better AVP at higher trait tiers, and attributed this to **selection bias** — stronger boards naturally reach higher tiers.

But 3 traits is a small sample. Is this "universal improvement" pattern truly universal? Or are there traits where higher tier ≠ better placement? If so, what makes them different?

We test 5 additional traits across their breakpoints: **Space Groove**, **Mecha**, **Anima Squad**, **Conduit**, and **Vanguard**.

---

## Chapter 1: The Data — 8 Traits × Multiple Tiers

### Previously tested (from trait-breakpoint-multi-comp)

| Trait | Low Tier | Games | AVP | High Tier | Games | AVP | ΔAVP |
|---|---|---|---|---|---|---|---|
| N.O.V.A. (DRX) | 2 | 66k | 4.61 | 5 | 120k | 4.37 | -0.24 |
| Dark Star | 4 | 38k | 4.93 | 6 | 75k | 4.11 | -0.82 |
| Summon | 5 | 33k | 4.25 | 7 | 17k | 3.56 | -0.69 |

### New: Space Groove (4 tiers)

| Tier | Games | AVP | Top 4% | Win% |
|---|---|---|---|---|
| 3 | 459,292 | 4.30 | 53.9% | 13.8% |
| 5 | 267,126 | 4.27 | 54.1% | 15.1% |
| 7 | 70,554 | 3.65 | 66.1% | 20.7% |
| 10 | 1,117 | **1.10** | **99.6%** | **93.3%** |

Pattern holds — monotonically improving with each tier. Space Groove 10 is the most extreme case: 1,117 games with AVP 1.10 and 93% win rate. This is pure selection bias — only boards that are absolutely dominating can assemble 10 Space Groove units.

### New: Mecha (3 tiers, unfiltered)

| Tier | Games | AVP | Top 4% | Win% |
|---|---|---|---|---|
| 3 | 287,425 | 4.67 | 46.2% | 15.4% |
| 4 | 266,954 | 4.62 | 46.9% | 16.0% |
| 6 | 233,482 | 4.56 | 47.7% | 16.4% |

Pattern holds — monotonically improving, but the gaps are tiny (0.05 per tier step). Mecha's tight breakpoints (3→4→6) produce small incremental gains, unlike Space Groove's dramatic jumps.

### New: Vanguard (3 tiers, unfiltered)

| Tier | Games | AVP | Top 4% | Win% |
|---|---|---|---|---|
| 2 | 2,152,854 | 4.34 | 52.9% | 14.4% |
| 4 | 469,067 | 4.30 | 53.9% | 12.2% |
| 6 | 61,867 | 3.67 | 67.2% | 15.9% |

Pattern holds — 2→4 is a small improvement (-0.04), but 4→6 is a big jump (-0.63). This mirrors what we see in other traits: the highest breakpoints show the largest selection bias effects.

### New: Conduit (4 tiers, within conduit_mf comp)

| Tier | Games | AVP | Top 4% | Win% |
|---|---|---|---|---|
| 2 | 29,731 | 4.73 | 45.4% | 5.6% |
| 3 | 9,743 | 4.25 | 55.8% | 8.4% |
| 4 | 2,363 | 4.22 | 55.5% | 9.2% |
| 5 | 556 | 4.19 | 54.7% | 9.2% |

Pattern holds — monotonically improving. The biggest jump is 2→3 (-0.48), then 3→4 and 4→5 are marginal (-0.03 each). Interesting: win rate is very low across all tiers (5-9%), suggesting Conduit MF is a weak comp even at high trait investment.

### New: Anima Squad — THE EXCEPTION

#### Unfiltered (all Anima games)

| Tier | Games | AVP | Top 4% | Win% |
|---|---|---|---|---|
| 3 | 121,902 | 5.48 | 33.8% | 13.4% |
| 6 | 8,623 | **5.88** | **24.5%** | 12.7% |

**Pattern BROKEN.** Higher tier (6) has **worse** AVP than lower tier (3): 5.88 vs 5.48 (+0.40).

#### Within anima_diana comp

| Tier | Games | AVP | Top 4% | Win% |
|---|---|---|---|---|
| 3 | 41,402 | 4.75 | 45.0% | 15.2% |
| 6 | 693 | 5.48 | 32.2% | 15.7% |

Same reversal within the comp context: Anima 6 is dramatically worse (5.48 vs 4.75, +0.73 AVP). Only 693 games — but the direction is clear.

---

## Chapter 2: Why Anima Squad Breaks the Pattern

Every other trait follows the selection bias narrative: stronger boards reach higher tiers, so higher tier ≈ better AVP. Why does Anima Squad reverse this?

**Hypothesis: Opportunity cost exceeds trait benefit.**

Anima Squad 3→6 requires adding 3 more Anima Squad units. But the Anima Squad unit pool may not contain enough strong late-game units. Players who commit to 6 Anima are sacrificing unit quality for trait synergy — and the trade isn't worth it.

Supporting evidence:
- Anima 3 already has 121k games (reasonable play rate) but AVP 5.48 — the comp is mediocre even at the baseline.
- Going to 6 drops to just 8.6k games — very few players even attempt it. The ones who do likely have no better options (weak lobbies, forced pivots).
- In anima_diana, Anima 6 has only 693 games — a vanishingly small sample of players who both played Diana carry AND committed to 6 Anima. This is probably "desperation" territory.

**This is the key insight: selection bias assumes stronger boards can reach higher tiers. But when the trait requires weak units, the "stronger board" assumption breaks — committing to the trait actively weakens the board.**

---

## Chapter 3: The Spectrum of Selection Bias

Combining all 8 traits, we can see a spectrum:

| Trait | Low→High ΔAVP | Direction | Interpretation |
|---|---|---|---|
| Space Groove 7→10 | -2.55 | ↓ (better) | Extreme selection bias |
| Dark Star 4→6 | -0.82 | ↓ (better) | Strong selection bias |
| Summon 5→7 | -0.69 | ↓ (better) | Strong selection bias |
| Vanguard 4→6 | -0.63 | ↓ (better) | Strong selection bias |
| Conduit 2→3 | -0.48 | ↓ (better) | Moderate selection bias |
| N.O.V.A. 2→5 | -0.24 | ↓ (better) | Mild selection bias |
| Mecha 3→6 | -0.11 | ↓ (better) | Very mild selection bias |
| **Anima 3→6** | **+0.40** | **↑ (worse)** | **Opportunity cost > trait value** |

**7 of 8 traits follow the pattern. Anima Squad is the sole exception.**

The magnitude of selection bias correlates with how many units must be added: Space Groove 10 (adding many units to a 7-unit base) shows the largest effect; Mecha 3→6 (adding 3 units) shows the smallest positive effect.

---

## Chapter 4: Space Groove 10 — Selection Bias at Its Most Extreme

Space Groove 10 deserves special attention:
- **1,117 games**, AVP **1.10**, **93.3% win rate**
- This means assembling 10 Space Groove units virtually guarantees a win

But this isn't because Space Groove 10 is broken — it's because only a player who is already winning hard can afford to collect 10 units of a single trait. By the time you have 10 Space Groove units, you've likely already eliminated most opponents. The trait tier is a **consequence** of winning, not a **cause**.

This is the purest demonstration of selection bias in our data: the AVP doesn't measure "how good is Space Groove 10" — it measures "how good was the player's game when they happened to reach 10 Space Groove."

---

## What I Learned

1. **The pattern is near-universal but NOT universal.** 7 of 8 traits show higher tier → better AVP. Anima Squad is the exception, where tier 6 is actually worse than tier 3.

2. **Selection bias has a prerequisite: the trait must not weaken the board.** When higher trait tiers require adding low-quality units, the opportunity cost can overwhelm the selection bias effect. Anima Squad 6 actively weakens boards.

3. **Selection bias magnitude scales with commitment cost.** Space Groove 10 (massive unit investment) shows the most extreme bias; Mecha 3→6 (3 added units) shows the weakest. The harder it is to reach a tier, the stronger the filter on board quality.

4. **Space Groove 10 is the ultimate selection bias example.** AVP 1.10, 93% win rate, 1117 games. This should be a teaching case for Module 5 — it immediately shows that AVP at high tiers measures player strength, not trait strength.

5. **Trait tier comparisons require caution about direction.** We cannot assume "higher = better." Each trait must be checked individually, and Anima Squad shows that the assumption can be completely wrong.

---

## Open Questions

1. Are there other traits like Anima Squad where the unit pool is too weak to support high tiers? Could this be predicted from the units' individual stats?
2. Is the Anima Squad reversal stable across patches, or is it specific to S17's unit pool?
3. Can we separate selection bias from genuine trait effect? E.g., if we control for board strength (total unit stars, gold value), does the AVP-tier relationship change?

---

## Questions for Xing

1. **Anima Squad as counter-example**: Is the "opportunity cost > trait value" explanation correct? Or is there a simpler reason (e.g., Anima Squad 6 is just a bad trait bonus)?
2. **Teaching moment**: Space Groove 10 (AVP 1.10, 93% WR) feels like the single best example of selection bias in TFT. Is this worth adding to [[concepts/biases]] as a canonical example?
3. **Next for Module 5**: We've shown that (a) trait breakpoints don't change itemization, and (b) the "higher = better AVP" pattern is mostly selection bias with one exception. What question should Module 5 address next, or is this sufficient to consider it complete?

---

## Sources
- MetaTFT Explorer API: `total` endpoint with trait filters
- [[experiments/2026-04-22-trait-breakpoint-multi-comp]] — prior 3-trait experiment
- [[concepts/biases]] — selection bias framework

---

## Review

*(Awaiting review)*
