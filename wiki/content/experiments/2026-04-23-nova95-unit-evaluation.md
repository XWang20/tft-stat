# Experiment: Unit Evaluation -- Nova 95 十人口分析（Level-Controlled）
**Status**: 🧪 draft
**Date**: 2026-04-23
**Module**: 4 (Unit Evaluation)

## The Question

在 Nova 95 阵容中，标准 9 人口阵容由哪些 unit 组成？到 10 人口时，挂谁最能提升 AVP？

这是一个玩家每局都会面临的决策问题。Level 10 时选择的 unit 直接影响对局结果。

**方法论要点**: 使用 `--level` 参数控制玩家等级，`--filter` 固定核心 unit 控制阵容完整度。Nova 95 标准阵容是 9 人口，所以核心 unit 分析用 `--level 9`，十人口候选分析用 `--level 10` + 固定核心 9 人。两层控制消除了 level bias 和阵容完整度混杂。

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
| Level 10 + Core 9 固定 | 28,934 | 1.94 | 94.3% | 51.7% |

Level 9 和 Level 10 的 AVP 差异巨大（4.67 vs 2.08）。这正是为什么必须分开分析 -- 如果混合所有 level，任何在 level 10 出现率高的 unit 都会因为 level bias 而显得更好。

第三行是在 Level 10 基础上再固定核心 9 个 unit（Aatrox, Akali, Vex, Fiora, Shen, Graves, Morgana, Blitzcrank, Nunu），只保留"标准阵容 + 1"的局面。28,934 局占 Level 10 总局数的 53%，样本充足。AVP 从 2.08 提升到 1.94，说明能凑齐核心阵容的玩家本身就更强。

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

## Chapter 3: Level 10 +1 控制变量分析

### 方法论

之前的 Chapter 3 只控制了 level（`--level 10`），但 level 10 的局面中核心阵容可能不完整 -- 有些局缺 Shen、有些缺 Nunu，这些"残缺阵容"会污染分析。

现在用第二层控制：**固定核心 9 个 unit**。这和 build 分析的"固定两件看第三件"完全对应 -- 先固定基础条件，再看边际变量的影响。

```bash
python3 cli.py units --comp nova_95 --level 10 \
  --filter "Unit('TFT17_Aatrox') & Unit('TFT17_Akali') & Unit('TFT17_Vex') & Unit('TFT17_Fiora') & Unit('TFT17_Shen') & Unit('TFT17_Graves') & Unit('TFT17_Morgana') & Unit('TFT17_Blitzcrank') & Unit('TFT17_Nunu')"
```

结果：28,934 局（占 Level 10 总量的 53%），整体 AVP = 1.94。

### 正 Necessity 候选

| Rank | Unit | Play Rate | AVP | Necessity | w/o AVP | Games |
|---|---|---|---|---|---|---|
| 1 | Sona | 47.6% | 1.91 | **+0.027** | 1.97 | 13,780 |
| 2 | Rhaast | 6.3% | 1.63 | **+0.021** | 1.96 | 1,808 |
| 3 | Jhin | 10.6% | 1.78 | **+0.019** | 1.96 | 3,056 |
| 4 | Maokai | 3.9% | 1.90 | **+0.002** | 1.94 | 1,131 |

### 负 Necessity Unit

| Unit | Play Rate | AVP | Necessity | w/o AVP | Games |
|---|---|---|---|---|---|
| Rammus | 1.7% | 2.12 | **-0.003** | 1.94 | 497 |
| Bard | 7.8% | 2.09 | **-0.013** | 1.93 | 2,246 |
| TahmKench | 8.6% | 2.08 | **-0.013** | 1.93 | 2,489 |

### 关键发现

**Sona 在固定核心后回到第一**。固定核心 9 人后，Sona 的 Necessity 从 `--level 10` only 的 +0.015 上升到 +0.027，重新成为第一。原因：`--level 10` only 中有 47% 的局核心不完整，这些"残缺阵容"的局质量参差不齐，稀释了 Sona 的真实边际贡献。固定核心后，每局的基准条件一致，Sona 的边际效果更清晰。

**Top 3 排名逆转**。`--level 10` only 的排名是 Jhin > Rhaast > Sona；固定核心后变成 Sona > Rhaast > Jhin。这说明 `--level 10` only 的分析中存在混杂变量 -- 核心阵容完整度。

**Maokai 从负变正**。`--level 10` only 时 Maokai Necessity 为 -0.026；固定核心后变成 +0.002（近零）。之前 Maokai 的负 Necessity 很可能是因为：选 Maokai 的局中有相当比例核心不完整（如缺 Shen、缺 Nunu），是核心缺失导致的差表现，不是 Maokai 本身的问题。

**TahmKench 仍然是负价值**。即使控制了 level 和核心阵容，TahmKench 的 Necessity 仍为 -0.013。这是经过两层控制后依然成立的结论，可信度比之前高得多。

**Bard 暴露为负价值**。在 `--level 10` only 数据中 Bard 不够显眼；固定核心后，Bard（7.8%，-0.013）和 TahmKench 一样是负 Necessity，与 Maokai 的中性（+0.002）形成对比。

## Chapter 4: 三层控制的逐步精炼

三层分析展示了控制变量如何逐步改变结论。

### Top 3 候选的 Necessity 变化

| 控制层 | 条件 | Games | AVP | Sona | Jhin | Rhaast |
|---|---|---|---|---|---|---|
| 0 | 无控制（全局） | ~367K | ~3.6 | **+0.127** | +0.043 | +0.016 |
| 1 | `--level 10` | 54,360 | 2.08 | +0.015 | **+0.021** | +0.019 |
| 2 | `--level 10` + 核心 9 固定 | 28,934 | 1.94 | **+0.027** | +0.019 | +0.021 |

### Maokai / TahmKench 的 Necessity 变化

| 控制层 | Maokai | TahmKench |
|---|---|---|
| 1 | -0.026 | -0.035 |
| 2 | **+0.002** | -0.013 |

### 解读

**Sona 的三段式变化**。Layer 0（+0.127）→ Layer 1（+0.015）→ Layer 2（+0.027）。第一次控制（level）去掉了 level bias，Necessity 暴跌 88%。第二次控制（核心固定）去掉了阵容完整度混杂，Necessity 回升 80%。Sona 在层层控制后依然是最优候选，但优势从"压倒性"变成"微弱"。

**Jhin 和 Rhaast 非常稳定**。无论怎么控制，两者的 Necessity 都在 +0.016 ~ +0.021 范围内波动。它们不受 level bias 和阵容完整度的影响，是"真实价值"最稳定的候选。

**Maokai 的"平反"**。Layer 1 中 Maokai 是 -0.026（"劣质选择"），Layer 2 中变成 +0.002（中性）。之前的负 Necessity 是阵容完整度的混杂效应 -- 选 Maokai 的 level 10 局中有很多核心不全的弱局，不是 Maokai 本身有害。

**TahmKench 依然负**。经过两层控制后 TahmKench 仍为 -0.013，是三个控制层级中唯一始终为负的常见候选。这可能是真实的负面效应。

### 方法论启示

这个三层分析完美展示了控制变量法的核心逻辑：

1. **每一层控制都消除一种混杂变量**：Layer 1 消除 level bias，Layer 2 消除阵容完整度 bias
2. **控制可以改变结论方向**：Maokai 从"有害"变"中性"，Sona 的排名两次反转
3. **真实效应在多层控制后趋于收敛**：Jhin 和 Rhaast 几乎不受控制层影响，说明它们的 Necessity 反映的是真实边际价值

## Cross-Validation

### tftable 不可用

tftable SSH 连接超时，无法进行直接对比。

### 与历史实验关联

在 [[experiments/2026-04-22-cross-validation-vex-nova95]] 中发现：
- **Item necessity**: Spearman rho = 0.993 -- 几乎完美匹配
- **Unit necessity**: Spearman rho = -0.476 -- 接近反向

这意味着我们的 unit necessity 和 tftable 的 IC3 necessity 是完全不同的指标。IC3 可能衡量的是 "unit 作为 3 件套 carry 的重要性"，而我们衡量的是 "unit 存在对整体 AVP 的影响"。Shen 从不拿 3 件装备，在 IC3 中会很低，但在我们的 necessity 中排第一。

## What I Learned

### 1. 两层控制比单层控制更可靠，但结论变化不大

Layer 1（level only）：Jhin +0.021 ≈ Rhaast +0.019 ≈ Sona +0.015 → 三者持平。
Layer 2（level + 核心固定）：Sona +0.027 > Rhaast +0.021 ≈ Jhin +0.019 → Sona 微弱领先。

核心结论不变：**Sona、Jhin、Rhaast 都是合理的 Level 10 候选**。但 Layer 2 给了 Sona 一个微弱但一致的优势。

### 2. 控制变量揭示了混杂效应

Maokai 在 Layer 1 是 -0.026（"有害"），Layer 2 是 +0.002（"中性"）。差异来自阵容完整度混杂 -- Layer 1 中选 Maokai 的局有很多核心不全的弱局。固定核心后这个混杂被消除，Maokai 的"负价值"消失。

这说明 `--level` 只控制了一个维度的混杂，阵容完整度是另一个独立的混杂维度。

### 3. 控制越多，信号越弱但越真实

Layer 0 的 Necessity 数值（Sona +0.127）很大，但大部分是 bias。Layer 2 的数值（Sona +0.027）小得多，但去掉了两层混杂。在 AVP 已经低至 1.94 的 level 10 标准阵容中，任何第 10 人的边际影响确实很小 -- 这本身就是一个重要发现。

### 4. "固定核心看边际" = Unit 版的 "固定两件看第三件"

控制变量法在 unit evaluation 和 item build analysis 中的逻辑完全一致：
- Item: 固定 base pair → 看第三件的边际 Necessity
- Unit: 固定核心阵容 → 看 +1 unit 的边际 Necessity

这是同一个方法论框架在不同维度的应用。

## Open Questions

1. **Sona/Jhin/Rhaast 的差异是否有统计显著性？** 即使在 Layer 2 中 Sona 领先，Necessity 差距仅 0.006~0.008，可能在置信区间内。需要 CI 分析。
2. **IC3 necessity 到底怎么计算的？** 理解 tftable 的 unit 级指标是 Module 4 的关键前提。
3. **TahmKench 的负 Necessity 在两层控制后是否可以信任？** -0.013 不大，但方向一致。是因果还是仍有残余混杂？
4. **还有第三层控制吗？** 例如固定主 C 的星级、固定经济状态等。是否存在收益递减点？
5. **Bard 为什么是负价值？** Bard（-0.013）和 TahmKench 一样负，但 Bard 是 5-cost unit，理论上应该更强。是什么导致 Bard 与差表现相关？

## Questions for Xing

1. **IC3 necessity 的计算方式** -- 是 "Item Count 3" 的缩写吗？它衡量的是 unit 作为 carry 的重要性还是存在的重要性？
2. **Maokai 的"平反"是否合理？** Layer 1 中 Maokai 是负价值，Layer 2 中变成中性。这意味着之前"Maokai 是劣质选择"的结论是混杂效应。作为玩家，Maokai 在 level 10 完整阵容中确实中性吗？
3. **TahmKench 为什么经过两层控制仍然为负？** 是 TahmKench 本身的机制问题，还是选 TahmKench 反映了某种我们没控制的弱势局面？
4. **还有哪些混杂维度需要控制？** 目前控制了 level 和核心阵容完整度。血量、经济、3 star 数量等是否也是重要的混杂变量？

## Review

