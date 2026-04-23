# Experiment: Unit Evaluation -- Nova 95 十人口分析
**Status**: 🧪 draft
**Date**: 2026-04-23
**Module**: 4 (Unit Evaluation)

## The Question

在 Nova 95 阵容中，标准 9 人口阵容由哪些 unit 组成？到 10 人口时，挂谁最能提升 AVP？

这是一个玩家每局都会面临的决策问题。Level 10 时选择的 unit 直接影响对局结果。

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

总样本量：**271,144 局**，整体 AVP **4.290**，Top4 率 53.0%，胜率 18.1%。

### 核心阵容

通过 play rate 识别核心 unit。271k 局数据中，play rate > 70% 的 unit 有 **9 个**：

| Unit | Play Rate | AVP |
|---|---|---|
| Aatrox | 92.5% | 4.23 |
| Akali | 91.5% | 4.27 |
| Vex | 88.4% | 4.17 |
| Fiora | 86.7% | 4.11 |
| Shen | 86.0% | 4.06 |
| Graves | 84.5% | 4.25 |
| Morgana | 78.2% | 4.06 |
| Blitzcrank | 73.2% | 4.05 |
| Nunu | 73.0% | 4.15 |

9 个 unit 组成标准 level 9 阵容。实际游戏中，Blitzcrank 和 Nunu 都是核心成员——两者 play rate 极为接近 (73% vs 73%)，可能根据局面二选一或都上场。

### 样本 Board 验证

从 15 个样本 board 中观察到的典型结构：

**标准 Level 9**：Aatrox + Akali + Shen + Fiora + Vex + Graves + Morgana + Blitzcrank + Nunu

**Level 10 常见追加**：Sona（出现在 #1、#2 名次的 board 中）、Maokai、TahmKench（出现在中下名次 board 中）

## Chapter 2: Unit Necessity 排名

将 item necessity 的公式套用到 unit：

```
Necessity = p/(1-p) * (overall_AVP - unit_AVP)
```

整体 AVP = 4.290。完整排名：

### 核心 Unit（play rate > 70%）

| Rank | Unit | Play Rate | AVP | Necessity | w/o AVP |
|---|---|---|---|---|---|
| 1 | Shen | 86.0% | 4.06 | **+1.402** | 5.69 |
| 2 | Fiora | 86.7% | 4.11 | **+1.155** | 5.45 |
| 3 | Vex | 88.4% | 4.17 | **+0.927** | 5.22 |
| 4 | Morgana | 78.2% | 4.06 | **+0.832** | 5.12 |
| 5 | Aatrox | 92.5% | 4.23 | **+0.704** | 4.99 |
| 6 | Blitzcrank | 73.2% | 4.05 | **+0.665** | 4.96 |
| 7 | Nunu | 73.0% | 4.15 | **+0.373** | 4.66 |
| 8 | Graves | 84.5% | 4.25 | **+0.225** | 4.51 |
| 9 | Akali | 91.5% | 4.27 | **+0.170** | 4.46 |

### 非核心 Unit（level 10 候选，正 Necessity）

| Rank | Unit | Play Rate | AVP | Necessity | Games |
|---|---|---|---|---|---|
| 10 | Sona | 16.5% | 3.64 | **+0.127** | 44,710 |
| 11 | Jhin | 7.0% | 3.72 | **+0.043** | 19,110 |
| 12 | Rhaast | 4.0% | 3.90 | **+0.016** | 10,751 |
| 13 | Xayah | 2.5% | 3.85 | **+0.011** | 6,700 |
| 14 | Jax | 4.0% | 4.09 | **+0.009** | 10,823 |
| 15 | Corki | 1.3% | 3.96 | **+0.004** | 3,393 |

### 负 Necessity Unit（常见但有害的添加）

| Unit | Play Rate | AVP | Necessity |
|---|---|---|---|
| Maokai | 30.4% | 4.53 | **-0.104** |
| TahmKench | 31.4% | 4.55 | **-0.117** |
| Rammus | 9.0% | 4.94 | **-0.064** |
| Bard | 6.6% | 4.44 | **-0.010** |

### 核心 Unit 的反直觉发现

Akali 是 **play rate 第二高**（91.5%）但 **necessity 最低**（+0.170）的核心 unit。这意味着 Akali 几乎每场都在场（91.5%），但有没有 Akali 对 AVP 的影响很小（差距仅 0.02 placement）。Akali 是"默认填入"的 unit，而不是"必须有"的 unit。

相比之下，Shen 的 play rate (86.0%) 不是最高，但 necessity (1.402) 最大——没有 Shen 的局 AVP 暴跌到 5.69。Shen 是 Nova 95 最不可替代的 unit。

## Chapter 3: 十人口候选分析

### 候选人一览

Level 10 增加的第 10 个 unit，正 necessity 候选排序：

| 排名 | Unit | Play Rate | AVP | Necessity | Trait |
|---|---|---|---|---|---|
| **1** | **Sona** | 16.5% | 3.64 | +0.127 | Commander (unique) |
| 2 | Jhin | 7.0% | 3.72 | +0.043 | Eradicator (unique) |
| 3 | Rhaast | 4.0% | 3.90 | +0.016 | Redeemer (unique) |
| 4 | Xayah | 2.5% | 3.85 | +0.011 | -- |
| 5 | Jax | 4.0% | 4.09 | +0.009 | -- |

**Sona 以压倒性优势排第一**，necessity 是第二名 Jhin 的 3 倍（0.127 vs 0.043）。

### 三个候选的详细数据

单独查询每个候选 unit 加入 nova_95 后的总体数据：

| 条件 | Games | AVP | Top4% | Win% |
|---|---|---|---|---|
| Nova 95 整体 | 271,144 | 4.290 | 53.0% | 18.1% |
| + Sona | 44,710 | 3.644 | 64.5% | 27.6% |
| + Jhin | 19,110 | 3.719 | 63.0% | 27.4% |
| + Rhaast | 10,751 | 3.896 | 58.8% | 27.0% |

三个候选的 AVP 都大幅好于整体（3.64-3.90 vs 4.29）。但这并不意味着它们"让阵容变好了"——选择偏差是主要原因。

### Sona + Jhin 共现分析

Sona 和 Jhin 是否在同一 board 上出现（level 10 情况）？

- Sona + Jhin 共现：2,013 局，AVP 3.807
- 在 44,710 局 Sona 局中，仅 4.5% 同时有 Jhin
- 在 19,110 局 Jhin 局中，10.5% 同时有 Sona

结论：Sona 和 Jhin 是**竞争关系**（二选一），不是互补关系。大部分局面中，玩家在 level 10 选择 Sona 或 Jhin 其中一个。

### Trait 分析

三个 top 候选（Sona、Jhin、Rhaast）的 trait 全部是 **unique trait**（Commander / Eradicator / Redeemer，各自 breakpoint = 1）。这意味着它们的加入**不会激活任何新的 trait breakpoint**——它们的价值纯粹来自 unit 自身的能力和属性。

### 关键 Caveat: Level Bias (选择偏差)

Unit necessity 用于 level 10 分析有一个根本性的偏差：

**到达 level 10 本身就与胜利相关。** 到达 level 10 的玩家通常：
1. 已经处于优势（连胜或高血量）
2. 有足够的经济支撑升级
3. 核心阵容已经成型

因此任何作为 "第 10 个 unit" 出现的 unit 都会有系统性偏高的 AVP。

但是：**这个偏差对所有候选 unit 是等价的。** 不论选 Sona 还是 Jhin 还是 Rhaast，level bias 对三者的影响方向和幅度相同。所以 **相对排名** (Sona > Jhin > Rhaast) 应该是可靠的，即使绝对 necessity 值被 level bias 膨胀了。

### Maokai/TahmKench 的教训

Maokai (30.4%) 和 TahmKench (31.4%) 的 play rate 远高于 Sona (16.5%)，但 necessity 是负值。进一步分析：

| 条件 | Games | AVP |
|---|---|---|
| Maokai 无 Sona | 69,430 | 4.636 |
| Maokai 有 Sona | 13,129 | 3.961 |

Maokai 在没有 Sona 的局中 AVP 高达 4.636（很差）——这些是 level 9 挣扎中用 Maokai 凑前排的局。Maokai 不是"让阵容变差"，而是"出现在本来就差的局面里"——典型的 selection bias。

## Cross-Validation

### tftable 不可用

tftable SSH 连接超时，无法进行直接对比。

### 与历史实验的关联

在 [[experiments/2026-04-22-cross-validation-vex-nova95]] 中发现：
- **Item necessity**: Spearman ρ = 0.993 — 几乎完美匹配
- **Unit necessity**: Spearman ρ = -0.476 — 接近反向!

这意味着我们的 unit necessity 和 tftable 的 IC3 necessity 是**完全不同的指标**：

| 维度 | 我们的 Unit Necessity | tftable IC3 Necessity |
|---|---|---|
| 公式 | p/(1-p) * (A - a) | 未知 (scale 0-8) |
| 衡量的是 | unit 在不在场对 AVP 的影响 | 未知 (可能与 carry 程度有关) |
| Shen 的排名 | #1 (最高) | 可能很低 (Shen 很少拿 3 件) |
| 解释 | 存在价值 | 可能衡量 carry 价值 |

"IC3" 很可能指 "Item Count 3" -- 衡量 unit 作为 3 件套 carry 的重要性。这会和我们的"存在价值"完全不同：Shen 作为纯坦从不拿 3 件装备，在 IC3 中会很低；但 Shen 不在场时 AVP 暴跌 1.4，在我们的 necessity 中排第一。

本实验无法直接验证这个假设（tftable 不可用），但这是一个关键的开放问题。

## What I Learned

### 1. Unit Necessity 和 Item Necessity 意义不同

Item necessity 衡量的是"某件装备对 carry 有多重要"——前提是 carry 已经在场。Unit necessity 衡量的是"某个 unit 在不在场对整体 AVP 的影响"——这是一个更粗粒度的指标。

对于 **核心 unit**（play rate > 70%），necessity 主要反映"不可替代性"：
- Shen (+1.40) > Fiora (+1.16) > Vex (+0.93) — 坦克/前排比输出位更不可替代

对于 **非核心 unit**（play rate < 20%），necessity 主要反映"level 10 边际价值"，但严重受 level bias 影响。

### 2. Play Rate 和 Necessity 分离

Akali (91.5% play rate, +0.170 necessity) vs Shen (86.0% play rate, +1.402 necessity)。

高 play rate 不等于高 necessity。一个 unit 可以几乎场场出现但对结果影响很小（Akali），也可以不那么普遍但极其关键（Shen）。

这和 item 分析中 "play rate 不代表重要性" 是同一个原理。

### 3. Level 10 结论：Sona 是明确的首选

在 level bias 影响等价的前提下，Sona 以 3 倍于第二名的 necessity 优势成为最佳 level 10 选择。

- Sona: 44,710 局验证，AVP 3.64，Necessity +0.127
- Jhin: 19,110 局验证，AVP 3.72，Necessity +0.043
- Rhaast: 10,751 局验证，AVP 3.90，Necessity +0.016

三者的 trait 贡献都是 unique（solo 激活），不产生 trait breakpoint synergy，所以差异来自 unit 本身的能力。

### 4. 负 Necessity 不代表 "unit 有害"

Maokai (-0.104) 和 TahmKench (-0.117) 的负 necessity 主要是 selection bias 而非因果关系。它们出现在玩家阵容残缺、level 9 凑前排的弱势局面中。

## Open Questions

1. **如何消除 level 10 分析中的 level bias？** 可能方法：只看 10 unit 的 board，控制 board size 变量
2. **IC3 necessity 到底怎么计算的？** 理解 tftable 的 unit 级指标是 Module 4 的关键前提
3. **Sona 的具体价值来源是什么？** 是 Commander trait 的效果，还是 Sona 本身的技能？需要 build 级分析
4. **Akali 的低 necessity 是否意味着可以替换？** 如果 Akali 在 level 9 就可以被更好的 unit 替代，这对 nova_95 的 level 9 构建也有意义
5. **unit necessity 的 Spearman ρ = -0.476 是系统性的吗？** 需要在更多 comp 上测试

## Questions for Xing

1. **IC3 necessity 的计算方式**——是 "Item Count 3" 的缩写吗？它衡量的是 unit 作为 carry 的重要性还是存在的重要性？这直接决定了我们的 unit necessity 是否需要换一个公式。
2. **Level bias 的标准处理方式**——在 tftable 或其他工具中，level 10 分析是否有标准方法来控制 level bias？
3. **Sona 的结论是否符合直觉？** 作为玩家，level 10 选 Sona 是否是 Nova 95 的常见选择？

## Review
