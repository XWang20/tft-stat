# Experiment: Is 5 N.O.V.A. Worth the Cost?
**Status**: ✅ Complete
**Date**: 2026-04-22
**Module**: 5 (Trait Breakpoints — preview)

---

## The Question

N.O.V.A. in S17 has two breakpoints: **2 units** and **5 units**. The Nova 95 comp typically runs at 2 NOVA. Is upgrading to 5 NOVA worth it?

This seems straightforward — compare AVP at 2 vs 5 NOVA. But the whole course so far warns me: **raw AVP comparisons are corrupted by survivorship bias.** Players who hit 5 NOVA might already be winning (more gold, better boards, luckier shops). Can we actually separate "the trait made me stronger" from "I was already strong enough to hit 5"?

**Setup**: Nova 95 base filter (OR: Fiora/Vex/Graves with 3 items). Compare `trait=TFT17_DRX_1 & !DRX_2` (exactly 2 NOVA) vs `trait=TFT17_DRX_2` (5+ NOVA). Patch: current. Days: 3. Ranks: Plat–Challenger.

---

## Chapter 1: The Headline Numbers

| Breakpoint | Games | Vex AVP | Top4% |
|---|---|---|---|
| 2 N.O.V.A. (exactly) | 217,994 | 4.13 | 55.8% |
| 5 N.O.V.A. | 9,189 | 3.73 | 64.7% |

5 NOVA looks incredible — **0.40 AVP better**, nearly a full placement. But immediately: 5 NOVA is only **4.0%** of all Nova 95 games. Red flag. Low frequency + high performance is the exact pattern of survivorship bias.

Global trait stats tell a similar story:
- DRX_1 (2 NOVA): 711k games, AVP 4.56 — below average
- DRX_2 (5 NOVA): 297k games, AVP 4.04 — above average

---

## Chapter 2: Every Unit Gets Better

If 5 NOVA is truly a powerful trait breakpoint, we'd expect NOVA-synergy units to improve more than non-NOVA units. Let's check.

| Unit | 2 NOVA AVP | 5 NOVA AVP | Δ | NOVA? |
|---|---|---|---|---|
| Briar | 4.85 | 2.94 | **-1.90** | No |
| Rek'Sai | 4.44 | 2.95 | **-1.49** | No |
| Caitlyn | 4.79 | 3.79 | -1.01 | No |
| Diana | 4.87 | 3.87 | -1.00 | No |
| Rammus | 4.85 | 3.98 | -0.87 | No |
| MissFortune | 4.64 | 3.80 | -0.85 | No |
| Shen | 3.97 | 3.18 | -0.79 | No |
| TahmKench | 4.36 | 3.58 | -0.79 | No |
| Riven | 4.29 | 3.51 | -0.77 | No |
| Morgana | 3.98 | 3.24 | -0.75 | No |
| Maokai | 4.35 | 3.64 | -0.71 | Yes (DRX) |
| Bel'Veth | 3.94 | 3.29 | -0.65 | Yes (DRX) |
| MasterYi | 4.04 | 3.41 | -0.63 | Yes (DRX) |
| Kindred | 4.19 | 3.63 | -0.56 | Yes (DRX) |
| Akali | 4.19 | 3.63 | -0.55 | No |
| Fiora | 4.03 | 3.46 | -0.56 | Yes (DRX) |
| Vex | 4.13 | 3.73 | -0.40 | Yes (DRX) |
| Nunu | 4.11 | 4.18 | **+0.08** | No |
| Jax | 4.13 | 4.17 | **+0.03** | No |

**Every single unit gets better in 5 NOVA** except Nunu (+0.08) and Jax (+0.03). The improvement is **not concentrated on NOVA units** — non-NOVA units like Briar (-1.90), Rek'Sai (-1.49), and Caitlyn (-1.01) improve even more than the NOVA core.

This is the smoking gun for survivorship bias. If the trait itself were the cause, NOVA units should benefit disproportionately. Instead, the improvement is universal, meaning **the player's overall board state is better**, not just the trait.

---

## Chapter 3: The Composition Shifts

Who actually appears in 5 NOVA games?

| Unit | 2 NOVA rate | 5 NOVA rate | Shift |
|---|---|---|---|
| Maokai | 43% | **100%** | +57pp — 5th NOVA unit, basically mandatory |
| Kindred | 12% | **99%** | +87pp — another NOVA unit, now core |
| TahmKench | 42% | **65%** | +23pp |
| MasterYi | 12% | **61%** | +49pp — NOVA unit |
| Bel'Veth | 7% | **51%** | +44pp — NOVA unit |
| Caitlyn | 3% | **44%** | +41pp |
| Shen | 91% | 61% | **-30pp** — dropped! |
| Morgana | 80% | 17% | **-63pp** — dropped hard |
| Blitzcrank | 72% | 6% | **-66pp** — dropped hard |
| Nunu | 72% | 5% | **-67pp** — dropped hard |

The board looks completely different. 5 NOVA means replacing the frontline (Shen/Morgana/Blitz/Nunu) with NOVA units (Maokai, Kindred, Bel'Veth, MasterYi). It's not "add 3 more NOVA units" — it's "replace your support shell with a NOVA shell."

This is effectively a **different composition**, not just a trait upgrade.

---

## Chapter 4: Vex's BIS Changes Too

| Rank | 2 NOVA (217k games) | 5 NOVA (9k games) |
|---|---|---|
| 1 | RFC (3.69) | Power Gauntlet (3.23) |
| 2 | Dcap (3.77) | RFC (3.28) |
| 3 | Shiv (3.79) | Dcap (3.42) |
| 4 | Power Gauntlet (3.80) | Leviathan (3.48) |
| 5 | Guinsoo (3.83) | Bloodrazor (3.51) |

Power Gauntlet jumps from #4 to #1. Bloodrazor appears in 5 NOVA (#5) but isn't even top 12 in 2 NOVA. This suggests the trait's power surge mechanic synergizes differently with certain items.

But again — 5 NOVA sample sizes are small (1,221 games for Power Gauntlet vs 34,450 in 2 NOVA). The usual caveat applies.

---

## Chapter 5: Can We Measure the Trait's True Value?

We want to isolate the causal effect of the trait. Three approaches:

### Approach A: Overall AVP Delta
- 5 NOVA AVP: 3.73
- 2 NOVA AVP: 4.13
- **Naive Delta: -0.40**

This is hopelessly confounded.

### Approach B: Board-Strength Normalization (idea)
If we could filter both groups to "same quality boards" (same # of 2-stars, same gold spent, same items), we could isolate the trait effect. But MetaTFT doesn't expose these variables.

### Approach C: Look at Nunu and Jax
Nunu and Jax are the only units that don't improve (or get slightly worse) in 5 NOVA. Why?

- **Nunu**: 72% presence in 2 NOVA → 5% in 5 NOVA. Nunu gets dropped when going 5 NOVA. The remaining 5% are players who kept Nunu despite going vertical — probably suboptimal boards.
- **Jax**: 4% → 1%. Same story.

These units get worse precisely because they're the "wrong" units to have in 5 NOVA. This is actually evidence that composition matters: the trait forces a specific board, and units that don't fit it suffer.

### Conclusion
We **cannot** cleanly measure the trait's causal value from endgame snapshots. The 5 NOVA filter selects for a completely different (and likely highrolled) player population. The 0.40 AVP improvement is **an upper bound** on the trait's true value — the real value is somewhere between 0 and 0.40.

---

## What I Learned

### About trait breakpoints
1. **Trait breakpoints are confounded by selection bias** — hitting a higher breakpoint requires specific units, which requires either luck or a strong economy, which correlates with winning
2. **Higher trait ≈ different comp, not "same comp but stronger"** — the unit composition shifts dramatically (frontline swapped for NOVA units)
3. **Universal improvement = bias signal** — when every unit gets better, including non-synergy units, it's the player that's stronger, not the trait
4. **Nunu/Jax as "negative controls"** — units that don't improve (or get worse) reveal compositional incompatibility, which is genuine signal

### About methodology
5. **The "every unit improves" test is a cheap bias detector** — if filtering by X improves everything equally, X is likely correlated with board quality, not causing the improvement
6. **We need a counterfactual**: "What if this exact player had stayed at 2 NOVA?" — endgame snapshot data can't answer this
7. **Trait analysis needs the Dishsoap treatment**: instead of trait level, we should compare specific board configurations (8-unit teams) where only the trait level differs

### Open questions
- [ ] Can we construct "matched pairs" — 2 NOVA and 5 NOVA boards with the same core 5 units, comparing AVP on the remaining slots?
- [ ] Do other traits show the same "everything gets better" pattern, or is NOVA special?
- [ ] Is there a trait where hitting the breakpoint actually makes some units *worse*? That would be genuine trait-specific signal
- [ ] Dishsoap's approach: look at "4 NOVA + 1 flex" vs "5 NOVA" — does the 5th NOVA unit beat the best flex option?

---

## Questions for Xing

1. **The "universal improvement" test** — I used it as a bias detector (if everything improves, it's bias not the trait). Is this a known technique in causal inference? Does it have a name? It feels like it's related to "positive control" in experiments.

2. **Matched-pair analysis** — Could we filter for boards that share 6 common units but differ on whether they have a 5th NOVA unit vs a non-NOVA flex? This would control for board quality. Would MetaTFT's filter system even support this level of specificity, or would we run out of sample size?

3. **Is there any trait in TFT history where the data clearly showed a causal breakpoint effect** (i.e., the trait itself is the reason, not selection bias)? Or is this fundamentally unmeasurable from endgame snapshots?

---

## Sources
- MetaTFT Explorer API: units_unique, unit_items_unique, traits endpoints
- [[concepts/biases]] — survivorship bias framework
- [[methods/filter-strategy]] — filter as foundation
- [[experiments/vex-nova95]] — prior Vex item analysis
- [[sources/dishsoap-frodan-stats]] — "add context first"
