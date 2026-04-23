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

> All queries use `--normal-only` to exclude radiant/special items.

### Data by Filter Level

| Filter Level | Games | Overall AVP | Description |
|-------------|-------|-------------|-------------|
| Comp (i3) | 52,448 | 4.29 | compositions.py: Nasus i3 |
| s3:i3 | 49,502 | 4.26 | 3-star Nasus with 3 items |
| None | 437,407 | 4.57 | All Nasus games |

### Necessity Rankings (8 tank items)

| Item | Comp (i3) | s3:i3 | None |
|------|-----------|-------|------|
| Warmog's Armor | 1 (+0.114) | 2 (+0.110) | 1 (+0.021) |
| Sunfire Cape | 2 (+0.111) | 1 (+0.115) | 2 (+0.019) |
| Ionic Spark | 3 (+0.084) | 3 (+0.086) | 5 (+0.014) |
| Spirit Visage | 4 (+0.079) | 4 (+0.080) | 3 (+0.017) |
| Steadfast Heart | 5 (+0.068) | 5 (+0.067) | 4 (+0.014) |
| Dragon's Claw | 6 (+0.056) | 6 (+0.056) | 6 (+0.012) |
| Bramble Vest | 7 (+0.053) | 7 (+0.052) | 7 (+0.011) |
| Protector's Vow | 8 (+0.046) | 8 (+0.050) | 8 (+0.010) |

### Spearman rho

| Comparison | rho |
|-----------|-----|
| Comp vs s3:i3 | **0.976** |
| Comp vs None | **0.929** |
| s3:i3 vs None | **0.905** |

**Finding**: Nasus's tank item rankings are highly stable. Warmog's and Sunfire are always the top 2 (swapping 1-2 between Comp and s3:i3, hence rho = 0.976 instead of 1.000). Even with no filter, rho = 0.929 -- the only movement is Ionic Spark dropping from 3 to 5 while Spirit Visage and Steadfast Heart rise. Ranks 6-8 are perfectly stable across all levels.

---

## Chapter 3: Poppy (termeepnal_velocity) -- Another Tanky Carry

> All queries use `--normal-only` to exclude radiant/special items.

### Data by Filter Level

| Filter Level | Games | Overall AVP | Description |
|-------------|-------|-------------|-------------|
| Comp (i3) | 77,914 | 4.32 | compositions.py: Poppy i3 |
| s3:i3 | 69,995 | 4.25 | 3-star Poppy with 3 items |
| None | 382,571 | 4.61 | All Poppy games |

### Necessity Rankings (8 tank items)

| Item | Comp (i3) | s3:i3 | None |
|------|-----------|-------|------|
| Crownguard | 1 (+0.115) | 1 (+0.116) | 1 (+0.034) |
| Ionic Spark | 2 (+0.085) | 2 (+0.093) | 2 (+0.029) |
| Protector's Vow | 3 (+0.061) | 3 (+0.061) | 4 (+0.025) |
| Sunfire Cape | 4 (+0.036) | 4 (+0.050) | 3 (+0.025) |
| Dragon's Claw | 5 (+0.030) | 7 (+0.034) | 7 (+0.018) |
| Spirit Visage | 6 (+0.029) | 6 (+0.035) | 6 (+0.020) |
| Steadfast Heart | 7 (+0.028) | 8 (+0.023) | 8 (+0.016) |
| Warmog's Armor | 8 (+0.026) | 5 (+0.036) | 5 (+0.023) |

### Spearman rho

| Comparison | rho |
|-----------|-----|
| Comp vs s3:i3 | **0.833** |
| Comp vs None | **0.810** |
| s3:i3 vs None | **0.976** |

**Finding**: Crownguard and Ionic Spark are always #1 and #2 -- exactly what you'd expect for a champion whose ability scales with armor. But the mid-tier rankings (5-8) shift more than Nasus. Warmog's Armor is rank 8 in Comp but rank 5 in s3:i3 and None, driving the lower Comp vs s3:i3 rho. Notably, s3:i3 vs None is highly stable (0.976), suggesting the Comp definition (which equals Poppy i3, without the 3-star requirement) happens to shift a few mid-tier items compared to the 3-star subset.

---

## Chapter 4: Cho'Gath (ez_chogath) -- True Tank with Complex Filter

> All queries use `--normal-only` to exclude radiant/special items.

### Filter Levels

| Level | Games | Overall AVP | Filter |
|-------|-------|-------------|--------|
| Full | 70,276 | 4.79 | (Cho i2 OR Pantheon i2) AND Ezreal i2 |
| Partial | 66,108 | 4.77 | Cho i2 AND Ezreal i2 (drop Pantheon OR) |
| Minimal | 90,922 | 4.73 | Cho i2 only |
| None | 233,129 | 4.74 | All Cho'Gath games |

Note: the ez_chogath comp is the first tank in our experiment with genuine filter complexity. The OR with Pantheon and the AND with Ezreal create meaningful structure to degrade.

### Necessity Rankings (7 tank items)

| Item | Full | Partial | Minimal | None |
|------|------|---------|---------|------|
| Spirit Visage | 1 (+0.107) | 1 (+0.097) | 1 (+0.083) | 1 (+0.021) |
| Warmog's Armor | 2 (+0.063) | 2 (+0.054) | 2 (+0.054) | 2 (+0.016) |
| Dragon's Claw | 3 (+0.056) | 3 (+0.050) | 3 (+0.048) | 3 (+0.015) |
| Protector's Vow | 4 (+0.045) | 4 (+0.043) | 4 (+0.042) | 4 (+0.014) |
| Crownguard | 5 (+0.028) | 5 (+0.027) | 5 (+0.023) | 5 (+0.009) |
| Bramble Vest | 6 (+0.013) | 6 (+0.010) | 6 (+0.014) | 6 (+0.005) |
| Ionic Spark | 7 (-0.001) | 7 (-0.002) | 7 (+0.002) | 7 (+0.001) |

### Spearman rho

| Comparison | rho |
|-----------|-----|
| Full vs Partial | **1.000** |
| Full vs Minimal | **1.000** |
| Full vs None | **1.000** |
| Partial vs Minimal | **1.000** |
| Partial vs None | **1.000** |
| Minimal vs None | **1.000** |

**Finding**: Cho'Gath's rankings are **perfectly stable** across all filter levels (rho = 1.000 for every pair). Spirit Visage is always #1, Warmog's #2, Dragon's Claw #3, all the way down to Ionic Spark at #7. With `--normal-only`, even the previously observed Warmog/Dragon's Claw swap in Partial (which produced rho = 0.929 in the original data) disappears. Cho'Gath's tank build is truly universal -- the same items are best regardless of comp context.

---

## Chapter 5: Galio (mecha) -- The Revealing Case

> All queries use `--normal-only` to exclude radiant/special items.

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

The previous experiment found Mordekaiser (dark_star) at rho = 0.048. This experiment shows that properly-itemized tanks achieve rho of 0.810-1.000. What explains the gap?

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
| Tanky Carry | Nasus (bonk) | 0.929 | Unit IS the comp, builds tank items |
| Tanky Carry | Poppy (termeepnal_velocity) | 0.810 | Unit IS the comp, mid-tier items shift |
| Primary Tank | Cho'Gath (ez_chogath) | 1.000 | Universally good tank items |
| Comp-Specific Tank | Galio (mecha) | 0.750 (generic only) | Comp determines build identity |
| Non-Itemized "Tank" | Mordekaiser (dark_star) | 0.048 | Sparse data, role confusion |

---

## Cross-Validation

tftable was unavailable during this experiment (SSH to desktop timed out). Cross-validation against tftable ground truth is pending.

---

## What I Learned

1. **The previous conclusion was wrong: "tanks have unstable item rankings" is not correct.** When we select tanks that players actually build (Nasus, Poppy, Cho'Gath), their Necessity rankings are substantially more stable than Mordekaiser (rho 0.810-1.000 vs 0.048). The Mordekaiser rho = 0.048 result was an artifact of studying a unit that isn't the primary item holder in its comp.

2. **Filter reliability depends on whether the unit IS the comp's identity, not on carry vs tank role.** Nasus (bonk) has rho = 0.929 and Cho'Gath has rho = 1.000 because the filter aligns with the unit's build context. Mordekaiser (dark_star) has rho = 0.048 because dark_star is NOT "Mordekaiser with items" -- he's a supporting unit in someone else's comp.

3. **`--normal-only` matters for ranking accuracy.** Excluding radiant/special items changed some results: Cho'Gath improved from rho = 0.929 (Full vs Partial) to 1.000 (the Warmog/Dragon's Claw swap in Partial disappeared). Nasus's Comp vs s3:i3 dropped from 1.000 to 0.976 (Warmog/Sunfire now swap). Poppy's Comp vs s3:i3 dropped from 0.976 to 0.833 (Warmog shifts from rank 8 to rank 5). The radiant items were masking some real mid-tier instability while also creating false instability in other cases.

4. **Poppy shows more mid-tier instability than Nasus, despite both being 1-cost reroll tanky carries.** Warmog's Armor is rank 8 in Poppy's Comp filter but rank 5 in s3:i3 and None. This suggests that the items per se are not interchangeable -- even among the same class of tanks, the specific champion's kit determines which items are stable and which are context-sensitive.

5. **Cho'Gath is the stability champion.** Perfect rho = 1.000 across all 6 filter pairs with 7 items. His tank build is truly universal -- Spirit Visage #1, Warmog's #2, Dragon's Claw #3, all the way down, regardless of comp context. This makes sense: Cho'Gath's kit (health stacking from feast) synergizes with the same items regardless of which carries surround him.

6. **Comp-specific items (Galio's Gargoyle + Sterak) are genuinely comp-specific.** In mecha, Gargoyle is 83% play rate with Necessity +0.490. Outside mecha, the normal version doesn't appear at all. Generic tank items maintain moderate stability (rho = 0.750) across the mecha/non-mecha boundary.

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
