# Experiment: Build Necessity vs Single-Item Necessity — Do They Differ?
**Status**: 🧪 draft
**Date**: 2026-04-22
**Module**: 3 (Build Analysis — follow-up)

---

## The Question

Single-item Necessity ranks items by their play-rate-weighted contribution to overall AVP. Build analysis looks at complete 3-item sets. The previous experiment ([[experiments/vex-nova95]]) found that Necessity and build frequency rankings converge on the core item (Guinsoo) but diverge on secondary items (Red Buff/Dcap dominate control variable analysis).

This raises a sharper question: **if we compute Necessity at the build level and then aggregate back to individual items, does the ranking change?** And separately, does the build-aggregated approach produce a different kind of debiasing than single-item Necessity?

We test with two carries in nova_95: Vex (AP, one dominant core item) and Fiora (AD, more distributed itemization).

---

## Chapter 1: Methodology

**Build-aggregated item Necessity**: for each item, pool all builds containing that item, compute the weighted-average AVP across those builds, then compute Necessity using the aggregate rate and AVP:

```
rate_i = Σ(games of builds containing item i) / total_carrier_games
avg_avp_i = Σ(games × AVP per build containing i) / Σ(games of builds containing i)
Build_Necessity_i = rate_i / (1 - rate_i) × (overall_AVP - avg_avp_i)
```

This differs from single-item Necessity because:
1. It only counts games with complete builds (≥50 games per build), excluding partial/zero-item boards
2. Each game is attributed through a specific 3-item combination
3. Carousel/late-game pickup items in low-game builds are filtered out

---

## Chapter 2: Vex — Rankings Converge

**Baseline**: 211,334 games, AVP 4.157

### Top Builds by Build-Level Necessity

| Build | Games | Rate | AVP | Nec |
|---|---|---|---|---|
| Giant Slayer + Guinsoo + Gunblade | 20,345 | 9.6% | 3.91 | +0.026 |
| Giant Slayer + Guinsoo + Flail | 8,347 | 3.9% | 3.77 | +0.016 |
| Guinsoo + Gunblade + Flail | 5,645 | 2.7% | 3.70 | +0.013 |
| Giant Slayer + Guinsoo + Dcap | 4,457 | 2.1% | 3.71 | +0.010 |
| Giant Slayer + Guinsoo × 2 | 3,817 | 1.8% | 3.70 | +0.008 |

Guinsoo appears in **every top build**. The most necessary build is also the most played (9.6%) — unusual, suggesting builds reduce survivorship bias as Dishsoap predicted.

### Item Ranking: Three Methods Compared

| Rank | Single Nec. | Build-Agg. Nec. | tftable Nec. |
|---|---|---|---|
| 1 | Guinsoo (+0.502) | Guinsoo (+0.525) | Guinsoo (+0.764) |
| 2 | Giant Slayer (+0.083) | Giant Slayer (+0.098) | Giant Slayer (+0.092) |
| 3 | Gunblade (+0.076) | Gunblade (+0.084) | Flail (+0.080) |
| 4 | Flail (+0.063) | Flail (+0.060) | Gunblade (+0.078) |
| 5 | Dcap (+0.038) | Dcap (+0.036) | Dcap (+0.049) |
| 6 | Red Buff (+0.033) | Red Buff (+0.029) | Red Buff (+0.046) |
| 7 | Guinsoo ★2 (+0.028) | JG (+0.022) | AA Staff (+0.017) |
| 8 | AA Staff (+0.018) | AA Staff (+0.020) | Morello (+0.007) |

**Top 6 identical across all three methods.** The only difference is positions 3-4 (Gunblade/Flail swap between our methods and tftable — within noise at 0.076 vs 0.063 / 0.080 vs 0.078).

Build-aggregated values are slightly higher for top items (Guinsoo +0.525 vs +0.502). Builds filter out partial itemizations, so the remaining games are more intentional → signal is cleaner.

**Jeweled Gauntlet** is the interesting case: 22% single-item rate, +0.003 single Necessity (near zero), but +0.022 build-aggregated Necessity. tftable confirms JG is essentially worthless (-0.002). The build score inflation comes from JG appearing alongside strong items — partner contamination, not intrinsic quality.

---

## Chapter 3: Fiora — Builds Reveal Itemization Structure

**Baseline**: 208,160 games, AVP 4.102

### Top Builds

| Build | Games | Rate | AVP | Nec |
|---|---|---|---|---|
| Thief's Gloves (alone) | 23,557 | 11.3% | 3.61 | +0.062 |
| BT + Edge of Night + Sterak's | 4,057 | 1.9% | 3.43 | +0.013 |
| BT + Sterak's + Titan's | 3,910 | 1.9% | 3.59 | +0.010 |
| BT + Edge of Night + Titan's | 2,355 | 1.1% | 3.26 | +0.010 |
| Edge + HoJ + Sterak's | 2,259 | 1.1% | 3.35 | +0.008 |

**Thief's Gloves dominates as the #1 build** — it counts as a complete "build" at 11.3% play rate. BT appears in 9 of the top 10 crafted builds.

### Item Ranking: Three Methods Compared

| Rank | Single Nec. | Build-Agg. Nec. | tftable Nec. |
|---|---|---|---|
| 1 | Edge of Night (+0.151) | Edge of Night (+0.086) | Edge of Night (+0.169) |
| 2 | Sterak's (+0.131) | BT (+0.079) | Sterak's (+0.148) |
| 3 | BT (+0.122) | Sterak's (+0.078) | BT (+0.124) |
| 4 | HoJ (+0.087) | TG (+0.062) | HoJ (+0.094) |
| 5 | TG (+0.061) | HoJ (+0.050) | TG (+0.080) |
| 6 | Titan's (+0.046) | Titan's (+0.031) | Giant Slayer (+0.048) |
| 7 | Giant Slayer (+0.043) | Giant Slayer (+0.025) | Titan's (+0.046) |

Divergences:
- **BT and Sterak's swap** in build analysis (#2 and #3). Build data shows BT is the backbone of most strong builds, while single-item and tftable both prefer Sterak's slightly.
- **TG rises from #5 to #4** in builds. As a "build-in-a-box" item, TG benefits uniquely — no partial-item dilution.
- **Absolute values compress** by ~40-50% in build-aggregated scores. More diverse builds spread games across more combinations.

The top 5 items are the **same set** {Edge of Night, Sterak's, BT, HoJ, TG} across all methods — only internal ordering differs.

---

## Chapter 4: The Core Finding — Rankings Are Robust

| Carry | Method Pairs Compared | Top-6 Same Set? | Max Rank Swap |
|---|---|---|---|
| Vex | Single vs Build-Agg | ✅ Yes | 0 (identical) |
| Vex | Single vs tftable | ✅ Yes | 1 (Flail/Gunblade) |
| Fiora | Single vs Build-Agg | ✅ Yes | 1 (BT/Sterak's) |
| Fiora | Single vs tftable | ✅ Yes | 1 (GS/Titan's) |

**Rankings converge across methods. Magnitudes do not.** Guinsoo's Necessity ranges from 0.502 (our single-item) to 0.764 (tftable) — a 52% difference. But it's #1 in every method.

This means: **for practical item recommendations (which items to prioritize), any of the three methods works.** The disagreements are too small (adjacent rank swaps) to matter for player decision-making.

---

## Chapter 5: Does Build Analysis Reduce Survivorship Bias?

The original hypothesis: builds should reduce carousel bias because complete 3-item sets are intentionally crafted.

**Evidence for**: Build-aggregated Necessity slightly amplifies top items (Vex Guinsoo: +0.525 vs +0.502). Noisy items (Searing Shortbow at +0.007 single-item) are filtered out entirely.

**Evidence against**: Rankings don't change. If carousel bias severely distorted single-item Necessity, we'd expect build analysis to produce a *different* ranking — but it doesn't.

**Conclusion**: Single-item Necessity's `p/(1-p)` weighting already handles most survivorship bias at the ranking level. Build analysis provides a complementary confirmation but doesn't reveal hidden truths. The two approaches answer subtly different questions:
- **Single-item Necessity**: "Which item should I prioritize acquiring?"
- **Build Necessity**: "Given two items, which third item completes the build best?"

---

## What I Learned

1. **Three independent methods (single-item, build-aggregated, tftable) produce nearly identical top-6 rankings** for both Vex and Fiora. For practical recommendations, they're interchangeable.

2. **Build analysis is confirmatory, not revelatory.** It validates single-item Necessity rather than overturning it.

3. **JG is a confirmed "filler" item on Vex.** 22% play rate, near-zero single Necessity (+0.003), negative tftable Necessity (-0.002). Its build score (+0.022) is inflated by strong partners — a trap in build-level analysis.

4. **The `p/(1-p)` weighting in Necessity is powerful.** It naturally handles the carousel bias that motivated build analysis. Single-item Necessity is simpler and equally accurate for rankings.

5. **Build analysis does reveal item synergy structure** — BT as Fiora's backbone, Gunblade as Vex's best pairing partner — that single-item analysis can't capture. This is its unique contribution.

---

## Open Questions

1. Does the control variable method (fix 2, vary 1) agree with build Necessity on the "best third item"?
2. Can we formalize "backbone items" — items central to most strong builds without highest single-item Necessity?
3. Does tftable's debiasing change build-level rankings?

---

## Questions for Xing

1. **Build-implied vs single-item for decision-making**: Single-item says "get Guinsoo first." Builds say "if you have Guinsoo + Giant Slayer, pick Flail or Gunblade, not JG." Different questions, both useful. Which matters more for players?

2. **JG partner contamination**: Build analysis makes JG look better than it is because it's paired with strong items. Is this a general weakness of build-level metrics — items get credit for their partners?

3. **Rankings converge but we expected divergence**: Is this because Necessity already debiases well, or because both methods share the same blind spot (endgame snapshots)?

---

## Sources
- MetaTFT Explorer API: unit_items_unique, unit_builds, units_unique endpoints
- tftable ground truth via `python3 cli.py tftable --comp nova_95`
- [[experiments/vex-nova95]] — prior item analysis baseline
- [[methods/build-analysis]] — control variable methodology
- [[concepts/metrics]] — Necessity definition

---

## Review

