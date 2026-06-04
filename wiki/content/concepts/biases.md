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

### Disentangling Investment from Survivor-Dumping (IC3)

A unit holding 3 items (IC3) with a good AVP has **two indistinguishable causal paths**:

- **Investment**: items were built on it early → it carries → it wins. IC3 is the *cause*.
- **Survivor-dumping**: the game was already won → player survived to lv9–10 → spare items get dumped on a spare unit. IC3 is the *consequence*.

Both produce "IC3 + good AVP". Neither IC3 frequency nor IC3 AVP can tell them apart — survivor-dumping inherits the high AVP of "games good enough to reach the item surplus." And because the API is [[tools/metatft-api|end-board-only]], there is **no early-game snapshot to inspect** — you cannot resolve this by "looking at who held items at the D-stage." Only end-board cross-sectional signals exist. Use a three-stage funnel:

**Stage 1 — IC3 build scale: does the unit even enter the 3-item pool?** Survivor-dump positions often *never* assemble a real 3-item build — they wear an auto-item (Thief's Gloves) or 1–2 leftovers. Query `unit_builds` and count distinct full builds and their total games. A unit with ~0 standard 3-item builds is a dump slot regardless of how often it appears.

**Stage 2 — two Necessities: core-ness vs item-hunger.** These answer different questions and must not be conflated:
- **unit-necessity** = ΔAVP when the *unit* is absent (`& ~Unit(X)`) → is it core?
- **item-necessity** = ΔAVP when a *specific item* is absent on a present unit (items endpoint) → does it want items?

**Stage 3 — build entropy: itemization focus**, meaningful *only within units that truly itemize* (passed Stage 1). Compute Shannon entropy over the unit's 3-item build distribution; report effective build count `2^H`. Low = locked BIS, high = flexible. It does **not** separate "flexible real carry" from "dump slot" on its own — both are high-entropy; combine with Stages 1–2.

**Worked example — `space_groove`, lv9 (2026-06-04):**

| Unit | Appearances | IC3 build games | builds (2^H) | unit-nec | item-nec | Verdict |
|---|---|---|---|---|---|---|
| Samira | 113k | 62k | 10.8 | +0.32 | +0.52 | **Item-hungry carry** (core + wants items, locked BIS) |
| Nami | 173k | 116k | 18.1 | **+0.82** | +0.05 | **Item-light core** (core but flexible/ability-based, not a dump) |
| Gwen | 167k | **0** | — | +0.22 | +0.01 | **Dump slot** (high appearance, never a real build) |
| Jhin | 41k | 132 | 1.0 | +0.18 | +0.004 | **Dump / off-carry** (best IC3 AVP, lowest necessity) |

The two traps this catches: **appearance frequency** says Gwen/Nami (167k/173k) matter more than Samira (113k) — wrong, Gwen is a dump. **IC3 AVP** says Jhin (2.18, the best of the four) is strongest — wrong, his necessity is ~0; his AVP is the survivorship signature ("games where Jhin got items were already won").

**The four quadrants (unit-nec × item-nec):**

| | item-nec high (wants items) | item-nec low (doesn't) |
|---|---|---|
| **unit-nec high (core)** | item-hungry carry (Samira) | ability/trait core (Nami) |
| **unit-nec low (edge)** | (rare) | dump slot / off-carry (Gwen, Jhin) |

**Caveats — do not over-read the numbers:**
- **unit-necessity over-credits trait anchors.** `~Unit(Nami)` under `SpaceGroove≥5` also breaks the trait (hard to reach 5 without her), so +0.82 measures "Nami **plus the trait slot she fills**", not Nami alone. The remaining sample (boards that hit 5 SpaceGroove yet lack Nami) is small and atypical.
- **"Remove the unit" ≠ "remove IC3."** `~Unit(X)` excludes the unit entirely (any star, any item count). To ask "is itemizing X worth it" cleanly, compare IC3 vs low-item *while the unit is present*, holding presence and trait fixed.
- **Necessities from different bases aren't directly comparable in magnitude** (unit-nec base here is `SpaceGroove≥5`; item-nec base is the `space_groove` comp). Read directions, not absolute gaps.
- This whole funnel *infers* investment from end-board cross-sections; it cannot *observe* it. Survivor-dumping is reduced, not eliminated.

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

## 3b. Dual-Comp Pollution (Context Confusion Bias)

When a unit is played in two or more different comps, aggregated stats mix their contexts. Each comp may require completely different itemization.

**Canonical example (Aesah)**: Gwen in 6 Sorcerer vs 8 Soul Fighter:
- 6 Sorc (weak frontline): Edge of Night is critical for Gwen's survival
- 8 Soul Fighter (trait gives +650 HP): Gunblade becomes viable; Edge of Night is less needed

Without filtering by comp, Gwen's item stats are a meaningless average of two contradictory strategies. The "best" item depends entirely on which comp you're playing.

**Related example**: Yumi as primary carry (damage items are BIS) vs Yumi as secondary carry behind Katarina 3 (support items look good because secondary carries inherit leftover items from winning boards).

**Diagnostic**: If a unit appears in multiple comps on the MetaTFT comps page, always filter by specific comp context before analyzing items.

**Mitigations**:
- Always use comp filters ([[methods/filter-strategy]])
- Use compositions.py definitions that distinguish comp variants
- Check games tab to verify filter captures intended comps

---

## 3c. Level Bias

Player level at endgame correlates with board strength. Higher-level players have more units, more gold spent, and generally stronger boards. Filtering or not filtering by level changes what question you're asking.

**Canonical example**: Sona in Nova 95. Without level control, Sona has Necessity +0.127 — appears to be the third most important unit. With `--level 10` control, Sona drops to +0.015 (an 88% decrease). The reason: Sona mostly appears at level 10 (9-unit boards), and level 10 games are already winning. Sona's apparent importance was almost entirely level bias.

**Why it matters**: Unit evaluation, flex slot analysis, and +1 candidate analysis are all heavily affected. A unit that only appears at high levels will always look important without level control — because reaching that level is already a signal of success.

**Diagnostic**: If a unit's Necessity drops dramatically when adding `--level`, the original value was inflated by level bias.

**Mitigations**:
- Always use `--level` when analyzing unit importance or flex slots
- Compare same-level cohorts when evaluating +1 candidates
- Level bias is a **variable to prevent**, not a finding to discover — control it upfront

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
- Ranking items by raw AVP (doesn't correct for frequency)
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

**Delta has a shifting baseline.** `Delta = item_AVP - without_item_AVP`. For high play rate items (Guinsoo at 87%), the "without" group is only 13% of players — a non-representative group that was likely struggling. For low play rate items (Red Buff at 7%), "without" is 93% of players — approximately the overall average. Comparisons across play rates are structurally unfair.

**Necessity = play_rate / (1 - play_rate) * (overall_AVP - item_AVP).** This is the best single-metric correction available without by-round data, but it assumes play rate is a sufficient proxy for survivorship exposure. It is not a complete solution.

---

## Sources
- [[sources/morbrid-reddit-post]]: Comprehensive writeup on all three biases
- [[sources/morbrid-aesah-talk]]: "CI doesn't fix survivorship bias", frequency-AVP graph
- [[sources/dishsoap-frodan-stats]]: Sample size rules of thumb
- [[sources/aesah-data-mistakes]]: Play rate as the key corrector
- [[sources/aesah-video-collection]]: Dual-comp pollution (Gwen), overfiltering, parametric verification
- [[experiments/2026-04-21-vex-nova95-items]]: Frequency-AVP regression (R² ≈ 0 in filtered data)
- [[experiments/2026-04-22-universal-improvement-bias]]: 8-trait universal improvement test
- [[experiments/2026-04-22-nova-trait-breakpoint]]: Necessity compression at higher tiers
- [[experiments/2026-04-22-trait-breakpoint-multi-comp]]: Selection bias across 3 traits x 3 comps
