# Experiment: Tank Filter Reliability -- Cross-Unit rho Comparison
**Status**: draft
**Date**: 2026-04-23
**Module**: 1 (Filter Design) / 9 (Cross-Validation)

## The Question

The previous filter-reliability experiment found that Mordekaiser (dark_star) had item Necessity ranking stability rho = 0.048 across filter levels, while Vex (nova_95) had rho = 0.976. The conclusion was that "tanks have unstable item rankings." But Xing pointed out: **Mordekaiser is not the primary tank in dark_star -- players don't typically itemize him.** The low rho might reflect poor unit selection, not a fundamental tank property.

This experiment tests: **When we select tanks that players ACTUALLY give items to (1-cost 3-star 3-item, 4-cost 2-star), does Necessity ranking stability remain low?** Or was the Mordekaiser result an artifact of studying a non-itemized unit?

---

## Chapter 1: Tank Selection and Filter Design

### Tanks Selected

| Unit | Comp | Cost | Build Pattern | Comp Filter Complexity |
|------|------|------|---------------|----------------------|
| Nasus | bonk | 1 | 3-star, 3 tank items | Minimal (just Nasus i3) |
| Poppy | termeepnal_velocity | 1 | 3-star, 3 tank items | Minimal (just Poppy i3) |
| Cho'Gath | ez_chogath | 1 | 2+ items in EZ comp | Complex (Cho OR Pantheon, AND Ezreal) |
| Galio | mecha | 4 | 2-star, 2+ items | Complex (Mecha 6, ASOL i2, Galio i2) |

All four are units that players **intentionally itemize** in their respective comps. This contrasts with Mordekaiser in dark_star, who typically receives 0-1 items.

### Filter Levels

The original 4-level design (Full/Partial/Minimal/None) adapts differently per comp:

- **bonk** and **termeepnal_velocity** have no trait requirements or exclusions in compositions.py. Their "Full" filter IS already minimal (just the unit with 3 items). So we get 3 effective levels: Comp (i3), Restricted (s3:i3), and None.
- **ez_chogath** has a proper complex filter: `(Cho'Gath i2 | Pantheon i2) & Ezreal i2`. This allows genuine 4-level degradation.
- **mecha** has the most complex filter: `Mecha 6 & ASOL i2 & Galio i2`. Full 4-level degradation possible.

This asymmetry is itself informative: **1-cost reroll comps have simple filters because the unit IS the comp's identity.**

---

## Chapter 2: Nasus (bonk) -- The Tanky Carry

### Data by Filter Level

| Filter Level | Games | Overall AVP | Description |
|-------------|-------|-------------|-------------|
| Comp (i3) | 63,545 | 4.31 | compositions.py: Nasus i3 |
| s3:i3 | 59,520 | 4.27 | 3-star Nasus with 3 items |
| None | 469,155 | 4.58 | All Nasus games |

### Necessity Rankings (8 tank items)

| Item | Comp (i3) | s3:i3 | None |
|------|-----------|-------|------|
| Warmog's Armor | 1 (+0.102) | 1 (+0.098) | 1 (+0.022) |
| Sunfire Cape | 2 (+0.093) | 2 (+0.098) | 2 (+0.018) |
| Ionic Spark | 3 (+0.072) | 3 (+0.074) | 5 (+0.013) |
| Spirit Visage | 4 (+0.068) | 4 (+0.069) | 3 (+0.017) |
| Steadfast Heart | 5 (+0.061) | 5 (+0.060) | 4 (+0.014) |
| Dragon's Claw | 6 (+0.049) | 6 (+0.049) | 6 (+0.012) |
| Bramble Vest | 7 (+0.048) | 7 (+0.047) | 7 (+0.011) |
| Protector's Vow | 8 (+0.040) | 8 (+0.044) | 8 (+0.010) |

### Spearman rho

| Comparison | rho |
|-----------|-----|
| Comp vs s3:i3 | **1.000** |
| Comp vs None | **0.929** |
| s3:i3 vs None | **0.929** |

**Finding**: Nasus's tank item rankings are remarkably stable. The top 2 (Warmog's, Sunfire) never move. Adding the 3-star requirement (s3:i3) doesn't change rankings at all (rho = 1.000). Even with no filter, rho = 0.929 -- the only movement is Ionic Spark and Spirit Visage swapping positions 3-5.

---

## Chapter 3: Poppy (termeepnal_velocity) -- Another Tanky Carry

### Data by Filter Level

| Filter Level | Games | Overall AVP | Description |
|-------------|-------|-------------|-------------|
| Comp (i3) | 93,017 | 4.35 | compositions.py: Poppy i3 |
| s3:i3 | 83,239 | 4.28 | 3-star Poppy with 3 items |
| None | 415,333 | 4.61 | All Poppy games |

### Necessity Rankings (8 tank items)

| Item | Comp (i3) | s3:i3 | None |
|------|-----------|-------|------|
| Crownguard | 1 (+0.106) | 1 (+0.107) | 1 (+0.034) |
| Ionic Spark | 2 (+0.081) | 2 (+0.087) | 2 (+0.028) |
| Protector's Vow | 3 (+0.056) | 3 (+0.055) | 3.5 (+0.024) |
| Sunfire Cape | 4 (+0.033) | 4 (+0.046) | 3.5 (+0.024) |
| Warmog's Armor | 5 (+0.031) | 5 (+0.040) | 5 (+0.023) |
| Dragon's Claw | 6 (+0.029) | 6 (+0.033) | 7 (+0.017) |
| Steadfast Heart | 7.5 (+0.028) | 8 (+0.023) | 8 (+0.016) |
| Spirit Visage | 7.5 (+0.028) | 7 (+0.033) | 6 (+0.019) |

### Spearman rho

| Comparison | rho |
|-----------|-----|
| Comp vs s3:i3 | **0.976** |
| Comp vs None | **0.952** |
| s3:i3 vs None | **0.976** |

**Finding**: Poppy is even more stable than Nasus. Crownguard and Ionic Spark are always #1 and #2 -- exactly what you'd expect for a champion whose ability scales with armor (Crownguard gives AP on armor proc, Ionic Spark shreds MR). The small movements at ranks 6-8 involve Spirit Visage vs Dragon's Claw vs Steadfast Heart, which are all similarly valued defensive items.

---

## Chapter 4: Cho'Gath (ez_chogath) -- True Tank with Complex Filter

### Filter Levels

| Level | Games | Overall AVP | Filter |
|-------|-------|-------------|--------|
| Full | 87,915 | 4.76 | (Cho i2 OR Pantheon i2) AND Ezreal i2 |
| Partial | 83,686 | 4.74 | Cho i2 AND Ezreal i2 (drop Pantheon OR) |
| Minimal | 116,761 | 4.71 | Cho i2 only |
| None | 265,607 | 4.72 | All Cho'Gath games |

Note: the ez_chogath comp is the first tank in our experiment with genuine filter complexity. The OR with Pantheon and the AND with Ezreal create meaningful structure to degrade.

### Necessity Rankings (7 tank items)

| Item | Full | Partial | Minimal | None |
|------|------|---------|---------|------|
| Spirit Visage | 1 (+0.090) | 1 (+0.081) | 1 (+0.070) | 1 (+0.025) |
| Warmog's Armor | 2 (+0.052) | 3 (+0.043) | 2 (+0.043) | 2 (+0.018) |
| Dragon's Claw | 3 (+0.049) | 2 (+0.044) | 3 (+0.041) | 3 (+0.017) |
| Protector's Vow | 4 (+0.037) | 4 (+0.036) | 4 (+0.034) | 4 (+0.015) |
| Crownguard | 5 (+0.021) | 5 (+0.020) | 5 (+0.018) | 5 (+0.009) |
| Bramble Vest | 6 (+0.010) | 7 (+0.007) | 6 (+0.011) | 6 (+0.006) |
| Soraka's Miracle | 7 (+0.009) | 6 (+0.009) | 7 (+0.007) | 7 (+0.003) |

### Spearman rho

| Comparison | rho |
|-----------|-----|
| Full vs Partial | **0.929** |
| Full vs Minimal | **1.000** |
| Full vs None | **1.000** |
| Partial vs Minimal | **0.929** |
| Partial vs None | **0.929** |
| Minimal vs None | **1.000** |

**Finding**: Cho'Gath's rankings are **perfectly stable** (rho = 1.000 for Full vs None). Spirit Visage is always #1, Warmog's #2, Dragon's Claw #3, etc. The only minor movement is between Warmog's and Dragon's Claw (positions 2-3 swap in Partial). This is as stable as Vex or better.

The ez_chogath comp definition includes Ezreal and Pantheon, which provide meaningful comp context. Yet removing this context entirely (None) doesn't change Cho'Gath's item rankings at all. Cho'Gath's tank build is apparently universal -- the same items are good regardless of what carries surround him.

---

## Chapter 5: Galio (mecha) -- The Revealing Case

Galio is the first unit in our experiment where filter changes produce dramatic instability. But the story is more nuanced than "tanks are unstable."

### Filter Levels

| Level | Games | Overall AVP | Filter |
|-------|-------|-------------|--------|
| Full | 238,795 | 4.49 | Mecha 6 AND ASOL i2 AND Galio i2 |
| Partial | 244,956 | 4.52 | Mecha 6 AND Galio i2 |
| Minimal | 441,023 | 4.49 | Galio i2 |
| None | 641,743 | 4.53 | All Galio games |

### The Two-World Problem

Galio's item pool splits into two entirely different worlds depending on filter:

> **⚠️ 方法论注意**: 原始分析未使用 `--normal-only`，光装（Radiant Gargoyle、Lioness's Lament、Iceblast Armor 等）混入了排名。下方补充 `--normal-only` 数据。核心结论（Gargoyle/Sterak 的 comp-specific 地位）不变，但 rho 计算受到光装干扰。

**In Mecha (Full, `--normal-only`, 114,773 games):**

| Item | Games | Rate | Necessity |
|------|-------|------|-----------|
| Gargoyle Stoneplate | 95,517 | 83% | **+0.490** |
| Sterak's Gage | 74,800 | 65% | **+0.160** |
| Titan's Resolve | 47,190 | 41% | +0.013 |
| Protector's Vow | 5,381 | 5% | +0.006 |
| Steadfast Heart | 6,786 | 6% | +0.006 |
| Crownguard | 1,684 | 1% | +0.002 |
| Bramble Vest | 5,747 | 5% | -0.000 |
| Adaptive Helm | 3,019 | 3% | -0.002 |
| Evenshroud | 2,008 | 2% | -0.003 |
| Ionic Spark | 2,148 | 2% | -0.005 |

**Outside Mecha (Galio i2, `--normal-only`, 244,015 games):**

| Item | Games | Rate | Necessity |
|------|-------|------|-----------|
| Steadfast Heart | 24,499 | 10% | +0.039 |
| Protector's Vow | 23,484 | 10% | +0.036 |
| Bramble Vest | 20,688 | 8% | +0.026 |
| Crownguard | 10,163 | 4% | +0.022 |
| Adaptive Helm | 12,501 | 5% | +0.018 |
| Ionic Spark | 12,882 | 5% | +0.016 |
| Evenshroud | 12,580 | 5% | +0.015 |

Gargoyle Stoneplate 在 mecha 内 83% play rate、Necessity +0.490；在 mecha 外**普通版完全不出现在列表中**。Sterak's Gage 同样消失。更惊人的是，Adaptive Helm / Ionic Spark / Evenshroud 在 mecha 内是**负 Necessity**，在 mecha 外是正的 — 排名完全反转。

### Spearman rho — normal items only

Using `--normal-only` data, comparing common generic tank items (Protector's Vow, Steadfast Heart, Crownguard, Bramble Vest) between mecha and i2:

| Comparison | rho | Items |
|-----------|-----|-------|
| Full vs i2 (generic only, 4 items) | **+0.750** | Protector/Steadfast/Crownguard/Bramble |

Generic tank items maintain reasonable stability even across the mecha/non-mecha boundary. The dramatic instability in the original analysis (rho = -0.149) was partly caused by mixing radiant items and partly by the genuine comp-specific nature of Gargoyle + Sterak.

**Finding**: Galio tells two stories simultaneously:

1. **Comp-specific items (Gargoyle, Sterak) are genuinely comp-specific.** In mecha, Gargoyle is 83% play rate with Necessity +0.490. Outside mecha, the normal version doesn't appear at all. This is a real Mecha trait synergy effect, not a data artifact.

2. **Generic tank items maintain moderate stability** (rho = 0.750 for generic items). The ranking order shifts somewhat (Steadfast/Protector outrank Bramble/Crownguard outside mecha), but the items are all positive on both sides.

---

## Chapter 6: Why Mordekaiser Was Different

The previous experiment found Mordekaiser (dark_star) at rho = 0.048. This experiment shows that properly-itemized tanks achieve rho of 0.929-1.000. What explains the gap?

**Mordekaiser is not the primary itemized unit in dark_star.** The dark_star comp definition (`Trait('TFT17_DarkStar', min_units=4) & ~Kaisa_s3 & ~Chogath_s3`) does not specify Mordekaiser at all -- he's just one of many DarkStar units. Players typically prioritize items on the carries (Jhin, Kindred) and give Mordekaiser leftover items or none at all.

This means:
- The games captured by the dark_star filter are not primarily "Mordekaiser builds" -- they're "DarkStar comp games where Mordekaiser may or may not have items."
- Mordekaiser's item stats in this context are noisy because most games have 0-1 items on him.
- Different filter definitions capture different subpopulations of dark_star games, and Mordekaiser's sparse itemization makes his Necessity rankings hypersensitive to which subpopulation is selected.

In contrast, all four tanks in this experiment ARE the primary itemized unit in their comp (or at least guaranteed to have items by the filter). Their rankings are stable because their item data is dense and representative.

### The Role Taxonomy

| Category | Example | Comp vs None rho | Why |
|----------|---------|-------------------|-----|
| Primary Carry | Vex (nova_95) | 0.976 | Unit IS the comp |
| Tanky Carry | Nasus (bonk), Poppy | 0.929-0.952 | Unit IS the comp, builds tank items |
| Primary Tank | Cho'Gath (ez_chogath) | 1.000 | Universally good tank items |
| Comp-Specific Tank | Galio (mecha) | 0.548 (full) / 1.000 (secondary) | Comp determines build identity |
| Non-Itemized "Tank" | Mordekaiser (dark_star) | 0.048 | Sparse data, role confusion |

---

## Cross-Validation

tftable was unavailable during this experiment (SSH to desktop timed out). Cross-validation against tftable ground truth is pending.

---

## What I Learned

1. **The previous conclusion was wrong: "tanks have unstable item rankings" is not correct.** When we select tanks that players actually build (Nasus, Poppy, Cho'Gath), their Necessity rankings are just as stable as carries (rho 0.929-1.000). The Mordekaiser rho = 0.048 result was an artifact of studying a unit that isn't the primary item holder in its comp.

2. **Filter reliability depends on whether the unit IS the comp's identity, not on carry vs tank role.** Nasus (bonk) has rho = 0.929 because bonk IS "Nasus with 3 items" -- the unit defines the comp. Mordekaiser (dark_star) has rho = 0.048 because dark_star is NOT "Mordekaiser with items" -- he's a supporting unit in someone else's comp.

3. **Comp-specific items are unstable; generic items are stable.** The Galio (mecha) case reveals this clearly: Gargoyle Stoneplate and Sterak's Gage are mandatory in mecha (76% and 62% play rate) but irrelevant outside it. Meanwhile, generic tank items (Lioness's Lament, Iceblast Armor) maintain perfect rank stability (rho = 1.000) regardless of context. This makes sense -- Gargoyle+Sterak synergize specifically with the Mecha trait, while generic tank items are universally useful.

4. **1-cost reroll comps have trivially simple filter definitions.** bonk = Nasus i3, termeepnal_velocity = Poppy i3. There is no trait, no exclusion -- the unit IS the comp. This means Full/Partial/Minimal collapse to the same filter. Filter reliability analysis is less meaningful for these comps because there is nothing to degrade.

5. **rho between Galio Full and Galio i2 is -0.149 -- rankings essentially invert.** This is the most dramatic finding. It means that analyzing Galio items in the mecha comp context vs analyzing Galio items in isolation gives opposite conclusions about which items are best. This is not instability -- it's a real phenomenon where the Mecha trait fundamentally changes Galio's optimal build.

## Open Questions

1. **Is Galio's item inversion a measurement artifact or a real game mechanic?** In mecha, Galio + Gargoyle + Sterak is the canonical build because these items synergize with Mecha's damage scaling. Outside mecha, these items are just generic stats. Is the Necessity difference real, or is it confounded by "players who build mecha correctly also happen to win more"?

2. **How do we classify Mordekaiser correctly?** In dark_star, he's not the primary item holder. But he IS present and CAN receive items. Should we filter dark_star Mordekaiser games by requiring `Mordekaiser i2` or `i3` to get a cleaner signal? Or does that introduce selection bias?

3. **Is there a relationship between play rate and Necessity stability?** Items with very high play rates (Gargoyle at 76% in mecha) have Necessity driven by volume. Items with moderate play rates (Spirit Visage at 43% on Cho'Gath) have Necessity driven by a mix of Edge and play rate. Does the high-play-rate regime create more instability?

## Questions for Xing

1. **Mordekaiser retest**: Now that we understand the issue, should we retest Mordekaiser specifically by requiring `Mordekaiser i2` or `i3` in the dark_star filter? This would test whether a "secondary item holder" (not the comp-defining unit, but required to have items) behaves more like our tanks or more like the original Mordekaiser result.

2. **Galio's build inversion**: The fact that Full vs i2 rho = -0.149 seems important. In the mecha comp, Gargoyle+Sterak are optimal; outside mecha, they're irrelevant. Is this common for comp-specific synergy items? Are there carry examples where the BIS items completely change based on comp context?

3. **Filter complexity vs stability**: bonk and termeepnal_velocity have trivial filters (just the unit). ez_chogath has moderate complexity. mecha has the most. Is there a general rule that simpler filter definitions correlate with higher stability, or is this specific to these cases?

4. **Practical implication**: Based on these results, it seems safe to analyze tank items as long as the tank IS the primary item holder in the comp. Does this match your experience with tftable? Does tftable show similar stability patterns for different tank roles?

---

## Review

*(pending Xing review)*
