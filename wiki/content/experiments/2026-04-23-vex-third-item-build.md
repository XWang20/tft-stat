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

Before analyzing builds, confirm the single-item picture. All queries use `--normal-only` to exclude artifact/radiant/trait/emblem items.

### nova_95 (186,815 games, overall AVP 4.21)

| Rank | Item | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Guinsoo's Rageblade | 170,652 | 91% | 4.13 | +0.766 |
| 2 | Giant Slayer | 76,114 | 41% | 4.05 | +0.108 |
| 3 | Hextech Gunblade | 58,580 | 31% | 4.03 | +0.080 |
| 4 | Striker's Flail | 30,757 | 16% | 3.85 | +0.069 |
| 5 | Rabadon's Deathcap | 19,534 | 10% | 3.83 | +0.043 |
| 6 | Red Buff | 14,077 | 8% | 3.78 | +0.034 |
| 7 | Archangel's Staff | 18,283 | 10% | 4.02 | +0.021 |
| 8 | Morellonomicon | 7,739 | 4% | 4.03 | +0.008 |
| 9 | Jeweled Gauntlet | 42,583 | 23% | 4.19 | +0.006 |

### vex_95 (117,491 games, overall AVP 3.83)

| Rank | Item | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Guinsoo's Rageblade | 113,510 | 97% | 3.82 | +0.483 |
| 2 | Giant Slayer | 67,665 | 58% | 3.76 | +0.103 |
| 3 | Rabadon's Deathcap | 18,448 | 16% | 3.66 | +0.033 |
| 4 | Hextech Gunblade | 33,685 | 29% | 3.79 | +0.019 |
| 5 | Void Staff | 29,849 | 25% | 3.82 | +0.006 |
| 6 | Striker's Flail | 11,350 | 10% | 3.80 | +0.004 |
| 7 | Red Buff | 3,825 | 3% | 3.78 | +0.002 |
| 8 | Jeweled Gauntlet | -- | -- | -- | -- |

**Observation**: Guinsoo is undisputed #1 in both comps (Necessity 7x higher than #2 in nova_95, 5x in vex_95). Giant Slayer is a clear #2. The community consensus holds.

But the single-item picture already hints at a cross-comp difference: in nova_95, Gunblade (#3) and Flail (#4) are close behind GS. In vex_95, Dcap (#3) pulls ahead of Gunblade (#4) by a wider margin.

---

## Chapter 2: Build Analysis -- Controlling for GS + Guinsoo

This is the core experiment. Fix Giant Slayer + Guinsoo's Rageblade, then rank the third item by **Build Necessity** (not raw AVP -- lesson #3).

Build Necessity within the GS+Guinsoo subset: `p/(1-p) * (overall_GS_Guinsoo_AVP - build_AVP)`, where p = build play rate within the GS+Guinsoo population. All build data uses `--normal-only` to exclude artifact/radiant/trait/emblem items.

### nova_95: GS + Guinsoo + X (64,332 games, overall GS+Guinsoo AVP 3.968)

| Rank | Third Item | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | **Striker's Flail** | 8,769 | 13.6% | 3.80 | **+0.027** |
| 2 | **Red Buff** | 2,681 | 4.2% | 3.58 | **+0.017** |
| 3 | **Rabadon's Deathcap** | 4,961 | 7.7% | 3.77 | **+0.016** |
| 4 | Archangel's Staff | 3,779 | 5.9% | 3.89 | +0.005 |
| 5 | Hextech Gunblade | 22,592 | 35.1% | 3.96 | +0.002 |
| 6 | Nashor's Tooth | 1,054 | 1.6% | 3.83 | +0.002 |
| 7 | Morellonomicon | 1,524 | 2.4% | 3.97 | +0.000 |
| 8 | Void Staff | 4,987 | 7.8% | 4.20 | -0.020 |
| 9 | **Jeweled Gauntlet** | 11,148 | **17.3%** | 4.10 | **-0.028** |

**Key findings in nova_95**:

1. **Striker's Flail is the best third item by Necessity** (+0.027). It has both decent play rate (13.6%) and strong AVP (3.80), making it the most reliably impactful choice.

2. **Red Buff** (+0.017) and **Dcap** (+0.016) are effectively tied at #2-3. Red Buff has better AVP (3.58) but its low play rate (4.2%) limits Necessity -- the low play rate may reflect survivorship bias (only built when ahead/lucky with components). Dcap has more stable play rate (7.7%).

3. **Hextech Gunblade is near-neutral** (+0.002). Despite 35.1% play rate (the most popular third item), its AVP (3.96) is nearly identical to the GS+Guinsoo baseline (3.968). Gunblade is the "default" choice, not the optimal one.

4. **Jeweled Gauntlet is the worst** (-0.028). High play rate (17.3%) combined with bad AVP (4.10) = large negative Necessity. JG actively drags down the average.

### vex_95: GS + Guinsoo + X (61,867 games, overall GS+Guinsoo AVP 3.720)

| Rank | Third Item | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | **Rabadon's Deathcap** | 9,942 | 16.1% | 3.59 | **+0.025** |
| 2 | **Void Staff** | 13,358 | 21.6% | 3.65 | **+0.019** |
| 3 | **Hextech Gunblade** | 14,830 | 24.0% | 3.66 | **+0.018** |
| 4 | Archangel's Staff | 2,958 | 4.8% | 3.70 | +0.001 |
| 5 | Red Buff | 926 | 1.5% | 3.76 | -0.001 |
| 6 | Nashor's Tooth | 606 | 1.0% | 4.13 | -0.004 |
| 7 | Morellonomicon | 528 | 0.9% | 4.33 | -0.005 |
| 8 | Striker's Flail | 2,546 | 4.1% | 3.91 | -0.008 |
| 9 | **Jeweled Gauntlet** | 14,517 | **23.5%** | 3.79 | **-0.020** |

**Key findings in vex_95**:

1. **Rabadon's Deathcap is the clear winner** (+0.025) -- strong AVP (3.59) and solid play rate (16.1%). Not a low-frequency fluke.

2. **Void Staff** (+0.019) and **Gunblade** (+0.018) are effectively tied at #2-3. In nova_95 Void Staff has large negative Necessity (-0.020). The DRX trait in nova_95 likely provides sufficient magic penetration, making Void Staff redundant; without DRX (vex_95), Void Staff fills a crucial gap.

3. **Gunblade is positive in vex_95** (+0.018) but near-neutral in nova_95 (+0.002). The Blitzcrank + Mordekaiser frontline in vex_95 may keep Vex alive longer, amplifying spell vamp value.

4. **Striker's Flail drops sharply**: from #1 in nova_95 (+0.027) to #8 in vex_95 (-0.008). The DRX shell (nova_95) seems to amplify on-hit items.

5. **JG remains the worst** (-0.020) -- same pattern as nova_95. High play rate (23.5%), bad AVP (3.79), large negative Necessity.

---

## Chapter 3: Cross-Comp Comparison (nova_95 vs vex_95)

### Direct comparison: GS + Guinsoo + X (by Necessity)

| Third Item | nova_95 Nec | nova_95 Rank | vex_95 Nec | vex_95 Rank | Shift |
|---|---|---|---|---|---|
| Striker's Flail | **+0.027** | **#1** | -0.008 | #8 | down 7 |
| Red Buff | +0.017 | #2 | -0.001 | #5 | down 3 |
| Rabadon's Deathcap | +0.016 | #3 | **+0.025** | **#1** | **up 2** |
| Hextech Gunblade | +0.002 | #5 | +0.018 | #3 | up 2 |
| Void Staff | -0.020 | #8 | +0.019 | **#2** | **up 6** |
| Jeweled Gauntlet | -0.028 | #9 | -0.020 | #9 | same |

The answer to the third-item question **changes dramatically between comps**:

1. **Striker's Flail is the biggest mover** -- from #1 (+0.027) in nova_95 to #8 (-0.008) in vex_95. The DRX shell amplifies on-hit items, while vex_95's shell does not.

2. **Void Staff swings massively** -- from #8 (-0.020) in nova_95 to #2 (+0.019) in vex_95. The DRX trait likely provides sufficient magic penetration, making Void Staff redundant in nova_95. Without DRX (vex_95), Void Staff fills a crucial gap.

3. **Dcap is universally good** -- top 3 in both comps. The safest "always right" third item.

4. **Gunblade performs much better in vex_95** (#3, +0.018) than nova_95 (#5, +0.002) -- possibly because the Blitzcrank + Mordekaiser frontline keeps Vex alive longer, amplifying the value of sustained healing.

5. **JG is consistently the worst** in both comps. High play rate + below-baseline AVP = negative Necessity everywhere.

### Consistency Check

To validate these rankings, I ranked each item across all valid base pairs (not just GS+Guinsoo) and averaged their percentile ranks. All data uses `--normal-only`.

**nova_95 consistency** (lower % = more consistently good):

| Item | Avg Rank% | Pairs | Interpretation |
|---|---|---|---|
| Flail | 13.8% | 7 | Consistently top-tier |
| Dcap | 20.0% | 7 | Solid |
| Red Buff | 33.3% | 6 | Solid |
| Gunblade | 41.9% | 7 | Average-good |
| GS | 61.4% | 7 | Average (as third item) |
| JG | 80.0% | 7 | Consistently weak |
| Void Staff | 92.4% | 7 | Consistently worst |

**vex_95 consistency**:

| Item | Avg Rank% | Pairs | Interpretation |
|---|---|---|---|
| Dcap | 15.7% | 5 | Consistently top-tier |
| GS | 38.1% | 7 | Average-good |
| Red Buff | 39.2% | 4 | Average-good |
| Void Staff | 50.7% | 7 | Average |
| Flail | 52.0% | 5 | Average |
| Gunblade | 61.1% | 6 | Average |
| JG | 78.6% | 7 | Below average |

**Dcap is the only item that is consistently top-tier in both comps.** Flail dominates nova_95 but drops to average in vex_95. Void Staff goes from worst (92.4%) in nova_95 to average (50.7%) in vex_95.

---

## Chapter 4: Challenging the Premise

Is GS + Guinsoo truly the best first-two-item core? I used Build Necessity to compare core pairs using `--normal-only` data. Each core pair is treated as a build choice within the Vex 3-item population.

### nova_95 (154,226 total Vex 3-item games, overall AVP 4.066)

| Core | W-AVP | Games | Rate | Necessity |
|---|---|---|---|---|
| Guinsoo + GS + X | 4.00 | 71,623 | 46.4% | **+0.055** |
| Guinsoo + Gunblade + X | 3.97 | 54,682 | 35.5% | +0.053 |
| Guinsoo + Dcap + X | **3.76** | 16,748 | 10.9% | +0.038 |
| Guinsoo + JG + X | 4.11 | 38,202 | 24.8% | -0.013 |
| Guinsoo + no-GS + X | 4.12 | 81,690 | 53.0% | -0.057 |

### vex_95 (104,487 total Vex 3-item games, overall AVP 3.756)

| Core | W-AVP | Games | Rate | Necessity |
|---|---|---|---|---|
| Guinsoo + GS + X | 3.72 | 64,356 | 61.6% | **+0.057** |
| Guinsoo + Dcap + X | **3.61** | 16,614 | 15.9% | +0.027 |
| Guinsoo + Gunblade + X | 3.74 | 31,742 | 30.4% | +0.005 |
| Guinsoo + JG + X | 3.81 | 36,314 | 34.8% | -0.027 |
| Guinsoo + no-GS + X | 3.81 | 40,079 | 38.4% | -0.035 |

**By Necessity, Guinsoo + GS is actually the best core in both comps** (+0.055 and +0.057). Its high play rate (46-62%) amplifies its moderate AVP advantage into the highest Necessity. The community consensus is validated.

Guinsoo + Dcap has the best raw AVP in both comps (3.76/3.61), but its much lower play rate (11-16%) limits its Necessity. The low play rate itself may reflect selection bias: players who build Dcap early may be in stronger game states or have better component luck.

The top builds by Necessity (min 300 games) in **nova_95**:

1. Guinsoo + Gunblade + GS (+0.018, 22,589 games, 3.96 AVP)
2. Guinsoo + GS + Flail (+0.016, 8,768 games, 3.80 AVP)
3. Guinsoo + Gunblade + Flail (+0.012, 5,553 games, 3.75 AVP)
4. Guinsoo + GS + Dcap (+0.010, 4,962 games, 3.77 AVP)
5. Guinsoo + GS + Red Buff (+0.009, 2,681 games, 3.58 AVP)

And in **vex_95**:

1. Guinsoo + GS + Dcap (+0.018, 9,945 games, 3.59 AVP)
2. Guinsoo + Gunblade + GS (+0.015, 14,828 games, 3.66 AVP)
3. Guinsoo + GS + Void Staff (+0.015, 13,359 games, 3.65 AVP)
4. Guinsoo + JG + Flail (+0.012, 4,479 games, 3.48 AVP)
5. Guinsoo + Gunblade + Dcap (+0.004, 2,293 games, 3.57 AVP)

In both comps, Guinsoo + GS builds dominate the top Necessity rankings. The most popular build in nova_95 (Guinsoo + Gunblade + GS, 22,589 games) has the highest Necessity (+0.018) -- here the community default is actually optimal by this metric.

**JG-core builds consistently show negative Necessity** (-0.013 / -0.027), confirming JG is a trap item across all analyses.

---

## Cross-Validation

tftable was unavailable during this experiment (SSH timeout to desktop). Cross-validation deferred.

However, the internal consistency check (7+ base pairs x 2 comps) serves as partial validation. The consistency of Dcap's dominance across nearly all pairs and both comps provides convergent evidence from multiple independent "experiments" within the data.

---

## What I Learned

1. **The third item answer depends on the comp** (by Build Necessity, `--normal-only`):
   - **nova_95**: Striker's Flail (+0.027) > Red Buff (+0.017) > Dcap (+0.016) >> Gunblade (+0.002) >> JG (-0.028)
   - **vex_95**: Dcap (+0.025) > Void Staff (+0.019) > Gunblade (+0.018) >> Flail (-0.008) >> JG (-0.020)
   - **Dcap is the universal safe pick** -- positive Necessity in both comps, consistently top-tier across base pairs.

2. **Hextech Gunblade is near-neutral in nova_95** (+0.002): 35% play rate but AVP nearly identical to baseline. Gunblade is the "default" choice, not the optimal one. In vex_95 it's solidly positive (+0.018) -- comp context matters.

3. **Jeweled Gauntlet is the worst in both comps**: largest negative Necessity (-0.028 / -0.020). High play rate + bad AVP = actively dragging down average placement. JG is a trap.

4. **Void Staff is comp-dependent**: -0.020 in nova_95 (DRX provides magic pen), +0.019 in vex_95 (no DRX, needs magic pen). This is a clear example of how trait context changes item value.

5. **Striker's Flail is the biggest cross-comp mover**: #1 in nova_95 (+0.027) but #8 in vex_95 (-0.008). The DRX shell amplifies on-hit items.

6. **Guinsoo + GS core is validated by Necessity**: despite Dcap-core having lower raw AVP, the GS-core's much higher play rate gives it the highest Build Necessity in both comps. The community consensus on core items is sound.

7. **`--normal-only` matters**: excluding artifact/radiant/trait/emblem items changes sample sizes noticeably (nova_95: 186k vs 240k games). Mixing normal and special items pollutes Necessity rankings.

---

## Open Questions

1. **Why is Dcap-core AVP so much better?** Is it a genuine item strength, or are Dcap-builders systematically different players (higher skill, better game state)? Would need per-round data or player-level analysis to disentangle.

2. **Red Buff in vex_95**: Only 926 games in the GS+Guinsoo+Red Buff build. Is the lack of data because Red Buff is genuinely bad in this comp, or because players don't build it? The consistency check puts it at 39.2% avg rank (4 pairs), which is average-good -- but small sample.

3. **Void Staff's comp sensitivity**: The DRX trait hypothesis (DRX provides magic pen, making Void Staff redundant) is plausible but untested. Could test by looking at Void Staff performance in other comps with/without DRX.

4. **Is the "Gunblade trap" real in nova_95?** If Gunblade is near-neutral (+0.002), why do 35% of players build it? Possible explanations: (a) it "feels" good because of healing visibility, (b) it was BIS in a previous patch and the meta hasn't updated, (c) component availability (Gunblade components are more flexible).

---

## Questions for Xing

1. **Dcap vs GS as second item**: Dcap-core has better raw AVP but lower Necessity than GS-core. Is the AVP gap a selection bias artifact? In your experience, do better players prioritize Dcap components?

2. **Void Staff comp-dependency**: My hypothesis is that DRX provides magic pen that makes Void Staff redundant in nova_95 but necessary in vex_95. Does this match your understanding of the trait mechanics?

3. **Red Buff's low play rate in vex_95**: Only 1.5% play rate in vex_95 vs 4.2% in nova_95 (in GS+Guinsoo builds). Is there a gameplay reason (e.g., Red Buff components are contested by the Blitzcrank/Mordekaiser frontline)?

4. **Next step**: Should we formalize the consistency check (rank across base pairs) as a standard metric in the pipeline? It seems more informative than Build Necessity alone for the "which third item" question.

---

## Sources
- MetaTFT Explorer API: `unit_items_unique`, `unit_builds` endpoints (all queries with `--normal-only`)
- [[concepts/metrics]] -- Necessity definition
- [[methods/build-analysis]] -- control variable method
- [[experiments/2026-04-21-vex-nova95-items]] -- prior Vex item analysis
- [[experiments/2026-04-22-build-vs-single-necessity]] -- build necessity methodology
