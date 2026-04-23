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

| Comp | Core Size | Level | +1 Games | +1 #1 (AVP, Nec) | +1 #2 (AVP, Nec) | +1 #3 (AVP, Nec) |
|---|---|---|---|---|---|---|
| nova_95 | 9u | 9 | 29,481 | Sona (1.91, +.027) | Rhaast (1.62, +.022) | Jhin (1.78, +.019) |
| vex_95 | 9u | 9 | 14,620 | Morgana (1.84, +.010) | Galio (1.86, -.001) | Fiora (1.96, -.005) |
| zed | 9u | 9 | 1,118 | Vex (1.52, +.060) | Sona (1.59, -.002) | — |
| dark_star | 9u | 9 | 2,503 | Morgana (2.37, +.021) | Xayah (2.41, +.019) | Sona (2.40, +.003) |
| space_groove | 9u | 9 | 19,468 | Samira (1.84, +.055) | Teemo (1.89, +.010) | Nunu (1.98, -.001) |
| meeple_corki | 9u | 9 | 2,744 | Veigar (1.51, +.226) | Jhin (2.11, +.007) | Galio (2.49, -.026) |
| mecha | 7u | 9 | 9,260 | Jhin (1.84, +.030) | Morgana (1.87, +.013) | Sona (2.01, -.006) |
| vanguard_leblanc | 9u | 9 | 4,884 | Bard (2.35, +.055) | Blitzcrank (2.31, +.036) | Sona (2.35, +.005) |
| shepherd | 10u | 10 | 0 | — | — | — |
| nova_yi | 9u | 9 | 6,674 | Morgana (1.84, +.035) | Urgot (1.70, +.023) | Graves (1.82, +.009) |
| xayah | 9u | 9 | 29,688 | Blitzcrank (1.54, +.005) | Shen (1.63, -.003) | Sona (1.68, -.004) |
| voyager | 9u | 9 | 163 | — (数据不足) | — | — |
| conduit_mf | 7u | 7 | 5,704 | ASol (3.17, +.044) | Mordekaiser (3.26, +.011) | Morgana (3.27, +.009) |
| lulu | 7u | 7 | 7,583 | Rhaast (3.98, +.277) | Riven (3.59, +.030) | Nunu (4.09, .000) |
| anima_diana | 8u | 8 | 4,391 | Rhaast (1.81, +.081) | Morgana (2.05, +.048) | Karma (2.07, +.045) |
| viktor | 9u | 9 | 4,957 | Blitzcrank (1.81, +.014) | Morgana (1.89, +.010) | Shen (1.94, -.004) |
| kaisa | 8u | 8 | 4,998 | Gwen (1.88, +.046) | Galio (1.83, +.011) | Talon (1.92, +.005) |
| two_tanky_samira | 10u | 10 | 0 | — | — | — |
| pyke | 8u | 8 | 2,152 | Morgana (2.40, +.020) | Bard (2.51, +.017) | Fizz (2.51, +.008) |
| reach_for_the_stars | 8u | 8 | 22,291 | Morgana (2.23, +.024) | Rhaast (2.08, +.017) | Shen (2.27, +.008) |
| the_big_bang | 8u | 9 | 4,627 | Summon (2.09, +.498) | Sona (2.06, +.340) | Morgana (2.17, .000) |
| primordian | 8u | 9 | 57,053 | Shen (2.42, +.256) | Rammus (2.71, -.005) | Sona (2.84, -.007) |
| bonk | 9u | 10 | 525 | Blitzcrank (1.86, +.054) | Leblanc (1.83, +.026) | Nunu (1.88, +.025) |
| stellar_combo | 8u | 9 | 1,762 | Shen (2.25, +.249) | Morgana (2.38, +.007) | Rammus (2.53, -.006) |
| termeepnal_velocity | 9u | 10 | 643 | Bard (1.79, +.369) | Fizz (1.94, -.041) | Gnar (2.20, -.076) |
| ez_chogath | 8u | 9 | 5,757 | Jhin (2.49, +.480) | Shen (2.94, -.006) | Kaisa (2.87, -.008) |
| tf | 8u | 9 | 21,927 | Morgana (2.24, +.027) | Rhaast (2.08, +.018) | Shen (2.28, +.011) |
| veigar | 9u | 10 | 1,155 | Bard (1.86, +.489) | Morgana (1.87, +.019) | Galio (1.79, +.017) |
| teemo | 9u | 10 | 1,686 | Blitzcrank (1.86, +.081) | Nunu (1.87, +.057) | Sona (1.87, +.013) |

## Results

### 5-Cost Comps

#### nova_95
**Primary**: Aatrox Akali Blitzcrank Fiora Graves Morgana Nunu Shen Vex (9u, 82.8k, AVP 3.96)
**+1 at level 10** (29,481 games, AVP 1.94):

| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Sona | 14,013 | 47.5% | 1.91 | +0.027 |
| 2 | Rhaast | 1,856 | 6.3% | 1.62 | +0.022 |
| 3 | Jhin | 3,138 | 10.6% | 1.78 | +0.019 |

#### vex_95
**Primary**: Bard Blitzcrank IvernMinion Karma Mordekaiser Rammus Rhaast Shen Vex (9u, 23.1k, AVP 3.98)
**+1 at level 10** (14,620 games, AVP 1.85):

| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Morgana | 7,130 | 48.8% | 1.84 | +0.010 |
| 2 | Galio | 756 | 5.2% | 1.86 | -0.001 |
| 3 | Fiora | 584 | 4.0% | 1.96 | -0.005 |

#### zed
**Primary**: Aatrox Akali Blitzcrank Fiora Graves Morgana Nunu Shen Zed (9u, 2.8k, AVP 3.04)
**+1 at level 10** (1,118 games, AVP 1.58):

| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Vex | 560 | 50.1% | 1.52 | +0.060 |
| 2 | Sona | 215 | 19.2% | 1.59 | -0.002 |

### 4-Cost Comps

#### dark_star
**Primary**: Blitzcrank Chogath Galio Jhin Kaisa Karma Lissandra Mordekaiser TahmKench (9u, 6.2k, AVP 4.08)
**+1 at level 10** (2,503 games, AVP 2.46):

| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Morgana | 478 | 19.1% | 2.37 | +0.021 |
| 2 | Xayah | 699 | 27.9% | 2.41 | +0.019 |
| 3 | Sona | 120 | 4.8% | 2.40 | +0.003 |

#### space_groove
**Primary**: Blitzcrank Gwen Nami Nasus Ornn Pantheon Riven Shen TahmKench (9u, 25.9k, AVP 3.79)
**+1 at level 10** (19,468 games, AVP 1.96):

| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Samira | 6,114 | 31.4% | 1.84 | +0.055 |
| 2 | Teemo | 2,339 | 12.0% | 1.89 | +0.010 |
| 3 | Nunu | 806 | 4.1% | 1.98 | -0.001 |

#### meeple_corki
**Primary**: Bard Corki Fizz Gnar IvernMinion Milio Poppy Rammus Riven (9u, 9.5k, AVP 4.24)
**+1 at level 10** (2,744 games, AVP 2.25):

| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Veigar | 641 | 23.4% | 1.51 | +0.226 |
| 2 | Jhin | 127 | 4.6% | 2.11 | +0.007 |
| 3 | Galio | 267 | 9.7% | 2.49 | -0.026 |

#### mecha
**Primary**: AurelionSol Bard Fiora Galio Karma TahmKench Urgot (7u / level 9 with Mecha +2, 17.0k, AVP 3.53)
**+1 at level 10** (9,260 games, AVP 1.91):

| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Jhin | 2,798 | 30.2% | 1.84 | +0.030 |
| 2 | Morgana | 2,329 | 25.2% | 1.87 | +0.013 |
| 3 | Sona | 500 | 5.4% | 2.01 | -0.006 |

#### vanguard_leblanc
**Primary**: Illaoi IvernMinion Karma Leblanc Leona Mordekaiser Nunu Summon Zoe (9u, 35.4k, AVP 5.32)
**+1 at level 10** (4,884 games, AVP 2.39):

| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Bard | 2,817 | 57.7% | 2.35 | +0.055 |
| 2 | Blitzcrank | 1,503 | 30.8% | 2.31 | +0.036 |
| 3 | Sona | 513 | 10.5% | 2.35 | +0.005 |

#### shepherd
**Primary**: Galio Illaoi IvernMinion Karma Leblanc Leona Lissandra Sona Summon Teemo (10u, 1.6k, AVP 3.68)
**+1**: 无（level 11 无数据）

#### nova_yi
**Primary**: Aatrox Akali Belveth Fiora Kindred Maokai MasterYi Shen TahmKench (9u, 9.8k, AVP 3.23)
**+1 at level 10** (6,674 games, AVP 1.99):

| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Morgana | 1,256 | 18.8% | 1.84 | +0.035 |
| 2 | Urgot | 487 | 7.3% | 1.70 | +0.023 |
| 3 | Graves | 321 | 4.8% | 1.82 | +0.009 |

#### xayah
**Primary**: Bard Gnar Jax Jhin Mordekaiser Nunu Rammus Rhaast Xayah (9u, 13.5k, AVP 2.79)
**+1 at level 10** (29,688 games, AVP 1.61):

| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Blitzcrank | 1,882 | 6.3% | 1.54 | +0.005 |
| 2 | Shen | 3,500 | 11.8% | 1.63 | -0.003 |
| 3 | Sona | 1,714 | 5.8% | 1.68 | -0.004 |

#### voyager
**Primary**: Galio Illaoi IvernMinion Karma Lissandra Nami Nunu Rhaast Summon (9u, 1.3k, AVP 4.93)
**+1**: 数据不足（level 10 仅 163 games，无非 core unit 出现）

#### anima_diana
**Primary**: Aurora Diana Illaoi IvernMinion Jinx Leblanc Leona Summon (8u, 9.5k, AVP 6.24)
**+1 at level 9** (4,391 games, AVP 2.20):

| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Rhaast | 757 | 17.2% | 1.81 | +0.081 |
| 2 | Morgana | 1,059 | 24.1% | 2.05 | +0.048 |
| 3 | Karma | 1,125 | 25.6% | 2.07 | +0.045 |

### 3-Cost Comps

#### conduit_mf
**Primary**: Aatrox Gragas Maokai MissFortune Ornn Rhaast Viktor (7u, 10.9k, AVP 5.23)
**+1 at level 8** (5,704 games, AVP 3.40):

| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | AurelionSol | 913 | 16.0% | 3.17 | +0.044 |
| 2 | Mordekaiser | 399 | 7.0% | 3.26 | +0.011 |
| 3 | Morgana | 377 | 6.6% | 3.27 | +0.009 |

#### viktor
**Primary**: Illaoi IvernMinion Lissandra Mordekaiser Nami Pyke Rhaast Summon Viktor (9u, 115.4k, AVP 3.59)
**+1 at level 10** (4,957 games, AVP 1.91):

| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Blitzcrank | 609 | 12.3% | 1.81 | +0.014 |
| 2 | Morgana | 1,694 | 34.2% | 1.89 | +0.010 |
| 3 | Shen | 600 | 12.1% | 1.94 | -0.004 |

#### kaisa
**Primary**: Fizz IvernMinion Kaisa Karma Ornn Rammus Rhaast Riven (8u, 25.6k, AVP 3.09)
**+1 at level 9** (4,998 games, AVP 2.00):

| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Gwen | 1,379 | 27.6% | 1.88 | +0.046 |
| 2 | Galio | 305 | 6.1% | 1.83 | +0.011 |
| 3 | Talon | 290 | 5.8% | 1.92 | +0.005 |

#### lulu
**Primary**: Aatrox Jax Lulu Maokai Milio Pantheon TwistedFate (7u, 2.1k, AVP 6.65)
**+1 at level 8** (7,583 games, AVP 4.09):

| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Rhaast | 5,426 | 71.6% | 3.98 | +0.277 |
| 2 | Riven | 434 | 5.7% | 3.59 | +0.030 |
| 3 | Nunu | 346 | 4.6% | 4.09 | +0.000 |

### 2-Cost Comps

#### pyke
**Primary**: Corki Gragas Gwen IvernMinion Milio Pantheon Pyke Riven (8u, 5.6k, AVP 3.74)
**+1 at level 9** (2,152 games, AVP 2.56):

| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Morgana | 243 | 11.3% | 2.40 | +0.020 |
| 2 | Bard | 543 | 25.2% | 2.51 | +0.017 |
| 3 | Fizz | 301 | 14.0% | 2.51 | +0.008 |

#### reach_for_the_stars
**Primary**: Aatrox Caitlyn Corki Jax Milio Riven Talon TwistedFate (8u, 15.1k, AVP 3.12)
**+1 at level 9** (22,291 games, AVP 2.30):

| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Morgana | 5,713 | 25.6% | 2.23 | +0.024 |
| 2 | Rhaast | 1,591 | 7.1% | 2.08 | +0.017 |
| 3 | Shen | 4,673 | 21.0% | 2.27 | +0.008 |

#### the_big_bang
**Primary**: Aurora Galio IvernMinion Karma Lissandra Poppy Pyke Rammus (8u, 5.7k, AVP 3.61)
**+1 at level 9** (4,627 games, AVP 2.17):

| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Summon | 3,987 | 86.2% | 2.09 | +0.498 |
| 2 | Sona | 3,495 | 75.5% | 2.06 | +0.340 |
| 3 | Morgana | 120 | 2.6% | 2.17 | +0.000 |

#### primordian
**Primary**: Aatrox Akali Belveth Briar Caitlyn Kindred Maokai RekSai (8u, 90.5k, AVP 4.27)
**+1 at level 9** (57,053 games, AVP 2.62):

| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Shen | 32,030 | 56.1% | 2.42 | +0.256 |
| 2 | Rammus | 2,878 | 5.0% | 2.71 | -0.005 |
| 3 | Sona | 1,787 | 3.1% | 2.84 | -0.007 |

#### two_tanky_samira
**Primary**: Blitzcrank Gwen Nami Nasus Ornn Pantheon Riven Samira Shen TahmKench (10u, 6.2k, AVP 2.03)
**+1**: 无（level 11 无数据）

#### ez_chogath
**Primary**: Chogath Ezreal Maokai Milio Pantheon Riven TahmKench Xayah (8u, 5.1k, AVP 5.06)
**+1 at level 9** (5,757 games, AVP 2.74):

| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Jhin | 3,786 | 65.8% | 2.49 | +0.480 |
| 2 | Shen | 154 | 2.7% | 2.94 | -0.006 |
| 3 | Kaisa | 335 | 5.8% | 2.87 | -0.008 |

### 1-Cost Comps

#### bonk
**Primary**: Illaoi Leona Lissandra Mordekaiser Nami Nasus Summon Teemo Zoe (9u, 8.4k, AVP 3.84)
**+1 at level 10** (525 games, AVP 1.91):

| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Blitzcrank | 272 | 51.8% | 1.86 | +0.054 |
| 2 | Leblanc | 129 | 24.6% | 1.83 | +0.026 |
| 3 | Nunu | 239 | 45.5% | 1.88 | +0.025 |

#### stellar_combo
**Primary**: Aatrox Akali Belveth Briar Caitlyn Kindred Maokai RekSai (8u, 2.8k, AVP 4.14)
**+1 at level 9** (1,762 games, AVP 2.45):

| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Shen | 977 | 55.4% | 2.25 | +0.249 |
| 2 | Morgana | 161 | 9.1% | 2.38 | +0.007 |
| 3 | Rammus | 115 | 6.5% | 2.53 | -0.006 |

#### termeepnal_velocity
**Primary**: Corki Illaoi IvernMinion Lissandra Mordekaiser Poppy Rammus Summon Veigar (9u, 13.2k, AVP 4.24)
**+1 at level 10** (643 games, AVP 1.88):

| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Bard | 517 | 80.4% | 1.79 | +0.369 |
| 2 | Fizz | 262 | 40.7% | 1.94 | -0.041 |
| 3 | Gnar | 123 | 19.1% | 2.20 | -0.076 |

#### tf
**Primary**: Aatrox Caitlyn Corki Jax Milio Riven Talon TwistedFate (8u, 15.1k, AVP 3.19)
**+1 at level 9** (21,927 games, AVP 2.32):

| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Morgana | 5,590 | 25.5% | 2.24 | +0.027 |
| 2 | Rhaast | 1,559 | 7.1% | 2.08 | +0.018 |
| 3 | Shen | 4,602 | 21.0% | 2.28 | +0.011 |

#### veigar
**Primary**: Corki Illaoi IvernMinion Lissandra Mordekaiser Poppy Rammus Summon Veigar (9u, 19.4k, AVP 4.35)
**+1 at level 10** (1,155 games, AVP 1.97):

| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Bard | 943 | 81.6% | 1.86 | +0.489 |
| 2 | Morgana | 187 | 16.2% | 1.87 | +0.019 |
| 3 | Galio | 101 | 8.7% | 1.79 | +0.017 |

#### teemo
**Primary**: Illaoi Leona Lissandra Mordekaiser Nami Nasus Summon Teemo Zoe (9u, 24.3k, AVP 4.01)
**+1 at level 10** (1,686 games, AVP 1.92):

| # | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Blitzcrank | 968 | 57.4% | 1.86 | +0.081 |
| 2 | Nunu | 895 | 53.1% | 1.87 | +0.057 |
| 3 | Sona | 357 | 21.2% | 1.87 | +0.013 |

---

## What I Learned

### 1. 最常见的 +1 Unit（across all comps with data）

| Unit | 出现次数（作为 top 3 +1） |
|---|---|
| Morgana | 11 comp |
| Shen | 6 comp |
| Sona | 6 comp |
| Rhaast | 5 comp |
| Bard | 4 comp |
| Blitzcrank | 4 comp |
| Jhin | 4 comp |

Morgana 依然是万金油 +1（11/26 有数据的 comp）。

### 2. 压倒性 +1（Necessity > 0.2）

| Comp | +1 Unit | Rate | Necessity | 解读 |
|---|---|---|---|---|
| the_big_bang | Summon | 86.2% | +0.498 | Summon 本质上是 comp 的一部分 |
| veigar | Bard | 81.6% | +0.489 | 几乎必挂 |
| ez_chogath | Jhin | 65.8% | +0.480 | Jhin 是阵容的核心补充 |
| termeepnal_velocity | Bard | 80.4% | +0.369 | 几乎必挂 |
| lulu | Rhaast | 71.6% | +0.277 | Rhaast 是阵容必需的 5-cost |
| primordian | Shen | 56.1% | +0.256 | 前排坦克刚需 |
| stellar_combo | Shen | 55.4% | +0.249 | 同上（共享 primary board） |

### 3. 无 +1 或数据不足（3/29）

- **shepherd**: primary 已 10 units，level 11 无数据
- **two_tanky_samira**: primary 已 10 units
- **voyager**: level 10 仅 163 games，样本不足

### 4. Comp 共享 Primary Board 确认

| 共享 Board | Comps | +1 也相同？ |
|---|---|---|
| Nasus/Teemo 9u reroll | bonk, teemo | 是：Blitzcrank/Nunu |
| Poppy/Veigar 9u | termeepnal_velocity, veigar | 是：Bard |
| Primordian 8u | primordian, stellar_combo | 是：Shen |
| TF/Reach 8u | tf, reach_for_the_stars | 近似：Morgana 都是 #1 |

## Open Questions

1. **Summon 作为 +1 有多少是 trait 机制？** the_big_bang 的 Summon 86% rate + Sona 75% rate 说明两者高度共现，可能是 Summoner trait 联动
2. **Comp 共享是否应该合并定义？** 4 对 comp 共享 primary board 且 +1 相同
3. **负 Necessity 的 +1 是否仍值得选？** 如 vex_95 的 Galio (-0.001) 和 Fiora (-0.005)，在 AVP 1.85 的环境下差异极小

## Questions for Xing

1. **Comp 共享**（bonk=teemo, primordian=stellar_combo）— 这些应该合并吗？还是 hero augment 的存在使得分开有意义？
2. **Summon 的 +1 机制** — the_big_bang 的 Summon 是因为 Summoner trait 自动召唤还是玩家手动放？
3. **这个实验的结果可以直接集成到 tftable 吗？** 或者需要进一步验证？

## Sources
- MetaTFT `exact_units_traits2` + `units_unique` endpoints
- [[methods/flex-slot-detection]] — 分析方法
- [[concepts/composition]] — comp structure definitions

---

## Appendix: Raw Data

### Batch 1 (nova_95 ~ nova_yi)

## nova_95

**Primary**: Aatrox, Akali, Blitzcrank, Fiora, Graves, Morgana, Nunu, Shen, Vex (9 units, 82,755 games, AVP 3.96)
**Level**: 9
**+1 sample**: 29,481 games at level 10, overall AVP 1.94

| Rank | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Sona | 14,013 | 47.5% | 1.91 | +0.027 |
| 2 | Rhaast | 1,856 | 6.3% | 1.62 | +0.022 |
| 3 | Jhin | 3,138 | 10.6% | 1.78 | +0.019 |
| ref | TahmKench | 2,573 | 8.7% | 2.09 | -0.014 |
| ref | Bard | 2,266 | 7.7% | 2.09 | -0.012 |

---

## vex_95

**Primary**: Bard, Blitzcrank, IvernMinion, Karma, Mordekaiser, Rammus, Rhaast, Shen, Vex (9 units, 23,054 games, AVP 3.98)
**Level**: 9
**+1 sample**: 14,620 games at level 10, overall AVP 1.85

| Rank | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Morgana | 7,130 | 48.8% | 1.84 | +0.010 |
| 2 | Galio | 756 | 5.2% | 1.86 | -0.001 |
| 3 | Fiora | 584 | 4.0% | 1.96 | -0.005 |
| ref | Graves | 705 | 4.8% | 2.02 | -0.009 |
| ref | Sona | 1,807 | 12.4% | 1.95 | -0.014 |

---

## zed

**Primary**: Aatrox, Akali, Blitzcrank, Fiora, Graves, Morgana, Nunu, Shen, Zed (9 units, 2,776 games, AVP 3.04)
**Level**: 9
**+1 sample**: 1,118 games at level 10, overall AVP 1.58

| Rank | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Vex | 560 | 50.1% | 1.52 | +0.060 |
| 2 | Sona | 215 | 19.2% | 1.59 | -0.002 |

(only 2 non-core units available)

---

## dark_star

**Primary**: Blitzcrank, Chogath, Galio, Jhin, Kaisa, Karma, Lissandra, Mordekaiser, TahmKench (9 units, 6,214 games, AVP 4.08)
**Level**: 9
**+1 sample**: 2,503 games at level 10, overall AVP 2.46

| Rank | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Morgana | 478 | 19.1% | 2.37 | +0.021 |
| 2 | Xayah | 699 | 27.9% | 2.41 | +0.019 |
| 3 | Sona | 120 | 4.8% | 2.40 | +0.003 |
| ref | Bard | 303 | 12.1% | 2.45 | +0.001 |
| ref | Shen | 138 | 5.5% | 2.45 | +0.001 |

---

## space_groove

**Primary**: Blitzcrank, Gwen, Nami, Nasus, Ornn, Pantheon, Riven, Shen, TahmKench (9 units, 25,914 games, AVP 3.79)
**Level**: 9
**+1 sample**: 19,468 games at level 10, overall AVP 1.96

| Rank | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Samira | 6,114 | 31.4% | 1.84 | +0.055 |
| 2 | Teemo | 2,339 | 12.0% | 1.89 | +0.010 |
| 3 | Nunu | 806 | 4.1% | 1.98 | -0.001 |
| ref | Morgana | 5,161 | 26.5% | 1.99 | -0.011 |
| ref | Sona | 1,427 | 7.3% | 2.12 | -0.013 |

---

## meeple_corki

**Primary**: Bard, Corki, Fizz, Gnar, IvernMinion, Milio, Poppy, Rammus, Riven (9 units, 9,527 games, AVP 4.24)
**Level**: 9
**+1 sample**: 2,744 games at level 10, overall AVP 2.25

| Rank | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Veigar | 641 | 23.4% | 1.51 | +0.226 |
| 2 | Jhin | 127 | 4.6% | 2.11 | +0.007 |
| 3 | Galio | 267 | 9.7% | 2.49 | -0.026 |
| ref | Morgana | 418 | 15.2% | 2.54 | -0.052 |
| ref | Shen | 479 | 17.5% | 2.65 | -0.085 |

---

## mecha

**Primary**: AurelionSol, Bard, Fiora, Galio, Karma, TahmKench, Urgot (7 units / 9 slots with Mecha +2, 17,015 games, AVP 3.53)
**Level**: 9 (7 + 2 Mecha)
**+1 sample**: 9,260 games at level 10, overall AVP 1.91

| Rank | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Jhin | 2,798 | 30.2% | 1.84 | +0.030 |
| 2 | Morgana | 2,329 | 25.2% | 1.87 | +0.013 |
| 3 | Sona | 500 | 5.4% | 2.01 | -0.006 |
| ref | Shen | 711 | 7.7% | 2.02 | -0.009 |
| ref | Mordekaiser | 811 | 8.8% | 2.06 | -0.014 |

---

## vanguard_leblanc

**Primary**: Illaoi, IvernMinion, Karma, Leblanc, Leona, Mordekaiser, Nunu, Summon, Zoe (9 units, 35,392 games, AVP 5.32)
**Level**: 9
**+1 sample**: 4,884 games at level 10, overall AVP 2.39

| Rank | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Bard | 2,817 | 57.7% | 2.35 | +0.055 |
| 2 | Blitzcrank | 1,503 | 30.8% | 2.31 | +0.036 |
| 3 | Sona | 513 | 10.5% | 2.35 | +0.005 |
| ref | Morgana | 1,551 | 31.8% | 2.38 | +0.005 |
| ref | Galio | 573 | 11.7% | 2.41 | -0.003 |

---

## shepherd

**Primary**: Galio, Illaoi, IvernMinion, Karma, Leblanc, Leona, Lissandra, Sona, Summon, Teemo (10 units, 1,598 games, AVP 3.68)
**Level**: 10
**+1 sample**: 无 +1 (level 11 data unavailable, 0 games returned)

---

## nova_yi

**Primary**: Aatrox, Akali, Belveth, Fiora, Kindred, Maokai, MasterYi, Shen, TahmKench (9 units, 9,796 games, AVP 3.23)
**Level**: 9
**+1 sample**: 6,674 games at level 10, overall AVP 1.99

| Rank | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Morgana | 1,256 | 18.8% | 1.84 | +0.035 |
| 2 | Urgot | 487 | 7.3% | 1.70 | +0.023 |
| 3 | Graves | 321 | 4.8% | 1.82 | +0.009 |
| ref | Sona | 1,560 | 23.4% | 1.97 | +0.006 |
| ref | Caitlyn | 2,106 | 31.6% | 2.17 | -0.083 |

### Batch 2 (xayah ~ reach_for_the_stars)

## xayah

**Primary**: Bard, Gnar, Jax, Jhin, Mordekaiser, Nunu, Rammus, Rhaast, Xayah (9 units, 13,541 games, AVP 2.79)
**Level**: 9
**+1 sample**: 29,688 games at level 10, overall AVP 1.61

| Rank | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Blitzcrank | 1,882 | 6.3% | 1.54 | +0.005 |
| 2 | Shen | 3,500 | 11.8% | 1.63 | -0.003 |
| 3 | Sona | 1,714 | 5.8% | 1.68 | -0.004 |

## voyager

**Primary**: Galio, Illaoi, IvernMinion, Karma, Lissandra, Nami, Nunu, Rhaast, Summon (9 units, 1,274 games, AVP 4.93)
**Level**: 9
**+1**: Only 163 games at level 10 with all 9 core units, no non-core units visible. Insufficient data for +1 analysis.

## conduit_mf

**Primary**: Aatrox, Gragas, Maokai, MissFortune, Ornn, Rhaast, Viktor (7 units, 10,860 games, AVP 5.23)
**Level**: 7
**+1 sample**: 5,704 games at level 8, overall AVP 3.40

| Rank | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | AurelionSol | 913 | 16.0% | 3.17 | +0.044 |
| 2 | Mordekaiser | 399 | 7.0% | 3.26 | +0.011 |
| 3 | Morgana | 377 | 6.6% | 3.27 | +0.009 |

## lulu

**Primary**: Aatrox, Jax, Lulu, Maokai, Milio, Pantheon, TwistedFate (7 units, 2,080 games, AVP 6.65)
**Level**: 7
**+1 sample**: 7,583 games at level 8, overall AVP 4.09

| Rank | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Rhaast | 5,426 | 71.6% | 3.98 | +0.277 |
| 2 | Riven | 434 | 5.7% | 3.59 | +0.030 |
| 3 | Nunu | 346 | 4.6% | 4.09 | +0.000 |

## anima_diana

**Primary**: Aurora, Diana, Illaoi, IvernMinion, Jinx, Leblanc, Leona, Summon (8 units, 9,490 games, AVP 6.24)
**Level**: 8
**+1 sample**: 4,391 games at level 9, overall AVP 2.20

| Rank | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Rhaast | 757 | 17.2% | 1.81 | +0.081 |
| 2 | Morgana | 1,059 | 24.1% | 2.05 | +0.048 |
| 3 | Karma | 1,125 | 25.6% | 2.07 | +0.045 |

## viktor

**Primary**: Illaoi, IvernMinion, Lissandra, Mordekaiser, Nami, Pyke, Rhaast, Summon, Viktor (9 units, 115,445 games, AVP 3.59)
**Level**: 9
**+1 sample**: 4,957 games at level 10, overall AVP 1.91

| Rank | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Blitzcrank | 609 | 12.3% | 1.81 | +0.014 |
| 2 | Morgana | 1,694 | 34.2% | 1.89 | +0.010 |
| 3 | Shen | 600 | 12.1% | 1.94 | -0.004 |

## kaisa

**Primary**: Fizz, IvernMinion, Kaisa, Karma, Ornn, Rammus, Rhaast, Riven (8 units, 25,623 games, AVP 3.09)
**Level**: 8
**+1 sample**: 4,998 games at level 9, overall AVP 2.00

| Rank | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Gwen | 1,379 | 27.6% | 1.88 | +0.046 |
| 2 | Galio | 305 | 6.1% | 1.83 | +0.011 |
| 3 | Talon | 290 | 5.8% | 1.92 | +0.005 |

## two_tanky_samira

**Primary**: Blitzcrank, Gwen, Nami, Nasus, Ornn, Pantheon, Riven, Samira, Shen, TahmKench (10 units, 6,212 games, AVP 2.03)
**Level**: 10
**+1**: Primary board is already 10 units; level 11 returns no data. No +1 analysis possible.

## pyke

**Primary**: Corki, Gragas, Gwen, IvernMinion, Milio, Pantheon, Pyke, Riven (8 units, 5,618 games, AVP 3.74)
**Level**: 8
**+1 sample**: 2,152 games at level 9, overall AVP 2.56

| Rank | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Morgana | 243 | 11.3% | 2.40 | +0.020 |
| 2 | Bard | 543 | 25.2% | 2.51 | +0.017 |
| 3 | Fizz | 301 | 14.0% | 2.51 | +0.008 |

## reach_for_the_stars

**Primary**: Aatrox, Caitlyn, Corki, Jax, Milio, Riven, Talon, TwistedFate (8 units, 15,101 games, AVP 3.12)
**Level**: 8
**+1 sample**: 22,291 games at level 9, overall AVP 2.30

| Rank | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Morgana | 5,713 | 25.6% | 2.23 | +0.024 |
| 2 | Rhaast | 1,591 | 7.1% | 2.08 | +0.017 |
| 3 | Shen | 4,673 | 21.0% | 2.27 | +0.008 |

### Batch 3 (the_big_bang ~ teemo)

## the_big_bang

**Primary**: Aurora, Galio, IvernMinion, Karma, Lissandra, Poppy, Pyke, Rammus (8 units, 5740 games, AVP 3.61)
**Level**: 9
**+1 sample**: 4627 games at level 9, overall AVP 2.17

| Rank | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Summon | 3987 | 86.2% | 2.09 | 0.498 |
| 2 | Sona | 3495 | 75.5% | 2.06 | 0.340 |
| 3 | Morgana | 120 | 2.6% | 2.17 | 0.000 |

## primordian

**Primary**: Aatrox, Akali, Belveth, Briar, Caitlyn, Kindred, Maokai, RekSai (8 units, 90521 games, AVP 4.27)
**Level**: 9
**+1 sample**: 57053 games at level 9, overall AVP 2.62

| Rank | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Shen | 32030 | 56.1% | 2.42 | 0.256 |
| 2 | Rammus | 2878 | 5.0% | 2.71 | -0.005 |
| 3 | Sona | 1787 | 3.1% | 2.84 | -0.007 |

## bonk

**Primary**: Illaoi, Leona, Lissandra, Mordekaiser, Nami, Nasus, Summon, Teemo, Zoe (9 units, 8401 games, AVP 3.84)
**Level**: 10
**+1 sample**: 525 games at level 10, overall AVP 1.91

| Rank | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Blitzcrank | 272 | 51.8% | 1.86 | 0.054 |
| 2 | Leblanc | 129 | 24.6% | 1.83 | 0.026 |
| 3 | Nunu | 239 | 45.5% | 1.88 | 0.025 |

## stellar_combo

**Primary**: Aatrox, Akali, Belveth, Briar, Caitlyn, Kindred, Maokai, RekSai (8 units, 2782 games, AVP 4.14)
**Level**: 9
**+1 sample**: 1762 games at level 9, overall AVP 2.45

| Rank | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Shen | 977 | 55.4% | 2.25 | 0.249 |
| 2 | Morgana | 161 | 9.1% | 2.38 | 0.007 |
| 3 | Rammus | 115 | 6.5% | 2.53 | -0.006 |

## termeepnal_velocity

**Primary**: Corki, Illaoi, IvernMinion, Lissandra, Mordekaiser, Poppy, Rammus, Summon, Veigar (9 units, 13210 games, AVP 4.24)
**Level**: 10
**+1 sample**: 643 games at level 10, overall AVP 1.88

| Rank | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Bard | 517 | 80.4% | 1.79 | 0.369 |
| 2 | Fizz | 262 | 40.7% | 1.94 | -0.041 |
| 3 | Gnar | 123 | 19.1% | 2.20 | -0.076 |

## ez_chogath

**Primary**: Chogath, Ezreal, Maokai, Milio, Pantheon, Riven, TahmKench, Xayah (8 units, 5092 games, AVP 5.06)
**Level**: 9
**+1 sample**: 5757 games at level 9, overall AVP 2.74

| Rank | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Jhin | 3786 | 65.8% | 2.49 | 0.480 |
| 2 | Shen | 154 | 2.7% | 2.94 | -0.006 |
| 3 | Kaisa | 335 | 5.8% | 2.87 | -0.008 |

## tf

**Primary**: Aatrox, Caitlyn, Corki, Jax, Milio, Riven, Talon, TwistedFate (8 units, 15115 games, AVP 3.19)
**Level**: 9
**+1 sample**: 21927 games at level 9, overall AVP 2.32

| Rank | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Morgana | 5590 | 25.5% | 2.24 | 0.027 |
| 2 | Rhaast | 1559 | 7.1% | 2.08 | 0.018 |
| 3 | Shen | 4602 | 21.0% | 2.28 | 0.011 |

## veigar

**Primary**: Corki, Illaoi, IvernMinion, Lissandra, Mordekaiser, Poppy, Rammus, Summon, Veigar (9 units, 19424 games, AVP 4.35)
**Level**: 10
**+1 sample**: 1155 games at level 10, overall AVP 1.97

| Rank | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Bard | 943 | 81.6% | 1.86 | 0.489 |
| 2 | Morgana | 187 | 16.2% | 1.87 | 0.019 |
| 3 | Galio | 101 | 8.7% | 1.79 | 0.017 |

## teemo

**Primary**: Illaoi, Leona, Lissandra, Mordekaiser, Nami, Nasus, Summon, Teemo, Zoe (9 units, 24328 games, AVP 4.01)
**Level**: 10
**+1 sample**: 1686 games at level 10, overall AVP 1.92

| Rank | Unit | Games | Rate | AVP | Necessity |
|---|---|---|---|---|---|
| 1 | Blitzcrank | 968 | 57.4% | 1.86 | 0.081 |
| 2 | Nunu | 895 | 53.1% | 1.87 | 0.057 |
| 3 | Sona | 357 | 21.2% | 1.87 | 0.013 |
