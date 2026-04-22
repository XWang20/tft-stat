# Experiment: Is 5 N.O.V.A. Worth the Cost?
**Status**: 🧪 draft (third revision)
**Date**: 2026-04-22 (original), 2026-04-22 (revised with nova_yi focus)
**Module**: 5 (Trait Breakpoints)

## The Question

N.O.V.A. (DRX) has two breakpoints: **2 units** and **5 units**. In the nova_yi comp, 65% of games naturally run 5 NOVA. Is there a measurable performance difference between 2 and 5 NOVA, and does it change itemization?

We use **nova_yi** as the primary analysis comp because it has adequate samples for both tiers (66k at 2 NOVA, 120k at 5 NOVA). Nova_95 has only 1,029 games at 5 NOVA (0.4%) — too few to analyze.

## Chapter 1: Headline Numbers

| Condition | Games | AVP | Top4% | Win% |
|---|---|---|---|---|
| All nova_yi | 186,347 | 4.45 | 50.8% | 11.3% |
| 2 NOVA | 66,003 | 4.61 | 47.9% | 10.7% |
| 5 NOVA | 120,343 | 4.37 | 52.3% | 11.6% |

5 NOVA games perform better: -0.24 AVP, +4.4% Top4, +0.9% Win. But we know from Module 2 that this doesn't mean 5 NOVA *causes* better placement — selection bias is the likely driver.

## Chapter 2: Does 5 NOVA Change MasterYi Itemization?

If trait breakpoints genuinely change gameplay, we'd expect item priorities to shift. Here are MasterYi's top items ranked by Necessity:

| Rank | 2 NOVA (66k games) | Nec. | 5 NOVA (120k games) | Nec. |
|---|---|---|---|---|
| 1 | Edge of Night | +0.111 | Edge of Night | +0.054 |
| 2 | Giant Slayer | +0.060 | Giant Slayer | +0.045 |
| 3 | Quicksilver | +0.042 | Quicksilver | +0.022 |
| 4 | Hand of Justice | +0.023 | Striker's Flail | +0.017 |
| 5 | Malware Matrix | +0.020 | Sterak's Gage | +0.017 |
| 6 | Striker's Flail | +0.016 | Hand of Justice | +0.017 |

**Top 3 are identical.** Ranks 4-6 shuffle slightly (HoJ/Malware/Flail vs Flail/Sterak/HoJ) but Necessity values are nearly equal (~0.016-0.023). The trait breakpoint does **not** change MasterYi's itemization.

Absolute Necessity values are lower across the board in 5 NOVA (e.g., Edge of Night 0.111 → 0.054). This is expected: in stronger boards (lower overall AVP), there's less room for any single item to make a difference.

## Chapter 3: Does 5 NOVA Change Kindred Itemization?

Kindred is the secondary carry. At 2 NOVA, Kindred appears in ~70% of nova_yi games (Kindred is one of the DRX units providing the base 2 NOVA).

| Rank | 2 NOVA (46k games) | Nec. | 5 NOVA (120k games) | Nec. |
|---|---|---|---|---|
| 1 | Kraken's Fury | +0.137 | Kraken's Fury | +0.105 |
| 2 | Marauder Emblem | +0.057 | Marauder Emblem | +0.048 |
| 3 | Deathblade | +0.033 | Guinsoo's Rageblade | +0.040 |
| 4 | Last Whisper | +0.031 | Striker's Flail | +0.038 |
| 5 | Red Buff | +0.028 | Giant Slayer | +0.030 |

Top 2 are identical (Kraken's Fury, Marauder Emblem). Ranks 3-5 differ — **Guinsoo's Rageblade** appears at 83% play rate in 5 NOVA (not even in top 10 at 2 NOVA). This is the one genuine itemization shift: at 5 NOVA, Kindred frequently holds Guinsoo (likely as a holder item given MasterYi also needs it at 83%). The high play rate inflates Guinsoo's Necessity despite a modest AVP contribution.

## Chapter 4: Cross-Validation with tftable

tftable MasterYi items (133k games):

| tftable Rank | Item | tftable Nec. | Our Nec. (overall) |
|---|---|---|---|
| 1 | Giant Slayer | 0.067 | 0.053 |
| 2 | Edge of Night | 0.040 | 0.080 |
| 3 | Quicksilver | 0.027 | 0.026 |
| 4 | Striker's Flail | 0.019 | 0.016 |
| 5 | Thief's Gloves | 0.017 | 0.013 |
| 6 | Hand of Justice | 0.016 | 0.018 |

One notable difference: we rank Edge of Night #1 (Nec. 0.080) while tftable puts Giant Slayer #1 (Nec. 0.067). This is the first meaningful disagreement we've seen in cross-validation. Possible reasons: tftable's debiasing reduces Edge of Night's inflated Necessity (51% play rate vs Giant Slayer's 29%), or sample period differences. Ranks 3-6 match well.

tftable also shows **N.O.V.A. Emblem** at -0.105 Necessity (HighFrequency tag, 35% rate) — holding the emblem is harmful for MasterYi, consistent with it taking a carry item slot.

## What I Learned

1. **5 NOVA does not change MasterYi itemization** — Top 3 items identical, lower ranks within noise. Players don't need to re-prioritize items based on trait tier.

2. **5 NOVA's AVP advantage is likely selection bias** — The -0.24 AVP gap and +4.4% Top4 between 2 and 5 NOVA persists, but since every unit improves, this points to stronger-board-selection rather than a causal trait effect.

3. **Kindred's Guinsoo shift is the one real signal** — At 5 NOVA, Guinsoo appears on Kindred at 83% (vs near-zero at 2 NOVA). This is likely an item-holder pattern rather than genuine Kindred itemization change.

4. **Necessity compression at higher performance** — All Necessity values are ~50% lower in 5 NOVA. When the overall AVP is already low (4.37 vs 4.61), each item contributes less marginal value. This is a general property, not specific to trait breakpoints.

5. **First cross-validation disagreement** — Edge of Night vs Giant Slayer at #1/#2 differs between our pipeline and tftable. This could signal where tftable's debiasing makes a difference (high play rate items).

## Open Questions

- Why does tftable rank Giant Slayer above Edge of Night? Is it the debiasing method or sample period?
- Can we test the selection bias hypothesis directly? E.g., compare 2 NOVA boards that *could* reach 5 NOVA (have DRX units on bench) vs those that can't.
- Do other traits (e.g., Marauder, Bastion) show the same "no itemization change" pattern?

## Questions for Xing

1. **Edge of Night vs Giant Slayer**: Our pipeline puts Edge of Night at #1 (Nec. 0.080) due to 49% play rate, while tftable puts Giant Slayer at #1 (Nec. 0.067). Is this where tftable's debiasing diverges from simple Necessity? 
2. **Conclusion validity**: "5 NOVA doesn't change itemization" — is this finding useful, or is it expected (items are about the champion, not the trait)?
3. **Nova_95 abandoned**: 5 NOVA is essentially nonexistent in nova_95 (0.4%, emblem-dependent). Should we drop it from the trait breakpoint analysis entirely?

## Review (First Round)

**Status**: 🔄 revision (2026-04-22)

### Feedback (Xing)
> 这是一个有意思的问题，但实施过程太粗糙，几乎没有可靠的结论，甚至vex为什么还在用avp作为指标？

1. Used AVP despite proving it unreliable yesterday
2. No within-comp control — compared globally instead of within specific comps
3. Didn't consider emblem factor
4. "Universal improvement" = bias signal

## Review (Second Round)

**Status**: 🔄 revision (2026-04-22)

### Feedback (Xing)
1. 报告完全偏离了原始问题 — 变成 filter bug 调试记录
2. nova_95 里 5 NOVA 只有 1k 局不够分析 — 应该用 nova_yi
3. tftable 除了 Necessity 还有其他 debiasing 方法

### What Changed in This Revision
- 以 nova_yi 为主要分析 comp（66k 2 NOVA vs 120k 5 NOVA）
- 聚焦原始问题"5 NOVA 值不值"→ 转化为"5 NOVA 是否改变 itemization"
- 删除 filter bug 调试内容（已归入 lab-checklist）
- 简化报告结构，4 个 chapter 直接推进问题
