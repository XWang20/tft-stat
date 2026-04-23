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

All data excludes emblem/spatula games (`--no-emblem`).

| Comp | Level | +1 Games | +1 #1 (AVP, Nec) | +1 #2 (AVP, Nec) | +1 #3 (AVP, Nec) |
|---|---|---|---|---|---|
| nova_95 | 9 | 27,754 | Rhaast (1.63, +.022) | Jhin (1.78, +.020) | Sona (1.91, +.038) |
| vex_95 | 9 | 13,729 | Morgana (1.84, +.010) | Galio (1.84, +.001) | Fiora (1.97, -.005) |
| zed | 9 | 1,051 | Vex (1.50, +.074) | Sona (1.61, -.009) | — |
| dark_star | 9 | 2,281 | Sona (2.39, +.004) | Morgana (2.40, +.019) | Xayah (2.43, +.021) |
| space_groove | 9 | 5,633 | Rhaast (2.00, +.014) | Vex (2.17, +.006) | Morgana (2.20, +.059) |
| meeple_corki | 9 | 1,814 | Jhin (2.16, +.020) | Galio (2.54, -.007) | Morgana (2.64, -.038) |
| mecha | 9 | 8,605 | Jhin (1.84, +.031) | Morgana (1.88, +.010) | Shen (2.01, -.008) |
| vanguard_leblanc | 8 | 30,605 | Galio (3.55, +.020) | Morgana (3.63, +.028) | Blitzcrank (3.68, +.009) |
| shepherd | 9 | 699† | Morgana (2.25, -.020) | — | — |
| nova_yi | 9 | 2,685 | Morgana (1.96, +.028) | Sona (2.10, +.011) | Caitlyn (2.19, -.053) |
| xayah | 9 | 23,699 | Blitzcrank (1.58, +.003) | Shen (1.64, -.003) | Samira (1.67, -.006) |
| voyager | 8 | 988 | Morgana (3.20, +.134) | — | — |
| conduit_mf | 7 | 4,976 | Mordekaiser (3.14, +.018) | ASol (3.17, +.043) | Morgana (3.24, +.010) |
| lulu | 7 | 6,299 | Riven (3.58, +.031) | Rhaast (4.01, +.269) | Shen (4.22, -.004) |
| anima_diana | 7 | 10,407 | Rhaast (3.25, +.108) | Karma (3.61, +.013) | Morgana (3.81, .000) |
| viktor | 8 | 35,499 | Morgana (2.34, +.032) | Shen (2.34, +.007) | Sona (2.37, +.007) |
| kaisa | 8 | 3,745 | Galio (1.79, +.017) | Gwen (1.91, +.048) | Talon (1.91, +.008) |
| two_tanky_samira | 10 | 0 | — | — | — |
| pyke | 8 | 1,904 | Morgana (2.40, +.023) | Bard (2.52, +.021) | Fizz (2.55, +.005) |
| reach_for_the_stars | 8 | 18,303 | Rhaast (2.08, +.020) | Morgana (2.24, +.027) | Shen (2.26, +.015) |
| the_big_bang | 8 | 4,268 | Sona (2.07, +.321) | Morgana (2.19, -.001) | Illaoi (2.25, -.005) |
| primordian | 8 | 51,422 | Shen (2.42, +.262) | Morgana (2.71, -.011) | Rammus (2.71, -.006) |
| bonk | 8 | 3,453 | Morgana (2.58, +.030) | Leblanc (2.65, +.012) | Blitzcrank (2.65, +.010) |
| stellar_combo | 8 | 1,516 | Shen (2.26, +.271) | Morgana (2.43, +.002) | Rammus (2.51, -.004) |
| termeepnal_velocity | 8 | 3,564 | Bard (2.42, +.104) | Galio (2.66, +.006) | Karma (2.70, -.001) |
| ez_chogath | 8 | 5,518 | Jhin (2.49, +.472) | Kaisa (2.89, -.010) | Shen (2.94, -.006) |
| tf | 8 | 17,991 | Morgana (2.25, +.027) | Shen (2.28, +.012) | Sona (2.34, -.001) |
| veigar | 8 | 5,594 | Bard (2.62, +.118) | Galio (2.78, +.024) | Karma (2.90, +.001) |
| teemo | 8 | 9,374 | Morgana (2.69, +.026) | Blitzcrank (2.74, +.012) | Leblanc (2.76, +.012) |

\* shepherd is emblem-dependent: 0 games without emblem at level 10. Data shown includes emblem games.

† shepherd primary board only represents 9% of games (variant-heavy comp with 9,809 games at level 10 total). The fixed-core method captures only 699 of those. Multiple distinct variants exist (Galio/Karma/Teemo version vs Mordekaiser/Nunu version).

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

### 3. No +1 or Insufficient Data (1/29)

- **two_tanky_samira**: primary already 10 units, no level 11 data

Note: **shepherd** is fully emblem-dependent at level 10 (0 games without emblem). Data shown with emblem; sole +1 candidate Morgana has negative Necessity.

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

## Appendix: Per-Comp Details

## nova_95
**Primary**: Aatrox Akali Blitzcrank Fiora Graves Morgana Nunu Shen Vex (level 9, 83130g, AVP 3.96)
**+1 at level 10** (27754g, AVP 1.95, no emblem):
| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Rhaast | 1813 | 6.5% | 1.63 | +0.022 |
| 2 | Jhin | 2958 | 10.7% | 1.78 | +0.020 |
| 3 | Sona | 13498 | 48.7% | 1.91 | +0.038 |

## vex_95
**Primary**: Bard Blitzcrank IvernMinion Karma Mordekaiser Rammus Rhaast Shen Vex (level 9, 22935g, AVP 3.98)
**+1 at level 10** (13729g, AVP 1.85, no emblem):
| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Morgana | 6856 | 49.9% | 1.84 | +0.010 |
| 2 | Galio | 697 | 5.1% | 1.84 | +0.001 |
| 3 | Fiora | 548 | 4.0% | 1.97 | -0.005 |

## zed
**Primary**: Aatrox Akali Blitzcrank Fiora Graves Morgana Nunu Shen Zed (level 9, 2787g, AVP 3.03)
**+1 at level 10** (1051g, AVP 1.57, no emblem):
| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Vex | 541 | 51.5% | 1.50 | +0.074 |
| 2 | Sona | 201 | 19.1% | 1.61 | -0.009 |

## dark_star
**Primary**: Blitzcrank Chogath Galio Jhin Kaisa Karma Lissandra Mordekaiser TahmKench (level 9, 6235g, AVP 4.08)
**+1 at level 10** (2281g, AVP 2.48, no emblem):
| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Sona | 107 | 4.7% | 2.39 | +0.004 |
| 2 | Morgana | 445 | 19.5% | 2.40 | +0.019 |
| 3 | Xayah | 665 | 29.2% | 2.43 | +0.021 |

## space_groove
**Primary**: Blitzcrank Gwen Nami Nasus Ornn Pantheon Riven Shen TahmKench (level 9, 25906g, AVP 3.79)
**+1 at level 10** (5633g, AVP 2.26, no emblem):
| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Rhaast | 280 | 5.0% | 2.00 | +0.014 |
| 2 | Vex | 363 | 6.4% | 2.17 | +0.006 |
| 3 | Morgana | 2796 | 49.6% | 2.20 | +0.059 |

## meeple_corki
**Primary**: Bard Corki Fizz Gnar IvernMinion Milio Poppy Rammus Riven (level 9, 9518g, AVP 4.24)
**+1 at level 10** (1814g, AVP 2.49, no emblem):
| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Jhin | 106 | 5.8% | 2.16 | +0.020 |
| 2 | Galio | 235 | 13.0% | 2.54 | -0.007 |
| 3 | Morgana | 363 | 20.0% | 2.64 | -0.038 |

## mecha
**Primary**: AurelionSol Bard Fiora Galio Karma TahmKench Urgot (level 9, 17001g, AVP 3.53)
**+1 at level 10** (8605g, AVP 1.91, no emblem):
| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Jhin | 2633 | 30.6% | 1.84 | +0.031 |
| 2 | Morgana | 2196 | 25.5% | 1.88 | +0.010 |
| 3 | Shen | 651 | 7.6% | 2.01 | -0.008 |

## vanguard_leblanc
**Primary**: Illaoi IvernMinion Karma Leblanc Leona Mordekaiser Nunu Zoe (level 8, 35466g, AVP 5.32)
**+1 at level 9** (30605g, AVP 3.77, no emblem):
| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Galio | 2554 | 8.3% | 3.55 | +0.020 |
| 2 | Morgana | 5106 | 16.7% | 3.63 | +0.028 |
| 3 | Blitzcrank | 2643 | 8.6% | 3.68 | +0.009 |

## shepherd
**Primary**: Galio Illaoi IvernMinion Karma Leblanc Leona Lissandra Sona Teemo (level 9, 1594g, AVP 3.69)
**+1 at level 10**: N/A (0g with no-emblem filter)

## nova_yi
**Primary**: Aatrox Akali Belveth Fiora Kindred Maokai MasterYi Shen TahmKench (level 9, 9837g, AVP 3.23)
**+1 at level 10** (2685g, AVP 2.16, no emblem):
| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Morgana | 333 | 12.4% | 1.96 | +0.028 |
| 2 | Sona | 401 | 14.9% | 2.10 | +0.011 |
| 3 | Caitlyn | 1713 | 63.8% | 2.19 | -0.053 |
## xayah
**Primary**: Bard Gnar Jax Jhin Mordekaiser Nunu Rammus Rhaast Xayah (level 9, 13608g, AVP 2.79)
**+1 at level 10** (23699g, AVP 1.62, no emblem):
| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Blitzcrank | 1396 | 5.9% | 1.58 | +0.003 |
| 2 | Shen | 2759 | 11.6% | 1.64 | -0.003 |
| 3 | Samira | 2644 | 11.2% | 1.67 | -0.006 |

## voyager
**Primary**: Galio Illaoi IvernMinion Karma Lissandra Nami Nunu Rhaast (level 8, 1279g, AVP 4.93)
**+1 at level 9** (988g, AVP 3.38, no emblem):
| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Morgana | 421 | 42.6% | 3.20 | +0.134 |

## conduit_mf
**Primary**: Aatrox Gragas Maokai MissFortune Ornn Rhaast Viktor (level 7, 10865g, AVP 5.23)
**+1 at level 8** (4976g, AVP 3.37, no emblem):
| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Mordekaiser | 359 | 7.2% | 3.14 | +0.018 |
| 2 | AurelionSol | 888 | 17.8% | 3.17 | +0.043 |
| 3 | Morgana | 360 | 7.2% | 3.24 | +0.010 |

## lulu
**Primary**: Aatrox Jax Lulu Maokai Milio Pantheon TwistedFate (level 7, 2086g, AVP 6.66)
**+1 at level 8** (6299g, AVP 4.10, no emblem):
| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Riven | 350 | 5.6% | 3.58 | +0.031 |
| 2 | Rhaast | 4721 | 74.9% | 4.01 | +0.269 |
| 3 | Shen | 207 | 3.3% | 4.22 | -0.004 |

## anima_diana
**Primary**: Aurora Diana Illaoi IvernMinion Jinx Leblanc Leona (level 7, 9479g, AVP 6.24)
**+1 at level 8** (10407g, AVP 3.81, no emblem):
| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Rhaast | 1677 | 16.1% | 3.25 | +0.108 |
| 2 | Karma | 653 | 6.3% | 3.61 | +0.013 |
| 3 | Morgana | 990 | 9.5% | 3.81 | +0.000 |

## viktor
**Primary**: Illaoi IvernMinion Lissandra Mordekaiser Nami Pyke Rhaast Viktor (level 8, 115896g, AVP 3.59)
**+1 at level 9** (35499g, AVP 2.45, no emblem):
| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Morgana | 8001 | 22.5% | 2.34 | +0.032 |
| 2 | Shen | 2158 | 6.1% | 2.34 | +0.007 |
| 3 | Sona | 2673 | 7.5% | 2.37 | +0.007 |

## kaisa
**Primary**: Fizz IvernMinion Kaisa Karma Ornn Rammus Rhaast Riven (level 8, 25683g, AVP 3.09)
**+1 at level 9** (3745g, AVP 2.04, no emblem):
| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Galio | 242 | 6.5% | 1.79 | +0.017 |
| 2 | Gwen | 1017 | 27.2% | 1.91 | +0.048 |
| 3 | Talon | 208 | 5.6% | 1.91 | +0.008 |

## two_tanky_samira
**Primary**: Blitzcrank Gwen Nami Nasus Ornn Pantheon Riven Samira Shen TahmKench (level 10, 6223g, AVP 2.03)
**+1 at level 11**: no data (level 11 games too rare)

## pyke
**Primary**: Corki Gragas Gwen IvernMinion Milio Pantheon Pyke Riven (level 8, 5653g, AVP 3.74)
**+1 at level 9** (1904g, AVP 2.58, no emblem):
| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Morgana | 216 | 11.3% | 2.40 | +0.023 |
| 2 | Bard | 496 | 26.1% | 2.52 | +0.021 |
| 3 | Fizz | 268 | 14.1% | 2.55 | +0.005 |

## reach_for_the_stars
**Primary**: Aatrox Caitlyn Corki Jax Milio Riven Talon TwistedFate (level 8, 15236g, AVP 3.12)
**+1 at level 9** (18303g, AVP 2.31, no emblem):
| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Rhaast | 1433 | 7.8% | 2.08 | +0.020 |
| 2 | Morgana | 5085 | 27.8% | 2.24 | +0.027 |
| 3 | Shen | 4144 | 22.6% | 2.26 | +0.015 |
## the_big_bang
**Primary**: Aurora Galio IvernMinion Karma Lissandra Poppy Pyke Rammus (level 8, 5,802g, AVP 3.60)
**+1 at level 9** (4,268g, AVP 2.17, no emblem):
| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Sona | 3,254 | 76.2% | 2.07 | +0.321 |
| 2 | Morgana | 110 | 2.6% | 2.19 | -0.001 |
| 3 | Illaoi | 248 | 5.8% | 2.25 | -0.005 |

## primordian
**Primary**: Aatrox Akali Belveth Briar Caitlyn Kindred Maokai RekSai (level 8, 90,936g, AVP 4.27)
**+1 at level 9** (51,422g, AVP 2.61, no emblem):
| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Shen | 29,787 | 57.9% | 2.42 | +0.262 |
| 2 | Morgana | 5,066 | 9.9% | 2.71 | -0.011 |
| 3 | Rammus | 2,681 | 5.2% | 2.71 | -0.006 |

## bonk
**Primary**: Illaoi Leona Lissandra Mordekaiser Nami Nasus Teemo Zoe (level 8, 8,495g, AVP 3.83)
**+1 at level 9** (3,453g, AVP 2.72, no emblem):
| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Morgana | 606 | 17.5% | 2.58 | +0.030 |
| 2 | Leblanc | 499 | 14.5% | 2.65 | +0.012 |
| 3 | Blitzcrank | 419 | 12.1% | 2.65 | +0.010 |

## stellar_combo
**Primary**: Aatrox Akali Belveth Briar Caitlyn Kindred Maokai RekSai (level 8, 2,808g, AVP 4.15)
**+1 at level 9** (1,516g, AVP 2.45, no emblem):
| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Shen | 891 | 58.8% | 2.26 | +0.271 |
| 2 | Morgana | 142 | 9.4% | 2.43 | +0.002 |
| 3 | Rammus | 103 | 6.8% | 2.51 | -0.004 |

## termeepnal_velocity
**Primary**: Corki Illaoi IvernMinion Lissandra Mordekaiser Poppy Rammus Veigar (level 8, 13,294g, AVP 4.24)
**+1 at level 9** (3,564g, AVP 2.69, no emblem):
| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Bard | 992 | 27.8% | 2.42 | +0.104 |
| 2 | Galio | 577 | 16.2% | 2.66 | +0.006 |
| 3 | Karma | 191 | 5.4% | 2.70 | -0.001 |

## ez_chogath
**Primary**: Chogath Ezreal Maokai Milio Pantheon Riven TahmKench Xayah (level 8, 5,072g, AVP 5.07)
**+1 at level 9** (5,518g, AVP 2.73, no emblem):
| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Jhin | 3,658 | 66.3% | 2.49 | +0.472 |
| 2 | Kaisa | 323 | 5.9% | 2.89 | -0.010 |
| 3 | Shen | 148 | 2.7% | 2.94 | -0.006 |

## tf
**Primary**: Aatrox Caitlyn Corki Jax Milio Riven Talon TwistedFate (level 8, 15,248g, AVP 3.19)
**+1 at level 9** (17,991g, AVP 2.32, no emblem):
| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Morgana | 4,974 | 27.6% | 2.25 | +0.027 |
| 2 | Shen | 4,083 | 22.7% | 2.28 | +0.012 |
| 3 | Sona | 1,081 | 6.0% | 2.34 | -0.001 |

## veigar
**Primary**: Corki Illaoi IvernMinion Lissandra Mordekaiser Poppy Rammus Veigar (level 8, 19,545g, AVP 4.35)
**+1 at level 9** (5,594g, AVP 2.92, no emblem):
| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Bard | 1,581 | 28.3% | 2.62 | +0.118 |
| 2 | Galio | 830 | 14.8% | 2.78 | +0.024 |
| 3 | Karma | 283 | 5.1% | 2.90 | +0.001 |

## teemo
**Primary**: Illaoi Leona Lissandra Mordekaiser Nami Nasus Teemo Zoe (level 8, 24,664g, AVP 4.01)
**+1 at level 9** (9,374g, AVP 2.82, no emblem):
| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Morgana | 1,567 | 16.7% | 2.69 | +0.026 |
| 2 | Blitzcrank | 1,247 | 13.3% | 2.74 | +0.012 |
| 3 | Leblanc | 1,530 | 16.3% | 2.76 | +0.012 |

