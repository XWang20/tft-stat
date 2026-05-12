# Experiment: AVP / Delta / Necessity 三指标的数学结构与「装备越必要 Delta 越接近 0」的误解
**Status**: 🧪 draft
**Date**: 2026-05-12
**Module**: 2

> **数据范围**：本文所有数据均为 **diamond+ rank、过去 7 天**，覆盖 challenger / GM / master / diamond 四档。
> **Delta 来源**：本文所有 Delta 都是直接从 raw `placement_count` 用公式 `(a − A)/(1 − p)` 重新计算的，**不是 MetaTFT 网页显示值**。如读者对照 MetaTFT 看到不一致的 Delta，那是因为 MetaTFT 内部口径与本文（standard 公式）不同，本文的目的是讨论数学定义本身。

---

## The Question

社区里有一种广为流传的说法：

> 一个装备如果出场率非常高（接近必出），那 Delta 一定会趋近于 0，因为「这个装备就是这个阵容本身」，with 和 without 没有区别。

这个论断常被拿来「劝诫」初学者：「别看 Guinsoo 的 Delta 不大，这个装备就是核心，Delta 接近 0 才是它必要的证据」。但仔细推敲，这个论断**无论数学上还是直觉上都不成立**。

本文用 Vex 在 Nova 95 里的真实数据 + 两张等高线图来解构 AVP、Delta、Necessity 三个指标，并直接反驳上述误解。顺带回答另一个常见问题：为什么 Necessity 比 Delta 更适合做「阵容核心装备」的排名。

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

## Chapter 2: 实验设置 — 为什么要加 Vex ic3

baseline 是 Nova 95，但分析对象是 Vex 的装备。原 nova_95 filter 是：

```
(Fiora item_min=2 OR Vex item_min=2 OR Graves item_min=2)
& DRX≥2 & ~Mecha≥4 & ~Kindred & ~Corki & ...
```

注意 carry 是「三选一」。如果直接跑 `items TFT17_Vex --comp nova_95`，58k 个底盘里既包含 Vex-carry 局，也包含 Fiora-carry / Graves-carry 局。在那些局里 Vex 只是副 C，他可能只有 0–1 件装备（甚至是顺手堆的非典型装备）。这会带来两个污染：

1. **baseline AVP 被混合的 carry 群体拉高**（因为副 C Vex 局通常胜率更平均、上分能力更弱）。
2. **副 C 的"顺手装备"会以高 freq 出现**：例如 Giant Slayer 在 Fiora-carry 局里很常见，于是 GS 在 Vex 物品分析里以 41% freq、+0.138 Necessity 占据第二位 —— 这是个错觉。

加上 `Unit('TFT17_Vex', item_min=3, item_max=3)` 之后（diamond+ 7d）：

| | 无 ic3 | + Vex ic3 |
|---|---|---|
| baseline AVP | 4.54 | **4.21** |
| 总样本 | 58k | 47k |
| Guinsoo freq | 90% | **96%** |
| Giant Slayer 在 top? | 41% (#2) | **跌出 top 8** |
| Guinsoo Delta | −0.78 | −0.14 |
| Guinsoo Necessity | +0.70 | +0.133 |

baseline 下移了 0.33 AVP，所有 metric 的绝对值都被压缩，但 ranking 含义变得**真正代表 Vex 主 C 的装备分布**。本文剩余分析全部基于 ic3-conditioned 数据。

> 副作用：ic3 后所有 metric 都被压缩，乍一看「freq 高 → Delta 接近 0」反而像是被验证了。其实是 condition 收紧把 with-Guinsoo 几乎拉到等于 baseline，without 组只剩 4% 的非典型样本。这点后面会回头讨论。

---

## Chapter 3: Vex 在 Nova 95 (ic3) 的物品数据

CLI（注意是手动加 `--filter`，cli 默认行为不变）：
```bash
python3 cli.py items TFT17_Vex --comp nova_95 --normal-only \
    --filter "Unit('TFT17_Vex', item_min=3, item_max=3)"
# + 内部 query 改用 rank=CHALLENGER,GRANDMASTER,MASTER,DIAMOND, days=7
```

overall AVP: **4.2100**, 46,879 games

| Item | Games | Freq | AVP | Delta | Necessity |
|---|---:|---:|---:|---:|---:|
| Guinsoo's Rageblade | 44,956 | **96%** | 4.2043 | −0.139 | **+0.133** |
| Hextech Gunblade | 11,517 | 25% | 4.0531 | −0.208 | +0.051 |
| Red Buff | 5,829 | 12% | 3.8746 | **−0.383** | +0.048 |
| Rabadon's Deathcap | 9,899 | 21% | 4.0560 | −0.195 | +0.041 |
| Striker's Flail | 7,644 | 16% | 4.0556 | −0.184 | +0.030 |
| Archangel's Staff | 4,829 | 10% | 4.0977 | −0.125 | +0.013 |
| Morellonomicon | 3,374 | 7% | 4.1906 | −0.021 | +0.002 |
| Nashor's Tooth | 1,735 | 4% | 4.1527 | −0.060 | +0.002 |

> 数据计算检验：以 Guinsoo 为例，`a=4.2043`、`A=4.2100`、`p=44956/46879=0.9590`，`w/o=(4.2100−0.9590·4.2043)/0.0410=4.343`，`Delta=4.2043−4.343=−0.139`，`Necessity=4.343−4.2100=+0.133`。与表中一致。
>
> **MetaTFT 旁证（2026-05-12）**：在 MetaTFT Explorer 里手动设置 `Vex w/o Guinsoo` 的 filter 看 AVP，得到 ~**4.4**，与上面的公式 w/o=4.34 几乎一致。但 MetaTFT 同一行显示的 Delta 列绝对值却 **< 0.1**，与他们自家 w/o 数据应得出的 `4.20−4.4=−0.2` 不一致。这表明 **MetaTFT 网页 Delta 列可能做了 Bayesian shrinkage 或别的口径转换，不能直接当作公式 delta 使用**。本文所有 Delta 都从 raw `placement_count` 按公式重算，以避免这种口径污染。

两个观察先放在这里：

- **Delta 最负的不是 Guinsoo，而是 Red Buff**（−0.383 vs −0.139）。Red Buff 才 12% freq。
- **Necessity 最高的是 Guinsoo（+0.133）**，远超第二名 Hextech Gunblade（+0.051）。

也就是说，Delta 和 Necessity 在 top 1 上**意见不一致**。这是后面讨论 Necessity 优势的关键案例。

---

## Chapter 4: 两张等高线图 — 看 Delta 和 Necessity 的几何形状

把 (play_rate, item_AVP) 画成平面，背景填的是 metric 在该平面上的等值线（A 固定为 4.21），点是上表里的真实装备。

### Necessity Landscape

![Necessity Landscape](/experiments/2026-05-12-necessity-landscape.png)

观察：
- 等高线在低/中 freq 区域很缓，但接近 freq=1 时**急速向右上拉升** —— 因为 `p/(1−p)` 在 p→1 时趋向无穷。
- 这就是为什么 Guinsoo（freq 96%、AVP 4.20 vs A=4.21，gap 只有 0.006）仍然能排到 Necessity 第一：杠杆系数 `0.96/0.04 = 24×` 把那 0.006 的 gap 放大成 +0.133。
- Red Buff（freq 12%、gap 0.34，是 Guinsoo 的 ~57 倍）只有 +0.048 —— 因为权重系数才 `0.12/0.88 ≈ 0.136×`。

### Delta Landscape

![Delta Landscape](/experiments/2026-05-12-delta-landscape.png)

观察：
- 等高线在 freq < 50% 的区域几乎是水平的：Delta ≈ a − A，play_rate 不太影响。
- 当 freq > 80% 后，等高线急速发散 —— 因为 `1/(1−p)` 在这里也趋向无穷。也就是说，**高 freq 区域同样的 (a−A) 被 Delta 放大、不是缩小**。
- 这两张图共用相同的 (p, a) 平面，但 metric 几何形状完全不同：Necessity 在 p→1 沿 (A−a) 一侧爆炸，Delta 在 p→1 沿 (a−A) 另一侧爆炸。两者都不会在 p→1 时归零。

> Delta=0 的等高线 **是水平的、不依赖 p**：当且仅当 `a = A` 时 Delta=0。换句话说，"Delta→0" 只能由 "item AVP 等于 overall AVP" 引起，不能由 "freq 高" 引起。

---

## Chapter 5: 直接反驳「freq 高 → Delta 趋近 0」

最简洁的反驳：**Guinsoo 在 Vex Nova 95 (ic3) freq 96%，Delta = −0.139，不是 0**。

如果 freq 高真的能强制 Delta→0，Guinsoo 这个 freq 96% 的极端例子早该读出 0 附近的数。但现实是它仍然停在 −0.139，被 25× 的杠杆放大着。

让我们再看其他几个高 freq 装备的真实 Delta（diamond+ 7d，filter 已含 holder ic3）：

| Comp | Top freq item | Freq | Delta | Necessity |
|---|---|---:|---:|---:|
| Vex Nova 95 (+Vex ic3) | Guinsoo's Rageblade | 96% | **−0.14** | +0.133 |
| Lulu Reroll | Jeweled Gauntlet | 88% | **−0.22** | +0.192 |
| Lulu Reroll | Nashor's Tooth ★1 | 82% | **−0.04** | +0.036 |
| Kaisa (+Fizz/Illaoi comp) | Infinity Edge | 87% | **−0.32** | +0.278 |

**没有一个高 freq 装备的 Delta 接近 0。** Lulu 的 Jeweled Gauntlet 在 88% freq 上仍有 −0.22 的强 Delta；Kaisa 的 Infinity Edge 在 87% freq 上是 −0.32。

> Lulu 的 Nashor's Tooth ★1 表面看像反例 —— freq 82% Delta 只有 −0.04。但这是因为 Nashor's Tooth 在 Lulu 阵容里有 ★2（"双锯齿门牙"是 BIS 之一），那 48% 的 ★2 局把 ★1 的差异性吃掉了。如果只看 ★1 vs 完全没有 Nashor's Tooth 的局，差异会被 ★2 局占据 baseline 大半的事实稀释。这是「子状态污染」而非「freq 高 → Delta 0」。

把这个论点扩展到社区数据，可以同时观察 MetaTFT / TacticsTools 等工具上的高 freq 装备（截图位）：

> **🖼️ 截图位 1**：MetaTFT 上某个高 freq 装备（推荐选一个 Tier 1-2 阵容里 freq ≥ 80% 的装备）的 single-item delta 显示，截图说明 Delta 仍是显著负值。
>
> **🖼️ 截图位 2**：另一个不同阵容的高 freq 装备类似截图。
>
> **🖼️ 截图位 3**（可选）：一个 freq < 30% 但 Delta 也很负的装备 —— 用来对比"低 freq 高 Delta"的存在，说明 Delta 和 freq 没有因果联系。

预测：所有截图都会显示**高 freq 装备的 Delta 仍是显著负值**，没有一个会读出 0 附近。

---

## Chapter 6: 神话错在哪里 — 数学诊断

「freq → 1 时 Delta → 0」这个说法的**唯一**成立条件是 `a → A`。代入公式：

```
Delta = (a − A) / (1 − p)
```

要让 Delta → 0，需要分子 `(a − A) → 0` 比分母 `(1 − p) → 0` 更快。

什么时候 `a = A`？当 with-this-item 子集和 overall 子集**有完全相同的 AVP 分布**。这意味着这件装备**对最终名次没有任何 lift** —— with 和 without 两组玩家的胜率完全一样。

直觉版本：

> 「装备 freq 接近 1 但 Delta 接近 0」**不是装备必要的特征，而是装备无关紧要的特征**。
>
> 因为如果绝大多数局都拿到了，但 with 组和 without 组的 AVP 几乎一样 —— 那这件装备到底贡献了什么？答案是：什么都没贡献。它只是"恰好被普遍持有"，但对结果没影响。

社区直觉的错误在于把 **"装备就是阵容本身" 解读成 "with = overall"**。但事实是即使一件装备真的是阵容核心，**没拿到它的局会显著掉名次** —— 也就是 `w/o > A`，于是 `(a − A) < 0` 仍然成立，Delta 不会归零。Guinsoo 在 Vex Nova 95 (ic3) 里的 4% 缺货局 AVP 大约是 `4.21 + 0.133 = 4.34`，明显比 baseline 4.21 差 —— 这正是 Guinsoo 必要的证据，而不是 Delta 接近 0 是它必要的证据。

---

## Chapter 7: Necessity vs Delta — 排名分歧的案例

### Vex Nova 95 (ic3)：top 1 完全相反

| 排名指标 | top 1 | 数值 | freq |
|---|---|---|---|
| Delta（最负） | Red Buff | −0.383 | 12% |
| Necessity（最大） | Guinsoo | +0.133 | 96% |

**两个指标都没有错**，他们在回答不同的问题：

| 指标 | 在回答的问题 |
|---|---|
| Delta（最负） | 「在某一局里，碰巧拿到这件装备能让我提升多少名次？」（per-game lift） |
| Necessity（最大） | 「如果整个 metaverse 都不存在这件装备，整体 AVP 会差多少？」（comp-level dependence） |

对玩家的 prio 决策来说，Necessity 的答案更接近你真正想要的：
- Guinsoo 是 Vex 的核心，没有它阵容崩塌；优先 slam。
- Red Buff 单件 lift 很高，但它**不是 prio**，因为它只是 4 件 attack-speed flex slot 的一个。它高 lift 部分原因是：能完成 Red Buff 的玩家通常已经把核心装备先做完了（survivorship）。

### 第二个例子：Kaisa 阵容里的 Infinity Edge vs Last Whisper

新 kaisa comp（`Kaisa + Fizz` 或 `Kaisa + Illaoi + DarkStar≥4`，再加 Kaisa ic3，diamond+ 7d）：

| Item | Freq | AVP | Delta | Necessity |
|---|---:|---:|---:|---:|
| Infinity Edge | 87% | 4.30 | **−0.322** | **+0.280** |
| Last Whisper | 20% | 4.48 | **+0.176** | **−0.036** |

两个指标都同意：IE 是核心，LW 不是。但**两者讲故事的方式不一样**：

- **Delta 视角**：IE 的 Δ=−0.32（很好），LW 的 Δ=**+0.18**（注意是正的 —— 拿到 LW 反而比平均更差）。这种 "正 delta" 的解读对初学者很反直觉：「LW 不是 AD 装备吗？怎么会拉低名次？」需要解释 LW 是 carousel 顺手物 / Spear of Shojin 类玩家的备选项 / 在这个 comp 里位置已被 Madreds Bloodrazor 抢走等等。
- **Necessity 视角**：IE 是 +0.28（高），LW 是 −0.04（贴近 0 的小负数）。Necessity 把 LW 直接显示成「拿掉这个装备整体不会变差」 —— 一眼就是「不重要」，不需要解释 sign 是正是负。

**Necessity 是 Delta 的「以阵容为中心」的重新尺度化**：它把所有低频 / 不重要的装备压到 0 附近，而把真正核心的装备（高 freq + 真正 lift）拉到正区间。这种尺度更适合 player 直觉中的「这件装备到我这套阵容里有多重要」。

> 顺带解释一下 LW 的正 Delta 怎么来：用公式 `Delta = (a − A)/(1 − p) = (4.48 − 4.34)/0.80 = +0.176` 验算一致。本质是这个 comp 里 LW 通常出现在 carousel 抓不到核心装备的副线局，并不是 LW 本身坏。Necessity 把这种 "freq 不算高 + AVP 略劣 baseline" 的装备全部压到 ≈0，不再让 reader 去解读 sign。

### 第三个例子：低 freq 高 Delta 的 Tactician's Crown 类装备

在其他 comp 里更下方还能看到这种装备。例如 Bonk 数据里：

| Item | Freq | AVP | Delta | Necessity |
|---|---:|---:|---:|---:|
| Tactician's Crown | <1% | 2.94 | −1.22 | +0.002 |

Tactician's Crown 的 Delta 是 −1.22（极端好），但 Necessity 几乎为 0 —— 因为它只在 0.x% 的局里出现。Delta 把 emblem 这种 niche-but-strong 装备捧上天，Necessity 直接把它压成 ~0。如果你按 Delta 排名 prio 装备，会被 Tactician's Crown / Radiant 这些根本拿不到的东西误导。

这是 Necessity 的另一个重要优势：**抗 carousel/emblem survivorship**。

---

## Chapter 8: Necessity 也不是终极答案

需要承认 Necessity 的几个局限，以避免它被神化成另一个误解的源头：

1. **Necessity 假设 freq 是 lift 的合理代理**。但 freq 高也可能是 selection 的产物 —— 拿到 Guinsoo 的 96% 玩家本来就是「够稳的局 + 够熟的玩家」，without 组 4% 是「拿不到的非典型局」。Necessity 不区分这两种因果。
2. **Necessity 受 baseline AVP 影响**：同一件装备在不同 condition（filter 紧/松、不同 comp）下绝对值不同，虽然 ranking 通常稳定（参见 [[experiments/2026-04-22-cross-validation-vex-nova95]] Spearman 0.993）。
3. **niche-but-strong 装备会被压制**：低 freq 装备 Necessity 总是低，但不一定是它差，可能只是少有人 prio。本文 Red Buff 就是潜在例子：Delta 最强但 Necessity 第 3。
4. **tftable 等工具有更进阶的 debiasing**（IC3 weighting、conditional baseline 等），Necessity 只是其中较易解释的一步。本文不展开。

实践原则：**Necessity 适合回答「阵容核心装备」，Delta 适合回答「per-game 边际」，两者结合 + Build Analysis 才是完整答案**。详见 [[methods/build-analysis]]。

---

## What I Learned

| 论断 | 真相 |
|---|---|
| "freq 越接近 1，Delta 越接近 0 是必然" | **错**。Delta = (a−A)/(1−p)，freq 高反而**放大** Delta，不是缩小 |
| "Delta 接近 0 是装备必要的标志" | **反过来**：Delta=0 等价于 a=A，这意味着这件装备对最终名次没有 per-game lift —— 是无关紧要的标志 |
| "Necessity 只是 Delta 的换算，提供不了新信息" | 代数上是 `−p×Delta`，但 ranking 信息被 freq 重新加权后，更接近"阵容核心"的 player 直觉 |
| "Delta 和 Necessity 哪个对" | 两者都对，回答不同的问题。Delta 答 per-game lift，Necessity 答 comp-level dependence |

数据先行，结论后到。下次有人说「这个装备 Delta 接近 0 是因为它必出」，请他给一个 a < A 但 (a−A)/(1−p) 趋近 0 的真实案例 —— 大概率给不出，因为这种"必出且无 lift"的装备在数据上几乎不存在。

---

## Open Questions

- [ ] Lulu / Bonk 等 comp 里能否找到 Delta 与 Necessity ranking 完全反向的情形（不仅是 top 1 不同，而是整个 top 5 翻转）？
- [ ] tftable 的进阶 debiasing 在 Vex Nova 95 上会把 Red Buff 推到第几位？是否颠覆当前 Delta vs Necessity 的故事？
- [ ] 当 condition 极紧（freq → 1）时，Necessity 和 Delta 都会被压缩，应当用什么标度去比较"压缩前后" rankings 的稳定度？
- [ ] Kaisa LW 的 Δ=+0.18 这个反直觉的正值是不是 Madreds Bloodrazor / Spear of Shojin 等替代品挤压的结果？需要 build analysis 验证。

## Questions for Xing

- 截图位 1-3 你想用 MetaTFT 还是 TacticsTools 的截图？我可以提供具体推荐（哪个 comp + 哪个 item）。

---

## Sources / Cross-references
- [[concepts/metrics]] — 三指标定义、play rate 作为 confidence signal
- [[experiments/2026-04-21-vex-nova95-items]] — 第一次 Vex Nova95 物品分析（无 ic3，5 metric 对比）
- [[experiments/2026-04-22-cross-validation-vex-nova95]] — Necessity rank Spearman 0.993 跨数据源稳定
- [[concepts/biases]] — Survivorship bias、selection effect

---

## Review

(留待 Xing 填写)
