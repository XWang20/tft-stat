# Experiment: Cross-Validation — Vex Items in Nova 95
**Status**: ✅ accepted
**Date**: 2026-04-22
**Module**: 9 (Cross-Validation)

## The Question

Do our item Necessity rankings match tftable's for Vex in Nova 95? This tests whether our pipeline (MetaTFT API + Necessity formula) produces conclusions consistent with the expert ground truth.

## Chapter 1: Our Results

`python3 cli.py items TFT17_Vex --comp nova_95` (211k games, overall AVP 4.16):

```
Item                     Rate   Necessity
Guinsoo's Rageblade       88%   +0.502
Giant Slayer              38%   +0.084
Hextech Gunblade          29%   +0.076
Striker's Flail           16%   +0.063
Rabadon's Deathcap        10%   +0.038
Red Buff                   7%   +0.033
Archangel's Staff         10%   +0.018
Morellonomicon             4%   +0.007
Nashor's Tooth             4%   +0.006
```

## Chapter 2: tftable Ground Truth

`python3 cli.py tftable TFT17_Vex --comp nova_95` (136k games, AVP 4.26):

```
Item                     Rate   Necessity   Rating
Guinsoo's Rageblade      91%    0.7641      Core
Giant Slayer             40%    0.0924      Important
Striker's Flail          19%    0.0801      Optional
Hextech Gunblade         32%    0.0778      Optional
Rabadon's Deathcap       10%    0.0491      Optional
Red Buff                  9%    0.0457      Optional
Archangel's Staff        10%    0.0169      Optional
Morellonomicon            5%    0.0072      Optional
Nashor's Tooth            4%    0.0056      Optional
```

## Chapter 3: Comparison

| Rank | tftable | Ours | Match? |
|---|---|---|---|
| 1 | Guinsoo's | Guinsoo's | ✅ |
| 2 | Giant Slayer | Giant Slayer | ✅ |
| 3 | Striker's Flail | Hextech Gunblade | 🔄 3↔4 |
| 4 | Hextech Gunblade | Striker's Flail | 🔄 3↔4 |
| 5 | Rabadon's | Rabadon's | ✅ |
| 6 | Red Buff | Red Buff | ✅ |
| 7 | Archangel's | Archangel's | ✅ |
| 8 | Morellonomicon | Morellonomicon | ✅ |
| 9 | Nashor's Tooth | Nashor's Tooth | ✅ |

15 个装备中 13 个排名完全一致。仅 #3/#4（Flail/Gunblade，Necessity 值相近）和 #10/#11（Quicksilver/JG）各差一位。

Spearman rank correlation: **0.993**

### Necessity 数值差异

tftable 的 Necessity 值普遍更大（Guinsoo 0.764 vs 0.502）。可能原因：
- 样本差异：tftable 136k games vs MetaTFT 211k games
- 时间窗口：tftable 可能用更长的数据窗口
- 计算方式：公式相同但 overall AVP baseline 不同（tftable 4.26 vs 我们 4.16）
- tftable 使用了额外的 debiasing 方法（Xing 会后续教）

修复 filter bug 后差距缩小了（Guinsoo 从 0.451→0.502，更接近 tftable 的 0.764）。排名一致但数值不同说明 Necessity 的**排序特性**很鲁棒。

## What I Learned

1. **我们的 pipeline 方法论是可靠的** — Top 9 装备排名和 tftable 高度一致，说明 MetaTFT API + compositions.py filter + Necessity 公式这套方法可以产出正确的结论
2. **Necessity 的排序比数值更重要** — 两边数值差距大但排名几乎相同，这是好的特性：说明 Necessity 作为排序指标对 baseline 不敏感
3. **#3/#4 的交换是正常的** — Flail 和 Gunblade 的 Necessity 非常接近（差距 <0.01），这种微小差异在不同样本下翻转是预期行为

## Open Questions

- tftable 的 Necessity 值为什么系统性偏大？是 baseline 差异还是公式差异？
- 在其他阵容上排名一致性是否同样高？需要多阵容测试
- Unit necessity 的对比差异很大（Spearman -0.476），tftable 的 IC3 necessity 和我们的 unit necessity 是不同的指标体系，需要理解 IC3 necessity 的计算方式

## Questions for Xing

1. tftable 的 item Necessity 公式和我们用的一样吗（`w/o_AVP - overall_AVP`）？数值差异来自哪里？
2. IC3 necessity（unit 级别的 necessity，最大值 8.0）是怎么计算的？和 item necessity 的公式不同？
3. 下一步应该多阵容测试一致性，还是先深入理解数值差异？

## Review

### Feedback (Xing) — Round 1
1. **交叉验证的目的是验证"我们的结论"，不是对比两个数据源** — crossval 应该比的是我们的分析结论（经过 filter 设计、metric 选择、分析判断）和 tftable 的结论，而不是 MetaTFT raw data vs tftable raw data
2. **tftable 除了 Necessity 还用了别的 debiasing 方法** — 这解释了数值差异，后续 Xing 会逐步教
3. **未来交叉验证不只是 items** — 还会有阵容条件、meta 判断、unit 评估等

### Giscus Review — 2026-04-22
**Status**: ✅ accepted
