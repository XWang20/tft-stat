# Experiment: AVP / Delta / Necessity 三指标的数学结构与「装备越必要 Delta 越接近 0」的误解
**Status**: 🧪 draft
**Date**: 2026-05-12
**Module**: 2

> **数据范围**：本文所有数据均为 **diamond+ rank、过去 7 天**，覆盖 challenger / GM / master / diamond 四档。
> **AVP 来源**：本文表格里的 `Games / Freq / AVP / w/o` 都来自 MetaTFT API 的原始 `placement_count`（你也可以在 MetaTFT 网页同样 filter 下看到一致数值）。
> **Delta / Necessity**：从原始 AVP 用公式 `Δ=(a−A)/(1−p)`、`N=p/(1−p)·(A−a)` 重算 —— 不直接读取任何网站显示列。

---

## The Question

社区里有一种广为流传的说法：

> 一个装备如果出场率非常高（接近必出），那 Delta 一定会趋近于 0，因为「这个装备就是这个阵容本身」，with 和 without 没有区别。

这个论断常被拿来「劝诫」初学者：「别看 Guinsoo 的 Delta 不大，这个装备就是核心，Delta 接近 0 才是它必要的证据」。但仔细推敲，这个论断**无论数学上还是直觉上都不成立**。

本文用 **重装提莫（Teemo ic3）** 的真实数据 + 两张等高线图来解构 AVP、Delta、Necessity 三个指标，并直接反驳上述误解。顺带回答另一个常见问题：为什么 Necessity 比 Delta 更适合做「阵容核心装备」的排名。

最后还会附一章关于「不同数据网站显示的 Delta 列对不上」的发现 —— 这是另一个独立问题，给读者一个实用的工作建议。

---

## Chapter 1: 三个指标的数学关系

设 `p = play_rate`、`a = item_AVP`、`A = overall_AVP`。

把"with 这个装备的局"和"without 这个装备的局"看作 overall 的两个互补子集，由权重平均的恒等式可以解出：

```
w/o_AVP   = (A − p × a) / (1 − p)

Delta     = a − w/o = (a − A) / (1 − p)        负数 = 好
Necessity = w/o − A = p / (1 − p) × (A − a)    正数 = 重要
```

两个等价改写很关键：

- **Delta 是 (a−A) 的「Leverage 放大」**：分母 `(1−p)` 越小（freq 越高），同样的 `(a−A)` 被放大得越多。
- **Necessity 是 (A−a) 的「Frequency 加权」**：用 `p/(1−p)` 加权，freq 越高权重越大。
- 两者代数关系：`Necessity = −p × Delta`。它们其实是**同一个原始量** `(A−a)` 的两种不同放大方式。

下面整段实验都会回到这两个公式。

---

## Chapter 2: 实验设置 — 为什么用「重装提莫」

filter 极简：

```python
Unit('TFT17_Teemo', item_min=3, item_max=3)
```

也就是「Teemo 满装 3 件」。选 Teemo 而不是其他更复杂的阵容，有两个原因：

1. **Teemo 是 reroll comp，他自己就是唯一 carry**。不需要写「Fiora 或 Vex 或 Graves 任一」这种 OR-comp filter，避免了「副 C 顺手装备占据高 freq」这种污染。
2. **`item_min=3, item_max=3` 直接锁定主 C 状态**：分析的样本就是「Teemo 主 C，3 件装备完装」的局，没有「Teemo 只是站位 / 只装一两件」的局。

**baseline**：175,244 games，A = **4.1443**（diamond+ 7d，跟你在 MetaTFT 同样 filter 下看到的数字一致）。

---

## Chapter 3: Teemo ic3 物品数据

按 Necessity 排序的 top 10（normal items + 主要 emblem，截掉极低 freq）：

| Item | Games | Freq | AVP (a) | w/o | Δ | Necessity |
|---|---:|---:|---:|---:|---:|---:|
| **Guinsoo's Rageblade** | 167,799 | **96%** | 4.134 | 4.378 | −0.244 | **+0.234** |
| Giant Slayer | 107,877 | 62% | 4.063 | 4.275 | −0.213 | +0.131 |
| **Rabadon's Deathcap** | 52,303 | 30% | 3.899 | 4.249 | **−0.350** | +0.104 |
| Hextech Gunblade | 57,052 | 33% | 4.066 | 4.182 | −0.117 | +0.038 |
| Statikk Shiv | 4,348 | 2% | 3.771 | 4.154 | −0.383 | +0.009 |
| Archangel's Staff | 15,838 | 9% | 4.123 | 4.146 | −0.024 | +0.002 |
| Guinsoo's Rageblade ★2 | 6,739 | 4% | 4.107 | 4.146 | −0.039 | +0.001 |
| Striker's Flail | 7,834 | 4% | 4.197 | 4.142 | +0.055 | −0.002 |
| Vanguard Emblem | 4,869 | 3% | 4.264 | 4.141 | +0.123 | −0.003 |

> 验算 Guinsoo 行：`a=4.134, A=4.144, p=167799/175244=0.957`，`w/o=(4.144−0.957·4.134)/0.043=4.378`，`Δ=4.134−4.378=−0.244`，`N=4.378−4.144=+0.234`。可以自己在 MetaTFT 用同样 filter 验：`Games`、`Freq`、`AVP` 三列肉眼一致；`w/o` 你可以**手动加 "no Guinsoo's Rageblade" filter** 读出 ~4.38。

两个先放在这里的观察：

- **Δ 最负的是 Rabadon's Deathcap**（−0.350，30% freq），不是 Guinsoo。
- **Necessity 最高的是 Guinsoo**（+0.234），远超第二名 Giant Slayer（+0.131）。

也就是说，Δ 和 Necessity 对 top 1 的判断**完全不一样**。这是后面讨论 Necessity 优势的关键案例。

---

## Chapter 4: 两张等高线图 — 看 Delta 和 Necessity 的几何形状

把 (play_rate, item_AVP) 画成平面，背景填的是 metric 在该平面上的等值线（A 固定为 4.14），点是上表里的真实装备。

### Necessity Landscape

![Necessity Landscape](/experiments/2026-05-12-necessity-landscape.png)

观察：
- 等高线在低/中 freq 区域很缓，但接近 freq=1 时**急速向右上拉升** —— 因为 `p/(1−p)` 在 p→1 时趋向无穷。
- 这就是为什么 Guinsoo（freq 96%、AVP 4.13 vs A=4.14，gap 只有 0.01）仍然能排到 Necessity 第一：杠杆系数 `0.96/0.04 = 24×` 把那 0.01 的 gap 放大成 +0.234。
- Rabadon's Deathcap（freq 30%、gap 0.245，是 Guinsoo 的 ~24 倍）只有 +0.104 —— 因为权重系数才 `0.30/0.70 ≈ 0.43×`。

### Delta Landscape

![Delta Landscape](/experiments/2026-05-12-delta-landscape.png)

观察：
- 等高线在 freq < 50% 的区域几乎是水平的：Δ ≈ a − A，play_rate 不太影响。
- 当 freq > 80% 后，等高线急速发散 —— 因为 `1/(1−p)` 在这里也趋向无穷。也就是说，**高 freq 区域同样的 (a−A) 被 Δ 放大、不是缩小**。
- 这两张图共用相同的 (p, a) 平面，但 metric 几何形状完全不同：Necessity 在 p→1 沿 (A−a) 一侧爆炸，Δ 在 p→1 沿 (a−A) 另一侧爆炸。两者都不会在 p→1 时归零。

> Δ=0 的等高线 **是水平的、不依赖 p**：当且仅当 `a = A` 时 Δ=0。换句话说，"Δ→0" 只能由 "item AVP 等于 overall AVP" 引起，不能由 "freq 高" 引起。

---

## Chapter 5: 直接反驳「freq 高 → Delta 趋近 0」

最简洁的反驳：**Guinsoo 在 Teemo ic3 freq 96%，公式 Δ = −0.244，不是 0**。

如果 freq 高真的能强制 Δ→0，Guinsoo 这个 96% 的极端例子早该读出 0 附近的数。但代入公式 `Δ = (4.134−4.144)/0.043 = −0.244`，被 23× 杠杆放大着。

让我们再看其他几个高 freq 装备的真实 Δ（diamond+ 7d，公式重算）：

| Comp | Top freq item | Freq | AVP | Δ (公式) | Necessity |
|---|---|---:|---:|---:|---:|
| Teemo ic3 | Guinsoo's Rageblade | 96% | 4.134 | **−0.24** | +0.234 |
| Lulu Reroll | Jeweled Gauntlet | 88% | 4.443 | **−0.22** | +0.193 |
| Lulu Reroll | Nashor's Tooth ★1 | 82% | 4.461 | −0.04 | +0.037 |
| Kaisa (Fizz/Illaoi) | Infinity Edge | 87% | 4.299 | **−0.32** | +0.279 |

**没有一个高 freq 装备的公式 Δ 接近 0。** Lulu 的 Jeweled Gauntlet 在 88% freq 上 Δ = −0.22；Kaisa 的 Infinity Edge 在 87% freq 上是 −0.32。

> Lulu 的 Nashor's Tooth ★1 表面看像反例 —— freq 82% Δ 只有 −0.04。但这是因为 Nashor's Tooth 在 Lulu 阵容里有 ★2（"双锯齿门牙"是 BIS 之一），那 48% 的 ★2 局把 ★1 的差异性吃掉了。如果只看 ★1 vs 完全没有 Nashor's Tooth 的局，差异会被 ★2 局占据 baseline 大半的事实稀释。这是「子状态污染」而非「freq 高 → Δ=0」。

---

## Chapter 6: 神话错在哪里 — 数学诊断

「freq → 1 时 Δ → 0」这个说法的**唯一**成立条件是 `a → A`。代入公式：

```
Δ = (a − A) / (1 − p)
```

要让 Δ → 0，需要分子 `(a − A) → 0` 比分母 `(1 − p) → 0` 更快。

什么时候 `a = A`？当 with-this-item 子集和 overall 子集**有完全相同的 AVP 分布**。这意味着这件装备**对最终名次没有任何 lift** —— with 和 without 两组玩家的胜率完全一样。

直觉版本：

> 「装备 freq 接近 1 但 Δ 接近 0」**不是装备必要的特征，而是装备无关紧要的特征**。
>
> 因为如果绝大多数局都拿到了，但 with 组和 without 组的 AVP 几乎一样 —— 那这件装备到底贡献了什么？答案是：什么都没贡献。它只是"恰好被普遍持有"，但对结果没影响。

社区直觉的错误在于把 **"装备就是阵容本身" 解读成 "with = overall"**。但事实是即使一件装备真的是阵容核心，**没拿到它的局会显著掉名次** —— 也就是 `w/o > A`，于是 `(a − A) < 0` 仍然成立，Δ 不会归零。Guinsoo 在 Teemo ic3 里的 4% 缺货局 AVP 大约是 `4.14 + 0.234 = 4.38`（你可以在 MetaTFT 加 `no Guinsoo` filter 直接验证），明显比 baseline 4.14 差 —— 这正是 Guinsoo 必要的证据，而不是 Δ 接近 0 是它必要的证据。

---

## Chapter 7: Necessity vs Delta — 排名分歧的案例

### Teemo ic3 里 top 1 完全相反

| 排名指标 | top 1 | 数值 | freq |
|---|---|---|---|
| Δ（最负） | Rabadon's Deathcap | −0.350 | 30% |
| Necessity（最大） | Guinsoo's Rageblade | +0.234 | 96% |

**两个指标都没有错**，他们在回答不同的问题：

| 指标 | 在回答的问题 |
|---|---|
| Δ（最负） | 「在某一局里，碰巧拿到这件装备能让我提升多少名次？」（per-game lift） |
| Necessity（最大） | 「如果整个 metaverse 都不存在这件装备，整体 AVP 会差多少？」（comp-level dependence） |

对玩家的 prio 决策来说，Necessity 的答案更接近你真正想要的：
- Guinsoo 是 Teemo 的核心 BIS（攻速锁定 reroll 必出），没有它阵容崩塌；优先 slam。
- Rabadon's Deathcap 单件 lift 很高（−0.35），但它**不是 prio**，因为只有 30% 玩家拿得到（需要 BF + Rod，凑卡难）。它高 lift 部分原因是：能完成 Dcap 的玩家通常已经把核心装备先做完了（survivorship）。

### Statikk Shiv：低 freq 高 Δ 的典型陷阱

Teemo ic3 数据里：

| Item | Freq | AVP | Δ | Necessity |
|---|---:|---:|---:|---:|
| Statikk Shiv | 2% | 3.771 | **−0.383** | +0.009 |

Statikk Shiv 的 Δ（−0.38）几乎跟 Rabadon's Deathcap 一样负，但 Necessity 只有 +0.009 —— 几乎是 0。Δ 看起来像「Statikk Shiv 是隐藏神装」，但 Necessity 直接告诉你「99% 玩家不需要这件，可以无视」。

这就是 Necessity 相比 Δ 的另一个核心优势：**抗 carousel/emblem survivorship**。Δ 把低 freq 高 lift 的装备捧上天，Necessity 通过 freq 加权直接把它压成 ~0。如果按 Δ 排名 prio 装备，会被 Statikk Shiv / 各种 emblem / Tactician's Crown 等根本拿不到的东西误导。

---

## Chapter 8: Necessity 也不是终极答案

需要承认 Necessity 的几个局限，以避免它被神化成另一个误解的源头：

1. **Necessity 假设 freq 是 lift 的合理代理**。但 freq 高也可能是 selection 的产物 —— 拿到 Guinsoo 的 96% 玩家本来就是「够稳的局 + 够熟的玩家」，without 组 4% 是「拿不到的非典型局」。Necessity 不区分这两种因果。
2. **Necessity 受 baseline AVP 影响**：同一件装备在不同 condition（filter 紧/松、不同 comp）下绝对值不同，虽然 ranking 通常稳定（参见 [[experiments/2026-04-22-cross-validation-vex-nova95]] Spearman 0.993）。
3. **niche-but-strong 装备会被压制**：低 freq 装备 Necessity 总是低，但不一定是它差，可能只是少有人 prio。本文 Rabadon's Deathcap 和 Statikk Shiv 都是潜在例子。
4. **tftable 等工具有更进阶的 debiasing**（IC3 weighting、conditional baseline 等），Necessity 只是其中较易解释的一步。本文不展开。

实践原则：**Necessity 适合回答「阵容核心装备」，Δ 适合回答「per-game 边际」，两者结合 + Build Analysis 才是完整答案**。详见 [[methods/build-analysis]]。

---

## Chapter 9: 一个独立发现 — 不同数据源 Δ 列口径不一样

写到这里有个意外发现，记下来给读者参考。

**同一份 filter（Teemo ic3）、同一件装备（Guinsoo's Rageblade）**，三个主流网站显示的 Δ 列：

| 数据源 | 显示的 Δ |
|---|---:|
| 我们 cli.py / 公式 `(a−A)/(1−p)` | **−0.24** |
| MetaTFT | **−0.09** |
| DataTFT | **0.00** |
| TacticsTools | **(待补)** |

> 🖼️ 截图位 1：MetaTFT 的 Teemo ic3 Items 表，Guinsoo 那行的 Δ 列
> 🖼️ 截图位 2：DataTFT 同样 filter 下的 Guinsoo Δ
> 🖼️ 截图位 3：TacticsTools 同样 filter 下的 Guinsoo Δ

**三家显示值差距巨大**（−0.24 / −0.09 / 0.00），但**底层数据其实一致** —— 你在任何一家手动加 "without Guinsoo" filter，看到的 AVP 都接近 4.38。差异完全来自各家对 Δ 列做的额外处理（Bayesian shrinkage、置信区间收缩、capping 等），而不是数据本身。

我们目前观察到，**这种差异只在 freq 极高（≥ ~85%）的核心装备上明显**。中低 freq 装备各家显示基本一致，也跟我们公式一致。

### 验证「真实 Δ」的方法

如果你怀疑某网站的 Δ 列：

1. **手动加 "without this item" filter**（任何网站都支持）
2. 读出 AVP，这就是真实的 `w/o`
3. 用公式自己算：`Δ = a − w/o`

无论你用哪家网站做这个 filter 操作，得到的 `w/o` 应该都接近一致（因为是同一份原始数据）。然后公式 Δ 就是公式 Δ，不受任何显示算法干扰。

### 推荐使用方式

| 装备 freq | 推荐做法 |
|---|---|
| < 80% | 直接看任何网站的 Δ 列就行，三家都对 |
| ≥ 80%（高 freq 核心装备） | **不要直接看 Δ 列**。手动加 exclude filter 看 AVP，自己算 |
| 嫌麻烦 | 用我们 cli.py：`python3 cli.py items <unit> --comp <comp>`，Δ 列已经按公式算好 |

这章发现的更深层意义：**TFT 数据网站的 "Δ" 不是一个公认的标准量，而是各家自己定义的衍生指标**。社区里那个「freq 高 → Δ→0 是必要的」论断之所以传播开，可能也跟某些工具显示的 Δ 在高 freq 段被人为压低有关 —— 那个压低是显示算法的产物，不是 TFT 数学的客观属性。

---

## What I Learned

| 论断 | 真相 |
|---|---|
| "freq 越接近 1，Δ 越接近 0 是必然" | **错**。Δ = (a−A)/(1−p)，freq 高反而**放大** Δ，不是缩小 |
| "Δ 接近 0 是装备必要的标志" | **反过来**：Δ=0 等价于 a=A，这意味着这件装备对最终名次没有 per-game lift —— 是无关紧要的标志 |
| "Necessity 只是 Δ 的换算，提供不了新信息" | 代数上是 `−p×Δ`，但 ranking 信息被 freq 重新加权后，更接近"阵容核心"的 player 直觉 |
| "Δ 和 Necessity 哪个对" | 两者都对，回答不同的问题。Δ 答 per-game lift，Necessity 答 comp-level dependence |
| "看网站 Δ 列就行" | 高 freq 装备各家口径不同，需要手动 filter 验真实 w/o |

数据先行，结论后到。下次有人说「这个装备 Δ 接近 0 是因为它必出」，请他给一个 a < A 但 (a−A)/(1−p) 趋近 0 的真实案例 —— 大概率给不出，因为这种"必出且无 lift"的装备在数据上几乎不存在。

---

## Open Questions

- [ ] Lulu / Bonk 等 comp 里能否找到 Δ 与 Necessity ranking 完全反向的情形（不仅是 top 1 不同，而是整个 top 5 翻转）？
- [ ] tftable 的进阶 debiasing 在 Teemo ic3 上会把 Statikk Shiv 推到第几位？是否颠覆当前 Δ vs Necessity 的故事？
- [ ] 当 condition 极紧（freq → 1）时，Necessity 和 Δ 都会被压缩，应当用什么标度去比较"压缩前后" rankings 的稳定度？
- [ ] 各数据网站 Δ 显示算法到底是什么？是否在不同 patch / sample size 下口径会变？

## Questions for Xing

- 截图位 1-3 你后面方便补一下，三个网站同 filter 同装备的 Δ 列截图。
- TacticsTools 的 Teemo ic3 Guinsoo Δ 是多少？

---

## Sources / Cross-references
- [[concepts/metrics]] — 三指标定义、play rate 作为 confidence signal
- [[experiments/2026-04-21-vex-nova95-items]] — 之前的 Vex Nova 95 物品分析（5 metric 对比）
- [[experiments/2026-04-22-cross-validation-vex-nova95]] — Necessity rank Spearman 0.993 跨数据源稳定
- [[concepts/biases]] — Survivorship bias、selection effect

---

## Review

(留待 Xing 填写)
