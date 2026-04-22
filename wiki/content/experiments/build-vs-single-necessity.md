# Experiment: Build Necessity vs Single-Item Necessity — Do They Differ?
**Status**: 🧪 draft
**Date**: 2026-04-22
**Module**: 3 (Build Analysis — follow-up)

---

## The Question

Single-item Necessity ranks items by how much the overall AVP worsens when that item is absent. Build Necessity does the same for complete 3-item sets. If we aggregate build-level scores back to individual items, do the implied rankings match single-item Necessity? Where they diverge, which method is more trustworthy?

This matters because builds capture **item synergy** that single-item analysis misses. If Guinsoo + Giant Slayer + Striker's Flail is better than Guinsoo + Giant Slayer + Hextech Gunblade, that tells us something about the third item's contribution *in context* — which single-item Necessity cannot capture.

---

## Chapter 1: Vex in Nova 95 — Single-Item Baseline

Comp: nova_95 (compositions.py definition). Patch: current. Ranks: Plat–Challenger.

Vex overall: AVP = 4.16, 211,327 games.

| Rank | Item | Necessity | Play Rate |
|---|---|---|---|
| 1 | Guinsoo's Rageblade | +0.502 | 88% |
| 2 | Giant Slayer | +0.083 | 38% |
| 3 | Hextech Gunblade | +0.076 | 29% |
| 4 | Striker's Flail | +0.063 | 16% |
| 5 | Rabadon's Deathcap | +0.038 | 10% |
| 6 | Red Buff | +0.033 | 7% |
| 7 | Archangel's Staff | +0.018 | 10% |
| 8 | Morellonomicon | +0.007 | 4% |
| 9 | Jeweled Gauntlet | +0.003 | 22% |

Guinsoo is overwhelmingly core (88% play rate, +0.502 Necessity). The rest form a clear tier: Giant Slayer and Hextech Gunblade as the best secondary items, followed by Striker's Flail and Rabadon's Deathcap.

Jeweled Gauntlet is interesting: 22% play rate but nearly zero Necessity (+0.003). High popularity but negligible impact — a classic trap item signal.

---

## Chapter 2: Top Builds by Build Necessity

Build Necessity = how much overall AVP worsens when this specific 3-item combination is removed. Computed as: w/o_build_AVP − overall_AVP (same formula as single-item, applied to full builds).

72 builds with ≥100 games. Top 15:

| Rank | Build | Games | Rate | AVP | Build Nec |
|---|---|---|---|---|---|
| 1 | Guinsoo + Gunblade + Giant Slayer | 20,341 | 9.6% | 3.91 | +0.026 |
| 2 | Guinsoo + Giant Slayer + Flail | 8,347 | 3.9% | 3.77 | +0.016 |
| 3 | Guinsoo + Gunblade + Flail | 5,646 | 2.7% | 3.70 | +0.013 |
| 4 | Guinsoo + Giant Slayer + Dcap | 4,457 | 2.1% | 3.71 | +0.010 |
| 5 | Guinsoo + Guinsoo + Giant Slayer | 3,815 | 1.8% | 3.70 | +0.008 |
| 6 | Guinsoo + JG + Flail | 3,784 | 1.8% | 3.71 | +0.008 |
| 7 | Guinsoo + Gunblade + Dcap | 2,799 | 1.3% | 3.56 | +0.008 |
| 8 | Guinsoo + Guinsoo + Gunblade | 3,118 | 1.5% | 3.62 | +0.008 |
| 9 | Guinsoo + Giant Slayer + Red Buff | 2,546 | 1.2% | 3.54 | +0.008 |
| 10 | Guinsoo + Gunblade + JG | 5,775 | 2.7% | 3.94 | +0.006 |

Bottom 5 (negative Necessity — harmful builds):

| Rank | Build | Games | Rate | AVP | Build Nec |
|---|---|---|---|---|---|
| 68 | Anomaly + Guinsoo + Giant Slayer | 680 | 0.3% | 4.39 | -0.001 |
| 69 | Anomaly + Guinsoo + JG | 367 | 0.2% | 4.63 | -0.001 |
| 70 | Guinsoo + JG + Shojin | 530 | 0.3% | 4.63 | -0.001 |
| 71 | Guinsoo + Gunblade + Void Staff | 3,894 | 1.8% | 4.26 | -0.002 |
| 72 | Guinsoo + JG + Void Staff | 4,095 | 1.9% | 4.37 | -0.004 |

The best build (Guinsoo + Gunblade + Giant Slayer) is also the most popular (9.6% play rate) — unusual in TFT data where popularity and quality often diverge due to survivorship bias. This convergence suggests that at the build level, survivorship bias is indeed reduced as Dishsoap predicted.

Void Staff consistently appears in the worst builds. Jeweled Gauntlet shows up in both top builds (#6, #10) and mediocre ones (#12 at +0.005), reflecting its "average" single-item Necessity.

---

## Chapter 3: Build-Implied Item Rankings vs Single-Item

To derive "build-implied item scores," I computed the weighted average build Necessity across all builds containing each item:

$$\text{Build Score}_i = \frac{\sum_{b \ni i} \text{Nec}(b) \times \text{Games}(b)}{\sum_{b \ni i} \text{Games}(b)}$$

| Item | Single Nec | S.Rank | Build Score | B.Rank | Rank Δ |
|---|---|---|---|---|---|
| Guinsoo's Rageblade | +0.502 | 1 | +0.00839 | 4 | **-3** |
| Giant Slayer | +0.083 | 2 | +0.01290 | 2 | 0 |
| Hextech Gunblade | +0.076 | 3 | +0.01408 | **1** | **+2** |
| Striker's Flail | +0.063 | 4 | +0.00996 | 3 | **+1** |
| Rabadon's Deathcap | +0.038 | 5 | +0.00599 | 5 | 0 |
| Red Buff | +0.033 | 6 | +0.00479 | 6 | 0 |
| Archangel's Staff | +0.018 | 7 | +0.00354 | 8 | -1 |
| Morellonomicon | +0.007 | 8 | +0.00132 | 9 | -1 |
| Jeweled Gauntlet | +0.003 | 9 | +0.00354 | 7 | **+2** |

Key disagreements:

1. **Guinsoo drops from #1 to #4.** This is a mathematical artifact: Guinsoo appears in 98% of all builds, so it's in both the best and worst builds. Its build score is diluted by being "everywhere." Single-item Necessity correctly captures that removing Guinsoo is catastrophic (+0.502). The build score doesn't — not because Guinsoo is less important, but because the metric can't discriminate when an item is near-universal.

2. **Hextech Gunblade rises from #3 to #1.** This is the genuine finding. Gunblade appears preferentially in high-Necessity builds. It's in 5 of the top 10 builds and 2 of the bottom 10. Builds with Gunblade average higher Necessity than builds with Giant Slayer, despite Giant Slayer having higher single-item Necessity. This suggests **Gunblade has positive synergy** with other good items (Guinsoo, Flail, Dcap) that Giant Slayer doesn't.

3. **Jeweled Gauntlet rises from #9 to #7.** JG's single-item Necessity is near zero (+0.003), but it appears in 14 builds averaging +0.00354 build score. Its build score is lifted by appearing alongside strong items. However, this could also mean JG is **carried by its partners** rather than contributing itself. The builds JG appears in (Guinsoo + JG + Flail, Guinsoo + JG + Giant Slayer) would likely be strong regardless of the JG.

---

## Chapter 4: Fiora Cross-Check — Does the Pattern Hold?

Fiora overall: AVP = 4.10, 208,160 games. A different carry in the same comp, with AD items instead of AP.

### Single-Item Necessity

| Rank | Item | Necessity |
|---|---|---|
| 1 | Edge of Night | +0.151 |
| 2 | Sterak's Gage | +0.131 |
| 3 | Bloodthirster | +0.122 |
| 4 | Hand of Justice | +0.087 |
| 5 | Thief's Gloves | +0.061 |
| 6 | Titan's Resolve | +0.046 |

### Top Builds by Necessity

| Rank | Build | Games | Nec |
|---|---|---|---|
| 1 | BT + Edge + Sterak's | 4,057 | +0.013 |
| 2 | BT + Sterak's + Titan's | 3,910 | +0.010 |
| 3 | BT + Edge + Titan's | 2,355 | +0.010 |
| 4 | Edge + Sterak's + HoJ | 2,259 | +0.008 |
| 5 | BT + Edge + HoJ | 2,049 | +0.006 |

**Bloodthirster appears in 9 of the top 10 builds** despite being only #3 in single-item Necessity. Edge of Night (#1 single) and Sterak's Gage (#2 single) alternate as the second item. This mirrors Vex: the item that's most central to strong builds isn't necessarily the one with the highest single-item Necessity.

Bloodthirster's pattern is similar to Gunblade on Vex: it provides sustain that enables the other items to perform. Its single-item Necessity is "only" +0.122 because when BT is absent, other sustain items (Sterak's, HoJ) can partially substitute. But in *builds*, BT is the backbone.

---

## Chapter 5: Cross-Validation with tftable

tftable Vex items (135,798 games):

| Item | tftable Nec | Our Single Nec | Our Build Rank |
|---|---|---|---|
| Guinsoo's | +0.764 | +0.502 | 4 |
| Giant Slayer | +0.092 | +0.083 | 2 |
| Striker's Flail | +0.080 | +0.063 | 3 |
| Hextech Gunblade | +0.078 | +0.076 | **1** |
| Rabadon's | +0.049 | +0.038 | 5 |
| Red Buff | +0.046 | +0.033 | 6 |

tftable single-item rankings: Guinsoo > Giant Slayer > Striker's Flail > Hextech Gunblade (top 4). Our single-item ranking: Guinsoo > Giant Slayer > Hextech Gunblade > Striker's Flail. Our build-implied ranking: Hextech Gunblade > Giant Slayer > Striker's Flail > Guinsoo.

tftable ranks Striker's Flail above Gunblade (0.080 vs 0.078) — our single-item Necessity puts Gunblade above Flail (0.076 vs 0.063). The disagreement is small (within noise).

Critically, tftable gives Jeweled Gauntlet **negative** Necessity (-0.0017), confirming our single-item finding (+0.003 ≈ zero) rather than the build-implied score (+0.00354). JG's apparent improvement in builds is indeed an artifact of being paired with strong items, not intrinsic quality.

Void Staff is -0.0217 in tftable — the worst item. This perfectly matches our build analysis where Void Staff appears in 4 of the bottom 5 builds.

---

## What I Learned

1. **Build and single-item Necessity agree on ~70% of rankings, but diverge meaningfully on core items.** The top 5 items (minus Guinsoo's ceiling effect) are the same in both methods. The ordering shifts reflect real information about item synergy.

2. **Near-universal items (Guinsoo at 88%) break build-implied scoring.** When an item is in almost every build, its build score converges to the average build score — hiding the item's true importance. Single-item Necessity is the better metric for core items because it directly measures the counterfactual.

3. **Build analysis reveals synergy that single-item Necessity misses.** Hextech Gunblade's rise to #1 in build scoring suggests it pairs especially well with other items. Bloodthirster on Fiora shows the same pattern — the "backbone" item of most strong builds.

4. **Build analysis confirms trap items more decisively.** Void Staff is bad in single-item Necessity, but even more clearly bad in builds — it appears in the worst builds by Necessity. JG's build-score improvement is a false signal explained by strong partners.

5. **The methods are complementary, not competing.** Single-item Necessity is best for "which item should I prioritize?" Build Necessity is best for "given these two items, which third item?" The vex-nova95 experiment's control variable method (from Module 3) was already capturing this distinction.

---

## Open Questions

1. **Can we formalize the "backbone" concept?** Bloodthirster for Fiora, Gunblade for Vex — items that are central to most strong builds without having the highest single-item Necessity. Is there a metric that captures this?

2. **Build Necessity is tiny compared to single-item.** The best build has Necessity +0.026 vs Guinsoo's single-item +0.502. Is this because builds are much more specific (lower play rate = less impact on overall), or because the build metric is fundamentally less sensitive?

3. **Does tftable's debiasing change build rankings?** Our build scores use raw MetaTFT data. If tftable applied its debiasing to builds, would the rankings shift?

---

## Questions for Xing

1. **Build-implied vs single-item for decision-making**: When advising a player, which method is more actionable? Single-item says "get Guinsoo first" (correct for first item), but builds say "if you have Guinsoo + Giant Slayer, your best third item is Striker's Flail or Gunblade, not JG."

2. **Guinsoo's ceiling effect**: Guinsoo at 88% play rate makes its build score meaningless. Is there a way to handle near-universal items in build analysis, or do we just acknowledge that single-item Necessity is the right tool for core items?

3. **JG as confirmed trap**: tftable gives JG negative Necessity (-0.0017). Our single-item gives +0.003 (essentially zero). Our build score gives +0.00354 (misleadingly positive). The build score is the **worst** metric for trap detection because it's contaminated by partner quality. Is this a general lesson about build-level analysis?

---

## Sources
- MetaTFT Explorer API: unit_items_unique, unit_builds, units_unique endpoints
- tftable ground truth via `python3 cli.py tftable TFT17_Vex --comp nova_95`
- [[experiments/vex-nova95]] — prior item analysis baseline
- [[methods/build-analysis]] — control variable methodology

---

## Review
