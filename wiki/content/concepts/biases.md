# Biases in TFT Statistics
**Status**: ✅ verified

## 1. Selection Bias (Survivorship Bias)

**The biggest, most persistent bias in TFT stats.** It arises whenever the condition being measured is correlated with board strength.

**Core mechanism**: Items from late-game carousels appear on boards of players who survived to late game. Surviving late = already winning. These items get credited with performance they didn't cause. The same logic applies to trait tiers, 5-cost units, and secondary carry items.

### Canonical example: Space Groove 10

| Tier | Games | AVP | Win% |
|---|---|---|---|
| 3 | 459,292 | 4.30 | 13.8% |
| 7 | 70,554 | 3.65 | 20.7% |
| 10 | 1,117 | **1.10** | **93.3%** |

Space Groove 10 has a 93% win rate — not because the trait is broken, but because only a player who is already dominating can afford to collect 10 units of a single trait. The tier is a **consequence** of winning, not a **cause**. This is selection bias at its purest: AVP measures "how good was the player's game when they reached 10 Space Groove," not "how good is Space Groove 10."

### The universal improvement test

If filtering by condition X improves AVP for **everything equally**, the improvement is selection bias (stronger boards reach X), not a causal effect of X.

Tested across 8 traits at their breakpoints, 7 of 8 showed monotonically better AVP at higher tiers:

| Trait | Low→High ΔAVP | Interpretation |
|---|---|---|
| Space Groove 7→10 | -2.55 | Extreme selection bias |
| Dark Star 4→6 | -0.82 | Strong selection bias |
| Summon 5→7 | -0.69 | Strong selection bias |
| Vanguard 4→6 | -0.63 | Strong selection bias |
| Conduit 2→3 | -0.48 | Moderate selection bias |
| N.O.V.A. 2→5 | -0.24 | Mild selection bias |
| Mecha 3→6 | -0.11 | Very mild selection bias |
| **Anima Squad 3→6** | **+0.40** | **Pattern breaks** |

The test works because selection bias has a prerequisite: reaching the higher tier must not weaken the board. When it does (Anima Squad 6 requires adding weak units, actively degrading board quality), the pattern reverses — opportunity cost exceeds trait value. The magnitude scales with commitment cost: Space Groove 10 requires assembling 10 units of one trait (extreme filter on board quality); Mecha 3→6 adds just 3 units (weak filter).

**Diagnostic rule**: If higher tier → better AVP for a trait, assume selection bias until proven otherwise. If higher tier → worse AVP, the trait genuinely costs more than it gives.

### Manifestations

- **Low play rate items always look better than they are.** In Nova 95 (209k games), Red Buff at 7% play rate has AVP 3.67 while Guinsoo at 87% has AVP 4.05. Raw AVP says Red Buff is the best item on Vex. Necessity says Guinsoo is 6x more important (+0.416 vs +0.035).
- **5-cost units always top AVP charts** — you must survive to field them.
- **Secondary carry items look amazing** — you only give secondary carries items when you're already winning.
- **Every trait shows better AVP at higher tiers** (with rare exceptions like Anima Squad).

### Mitigations

- Use [[concepts/metrics|Necessity]] instead of raw AVP (play rate weighting)
- Use [[methods/build-analysis]] instead of single-item analysis
- Use [[methods/filter-strategy]] to condition on comp context
- Apply the universal improvement test to distinguish selection from causation

---

## 2. How Filtering Changes Bias Structure

Filtering (conditioning on comp) does not eliminate survivorship bias — it changes how bias manifests.

### Frequency-AVP correlation breaks in filtered data

Globally, play rate and AVP are inversely correlated — morbrid's "constant bias, every item, every set." But within a well-filtered comp, this relationship can vanish.

In Nova 95 (Vex items, 209k games after filtering):
```
AVP = 3.937 + 0.010 * ln(rate%)
R² = 0.004
```

R-squared near zero means frequency explains almost none of the AVP variance after conditioning. The comp filter already removes most of the board-strength variation that creates the global correlation. Residuals from this regression rank nearly identically to raw AVP — the regression adds no information.

**Implication**: The survivorship bias correction that works globally (frequency-weighting, regression residuals) may be unnecessary or even counterproductive in well-filtered data. Bias doesn't disappear — it changes form. In filtered data, the remaining bias is subtler: item availability by game state, carousel timing, and player decision quality.

### Necessity compression at lower baselines

When overall AVP drops (stronger board context), Necessity values compress. This is a mathematical property of the metric, not a property of the data.

MasterYi items in nova_yi at two NOVA tiers:

| Item | Nec. at DRX 2 (AVP 4.61) | Nec. at DRX 5 (AVP 4.37) | Change |
|---|---|---|---|
| Edge of Night | +0.111 | +0.054 | -51% |
| Giant Slayer | +0.060 | +0.045 | -25% |
| Quicksilver | +0.042 | +0.022 | -48% |

Edge of Night's Necessity drops 51% — not because the item becomes less important, but because the denominator (how much room there is to improve) shrinks. When the overall AVP is already low, each item contributes less marginal value.

**However, this is not universal.** Sona (Shepherd comp) shows the opposite — Necessity **increases** at higher trait tiers:

| Item | Nec. at Summon 5 | Nec. at Summon 7 | Change |
|---|---|---|---|
| Void Staff | +0.052 | +0.092 | +77% |
| Spear of Shojin | +0.031 | +0.086 | +177% |

The direction depends on carry leverage: when a stronger board makes the carry's role more impactful (Sona's AP damage in a viable team), individual item Necessity expands. When the team already carries regardless (MasterYi in 5 NOVA), item impact compresses.

**Practical rule**: Don't compare absolute Necessity values across different filter conditions or trait tiers. Rankings are stable (top 3 items are the same regardless of tier), but magnitudes are not.

---

## 3. Player Behavior Bias

Players tend to build "consensus best" items, creating a self-fulfilling prophecy.

**Effects**:
- Popular items include many forced/suboptimal builds → AVP pulled toward average (looks worse)
- Unpopular items only built by knowledgeable players or in ideal situations → AVP pulled away from average (looks better)

**Mitigations**:
- Factor in play rate (Necessity handles this)
- Filter by high rank (GM+) for more optimized builds
- Filter by region for specific meta reads

---

## 4. Low Sample Size Noise

Fewer observations → higher variance → more outliers. Not a systematic bias but interacts badly with selection bias (rare items are both biased AND noisy).

**Rules of thumb** (Dishsoap):
- Mature patch: >=1000 games to trust
- New patch: >=300 games minimum
- 4x games = 2x accuracy (SE proportional to 1/sqrt(n))

**Mitigations**:
- MetaTFT Advanced Mode: 95%/99% CI worst case sorting
- Multiple comparisons: more rows in table → more random outliers → use higher CI
- Don't overfilter: each filter reduces sample size

---

## 5. Decision Framework: When Does Bias Matter?

Not every analysis requires full debiasing. Use this framework:

**Bias matters most when**:
- Comparing items with very different play rates (e.g., 7% vs 87%)
- Comparing trait tiers (higher tier games are systematically stronger boards)
- Ranking items by AVP or Edge (both are just AVP; neither corrects for frequency)
- Working with unfiltered/lightly filtered data (global stats)

**Bias matters less when**:
- Comparing items with similar play rates (survivorship affects both equally)
- Rankings within a well-filtered comp (R² ≈ 0 means frequency-AVP correlation is already gone)
- Using Necessity (play rate weighted, partially corrects for survivorship)
- Using build analysis (three-item builds largely eliminate carousel bias)

**Bias is irrelevant for**:
- Identifying which items are *used* (play rate is unbiased by definition)
- Comparing the same item across two filter conditions with similar sample sizes
- Confirming top-3 item identity (rankings are robust even when magnitudes shift)

---

## Key Identities and Traps

**Edge = AVP.** `Edge = overall_AVP - item_AVP = constant - AVP`. Rankings are identical. Edge provides no additional information over AVP. Don't use it as a separate metric.

**Delta has a shifting baseline.** `Delta = item_AVP - without_item_AVP`. For high play rate items (Guinsoo at 87%), the "without" group is only 13% of players — a non-representative group that was likely struggling. For low play rate items (Red Buff at 7%), "without" is 93% of players — approximately the overall average. Comparisons across play rates are structurally unfair.

**Necessity = play_rate / (1 - play_rate) * (overall_AVP - item_AVP).** This is the best single-metric correction available without by-round data, but it assumes play rate is a sufficient proxy for survivorship exposure. It is not a complete solution.

---

## Sources
- [[sources/morbrid-reddit-post]]: Comprehensive writeup on all three biases
- [[sources/morbrid-aesah-talk]]: "CI doesn't fix survivorship bias", frequency-AVP graph
- [[sources/dishsoap-frodan-stats]]: Sample size rules of thumb
- [[sources/aesah-data-mistakes]]: Play rate as the key corrector
- [[experiments/2026-04-21-vex-nova95-items]]: Frequency-AVP regression (R² ≈ 0 in filtered data)
- [[experiments/2026-04-22-universal-improvement-bias]]: 8-trait universal improvement test
- [[experiments/2026-04-22-nova-trait-breakpoint]]: Necessity compression at higher tiers
- [[experiments/2026-04-22-trait-breakpoint-multi-comp]]: Selection bias across 3 traits x 3 comps
