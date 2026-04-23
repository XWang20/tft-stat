# Experiment: Vex Third Item -- Build Analysis Settles the Community Debate
**Status**: 🧪 draft
**Date**: 2026-04-23
**Module**: 2 (Item Metrics) / 3 (Build Analysis)

---

## The Question

Community consensus puts Giant Slayer + Guinsoo's Rageblade as Vex's first two items. The debate is the third slot:

- **Hextech Gunblade** -- spell vamp + survivability
- **Jeweled Gauntlet** -- crit spell damage
- **Rabadon's Deathcap** -- pure AP
- **Red Buff** -- anti-heal burn
- **Striker's Flail** -- on-hit damage

**Core question**: Given GS + Guinsoo as the base, which third item performs best? Does the answer change between nova_95 (DRX shell with Fiora/Graves) and vex_95 (Blitzcrank + Mordekaiser shell)?

This is decision-oriented: players face this choice every game when they've slammed Guinsoo + GS and need to pick a third.

---

## Chapter 1: Single-Item Necessity Baseline

Before analyzing builds, confirm the single-item picture.

### nova_95 (239,705 games, overall AVP 4.17)

| Rank | Item | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Guinsoo's Rageblade | 211,402 | 88% | 4.10 | +0.488 |
| 2 | Giant Slayer | 91,275 | 38% | 4.03 | +0.088 |
| 3 | Hextech Gunblade | 70,661 | 29% | 3.99 | +0.074 |
| 4 | Striker's Flail | 36,849 | 15% | 3.83 | +0.062 |
| 5 | Rabadon's Deathcap | 23,394 | 10% | 3.80 | +0.040 |
| 6 | Red Buff | 17,016 | 7% | 3.75 | +0.032 |
| 7 | Archangel's Staff | 22,159 | 9% | 3.99 | +0.019 |
| 8 | Morellonomicon | 9,214 | 4% | 4.00 | +0.007 |
| 9 | Jeweled Gauntlet | 52,384 | 22% | 4.15 | +0.005 |

### vex_95 (154,575 games, overall AVP 3.82)

| Rank | Item | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Guinsoo's Rageblade | 142,449 | 92% | 3.81 | +0.128 |
| 2 | Giant Slayer | 81,622 | 53% | 3.74 | +0.091 |
| 3 | Rabadon's Deathcap | 21,804 | 14% | 3.63 | +0.031 |
| 4 | Hextech Gunblade | 40,797 | 26% | 3.77 | +0.017 |
| 5 | Void Staff | 35,525 | 23% | 3.81 | +0.004 |
| 6 | Striker's Flail | 13,295 | 9% | 3.79 | +0.003 |
| 7 | Red Buff | 4,718 | 3% | 3.77 | +0.002 |
| 8 | Jeweled Gauntlet | (not top 7) | -- | -- | -- |

**Observation**: Guinsoo is undisputed #1 in both comps (Necessity 3-5x higher than #2). Giant Slayer is a clear #2. The community consensus holds.

But the single-item picture already hints at a cross-comp difference: in nova_95, Gunblade (#3) and Flail (#4) are close behind GS. In vex_95, Dcap (#3) pulls ahead of Gunblade (#4) by a wider margin.

---

## Chapter 2: Build Analysis -- Controlling for GS + Guinsoo

This is the core experiment. Fix Giant Slayer + Guinsoo's Rageblade, then rank the third item by **Build Necessity** (not raw AVP — lesson #3).

Build Necessity within the GS+Guinsoo subset: `p/(1-p) × (overall_GS_Guinsoo_AVP - build_AVP)`, where p = build play rate within the GS+Guinsoo population.

### nova_95: GS + Guinsoo + X (73,516 games, overall GS+Guinsoo AVP 3.895)

| Rank | Third Item | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | **Striker's Flail** | 9,348 | 12.7% | 3.76 | **+0.020** |
| 2 | **Red Buff** | 2,878 | 3.9% | 3.51 | **+0.016** |
| 3 | **Rabadon's Deathcap** | 5,247 | 7.1% | 3.74 | **+0.012** |
| 4 | Guinsoo's ★2 | 4,421 | 6.0% | 3.74 | +0.010 |
| 5 | Archangel's Staff | 4,004 | 5.4% | 3.85 | +0.003 |
| 6 | Nashor's Tooth | 1,106 | 1.5% | 3.80 | +0.002 |
| 7 | Radiant Hextech Gunblade | 542 | 0.7% | 3.92 | -0.000 |
| 8 | Morellonomicon | 1,622 | 2.2% | 3.93 | -0.001 |
| 9 | **Hextech Gunblade** | 23,679 | **32.2%** | 3.92 | **-0.012** |
| 10 | Void Staff | 5,293 | 7.2% | 4.17 | -0.021 |
| 11 | **Jeweled Gauntlet** | 11,784 | **16.0%** | 4.07 | **-0.033** |

**Key findings in nova_95**:

1. **Striker's Flail is the best third item by Necessity** (+0.020). It has both decent play rate (12.7%) and strong AVP (3.76), making it the most reliably impactful choice. Red Buff has better AVP (3.51) but its low play rate (3.9%) limits its Necessity — the low play rate may reflect survivorship bias (only built when ahead/lucky with components).

2. **Rabadon's Deathcap** (+0.012) is a solid #3 — good AVP and reasonable play rate.

3. **Hextech Gunblade has negative Necessity** (-0.012). Despite 32.2% play rate, its AVP (3.92) is barely better than the GS+Guinsoo baseline (3.895). The massive play rate means its "without" AVP is almost the same — Gunblade contributes almost nothing to placement improvement. Players default to it but it's actively worse than the population average.

4. **Jeweled Gauntlet is the worst** (-0.033). High play rate (16.0%) combined with bad AVP (4.07) = large negative Necessity. JG actively drags down the average.

### vex_95: GS + Guinsoo + X (70,035 games, overall GS+Guinsoo AVP 3.678)

| Rank | Third Item | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | **Rabadon's Deathcap** | 10,236 | 14.6% | 3.57 | **+0.018** |
| 2 | **Void Staff** | 13,997 | 20.0% | 3.63 | **+0.012** |
| 3 | **Hextech Gunblade** | 15,368 | 21.9% | 3.65 | **+0.008** |
| 4 | Guinsoo's ★2 | 2,118 | 3.0% | 3.64 | +0.001 |
| 5 | Red Buff | 959 | 1.4% | 3.69 | -0.000 |
| 6 | Archangel's Staff | 3,074 | 4.4% | 3.70 | -0.001 |
| 7 | Nashor's Tooth | 630 | 0.9% | 3.96 | -0.003 |
| 8 | Striker's Flail | 2,662 | 3.8% | 3.91 | -0.009 |
| 9 | **Jeweled Gauntlet** | 15,131 | **21.6%** | 3.77 | **-0.025** |

**Key findings in vex_95**:

1. **Rabadon's Deathcap is the clear winner** (+0.018) — strong AVP (3.57) and solid play rate (14.6%). Not a low-frequency fluke.

2. **Void Staff at #2** (+0.012). In nova_95 it has negative Necessity (-0.021). The DRX trait in nova_95 likely provides sufficient magic penetration, making Void Staff redundant; without DRX (vex_95), Void Staff fills a crucial gap.

3. **Gunblade is positive in vex_95** (+0.008) but negative in nova_95 (-0.012). The Blitzcrank + Mordekaiser frontline in vex_95 may keep Vex alive longer, amplifying spell vamp value.

4. **JG remains the worst** (-0.025) — same pattern as nova_95. High play rate, bad AVP, large negative Necessity.

3. **Gunblade is acceptable here** (#4, AVP 3.65) -- much closer to the top than in nova_95 (#8, AVP 3.92). The 0.27 AVP gap between the two comps suggests Gunblade's value is context-dependent.

4. **JG is mediocre in both comps**: 21.6% play rate but AVP 3.77 in vex_95. Better than in nova_95 (4.07) but still below average.

5. **Striker's Flail drops sharply**: from #4 in nova_95 to #8 in vex_95. The DRX shell (nova_95) seems to amplify on-hit items.

---

## Chapter 3: Cross-Comp Comparison (nova_95 vs vex_95)

### Direct comparison: GS + Guinsoo + X (by Necessity)

| Third Item | nova_95 Nec | nova_95 Rank | vex_95 Nec | vex_95 Rank | Shift |
|---|---|---|---|---|---|
| Striker's Flail | +0.020 | **#1** | -0.009 | #8 | down 7 |
| Red Buff | +0.016 | #2 | -0.000 | #5 | down 3 |
| Rabadon's Deathcap | +0.012 | #3 | **+0.018** | **#1** | **up 2** |
| Hextech Gunblade | -0.012 | #9 | +0.008 | #3 | up 6 |
| Void Staff | -0.021 | #10 | +0.012 | **#2** | **up 8** |
| Jeweled Gauntlet | -0.033 | #11 | -0.025 | #9 | up 2 |

The answer to the third-item question **changes dramatically between comps**:

1. **Void Staff is the biggest mover** -- from near-bottom (#11) in nova_95 to #2 in vex_95. The DRX trait in nova_95 likely provides sufficient magic penetration, making Void Staff redundant. Without DRX (vex_95), Void Staff fills a crucial gap.

2. **Red Buff and Striker's Flail are nova_95-specific strengths**. Both benefit from the aggressive DRX + AD carry shell (Fiora, Graves alongside Vex).

3. **Dcap is universally good** -- top 2 in both comps. The safest "always right" third item.

4. **Gunblade performs much better in vex_95** -- possibly because the Blitzcrank + Mordekaiser frontline keeps Vex alive longer, amplifying the value of sustained healing.

### Consistency Check

To validate these rankings, I ranked each item across 7 different base pairs (not just GS+Guinsoo) and averaged their percentile ranks:

**nova_95 consistency** (lower % = more consistently good):

| Item | Avg Rank% | Interpretation |
|---|---|---|
| Dcap | 3.4% | Consistently #1-2 across all 6 pairs |
| Red Buff | 9.4% | Consistently top 2-3 |
| Morello | 25.2% | Moderate (benefits from some pairs more than others) |
| Flail | 29.8% | Solid across most pairs |
| Gunblade | 47.3% | Average -- middle of the pack |
| GS | 57.3% | Below average as a "third item" |
| JG | 75.3% | Consistently weak |
| Void Staff | 89.0% | Consistently worst |

**vex_95 consistency**:

| Item | Avg Rank% | Interpretation |
|---|---|---|
| Dcap | 11.3% | Best across most pairs |
| GS | 35.3% | Solid |
| Red Buff | 48.5% | Average (only 3 pairs had enough data) |
| Flail | 54.6% | Volatile -- #1 with JG, #5-6 with others |
| Void Staff | 56.8% | Moderate (much better than nova_95) |
| JG | 58.0% | Average |
| Gunblade | 59.9% | Average |

**Dcap is the only item that is consistently top-tier in both comps.** Red Buff is excellent in nova_95 but has insufficient build data in vex_95 to be conclusive.

---

## Chapter 4: Challenging the Premise

Is GS + Guinsoo truly the best first-two-item core? I compared weighted-average AVP across all builds containing different cores:

### nova_95

| Core | Weighted AVP | Games |
|---|---|---|
| Guinsoo + Dcap + X | **3.69** | 12,398 |
| Guinsoo + Gunblade + X | 3.93 | 34,722 |
| Guinsoo + GS + X | 3.96 | 75,932 |
| Guinsoo + no-GS + X | 4.07 | 86,536 |
| Guinsoo + JG + X | 4.06 | 28,920 |

### vex_95

| Core | Weighted AVP | Games |
|---|---|---|
| Guinsoo + Dcap + X | **3.61** | 6,821 |
| Guinsoo + GS + X | 3.69 | 68,939 |
| Guinsoo + Gunblade + X | 3.78 | 17,791 |
| Guinsoo + JG + X | 3.79 | 23,163 |
| Guinsoo + no-GS + X | 3.78 | 41,919 |

**Guinsoo + Dcap outperforms Guinsoo + GS in both comps.** The gap is large: 0.27 AVP in nova_95, 0.08 in vex_95.

But this result needs careful interpretation. Dcap-core builds are much rarer (12k vs 76k games in nova_95), and players who build Dcap early may be making better decisions overall (skill confound), or Dcap may be more available to players who are ahead (selection bias).

What's more convincing: **every top build list is dominated by Guinsoo + Dcap/Red Buff combinations, not Guinsoo + GS**. The top 5 builds in nova_95 are:

1. Guinsoo + Morello + Dcap (3.33 AVP, 334 games)
2. Guinsoo + Dcap + Red Buff (3.42, 906 games)
3. Guinsoo + Guinsoo + Dcap (3.47, 1,034 games)
4. Guinsoo + Flail + Dcap (3.50, 1,809 games)
5. Guinsoo + Guinsoo + Red Buff (3.50, 615 games)

Giant Slayer doesn't appear until build #7 (Guinsoo + GS + Red Buff, 3.51, 2,878 games).

The most popular build (Guinsoo + Gunblade + GS) with 23,679 games has AVP 3.92 -- 0.59 worse than the top build. Players massively converge on a suboptimal default.

This also holds in vex_95, where the #1 build without considering radiant items is:

1. Guinsoo + JG + Flail (3.47, 4,719 games)
2. Guinsoo + Gunblade + Dcap (3.55, 2,398 games)
3. Guinsoo + GS + Dcap (3.57, 10,236 games)

**Guinsoo is the true cornerstone** (appears in virtually every build). GS is the popular second item but may not be the best -- Dcap could be superior as a slam-early item. However, this finding is subject to the survivorship caveat: Dcap-first players may be stronger players or in better game states.

---

## Cross-Validation

tftable was unavailable during this experiment (SSH timeout to desktop). Cross-validation deferred.

However, the internal consistency check (7 base pairs x 2 comps) serves as partial validation. The consistency of Dcap's dominance across nearly all pairs and both comps provides convergent evidence from multiple independent "experiments" within the data.

---

## What I Learned

1. **The third item answer depends on the comp** (by Build Necessity):
   - **nova_95**: Striker's Flail (+0.020) > Red Buff (+0.016) > Dcap (+0.012) >> Gunblade (-0.012) >> JG (-0.033)
   - **vex_95**: Dcap (+0.018) > Void Staff (+0.012) > Gunblade (+0.008) >> JG (-0.025)
   - **Dcap is the universal safe pick** -- positive Necessity in both comps, consistent across base pairs.

2. **Hextech Gunblade has negative Necessity in nova_95** (-0.012): 32% play rate but AVP barely above baseline. Gunblade is the "default" choice, not the optimal one. In vex_95 it's slightly positive (+0.008) — comp context matters.

3. **Jeweled Gauntlet is the worst in both comps**: largest negative Necessity (-0.033 / -0.025). High play rate + bad AVP = actively dragging down average placement. JG is a trap.

4. **Void Staff is comp-dependent**: -0.021 in nova_95 (DRX provides magic pen), +0.012 in vex_95 (no DRX, needs magic pen). This is a clear example of how trait context changes item value.

5. **Striker's Flail is the biggest cross-comp mover**: #1 in nova_95 (+0.020) but #8 in vex_95 (-0.009). The DRX shell amplifies on-hit items.

6. **Red Buff's AVP ranking was misleading**: AVP ranked it #1 in nova_95, but Necessity puts it #2 behind Striker's Flail — its low play rate (3.9%) limits its weighted impact. This is exactly why Build Necessity matters even in control variable analysis.

---

## Open Questions

1. **Why is Dcap-core so much better?** Is it a genuine item strength, or are Dcap-builders systematically different players (higher skill, better game state)? Would need per-round data or player-level analysis to disentangle.

2. **Red Buff in vex_95**: Only 959 games in the GS+Guinsoo+Red Buff build. Is the lack of data because Red Buff is genuinely bad in this comp, or because players don't build it? The 3 pairs with data show it at #5 (avg rank% 48.5%), which is middling -- a far cry from its dominance in nova_95.

3. **Void Staff's comp sensitivity**: The DRX trait hypothesis (DRX provides magic pen, making Void Staff redundant) is plausible but untested. Could test by looking at Void Staff performance in other comps with/without DRX.

4. **Is the "Gunblade trap" a coordination failure?** If Gunblade is suboptimal, why do 32% of players build it? Possible explanations: (a) it "feels" good because of healing visibility, (b) it was BIS in a previous patch and the meta hasn't updated, (c) component availability (Gunblade components are more flexible).

---

## Questions for Xing

1. **Dcap vs GS as second item**: The data suggests Guinsoo + Dcap outperforms Guinsoo + GS. Is this a real finding or a selection bias artifact? In your experience, do better players prioritize Dcap components?

2. **Void Staff comp-dependency**: My hypothesis is that DRX provides magic pen that makes Void Staff redundant in nova_95 but necessary in vex_95. Does this match your understanding of the trait mechanics?

3. **Red Buff's low play rate in vex_95**: Only 3% play rate in vex_95 vs 7% in nova_95. Is there a gameplay reason (e.g., Red Buff components are contested by the Blitzcrank/Mordekaiser frontline)?

4. **Next step**: Should we formalize the consistency check (rank across base pairs) as a standard metric in the pipeline? It seems more informative than Build Necessity for the "which third item" question.

---

## Sources
- MetaTFT Explorer API: `unit_items_unique`, `unit_builds` endpoints
- [[concepts/metrics]] -- Necessity definition
- [[methods/build-analysis]] -- control variable method
- [[experiments/2026-04-21-vex-nova95-items]] -- prior Vex item analysis
- [[experiments/2026-04-22-build-vs-single-necessity]] -- build necessity methodology
