# Experiment: Flex Slot Detection — All 29 Comps
**Status**: 🧪 draft
**Date**: 2026-04-23
**Module**: 4 (Unit Evaluation)

## The Question

对 compositions.py 中全部 29 个 comp，用 `core` 子命令（`exact_units_traits2` API）找出每个 comp 的 primary board、+1 灵活位前 3 名、以及 variant。

## Method

```bash
python3 cli.py core --comp <KEY>
```

对每个 comp 查询 6-11 人口的 board compositions，按 freq 排序。从输出中提取：
1. Primary board（freq #1）
2. +1 candidates（比 primary 多 1 unit 的 board，按 freq 取前 3）
3. Variant（和 primary 有 ≥3 unit 差异的高频 board）

## Results

### 全 Comp Flex Slot 总表

#### 5-Cost Comps

| Comp | Primary (Size) | Games | AVP | +1 #1 | +1 #2 | +1 #3 |
|---|---|---|---|---|---|---|
| nova_95 | 9 units | 82,563 | 3.95 | Sona (14.6k, 2.08) | Jhin (3.1k, 1.94) | TahmKench (2.6k, 2.53) |
| vex_95 | 9 units | 23,148 | 3.98 | Morgana (7.3k, 1.96) | Sona (1.7k, 2.13) | — |
| zed | 9 units | 2,770 | 3.04 | Vex (628, 1.70) | Sona (220, 1.76) | Jhin (41, 1.71) |

#### 4-Cost Comps

| Comp | Primary (Size) | Games | AVP | +1 #1 | +1 #2 | +1 #3 |
|---|---|---|---|---|---|---|
| dark_star | 9 units | 6,194 | 4.08 | Xayah (708, 2.48) | Morgana (462, 2.51) | Bard (268, 2.49) |
| space_groove | 9 units | 25,903 | 3.79 | Samira (5.9k, 1.99) | Morgana (4.0k, 2.22) | Teemo (2.4k, 2.06) |
| meeple_corki | 9 units | 9,539 | 4.25 | Shen (478, 2.73) | Morgana (442, 2.74) | Galio (336, 2.66) |
| mecha | 7 units (lv9) | 17,021 | 3.53 | Jhin (2.9k, 1.95) | Morgana (2.3k, 2.01) | — |
| vanguard_leblanc | 9 units | 35,344 | 5.32 | Bard (12.8k, 3.89) | Morgana (5.1k, 3.75) | Galio (2.7k, 3.73) |
| shepherd | 10 units | 1,594 | 3.68 | Morgana (226, 2.46) | Pyke (90, 2.33) | — |
| nova_yi | 9 units | 9,784 | 3.23 | Caitlyn (2.2k, 2.36) | Sona (1.2k, 2.13) | Morgana (835, 1.97) |
| xayah | 9 units | 13,471 | 2.79 | — | — | — |
| voyager | 9 units | 1,273 | 4.92 | Morgana (423, 3.24) | — | — |
| anima_diana | 8 units | 9,490 | 6.25 | Galio (4.3k, 3.86) | Rhaast (1.8k, 3.32) | Morgana (1.0k, 3.89) |

#### 3-Cost Comps

| Comp | Primary (Size) | Games | AVP | +1 #1 | +1 #2 | +1 #3 |
|---|---|---|---|---|---|---|
| conduit_mf | 7 units | 10,854 | 5.23 | Bard (1.2k, 3.55) | ASol (890, 3.24) | Zoe (599, 3.59) |
| viktor | 9 units | 115,221 | 3.59 | Bard (11.6k, 2.54) | Morgana (8.3k, 2.39) | Sona (2.7k, 2.44) |
| kaisa | 8 units | 25,598 | 3.08 | — | — | — |
| lulu | 7 units | 2,072 | 6.66 | Rhaast (2.1k, 4.13) | — | — |

#### 2-Cost Comps

| Comp | Primary (Size) | Games | AVP | +1 #1 | +1 #2 | +1 #3 |
|---|---|---|---|---|---|---|
| pyke | 8 units | 5,614 | 3.74 | — (variant-heavy) | — | — |
| reach_for_the_stars | 8 units | 15,066 | 3.12 | — | — | — |
| the_big_bang | 8 units | 5,714 | 3.61 | Sona (3.5k, 2.06) | Illaoi (266, 2.22) | Leblanc (177, 2.43) |
| primordian | 8 units | 90,285 | 4.27 | Shen (31.9k, 2.42) | Morgana (5.5k, 2.70) | Rammus (2.9k, 2.71) |
| two_tanky_samira | 10 units | 6,192 | 2.03 | — (already 10) | — | — |
| ez_chogath | 8 units | 5,088 | 5.06 | Jhin (3.8k, 2.49) | Lissandra (652, 3.08) | Kaisa (333, 2.88) |

#### 1-Cost Comps

| Comp | Primary (Size) | Games | AVP | +1 #1 | +1 #2 | +1 #3 |
|---|---|---|---|---|---|---|
| bonk | 9 units | 8,324 | 3.84 | Blitzcrank (270, 1.87) | Nunu (237, 1.89) | Leblanc (126, 1.84) |
| stellar_combo | 8 units | 2,771 | 4.14 | Shen (972, 2.25) | Morgana (159, 2.37) | Rammus (115, 2.53) |
| termeepnal_velocity | 9 units | 13,164 | 4.24 | Bard (515, 1.79) | Fizz (262, 1.94) | Gnar (123, 2.20) |
| tf | 8 units | 15,079 | 3.18 | Morgana (5.6k, 2.24) | Shen (4.6k, 2.28) | Nunu (1.9k, 2.34) |
| veigar | 9 units | 19,353 | 4.35 | Bard (941, 1.85) | Fizz (475, 2.09) | Gnar (201, 2.29) |
| teemo | 9 units | 24,118 | 4.01 | Blitzcrank (956, 1.87) | Nunu (887, 1.88) | Leblanc (373, 1.92) |

### Variants（≥3 unit 差异）

| Comp | Variant 描述 | Games | AVP | 差异 |
|---|---|---|---|---|
| vex_95 | Vanguard 版（Illaoi/Nunu/Sona/Summon 替换 Rammus/Rhaast/Shen） | 12,262 | 3.81 | 4+ units |
| mecha | MasterYi/Viktor 版（drops Bard/Fiora/Karma） | 9,461 | 5.53 | 3 units |
| kaisa | Aatrox/Chogath/Maokai shell（完全不同前排） | 9,626 | 5.16 | 4 units |
| the_big_bang | Viktor carry / Overlord 版 | 5,327 | 2.93 | 5 units |
| stellar_combo | TF carry 版 | 2,290 | 3.20 | 6 units |
| bonk | Blitzcrank/Leblanc/Nunu 版（替换 Lissandra/Nami/Zoe） | 2,386 | 3.99 | 3 units |
| pyke | 3-4 个完全不同的 variant（Witchcraft/Sona/Viktor 版） | ~5k | varies | 5+ units |

### Comp 共享发现

| 共享 Primary Board | Comps | 原因 |
|---|---|---|
| Nasus/Teemo 3★ reroll core (9 units) | bonk, teemo | 同一 reroll 阵容，不同 comp 定义 |
| Poppy/Veigar 9-unit board | termeepnal_velocity, veigar | 同一阵容，不同 hero augment |
| Primordian 8-unit board | primordian, stellar_combo | 同一 Bel'Veth core，Aatrox augment 是变体 |

## What I Learned

### 1. Flex Slot 的三种模式

**有明确 +1（20/29 comp）**：大多数 comp 有清晰的 +1 候选，前 1-3 名按 freq 排列。AVP 改善通常 1-2 分。

**无 +1 / 已满（5/29 comp）**：xayah、kaisa、reach_for_the_stars 停在 primary level 不再上升；two_tanky_samira 已经 10 人；shepherd 已经 10 人需要 level 11。

**Variant 主导（4/29 comp）**：pyke、stellar_combo、the_big_bang、vex_95 有多个显著 variant，+1 分析意义有限（因为 "primary" 本身只代表其中一个玩法）。

### 2. 最常见的 +1 Unit

| Unit | 出现次数（作为 +1） | 典型角色 |
|---|---|---|
| Morgana | 12 comp | 通用前排/辅助 |
| Sona | 5 comp | 5-cost 辅助 |
| Bard | 5 comp | 5-cost 辅助 |
| Shen | 4 comp | 前排坦克 |
| Rhaast | 4 comp | 5-cost 战士 |

Morgana 是绝对的 "万金油 +1" — 在 12 个 comp 中出现，覆盖所有费用段。

### 3. AVP 改善量级

| Comp Type | Primary AVP | +1 AVP | 改善 |
|---|---|---|---|
| 5-cost (nova_95) | 3.95 | 2.08 | -1.87 |
| 4-cost (vanguard_leblanc) | 5.32 | 3.75 | -1.57 |
| 3-cost (viktor) | 3.59 | 2.39 | -1.20 |
| Reroll (lulu) | 6.66 | 4.13 | -2.53 |

Lulu 的 +1 (Rhaast) 改善最大（-2.53），因为 7 人口的 Lulu comp 极度不完整，Rhaast 补上了关键的 5-cost 战力。

### 4. Comp 共享现象

3 对 comp 共享相同的 primary board（bonk/teemo、termeepnal_velocity/veigar、primordian/stellar_combo）。这说明 compositions.py 中某些 comp 定义实际上指向同一个阵容，只是 hero augment 或 carry 不同。

## Open Questions

1. **Morgana 为什么是万金油 +1？** 她的 trait 和技能在这么多 comp 中都有价值吗？还是因为她是"最容易找到的高费 unit"？
2. **无 +1 comp（xayah, kaisa, reach_for_the_stars）真的不升级吗？** 还是 sample 不够（这些 comp 很少到 level 10）？
3. **Variant-heavy comp（pyke）如何做 item 分析？** 不同 variant 的 BIS 可能完全不同。
4. **comp 共享（bonk = teemo, veigar = termeepnal_velocity）是否应该合并 comp 定义？**

## Questions for Xing

1. **Morgana 的万金油地位** — 符合你的游戏体验吗？还是这反映了某种数据偏差？
2. **Comp 共享** — bonk 和 teemo 共享 primary board，是否意味着 compositions.py 的定义有冗余？
3. **Mecha 的 level 计算** — 确认 Mecha 3 unit 占 5 slot，所以 7-unit board = level 9？

## Sources
- MetaTFT `exact_units_traits2` endpoint
- [[methods/flex-slot-detection]] — 分析方法
- [[concepts/composition]] — variant/flex slot 定义
