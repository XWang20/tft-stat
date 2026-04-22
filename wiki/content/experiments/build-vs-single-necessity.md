# Experiment: Build Necessity vs Single-Item Necessity — Do They Differ?
**Status**: 🧪 draft
**Date**: 2026-04-22
**Module**: 3 (Build Analysis — follow-up)

---

## The Question

Single-item Necessity measures how much worse a comp performs when a specific item is absent. Build Necessity measures the same thing but at the 3-item combination level — how much worse does the comp perform when builds containing item X are removed?

These two metrics could diverge because:
1. **Item synergies**: An item might be mediocre alone but excellent in specific combinations
2. **Survivorship bias**: Single-item stats are more polluted by carousel bias than builds (Dishsoap's key insight)
3. **Slot competition**: An item might rank high individually but get crowded out by better build combinations

**Core question**: Do build-level and single-item Necessity rankings agree? If they diverge, which items are most affected and why?

---

## Chapter 1: Method — Build Necessity

We define **Build Necessity** by analogy with single-item Necessity:

1. Query all 3-item builds for a carry (via `unit_builds` endpoint), filtered to nova_95
2. Filter to builds with ≥200 games (significance threshold)
3. Compute weighted-average AVP across all qualifying builds (= overall build AVP)
4. For each item, compute the weighted-average AVP of builds *containing* that item vs the overall
5. Apply the Necessity formula: `Build_Necessity = wo_AVP - overall_AVP`

This is identical to single-item Necessity, but applied to the build population rather than the game population.

**Key caveat**: Guinsoo's Rageblade appears in ~100% of Vex builds, making its Build Necessity undefined (~0). We exclude it from Vex comparisons.

---

## Chapter 2: Vex — Rankings Converge Strongly

### Single-Item Necessity (our pipeline, 211k games)

| Rank | Item | Necessity |
|---|---|---|
| 1 | Guinsoo's Rageblade | +0.503 |
| 2 | Giant Slayer | +0.083 |
| 3 | Hextech Gunblade | +0.076 |
| 4 | Striker's Flail | +0.063 |
| 5 | Rabadon's Deathcap | +0.038 |
| 6 | Red Buff | +0.033 |
| 7 | Archangel's Staff | +0.018 |
| 8 | Morellonomicon | +0.007 |

### Build Necessity (114 builds ≥200 games, 158k games)

| Rank | Item | Build Nec. | Top-10 Build Count |
|---|---|---|---|
| 1 | Hextech Gunblade | +0.064 | 2/10 |
| 2 | Striker's Flail | +0.061 | 3/10 |
| 3 | Giant Slayer | +0.049 | 1/10 |
| 4 | Rabadon's Deathcap | +0.037 | 3/10 |
| 5 | Red Buff | +0.029 | 6/10 |
| 6 | Archangel's Staff | +0.015 | 1/10 |
| 7 | Morellonomicon | +0.006 | 1/10 |
| 8 | Nashor's Tooth | +0.005 | 1/10 |

(Guinsoo excluded: appears in ~100% of builds → Build Necessity ≈ 0)

**Spearman ρ = 0.929** (8 items, excluding Guinsoo).

The top 2 swap (Giant Slayer #2→#3, Hextech Gunblade #3→#1), but from rank 4 onward the ordering is identical. The swap is small in absolute Necessity terms (+0.083 vs +0.076 in single, +0.064 vs +0.049 in build).

**Red Buff is the standout in builds**: despite ranking only #5 by Build Necessity, it appears in **6 of the top 10 builds** by raw AVP. This is the Dishsoap insight validated — Red Buff is a build *component* that elevates combinations, even if its marginal Necessity isn't the highest.

### Top Builds Confirm the Pattern

| Rank | Build | Games | AVP |
|---|---|---|---|
| 1 | Guinsoo + Rabadon + Red Buff | 807 | 3.35 |
| 2 | Guinsoo + Nashor + Striker's Flail | 505 | 3.38 |
| 3 | Guinsoo + Guinsoo + Rabadon | 945 | 3.41 |
| 4 | Guinsoo + Morellonomicon + Rabadon | 399 | 3.43 |
| 5 | Archangel + Guinsoo + Red Buff | 703 | 3.45 |

Every top build contains Guinsoo. Red Buff + Rabadon appears as the best duo, matching the vex-nova95 experiment's finding that Red Buff/Dcap are consistently strong in control variable analysis.

---

## Chapter 3: Fiora — Builds Reveal a Thief's Gloves Surprise

### Single-Item Necessity (208k games)

| Rank | Item | Necessity |
|---|---|---|
| 1 | Edge of Night | +0.151 |
| 2 | Sterak's Gage | +0.131 |
| 3 | Bloodthirster | +0.122 |
| 4 | Hand Of Justice | +0.087 |
| 5 | Thief's Gloves | +0.061 |
| 6 | Titan's Resolve | +0.046 |
| 7 | Giant Slayer | +0.043 |

### Build Necessity (97 builds, 97k games)

| Rank | Item | Build Nec. | Top-10 Build Count |
|---|---|---|---|
| 1 | Edge of Night | +0.109 | 7/10 |
| 2 | Sterak's Gage | +0.073 | 6/10 |
| 3 | Thief's Gloves | +0.045 | 0/10 |
| 4 | Giant Slayer | +0.032 | 2/10 |
| 5 | Bloodthirster | +0.029 | 4/10 |
| 6 | Hand Of Justice | +0.029 | 3/10 |
| 7 | Striker's Flail | +0.016 | 5/10 |

**Spearman ρ = 0.750** — the lowest of the three carries.

The biggest divergence: **Thief's Gloves jumps from #5 (single) to #3 (build)**. This makes sense — Thief's Gloves *is* a build. It occupies all 3 item slots, so it has no synergy interactions to analyze at the single-item level, but at the build level its "3 random items" package outperforms many intentional combinations.

Conversely, **Bloodthirster drops from #3 (single) to #5 (build)**. It has high individual Necessity but doesn't dominate builds — perhaps because it pairs redundantly with Sterak's Gage (both provide sustain), diluting its build-level contribution.

**Striker's Flail** shows a striking gap: #7 in Build Necessity but appears in **5 of the top 10 builds**. It's a strong build component (good synergies) even if its average-across-all-builds contribution is modest.

### Top Builds

| Rank | Build | Games | AVP |
|---|---|---|---|
| 1 | Bloodthirster + Deathblade + Edge of Night | 370 | 2.94 |
| 2 | Edge of Night + Striker's Flail + Hand Of Justice | 458 | 2.97 |
| 3 | Edge of Night + Striker's Flail + Sterak's Gage | 230 | 2.99 |
| 4 | Deathblade + Edge of Night + Hand Of Justice | 284 | 3.00 |
| 5 | Bloodthirster + Striker's Flail + Sterak's Gage | 462 | 3.05 |

Edge of Night dominates top builds (4 of top 5), confirming its #1 rank in both metrics.

---

## Chapter 4: Graves — Strong Agreement

### Single-Item Necessity (202k games)

| Rank | Item | Necessity |
|---|---|---|
| 1 | Quicksilver | +0.122 |
| 2 | Giant Slayer | +0.105 |
| 3 | Sterak's Gage | +0.094 |
| 4 | Hand Of Justice | +0.086 |
| 5 | Striker's Flail | +0.071 |
| 6 | Deathblade | +0.050 |
| 7 | Edge of Night | +0.042 |

### Build Necessity (151 builds, 94k games)

| Rank | Item | Build Nec. | Top-10 Build Count |
|---|---|---|---|
| 1 | Quicksilver | +0.124 | 3/10 |
| 2 | Giant Slayer | +0.086 | 6/10 |
| 3 | Sterak's Gage | +0.084 | 4/10 |
| 4 | Hand Of Justice | +0.078 | 3/10 |
| 5 | Striker's Flail | +0.041 | 3/10 |
| 6 | Thief's Gloves | +0.032 | 0/10 |
| 7 | Edge of Night | +0.028 | 3/10 |
| 8 | Deathblade | +0.018 | 4/10 |

**Spearman ρ = 0.940** — excellent agreement.

Top 5 identical. The only notable shift: Thief's Gloves inserts at #6 in builds (not ranked in single top 7). **Infinity Edge** is an interesting case — it appears in **2 of the top 10 builds** (including the extreme outlier #1 build with Battle Bunny Crossbow at AVP 2.07) but has **negative Build Necessity** (-0.004). This is the Battle Bunny Crossbow outlier pulling it up in top-10 counts while its average across all builds is poor — a reminder that top-N counts can be misleading.

---

## Chapter 5: Cross-Validation with tftable

tftable provides independent Necessity calculations (different codebase, slightly different sample).

### Spearman Rank Correlations (3-way)

| Carry | Single vs Build | Single vs tftable | Build vs tftable |
|---|---|---|---|
| Vex | 0.929 | 0.976 | 0.905 |
| Fiora | 0.750 | 0.983 | 0.817 |
| Graves | 0.940 | 0.988 | 0.952 |

**Key finding**: Single-item Necessity agrees more with tftable than Build Necessity does. This is expected — tftable also uses single-item Necessity. But Build Necessity doesn't disagree dramatically (all ρ > 0.8 except Fiora at 0.817, dragged down by the Thief's Gloves effect).

The fact that our single-item pipeline matches tftable at ρ > 0.97 for all three carries confirms our Necessity implementation is correct. Build Necessity is a genuinely different perspective, not a calculation error.

---

## What I Learned

1. **Build Necessity and single-item Necessity largely agree** — Spearman ρ = 0.75–0.94 across three carries. For practical BIS recommendations, the two methods converge on the same top items. The question "do they differ?" has a clear answer: **not much, for the items that matter most.**

2. **Where they diverge is informative, not alarming:**
   - **Thief's Gloves** rises in Build Necessity because it *is* a complete build. Single-item Necessity undervalues it.
   - **High-synergy items** (Red Buff on Vex, Striker's Flail on Fiora) appear in top builds more often than their Build Necessity rank suggests — they're strong *components* that elevate combinations.
   - **Sustain redundancy** (Bloodthirster on Fiora) drops in Build Necessity because it overlaps with Sterak's Gage.

3. **Build Necessity doesn't eliminate survivorship bias** — it reduces it (per Dishsoap's insight) but the ≥200-game filter and the build-level AVP calculation still have selection effects. The convergence with single-item Necessity suggests bias correction is modest, not transformative.

4. **Top-N build counts are misleading** — Red Buff appears in 6/10 top Vex builds but ranks #5 by Build Necessity. Infinity Edge appears in 2/10 top Graves builds but has negative Build Necessity. Frequency in top builds ≠ marginal importance.

5. **The pipeline validates against tftable** — Single vs tftable ρ > 0.97 for all three carries. Our Necessity calculation is sound.

---

## Open Questions

1. **Can control variable analysis (fix 2, vary 1) be formalized as a metric?** It produced the most granular rankings in vex-nova95 but is currently manual. Could we automate it and compare with Build Necessity?

2. **Thief's Gloves paradox**: It ranks high by Build Necessity but never appears in a top-10 build. Is this because its *average* performance is good but its *ceiling* is capped (random items can't be optimized)?

3. **Does build-level analysis reveal synergies?** We computed Build Necessity per item, but we haven't looked at whether specific *pairs* consistently outperform. E.g., does Red Buff + Rabadon on Vex have super-additive Necessity?

---

## Questions for Xing

1. **Convergence = validation or tautology?** Single-item and Build Necessity largely agree. Is this a reassuring validation that both methods work, or is it expected because builds are just 3× single items? When *should* we expect divergence?

2. **Thief's Gloves**: It rises in Build Necessity because it occupies all 3 slots. In tftable, how is Thief's Gloves handled — does it count as one item or three?

3. **Red Buff's build frequency**: Red Buff appears in 6/10 top Vex builds but ranks #5 by Build Necessity. Is this the kind of signal the control variable method captures better than Necessity?

4. **Next step for Module 3**: This experiment validates that single-item Necessity is sufficient for most ranking purposes. Should we move on to Module 4 (Unit Evaluation), or is there more to extract from build analysis?

---

## Sources
- MetaTFT Explorer API: `unit_items_unique`, `unit_builds` endpoints
- tftable ground truth via SSH (`python3 cli.py tftable`)
- [[concepts/metrics]] — Necessity definition
- [[methods/build-analysis]] — control variable, consistency check
- [[experiments/vex-nova95]] — prior build + single-item comparison

---

## Review

