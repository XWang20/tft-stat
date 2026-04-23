# Experiment: Unit Evaluation -- Nova 95 十人口分析（Level-Controlled）
**Status**: 🧪 draft
**Date**: 2026-04-23
**Module**: 4 (Unit Evaluation)

## The Question

在 Nova 95 阵容中，标准 9 人口阵容由哪些 unit 组成？到 10 人口时，挂谁最能提升 AVP？

这是一个玩家每局都会面临的决策问题。Level 10 时选择的 unit 直接影响对局结果。

**方法论要点**: 使用 `--level` 参数控制玩家等级。Nova 95 标准阵容是 9 人口，所以核心 unit 分析用 `--level 9`，十人口候选分析用 `--level 10`。这消除了 level bias -- 不同等级的玩家不会混入同一个分析中。

## Chapter 1: Nova 95 核心阵容结构

### Filter 定义

Nova 95 的 `compositions.py` 定义：

```
(Fiora(3items) | Vex(3items) | Graves(3items))
& DRX >= 2
& ~Mecha >= 4
& ~Kindred & ~Aurora(3items) & ~MasterYi(3items) & ~Zed
```

关键点：
- **三选一主 C**：Fiora、Vex、Graves 中任意一个带 3 件装备作为主力输出
- **DRX(N.O.V.A.) >= 2**：至少 2 个 NOVA trait unit
- **排除条件**：排除 nova_yi (MasterYi/Kindred)、Mecha、Zed 等其他阵容

### 样本量

| 条件 | Games | AVP | Top4% | Win% |
|---|---|---|---|---|
| Level 9 | 199,684 | 4.67 | 46.2% | 11.4% |
| Level 10 | 54,360 | 2.08 | 92.4% | 48.3% |

Level 9 和 Level 10 的 AVP 差异巨大（4.67 vs 2.08）。这正是为什么必须分开分析 -- 如果混合所有 level，任何在 level 10 出现率高的 unit 都会因为 level bias 而显得更好。

## Chapter 2: Level 9 核心 Unit Necessity 排名

在 199,684 局 level 9 数据中（整体 AVP = 4.67），play rate > 70% 的 unit 有 **9 个**，构成标准 level 9 阵容。

Necessity 公式：`p/(1-p) * (overall_AVP - unit_AVP)`

| Rank | Unit | Play Rate | AVP | Necessity | w/o AVP |
|---|---|---|---|---|---|
| 1 | Shen | 87.9% | 4.54 | **+0.946** | 5.62 |
| 2 | Fiora | 88.1% | 4.57 | **+0.740** | 5.41 |
| 3 | Vex | 90.0% | 4.61 | **+0.540** | 5.21 |
| 4 | Aatrox | 92.7% | 4.63 | **+0.511** | 5.18 |
| 5 | Blitzcrank | 74.8% | 4.52 | **+0.446** | 5.12 |
| 6 | Morgana | 79.8% | 4.56 | **+0.434** | 5.10 |
| 7 | Nunu | 74.0% | 4.54 | **+0.370** | 5.04 |
| 8 | Graves | 86.1% | 4.66 | **+0.062** | 4.73 |
| 9 | Akali | 92.5% | 4.67 | **+0.000** | 4.67 |

### 关键发现

**Shen 是最不可替代的 unit**。没有 Shen 的 level 9 局 AVP 暴跌到 5.62，Necessity 高达 +0.946。前排坦克的不可替代性远超输出位。

**Akali 是"空气 unit"**。Play rate 第二高（92.5%）但 Necessity 为零 -- 有没有 Akali 对 AVP 完全没影响。Akali 是"默认填入"的 unit，几乎场场在但不产生价值差异。

**前排 > 输出位**。Shen (+0.946) > Fiora (+0.740) > Vex (+0.540)。在 level 9 的标准对局中，前排坦克的稀缺性使其比 carry 更关键。这可能反映了一个事实：carry 之间可以互相替代（Fiora/Vex/Graves 三选一），但 Shen 没有替代品。

## Chapter 3: Level 10 +1 候选分析

在 54,360 局 level 10 数据中（整体 AVP = 2.08），分析非核心 unit 作为第 10 个 unit 的价值。因为已经限定 `--level 10`，所有数据来自同一个人口等级，level bias 被控制。

### 正 Necessity 候选

| Rank | Unit | Play Rate | AVP | Necessity | Games |
|---|---|---|---|---|---|
| 1 | Jhin | 13.9% | 1.95 | **+0.021** | 7,563 |
| 2 | Rhaast | 6.7% | 1.81 | **+0.019** | 3,630 |
| 3 | Sona | 42.4% | 2.06 | **+0.015** | 23,031 |
| 4 | Xayah | 2.9% | 1.83 | **+0.007** | 1,555 |
| 5 | Jax | 3.4% | 1.94 | **+0.005** | 1,853 |
| 6 | Mordekaiser | 3.3% | 2.07 | **~0.000** | 1,816 |

### 负 Necessity Unit

| Unit | Play Rate | AVP | Necessity | Games |
|---|---|---|---|---|
| Maokai | 34.2% | 2.13 | **-0.026** | 18,612 |
| TahmKench | 37.1% | 2.14 | **-0.035** | 20,164 |

### 关键发现

**Top 3 差距极小**。Jhin (+0.021)、Rhaast (+0.019)、Sona (+0.015) 的 Necessity 非常接近。在 level 10 的环境中（整体 AVP 已经是 2.08），任何 unit 的边际影响都很小。玩家不必纠结于这三者之间的选择 -- 差异在噪声范围内。

**Sona 是最常见但不是最好的选择**。Sona 的 play rate（42.4%）远高于 Jhin（13.9%）和 Rhaast（6.7%），但 Necessity 排第三。高采用率不等于高价值 -- 这和 Akali 的情况类似。

**Maokai 和 TahmKench 是负价值选择**。即使控制了 level 10，这两个 unit 仍然与更差的表现相关。Maokai（34.2%）和 TahmKench（37.1%）是非常常见的 level 10 选择，但数据一致显示它们是劣质选择。可能的解释：在 level 10 时加 Maokai/TahmKench 意味着玩家没有找到更好的 unit（店里没刷到 Sona/Jhin），本身就反映了较弱的局面。

### 与未控制 Level 的对比

之前不控制 level 时，Sona 的 Necessity 是 +0.127（Jhin 的 3 倍）。控制 level 后，Sona 降到 +0.015，排名从第 1 跌到第 3。

| Unit | 未控制 Necessity | Level 10 Necessity | 变化 |
|---|---|---|---|
| Sona | +0.127 | +0.015 | 下降 88% |
| Jhin | +0.043 | +0.021 | 下降 51% |
| Rhaast | +0.016 | +0.019 | 上升 19% |

Sona 的 play rate 从全局 16.5% 跳到 level 10 的 42.4%（2.6x），说明 Sona 高度集中在 level 10 -- 之前的高 Necessity 大部分是 level bias。Jhin 和 Rhaast 的 play rate 增幅较小（2.0x 和 1.7x），受 level bias 影响更小。

**这是 level bias 的教科书级演示**：不控制 level 时，Sona 看起来"以压倒性优势排第一"；控制 level 后，三者几乎持平。

## Chapter 4: Level 9 vs Level 10 核心 Unit 对比

核心 unit 在两个 level 下的 Necessity 变化本身是有趣的分析。

| Unit | L9 Play% | L9 Necessity | L10 Play% | L10 Necessity |
|---|---|---|---|---|
| Shen | 87.9% | +0.946 | 94.5% | +0.343 |
| Aatrox | 92.7% | +0.511 | 94.1% | +0.319 |
| Fiora | 88.1% | +0.740 | 93.5% | +0.285 |
| Nunu | 74.0% | +0.370 | 74.2% | +0.172 |
| Morgana | 79.8% | +0.434 | 88.4% | +0.153 |
| Vex | 90.0% | +0.540 | 93.0% | +0.132 |
| Blitzcrank | 74.8% | +0.446 | 80.7% | +0.126 |
| Graves | 86.1% | +0.062 | 85.6% | +0.000 |
| Akali | 92.5% | +0.000 | 92.3% | +0.000 |

### 观察

1. **所有核心 unit 的 Necessity 在 level 10 大幅缩小**。Level 10 的整体 AVP 只有 2.08（vs level 9 的 4.67），所以 AVP 差异空间被压缩。能到 level 10 的玩家本身就很强，单个 unit 的边际影响自然更小。

2. **排名基本稳定**。Shen 在两个 level 都排第一。Akali 和 Graves 在两个 level 都是最低。这说明核心 unit 的"不可替代性"是阵容结构决定的，不随 level 变化。

3. **Aatrox 在 level 10 上升到第二**。Level 9 时 Aatrox 排第四（+0.511），level 10 上升到第二（+0.319）。Fiora 从第二降到第三。这可能反映了在高水平对局中前排的相对重要性更高。

## Cross-Validation

### tftable 不可用

tftable SSH 连接超时，无法进行直接对比。

### 与历史实验关联

在 [[experiments/2026-04-22-cross-validation-vex-nova95]] 中发现：
- **Item necessity**: Spearman rho = 0.993 -- 几乎完美匹配
- **Unit necessity**: Spearman rho = -0.476 -- 接近反向

这意味着我们的 unit necessity 和 tftable 的 IC3 necessity 是完全不同的指标。IC3 可能衡量的是 "unit 作为 3 件套 carry 的重要性"，而我们衡量的是 "unit 存在对整体 AVP 的影响"。Shen 从不拿 3 件装备，在 IC3 中会很低，但在我们的 necessity 中排第一。

## What I Learned

### 1. 控制 Level 彻底改变了十人口结论

未控制 level 时：Sona 以 3 倍优势领先（"明确首选"）。
控制 level 后：Jhin、Rhaast、Sona 三者几乎持平（差距在 0.006 以内）。

这不是微调，而是结论性的改变。之前的"Sona 是明确首选"完全是 level bias 的产物。正确的结论是：**level 10 时 Jhin、Rhaast、Sona 都是合理选择，差异不大**。

### 2. Play Rate 和 Necessity 的分离在两个维度上都成立

- 核心 unit：Akali（92.5% play rate, 0 necessity）vs Shen（87.9% play rate, +0.946 necessity）
- Level 10 候选：Sona（42.4% play rate, +0.015 necessity）vs Jhin（13.9% play rate, +0.021 necessity）

在核心 unit 和非核心 unit 中，都可以看到"高频使用不等于高价值"。

### 3. 负 Necessity 在控制 Level 后依然成立

Maokai (-0.026) 和 TahmKench (-0.035) 在 level 10 仍然是负 Necessity。这不再能用 level bias 解释 -- 在同一个 level 下，选择这两个 unit 确实与更差的表现相关。

## Open Questions

1. **Jhin/Rhaast/Sona 的差异是否有统计显著性？** Necessity 差距仅 0.006，可能在置信区间内。需要 CI 分析。
2. **IC3 necessity 到底怎么计算的？** 理解 tftable 的 unit 级指标是 Module 4 的关键前提。
3. **Maokai/TahmKench 的负 Necessity 是因果还是相关？** 虽然控制了 level，但可能仍有未控制的混杂变量（如血量、经济状态）。
4. **Akali 的零 Necessity 是否意味着可替换？** 如果在 level 9 就用更好的 unit 替代 Akali，能否提升 AVP？

## Questions for Xing

1. **IC3 necessity 的计算方式** -- 是 "Item Count 3" 的缩写吗？它衡量的是 unit 作为 carry 的重要性还是存在的重要性？
2. **Sona 的结论是否符合直觉？** 控制 level 后 Sona 不再是明确首选 -- 作为玩家，这是否合理？
3. **Maokai/TahmKench 的实际情况** -- 玩家在 level 10 选择 Maokai/TahmKench 通常是什么情况？是"没刷到更好的"还是有其他原因？

## Review

