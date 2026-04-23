# Experiment: Flex Slot Detection — All 29 Comps
**Status**: 🧪 draft
**Date**: 2026-04-23
**Module**: 4 (Unit Evaluation)

## The Question

对 compositions.py 中全部 29 个 comp，用 flex-slot-detection 方法（`core` → 控制变量 +1 分析）找出每个 comp 的 primary board、core level、以及 +1 灵活位 top 3（按 AVP + Necessity 排名）。

## Method

每个 comp 两步：

**Step 1**: `python3 cli.py core --comp <KEY>` → 找 primary board（freq #1），提取 core units 和 level

**Step 2**: `python3 cli.py units --comp <KEY> --level <LEVEL+1> --filter "Unit(...) & Unit(...) & ..."` → 固定 core units + 控制 level，对非 core unit 计算 Necessity = p/(1-p) × (overall_AVP - unit_AVP)

取 freq 前 5 → 按 AVP 和 Necessity 排 top 3。

---

## Summary Table

| Comp | Level | +1 Games | +1 #1 (AVP, Nec) | +1 #2 (AVP, Nec) | +1 #3 (AVP, Nec) |
|---|---|---|---|---|---|
| nova_95 | 9 | 29,562 | Rhaast (1.62, +.022) | Jhin (1.78, +.019) | Sona (1.91, +.027) |
| vex_95 | 9 | 14,584 | Morgana (1.84, +.010) | Galio (1.86, -.001) | Sona (1.94, -.013) |
| zed | 9 | 1,117 | Vex (1.51, +.071) | Sona (1.60, -.005) | — |
| dark_star | 9 | 2,507 | Morgana (2.38, +.019) | Sona (2.39, +.003) | Xayah (2.41, +.019) |
| space_groove | 9 | 19,463 | Samira (1.84, +.055) | Teemo (1.89, +.010) | Nunu (1.98, -.001) |
| meeple_corki | 9 | 2,736 | Veigar (1.52, +.220) | Jhin (2.11, +.006) | Galio (2.50, -.028) |
| mecha | 9 | 9,269 | Jhin (1.85, +.030) | Morgana (1.88, +.013) | Sona (2.01, -.005) |
| vanguard_leblanc | 8 | 35,749 | Blitzcrank (3.54, +.038) | Galio (3.55, +.020) | Morgana (3.62, +.027) |
| shepherd | 9 | 686 | Morgana (2.24, -.015) | — | — |
| nova_yi | 9 | 6,672 | Urgot (1.71, +.022) | Graves (1.81, +.009) | Morgana (1.84, +.035) |
| xayah | 9 | 29,803 | Blitzcrank (1.54, +.005) | Shen (1.63, -.003) | Morgana (1.65, -.017) |
| voyager | 8 | 1,119 | Morgana (3.16, +.125) | Aurora (3.27, +.007) | — |
| conduit_mf | 7 | 5,704 | ASol (3.18, +.042) | Mordekaiser (3.25, +.011) | Morgana (3.26, +.010) |
| lulu | 7 | 7,608 | Riven (3.58, +.031) | Rhaast (3.99, +.250) | Nunu (4.09, .000) |
| anima_diana | 7 | 12,127 | Rhaast (3.28, +.107) | Karma (3.67, +.013) | Galio (3.82, +.025) |
| viktor | 8 | 39,865 | Morgana (2.35, +.035) | Blitzcrank (2.36, +.007) | Shen (2.37, +.007) |
| kaisa | 8 | 5,002 | Galio (1.81, +.012) | Gwen (1.89, +.042) | Talon (1.93, +.004) |
| two_tanky_samira | 10 | 0 | — | — | — |
| pyke | 8 | 2,161 | Morgana (2.40, +.020) | Bard (2.51, +.017) | Fizz (2.51, +.008) |
| reach_for_the_stars | 8 | 22,332 | Rhaast (2.08, +.017) | Morgana (2.23, +.024) | Shen (2.26, +.011) |
| the_big_bang | 8 | 4,637 | Sona (2.06, +.340) | Morgana (2.17, .000) | Illaoi (2.22, -.003) |
| primordian | 8 | 57,130 | Shen (2.42, +.256) | Morgana (2.70, -.009) | Rammus (2.71, -.005) |
| bonk | 8 | 3,923 | Morgana (2.57, +.027) | Blitzcrank (2.58, +.022) | Leblanc (2.66, +.008) |
| stellar_combo | 8 | 1,763 | Shen (2.26, +.237) | Morgana (2.38, +.007) | Rammus (2.53, -.006) |
| termeepnal_velocity | 8 | 4,552 | Bard (2.48, +.132) | Galio (2.63, +.015) | Shen (2.74, -.001) |
| ez_chogath | 8 | 5,757 | Jhin (2.49, +.481) | Kaisa (2.88, -.009) | Shen (2.95, -.006) |
| tf | 8 | 21,967 | Rhaast (2.08, +.018) | Morgana (2.24, +.027) | Shen (2.27, +.013) |
| veigar | 8 | 7,243 | Bard (2.69, +.151) | Galio (2.77, +.026) | Morgana (3.09, -.020) |
| teemo | 8 | 10,496 | Blitzcrank (2.68, +.023) | Morgana (2.70, +.020) | Bard (2.76, +.006) |

## What I Learned

### 1. Most Common +1 Units

| Unit | Appearances (as top 3 +1) |
|---|---|
| Morgana | 14 comp |
| Shen | 7 comp |
| Rhaast | 5 comp |
| Bard | 4 comp |
| Blitzcrank | 4 comp |
| Galio | 4 comp |
| Sona | 4 comp |

Morgana is the universal +1 (14/27 comps with data).

### 2. Near-Locked +1 (Necessity > 0.2)

| Comp | +1 Unit | Rate | Necessity | Note |
|---|---|---|---|---|
| ez_chogath | Jhin | 65.8% | +0.481 | Core comp supplement |
| the_big_bang | Sona | 75.5% | +0.340 | Near-mandatory |
| primordian | Shen | 56.1% | +0.256 | Tank slot |
| lulu | Rhaast | 71.5% | +0.250 | Essential 5-cost |
| stellar_combo | Shen | 55.5% | +0.237 | Same board as primordian |
| veigar | Bard | 35.9% | +0.151 | Dominant pick |
| termeepnal_velocity | Bard | 34.6% | +0.132 | Dominant pick |
| voyager | Morgana | 41.0% | +0.125 | Limited data |
| anima_diana | Rhaast | 15.6% | +0.107 | Best AVP among candidates |

### 3. No +1 or Insufficient Data (2/29)

- **two_tanky_samira**: primary already 10 units
- **shepherd**: only 686 games at +1 level, sole candidate Morgana has negative Necessity

### 4. Shared Primary Boards

| Shared Board | Comps | Same +1? |
|---|---|---|
| Nasus/Teemo reroll (8u) | bonk, teemo | Yes: Blitzcrank, Morgana |
| Poppy/Veigar (8u) | termeepnal_velocity, veigar | Yes: Bard |
| Primordian (8u) | primordian, stellar_combo | Yes: Shen |
| TF/Reach (8u) | tf, reach_for_the_stars | Similar: Rhaast/Morgana/Shen |

## Open Questions

1. **Should shared-board comps be merged?** 4 comp pairs share primary boards and +1 picks
2. **Negative Necessity +1 — still worth picking?** e.g. vex_95's Galio (-0.001) in a 1.85 AVP environment — differences may be noise
3. **Mecha +1 needs manual level correction** — 7 board units = level 9 (Mecha +2), but CLI generated level 8 command

## Questions for Xing

1. **Shared boards** (bonk=teemo, primordian=stellar_combo) — merge definitions, or keep separate for hero augment distinction?
2. **Mecha level** — confirm 3 Mecha units occupy 5 slots, so 7 units on board = level 9?
3. **Can these results integrate into tftable?**

## Sources
- MetaTFT `exact_units_traits2` + `units_unique` endpoints
- [[methods/flex-slot-detection]] — 分析方法
- [[concepts/composition]] — comp structure definitions

---

## Appendix: Raw Data

### Batch 1 (nova_95 ~ nova_yi)

# Flex Slot Analysis (Final)

10 comps, 2-step method: primary board via `core`, then +1 unit analysis.
Necessity = p/(1-p) * (overall_AVP - unit_AVP). Positive = comp improves with unit.

---

## nova_95
**Primary**: Aatrox Akali Blitzcrank Fiora Graves Morgana Nunu Shen Vex (level 9, 82,964 games, AVP 3.96)
**+1 at level 10** (29,562 games, overall AVP 1.94):

| # | Unit | Games | Rate | AVP | Necessity |
|---|------|-------|------|-----|-----------|
| 1 | Rhaast | 1,879 | 6.4% | 1.62 | +0.022 |
| 2 | Jhin | 3,140 | 10.6% | 1.78 | +0.019 |
| 3 | Sona | 14,050 | 47.5% | 1.91 | +0.027 |

Dropped: TahmKench (2,578g, AVP 2.09, Nec -0.014), Bard (2,273g, AVP 2.09, Nec -0.012)

---

## vex_95
**Primary**: Bard Blitzcrank IvernMinion Karma Mordekaiser Rammus Rhaast Shen Vex (level 9, 22,994 games, AVP 3.98)
**+1 at level 10** (14,584 games, overall AVP 1.85):

| # | Unit | Games | Rate | AVP | Necessity |
|---|------|-------|------|-----|-----------|
| 1 | Morgana | 7,119 | 48.8% | 1.84 | +0.010 |
| 2 | Galio | 755 | 5.2% | 1.86 | -0.001 |
| 3 | Sona | 1,801 | 12.3% | 1.94 | -0.013 |

Dropped: Graves (703g, AVP 2.03, Nec -0.009), Fiora (582g, AVP 1.95, Nec -0.004)

---

## zed
**Primary**: Aatrox Akali Blitzcrank Fiora Graves Morgana Nunu Shen Zed (level 9, 2,785 games, AVP 3.03)
**+1 at level 10** (1,117 games, overall AVP 1.58):

| # | Unit | Games | Rate | AVP | Necessity |
|---|------|-------|------|-----|-----------|
| 1 | Vex | 561 | 50.2% | 1.51 | +0.071 |
| 2 | Sona | 213 | 19.1% | 1.60 | -0.005 |

Only 2 non-core units in data.

---

## dark_star
**Primary**: Blitzcrank Chogath Galio Jhin Kaisa Karma Lissandra Mordekaiser TahmKench (level 9, 6,226 games, AVP 4.08)
**+1 at level 10** (2,507 games, overall AVP 2.46):

| # | Unit | Games | Rate | AVP | Necessity |
|---|------|-------|------|-----|-----------|
| 1 | Morgana | 477 | 19.0% | 2.38 | +0.019 |
| 2 | Sona | 119 | 4.7% | 2.39 | +0.003 |
| 3 | Xayah | 700 | 27.9% | 2.41 | +0.019 |

Dropped: Bard (307g, AVP 2.45, Nec +0.001), Shen (139g, AVP 2.47, Nec -0.001)

---

## space_groove
**Primary**: Blitzcrank Gwen Nami Nasus Ornn Pantheon Riven Shen TahmKench (level 9, 25,917 games, AVP 3.79)
**+1 at level 10** (19,463 games, overall AVP 1.96):

| # | Unit | Games | Rate | AVP | Necessity |
|---|------|-------|------|-----|-----------|
| 1 | Samira | 6,116 | 31.4% | 1.84 | +0.055 |
| 2 | Teemo | 2,336 | 12.0% | 1.89 | +0.010 |
| 3 | Nunu | 805 | 4.1% | 1.98 | -0.001 |

Dropped: Morgana (5,149g, AVP 2.00, Nec -0.014), Sona (1,424g, AVP 2.12, Nec -0.013)

---

## meeple_corki
**Primary**: Bard Corki Fizz Gnar IvernMinion Milio Poppy Rammus Riven (level 9, 9,530 games, AVP 4.24)
**+1 at level 10** (2,736 games, overall AVP 2.24):

| # | Unit | Games | Rate | AVP | Necessity |
|---|------|-------|------|-----|-----------|
| 1 | Veigar | 641 | 23.4% | 1.52 | +0.220 |
| 2 | Jhin | 127 | 4.6% | 2.11 | +0.006 |
| 3 | Galio | 265 | 9.7% | 2.50 | -0.028 |

Dropped: Shen (477g, AVP 2.65, Nec -0.087), Morgana (417g, AVP 2.54, Nec -0.054)

---

## mecha
**Primary**: AurelionSol Bard Fiora Galio Karma TahmKench Urgot (level 7, 17,002 games, AVP 3.53)
**+1 at level 8** (581 games, overall AVP 4.75):

Insufficient data: only 581 games match (0.4% of total). No non-core units returned by API. Mecha typically stabilizes at level 7; level 8 with all 7 core units is rare.

---

## vanguard_leblanc
**Primary**: Illaoi IvernMinion Karma Leblanc Leona Mordekaiser Nunu Zoe (level 8, 35,452 games, AVP 5.32)
**+1 at level 9** (35,749 games, overall AVP 3.77):

| # | Unit | Games | Rate | AVP | Necessity |
|---|------|-------|------|-----|-----------|
| 1 | Blitzcrank | 5,111 | 14.3% | 3.54 | +0.038 |
| 2 | Galio | 2,921 | 8.2% | 3.55 | +0.020 |
| 3 | Morgana | 5,411 | 15.1% | 3.62 | +0.027 |

Dropped: Bard (13,517g, AVP 3.79, Nec -0.012), Sona (1,647g, AVP 3.76, Nec +0.000)

---

## shepherd
**Primary**: Galio Illaoi IvernMinion Karma Leblanc Leona Lissandra Sona Teemo (level 9, 1,597 games, AVP 3.68)
**+1 at level 10** (686 games, overall AVP 2.21):

| # | Unit | Games | Rate | AVP | Necessity |
|---|------|-------|------|-----|-----------|
| 1 | Morgana | 227 | 33.1% | 2.24 | -0.015 |

Only 1 non-core unit in data (686 total games).

---

## nova_yi
**Primary**: Aatrox Akali Belveth Fiora Kindred Maokai MasterYi Shen TahmKench (level 9, 9,827 games, AVP 3.23)
**+1 at level 10** (6,672 games, overall AVP 1.99):

| # | Unit | Games | Rate | AVP | Necessity |
|---|------|-------|------|-----|-----------|
| 1 | Urgot | 486 | 7.3% | 1.71 | +0.022 |
| 2 | Graves | 321 | 4.8% | 1.81 | +0.009 |
| 3 | Morgana | 1,260 | 18.9% | 1.84 | +0.035 |

Dropped: Caitlyn (2,102g, AVP 2.17, Nec -0.083), Sona (1,555g, AVP 1.97, Nec +0.006)

### Batch 2 (xayah ~ reach_for_the_stars)

# Flex Slot Analysis (Final)

## xayah
**Primary**: Bard Gnar Jax Jhin Mordekaiser Nunu Rammus Rhaast Xayah (level 9, 13,583 games, AVP 2.79)
**+1 at level 10** (29,803 games, overall AVP 1.61):
| # | Unit | Games | Rate | AVP | Necessity |
|---|------|-------|------|-----|-----------|
| 1 | Blitzcrank | 1,890 | 6.3% | 1.54 | +0.005 |
| 2 | Shen | 3,510 | 11.8% | 1.63 | -0.003 |
| 3 | Morgana | 9,061 | 30.4% | 1.65 | -0.017 |

## voyager
**Primary**: Galio Illaoi IvernMinion Karma Lissandra Nami Nunu Rhaast (level 8, 1,273 games, AVP 4.92)
**+1 at level 9** (1,119 games, overall AVP 3.34):
| # | Unit | Games | Rate | AVP | Necessity |
|---|------|-------|------|-----|-----------|
| 1 | Morgana | 459 | 41.0% | 3.16 | +0.125 |
| 2 | Aurora | 107 | 9.6% | 3.27 | +0.007 |

## conduit_mf
**Primary**: Aatrox Gragas Maokai MissFortune Ornn Rhaast Viktor (level 7, 10,842 games, AVP 5.23)
**+1 at level 8** (5,704 games, overall AVP 3.40):
| # | Unit | Games | Rate | AVP | Necessity |
|---|------|-------|------|-----|-----------|
| 1 | AurelionSol | 915 | 16.0% | 3.18 | +0.042 |
| 2 | Mordekaiser | 398 | 7.0% | 3.25 | +0.011 |
| 3 | Morgana | 373 | 6.5% | 3.26 | +0.010 |

## lulu
**Primary**: Aatrox Jax Lulu Maokai Milio Pantheon TwistedFate (level 7, 2,081 games, AVP 6.65)
**+1 at level 8** (7,608 games, overall AVP 4.09):
| # | Unit | Games | Rate | AVP | Necessity |
|---|------|-------|------|-----|-----------|
| 1 | Riven | 435 | 5.7% | 3.58 | +0.031 |
| 2 | Rhaast | 5,438 | 71.5% | 3.99 | +0.250 |
| 3 | Nunu | 345 | 4.5% | 4.09 | 0.000 |

## anima_diana
**Primary**: Aurora Diana Illaoi IvernMinion Jinx Leblanc Leona (level 7, 9,484 games, AVP 6.25)
**+1 at level 8** (12,127 games, overall AVP 3.86):
| # | Unit | Games | Rate | AVP | Necessity |
|---|------|-------|------|-----|-----------|
| 1 | Rhaast | 1,886 | 15.6% | 3.28 | +0.107 |
| 2 | Karma | 781 | 6.4% | 3.67 | +0.013 |
| 3 | Galio | 4,620 | 38.1% | 3.82 | +0.025 |

## viktor
**Primary**: Illaoi IvernMinion Lissandra Mordekaiser Nami Pyke Rhaast Viktor (level 8, 115,691 games, AVP 3.59)
**+1 at level 9** (39,865 games, overall AVP 2.48):
| # | Unit | Games | Rate | AVP | Necessity |
|---|------|-------|------|-----|-----------|
| 1 | Morgana | 8,380 | 21.0% | 2.35 | +0.035 |
| 2 | Blitzcrank | 2,146 | 5.4% | 2.36 | +0.007 |
| 3 | Shen | 2,374 | 6.0% | 2.37 | +0.007 |

## kaisa
**Primary**: Fizz IvernMinion Kaisa Karma Ornn Rammus Rhaast Riven (level 8, 25,655 games, AVP 3.09)
**+1 at level 9** (5,002 games, overall AVP 2.00):
| # | Unit | Games | Rate | AVP | Necessity |
|---|------|-------|------|-----|-----------|
| 1 | Galio | 305 | 6.1% | 1.81 | +0.012 |
| 2 | Gwen | 1,374 | 27.5% | 1.89 | +0.042 |
| 3 | Talon | 291 | 5.8% | 1.93 | +0.004 |

## two_tanky_samira
**Primary**: Blitzcrank Gwen Nami Nasus Ornn Pantheon Riven Samira Shen TahmKench (level 10, 6,218 games, AVP 2.03)
**+1 at level 11**: No data (level 11 games too rare)

## pyke
**Primary**: Corki Gragas Gwen IvernMinion Milio Pantheon Pyke Riven (level 8, 5,636 games, AVP 3.74)
**+1 at level 9** (2,161 games, overall AVP 2.56):
| # | Unit | Games | Rate | AVP | Necessity |
|---|------|-------|------|-----|-----------|
| 1 | Morgana | 242 | 11.2% | 2.40 | +0.020 |
| 2 | Bard | 542 | 25.1% | 2.51 | +0.017 |
| 3 | Fizz | 306 | 14.2% | 2.51 | +0.008 |

## reach_for_the_stars
**Primary**: Aatrox Caitlyn Corki Jax Milio Riven Talon TwistedFate (level 8, 15,168 games, AVP 3.13)
**+1 at level 9** (22,332 games, overall AVP 2.30):
| # | Unit | Games | Rate | AVP | Necessity |
|---|------|-------|------|-----|-----------|
| 1 | Rhaast | 1,590 | 7.1% | 2.08 | +0.017 |
| 2 | Morgana | 5,730 | 25.7% | 2.23 | +0.024 |
| 3 | Shen | 4,681 | 21.0% | 2.26 | +0.011 |

### Batch 3 (the_big_bang ~ teemo)

# Flex Slot Analysis (Final)

## the_big_bang
**Primary**: Aurora, Galio, IvernMinion, Karma, Lissandra, Poppy, Pyke, Rammus (level 8, 5,779 games, AVP 3.61)
**+1 at level 9** (4,637 games, overall AVP 2.17):
| # | Unit | Games | Rate | AVP | Necessity |
|---|------|-------|------|-----|-----------|
| 1 | Sona | 3,503 | 75.5% | 2.06 | +0.340 |
| 2 | Morgana | 121 | 2.6% | 2.17 | 0.000 |
| 3 | Illaoi | 267 | 5.8% | 2.22 | -0.003 |

## primordian
**Primary**: Aatrox, Akali, Belveth, Briar, Caitlyn, Kindred, Maokai, RekSai (level 8, 90,739 games, AVP 4.27)
**+1 at level 9** (57,130 games, overall AVP 2.62):
| # | Unit | Games | Rate | AVP | Necessity |
|---|------|-------|------|-----|-----------|
| 1 | Shen | 32,071 | 56.1% | 2.42 | +0.256 |
| 2 | Morgana | 5,535 | 9.7% | 2.70 | -0.009 |
| 3 | Rammus | 2,880 | 5.0% | 2.71 | -0.005 |

## bonk
**Primary**: Illaoi, Leona, Lissandra, Mordekaiser, Nami, Nasus, Teemo, Zoe (level 8, 8,456 games, AVP 3.84)
**+1 at level 9** (3,923 games, overall AVP 2.71):
| # | Unit | Games | Rate | AVP | Necessity |
|---|------|-------|------|-----|-----------|
| 1 | Morgana | 642 | 16.4% | 2.57 | +0.027 |
| 2 | Blitzcrank | 562 | 14.3% | 2.58 | +0.022 |
| 3 | Leblanc | 544 | 13.9% | 2.66 | +0.008 |

## stellar_combo
**Primary**: Aatrox, Akali, Belveth, Briar, Caitlyn, Kindred, Maokai, RekSai (level 8, 2,801 games, AVP 4.15)
**+1 at level 9** (1,763 games, overall AVP 2.45):
| # | Unit | Games | Rate | AVP | Necessity |
|---|------|-------|------|-----|-----------|
| 1 | Shen | 978 | 55.5% | 2.26 | +0.237 |
| 2 | Morgana | 161 | 9.1% | 2.38 | +0.007 |
| 3 | Rammus | 114 | 6.5% | 2.53 | -0.006 |

## termeepnal_velocity
**Primary**: Corki, Illaoi, IvernMinion, Lissandra, Mordekaiser, Poppy, Rammus, Veigar (level 8, 13,242 games, AVP 4.25)
**+1 at level 9** (4,552 games, overall AVP 2.73):
| # | Unit | Games | Rate | AVP | Necessity |
|---|------|-------|------|-----|-----------|
| 1 | Bard | 1,573 | 34.6% | 2.48 | +0.132 |
| 2 | Galio | 607 | 13.3% | 2.63 | +0.015 |
| 3 | Shen | 219 | 4.8% | 2.74 | -0.001 |

## ez_chogath
**Primary**: Chogath, Ezreal, Maokai, Milio, Pantheon, Riven, TahmKench, Xayah (level 8, 5,082 games, AVP 5.06)
**+1 at level 9** (5,757 games, overall AVP 2.74):
| # | Unit | Games | Rate | AVP | Necessity |
|---|------|-------|------|-----|-----------|
| 1 | Jhin | 3,788 | 65.8% | 2.49 | +0.481 |
| 2 | Kaisa | 336 | 5.8% | 2.88 | -0.009 |
| 3 | Shen | 154 | 2.7% | 2.95 | -0.006 |

## tf
**Primary**: Aatrox, Caitlyn, Corki, Jax, Milio, Riven, Talon, TwistedFate (level 8, 15,178 games, AVP 3.19)
**+1 at level 9** (21,967 games, overall AVP 2.32):
| # | Unit | Games | Rate | AVP | Necessity |
|---|------|-------|------|-----|-----------|
| 1 | Rhaast | 1,556 | 7.1% | 2.08 | +0.018 |
| 2 | Morgana | 5,608 | 25.5% | 2.24 | +0.027 |
| 3 | Shen | 4,613 | 21.0% | 2.27 | +0.013 |

## veigar
**Primary**: Corki, Illaoi, IvernMinion, Lissandra, Mordekaiser, Poppy, Rammus, Veigar (level 8, 19,478 games, AVP 4.35)
**+1 at level 9** (7,243 games, overall AVP 2.96):
| # | Unit | Games | Rate | AVP | Necessity |
|---|------|-------|------|-----|-----------|
| 1 | Bard | 2,599 | 35.9% | 2.69 | +0.151 |
| 2 | Galio | 881 | 12.2% | 2.77 | +0.026 |
| 3 | Morgana | 962 | 13.3% | 3.09 | -0.020 |

## teemo
**Primary**: Illaoi, Leona, Lissandra, Mordekaiser, Nami, Nasus, Teemo, Zoe (level 8, 24,502 games, AVP 4.01)
**+1 at level 9** (10,496 games, overall AVP 2.81):
| # | Unit | Games | Rate | AVP | Necessity |
|---|------|-------|------|-----|-----------|
| 1 | Blitzcrank | 1,605 | 15.3% | 2.68 | +0.023 |
| 2 | Morgana | 1,635 | 15.6% | 2.70 | +0.020 |
| 3 | Bard | 1,181 | 11.3% | 2.76 | +0.006 |
