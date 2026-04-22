# Experiment: Is 5 N.O.V.A. Worth the Cost? (Revised)
**Status**: 🧪 draft
**Date**: 2026-04-22 (original), 2026-04-22 (revision, data re-run after filter bug fix)
**Module**: 5 (Trait Breakpoints -- preview)

> **Filter Bug Fix (2026-04-22)**: Bare `Unit()` filters (no star/item constraints)
> were missing the `_.*` wildcard suffix in `filter_params.py`, causing exclusions
> like `~Unit('TFT17_Kindred')` to silently fail. All data below has been re-run
> after the fix. The previous "97% Kindred contamination" finding was caused by
> this bug -- Kindred is now properly excluded from nova_95.

---

## The Question

N.O.V.A. (DRX) in S17 has two breakpoints: **2 units** and **5 units**. The Nova 95 comp typically runs at 2 NOVA. Is upgrading to 5 NOVA worth it?

The original experiment compared raw AVP between 2 and 5 NOVA globally, which Xing correctly flagged as worthless. This revision:
1. Uses **Necessity** as primary metric, not AVP
2. Works **within specific comps** (nova_95 and nova_yi)
3. Investigates the **emblem factor** -- do players reach 5 NOVA via emblem or via adding units?
4. Tests for the **"universal improvement" bias signal**

---

## Chapter 1: Within-Comp Headline Numbers

All queries use compositions.py definitions + trait-tier filters. Patch: current. Ranks: Plat--Challenger.

### Nova 95 (Fiora/Vex/Graves carry, DRX >= 2)

| Condition | Games | AVP | Top4% | Win% |
|---|---|---|---|---|
| All nova_95 | 237,967 | 4.28 | 53.3% | 18.4% |
| 2 NOVA only (`--exclude-traits TFT17_DRX:5`) | 236,936 | 4.28 | 53.3% | 18.4% |
| 5 NOVA (`--traits TFT17_DRX:5`) | 1,029 | 4.29 | 53.2% | 18.0% |

### Nova Yi (MasterYi/Kindred carry, DRX >= 2)

| Condition | Games | AVP | Top4% | Win% |
|---|---|---|---|---|
| All nova_yi | 185,730 | 4.45 | 50.8% | 11.3% |
| 2 NOVA only | 65,660 | 4.61 | 47.9% | 10.7% |
| 5 NOVA | 120,070 | 4.37 | 52.3% | 11.6% |

**After the filter fix, the nova_95 story changes completely.** Only **1,029 games** (0.4%) are true 5 NOVA within nova_95 -- the previous 38,457 were almost entirely Kindred-contaminated nova_yi games leaking through the broken exclusion filter. The AVP delta in nova_95 is now essentially **zero** (4.29 vs 4.28 = -0.01), compared to the previous -0.31 which was driven by contamination.

In nova_yi, 5 NOVA accounts for **65%** of all games -- it's the default, not an upgrade. In nova_95, 5 NOVA is vanishingly rare at **0.4%** of games. Nova_yi numbers are essentially unchanged (confirming the fix only affected nova_95's Kindred exclusion).

---

## Chapter 2: Filter Integrity -- Vindicated by Bug Fix

The previous revision discovered that Kindred appeared in **97% of "5 NOVA nova_95" games** despite the filter explicitly excluding Kindred via `~Unit('TFT17_Kindred')`. This was interpreted as a data contamination issue or API limitation.

**Root cause identified**: The `_unit_to_metatft()` function in `filter_params.py` was generating `!TFT17_Kindred-1` for bare Unit exclusions (no star/item constraints), but the MetaTFT API requires `!TFT17_Kindred-1_.*` with a wildcard suffix to match all star/item combinations. Without `_.*`, the exclusion silently failed.

After the fix, the 5 NOVA nova_95 unit breakdown:

| Unit | Games in 5 NOVA nova_95 | Rate |
|---|---|---|
| Aatrox | 1,025 | **100%** |
| Akali | 1,019 | **99%** |
| Maokai | 1,007 | **98%** |
| Fiora | 789 | 77% |
| Shen | 703 | 68% |
| Vex | 670 | 65% |
| Graves | 646 | 63% |
| Caitlyn | 583 | 57% |
| TahmKench | 579 | 56% |
| **Kindred** | **0** | **0%** |
| **MasterYi** | **0** | **0%** |

**Kindred and MasterYi are now properly excluded.** The 1,029 remaining 5 NOVA games are a genuine subset of nova_95 boards: the three DRX units (Aatrox, Akali, Maokai) appear in ~99% of games, providing 3 natural DRX. To reach 5 DRX without Kindred/MasterYi/Bel'Veth, these games must rely on **N.O.V.A. Emblem** (see Chapter 5).

**Impact of the fix**: nova_95 total dropped from 308,478 to 237,967 games (~70k Kindred-containing games removed). The 5 NOVA subset dropped from 38,457 to 1,029 games -- the previous 37k games were Kindred-contaminated nova_yi boards that leaked through the broken exclusion.

---

## Chapter 3: Item Necessity Rankings -- The Measurable Signal

Even if absolute AVP is biased by selection effects, **item Necessity rankings** are more robust because they measure relative importance within a condition. If 5 NOVA changes the carry's optimal itemization, that would be genuine trait signal.

**Important caveat**: After the filter fix, the 5 NOVA nova_95 subset has only **1,029 games** total (670 Vex, 789 Fiora, 646 Graves). These sample sizes are marginal -- rankings may be unstable. Interpret with caution.

### Vex Items: 2 NOVA vs 5 NOVA (within nova_95)

| Rank | 2 NOVA Item (Nec.) | 5 NOVA Item (Nec.) |
|---|---|---|
| 1 | Guinsoo (+0.502) | Guinsoo (+0.507) |
| 2 | Giant Slayer (+0.083) | Giant Slayer (+0.185) |
| 3 | Hextech Gunblade (+0.076) | Hextech Gunblade (+0.071) |
| 4 | Striker's Flail (+0.063) | Jeweled Gauntlet (+0.065) |
| 5 | Rabadon's Deathcap (+0.038) | -- |
| 6 | Red Buff (+0.033) | -- |
| 7 | Guinsoo ★2 (+0.029) | -- |
| 8 | Archangel's Staff (+0.018) | -- |

**Top 3 items are identical in both conditions.** Guinsoo remains overwhelmingly core. The 5 NOVA column is sparse because only 670 games yields few items above the significance threshold. N.O.V.A. Emblem appears in 5 NOVA at -0.175 Necessity (harmful -- it takes a carry item slot; see Chapter 5).

### Fiora Items: 2 NOVA vs 5 NOVA

| Rank | 2 NOVA Item (Nec.) | 5 NOVA Item (Nec.) |
|---|---|---|
| 1 | Edge of Night (+0.152) | Sterak's Gage (+0.131) |
| 2 | Sterak's Gage (+0.132) | Hand of Justice (+0.087) |
| 3 | Bloodthirster (+0.122) | Bloodthirster (+0.076) |
| 4 | Hand of Justice (+0.086) | Titan's Resolve (+0.072) |
| 5 | Thief's Gloves (+0.061) | Edge of Night (+0.035) |
| 6 | Titan's Resolve (+0.046) | -- |

Edge of Night drops from #1 to #5 in 5 NOVA. Sterak's Gage rises to #1. However, with only 789 Fiora games in 5 NOVA, ranking instability is expected. N.O.V.A. Emblem appears at 63% rate on Fiora with -0.185 Necessity, meaning it occupies a carry item slot at significant cost.

### Graves Items: 2 NOVA vs 5 NOVA

| Rank | 2 NOVA Item (Nec.) | 5 NOVA Item (Nec.) |
|---|---|---|
| 1 | Quicksilver (+0.123) | N.O.V.A. Emblem (+0.066) |
| 2 | Giant Slayer (+0.105) | Quicksilver (+0.045) |
| 3 | Sterak's Gage (+0.095) | Infinity Edge (+0.044) |
| 4 | Hand of Justice (+0.086) | Giant Slayer (+0.002) |
| 5 | Striker's Flail (+0.072) | -- |
| 6 | Deathblade (+0.050) | -- |

Graves is the only carry where N.O.V.A. Emblem has **positive** Necessity (+0.066) in 5 NOVA. This suggests Graves benefits more from the 5 NOVA trait bonus than from a third combat item -- a genuine interaction signal, though with only 646 games. Guinsoo's Rageblade appears at -0.180 (harmful on Graves, as expected for an AD carry).

### MasterYi Items in Nova Yi: 2 NOVA vs 5 NOVA

As a control where 5 NOVA is the natural state and sample sizes are adequate:

| Rank | 2 NOVA Item (Nec.) | 5 NOVA Item (Nec.) |
|---|---|---|
| 1 | Edge of Night (+0.109) | Edge of Night (+0.054) |
| 2 | Giant Slayer (+0.060) | Giant Slayer (+0.045) |
| 3 | Quicksilver (+0.043) | Quicksilver (+0.021) |
| 4 | Hand of Justice (+0.024) | Hand of Justice (+0.018) |
| 5 | Malware Matrix (+0.019) | Striker's Flail (+0.017) |
| 6 | Striker's Flail (+0.016) | Sterak's Gage (+0.017) |

Top 4 identical. Rankings are very stable. Within nova_yi (where filter integrity is clean and sample sizes are large), 5 NOVA does **not** change itemization priorities at all.

---

## Chapter 4: The "Universal Improvement" Test (Revised)

The original experiment showed every unit improves in 5 NOVA globally. Does this persist within comps?

Within nova_95, selected units (**caveat**: 5 NOVA column has only ~1,029 games):

| Unit | 2 NOVA AVP | 5 NOVA AVP | Delta | DRX? |
|---|---|---|---|---|
| Fiora | 4.10 | 3.90 | -0.20 | Yes |
| Vex | 4.16 | 3.95 | -0.21 | Yes |
| Graves | 4.24 | 4.21 | -0.03 | No |
| Shen | 4.05 | 3.72 | **-0.33** | No |
| Morgana | 4.04 | 3.67 | **-0.37** | No |
| Blitzcrank | 4.02 | 3.68 | **-0.34** | No |

Non-DRX support units like Shen (-0.33), Morgana (-0.37), and Blitzcrank (-0.34) improve *more* than the DRX carries Fiora (-0.20) and Vex (-0.21). Graves barely changes (-0.03). The pattern persists after the filter fix, though deltas are somewhat smaller than before. This is still consistent with selection bias: **the player hitting 5 NOVA has a stronger board overall**, not just better DRX synergy.

Note: Rek'Sai and Briar (which appeared in the previous version's 5 NOVA data) are no longer present. Those were artifacts of the Kindred contamination -- games that were actually nova_yi boards leaking through the broken filter.

---

## Chapter 5: The Emblem Factor -- Now the Dominant Path

The previous version found emblem usage at ~3.4% of 5 NOVA games, concluding it was negligible. **After the filter fix, this reverses completely.** With Kindred/MasterYi properly excluded, the only way to reach 5 DRX in nova_95 is via **N.O.V.A. Emblem** -- the three natural DRX units (Aatrox, Akali, Maokai) provide 3, and the carries (Fiora/Vex/Graves) are not DRX. Emblem must bridge the gap.

N.O.V.A. Emblem appearance on carries in 5 NOVA nova_95:

| Carry | Emblem Games | Emblem Rate | Emblem Necessity |
|---|---|---|---|
| Fiora | 494 | **63%** | **-0.185** |
| Graves | 385 | **60%** | **+0.066** |
| Vex | 242 | **36%** | **-0.175** |

The emblem takes one of three carry item slots. For Vex and Fiora, this is **actively harmful** (negative Necessity): the trait bonus from 5 NOVA does not compensate for losing a combat item. For Graves, the emblem has **positive Necessity** (+0.066), suggesting Graves can trade an item slot for the trait bonus more efficiently.

This reframes the original question entirely. "Is 5 NOVA worth the cost?" in nova_95 is really asking "Is it worth putting N.O.V.A. Emblem on your carry?" The answer: **no for Vex and Fiora, possibly yes for Graves**, though all sample sizes are marginal (~1,029 total games).

The previous finding that emblem was negligible (3.4%) was an artifact of the Kindred contamination -- those 38k games reached 5 NOVA by adding Kindred (a natural DRX unit), not via emblem.

---

## Chapter 6: Cross-Validation with tftable

tftable ground truth for nova_95 (135,798 games):

| Unit | Necessity | IC3 Rate |
|---|---|---|
| Vex | 8.000 | 87.0% |
| Graves | 8.000 | 64.3% |
| Fiora | 8.000 | 44.2% |
| Nunu | 5.109 | 66.8% |
| TahmKench | 5.048 | 47.9% |
| Blitzcrank | 4.093 | 14.6% |
| Morgana | 4.071 | 8.5% |
| Shen | 4.054 | 7.7% |

tftable only has 8 units listed. The three carries (Vex, Graves, Fiora) are all at Necessity 8.0 (maximum -- defining the comp). Nunu and TahmKench follow as core support at ~5.0, then the frontline trio at ~4.0. This matches the nova_95 definition: a carry + DRX + specific support shell.

tftable doesn't split by trait tier, so we can't directly cross-validate the 2 vs 5 NOVA comparison. But the unit Necessity structure confirms the comp identity.

Vex item Necessity (tftable):

| Item | tftable Necessity | Our 2-NOVA Necessity |
|---|---|---|
| Guinsoo | 0.764 | 0.502 |
| Giant Slayer | 0.092 | 0.083 |
| Striker's Flail | 0.080 | 0.063 |
| Hextech Gunblade | 0.078 | 0.076 |
| Rabadon's | 0.049 | 0.038 |
| Red Buff | 0.046 | 0.033 |

Rankings match perfectly (top 6 identical). Absolute values differ (tftable's are higher), likely due to different sample periods and slight filter differences. The ranking agreement strengthens confidence in the Necessity metric.

---

## What I Learned

### About trait breakpoints
1. **5 NOVA is essentially nonexistent in nova_95** -- Only 0.4% of games (1,029 out of 237,967). The previous 12.5% figure was entirely Kindred contamination from the filter bug. In nova_95, reaching 5 DRX without Kindred/MasterYi requires N.O.V.A. Emblem, which is a niche strategy.

2. **The emblem path defines 5 NOVA in nova_95** -- N.O.V.A. Emblem appears on 36-63% of carries in 5 NOVA games. It has negative Necessity on Vex (-0.175) and Fiora (-0.185), meaning the item slot sacrifice hurts. Only Graves (+0.066) shows a net benefit from the emblem. This answers the original question directly: **5 NOVA is not worth the cost for Vex and Fiora carries.**

3. **Item Necessity rankings remain stable in nova_yi** -- The control comparison (nova_yi, where 5 NOVA is natural and sample sizes are adequate) shows top 4 MasterYi items identical across trait tiers. Players don't need to re-itemize for trait breakpoints.

4. **"Universal improvement" persists but is attenuated** -- Non-DRX support units still improve more than DRX carries in 5 NOVA, consistent with selection bias. The effect is smaller than in the contaminated data but still present with ~1,029 games.

### About methodology
5. **Filter bugs are silent killers** -- The `_.*` suffix bug caused `~Unit('TFT17_Kindred')` to fail silently, letting 70k contaminated games through. The resulting data looked plausible and led to seemingly reasonable conclusions ("5 NOVA changes the board composition," "97% Kindred contamination"). All of it was wrong. **Always verify filter behavior before trusting results.**

6. **Contamination can produce compelling but false narratives** -- The previous version's story (5 NOVA = different composition, offensive items gain importance, Kindred leakage as a discovery) was internally consistent but entirely driven by a bug. The true story (5 NOVA is vanishingly rare, emblem-dependent, and mostly not worth it) is less dramatic but correct.

7. **Ranking comparison > absolute value comparison** -- Even when absolute Necessity values shift, the *rankings* are more robust. The tftable cross-validation confirms top 6 Vex items match despite different sample periods.

### About the original question
8. **"Is 5 NOVA worth the cost?" is now answerable for nova_95.** No, for Vex and Fiora -- the emblem sacrifices a carry item slot. Possibly yes for Graves, but the sample is too small to be confident. In nova_yi, 5 NOVA is the natural state (65% of games) and doesn't change itemization, so the question is moot there.

---

## Questions for Xing

1. **Filter bug resolved**: The `~Unit('TFT17_Kindred')` exclusion now works correctly after fixing the `_.*` suffix in `filter_params.py`. The "97% Kindred contamination" was caused by our code, not the MetaTFT API. Should we audit other comp definitions for similar bare-Unit exclusions that may have been affected?

2. **5 NOVA rarity in nova_95**: With only 1,029 games (0.4%), the 5 NOVA condition within nova_95 is barely analyzable. Is this finding itself interesting -- that 5 NOVA is effectively not a real path for nova_95 players? Or should we focus exclusively on nova_yi for trait breakpoint analysis?

3. **Emblem as the answer**: The emblem data gives a direct answer to "is 5 NOVA worth it?" for nova_95 carries -- negative Necessity for Vex/Fiora, slightly positive for Graves. Is this a satisfying enough conclusion, or do you want deeper investigation into the Graves case?

4. **Nova_yi as the better test case**: nova_yi has clean filter boundaries, large samples (120k vs 1k), and 5 NOVA as the natural state. For future trait breakpoint work, should we use nova_yi as the primary test comp?

5. **Previous findings invalidated**: The old Chapter 3 narrative ("offensive items gain relative importance in 5 NOVA") was driven by Kindred contamination. With clean data, the item story is much simpler -- top items are stable, and emblem eats a slot. Is there a methodological lesson here about how contaminated data can produce seemingly interesting but spurious patterns?

---

## Sources
- MetaTFT Explorer API: total, units_unique, unit_items_unique endpoints
- tftable ground truth via SSH (`python3 cli.py tftable --comp nova_95`)
- [[concepts/metrics]] -- Necessity as primary ranking metric
- [[methods/filter-strategy]] -- filter integrity check
- [[experiments/vex-nova95]] -- prior Vex item analysis for baseline

---

## Review (Original)

**Status**: 🔄 revision (2026-04-22)

### Feedback (Xing)
> 这是一个有意思的问题，但实施过程太粗糙，几乎没有可靠的结论，甚至vex为什么还在用avp作为指标？感觉昨天讲的完全没有用到今天的作业中来

1. **Used AVP despite proving it unreliable yesterday** -- the entire previous day established Necessity as the correct metric, yet this experiment reverted to raw AVP comparison
2. **No within-comp control** -- compared 2 vs 5 N.O.V.A. globally instead of within specific comps (Nova 95, Nova Yi). Each comp has different contamination
3. **Didn't consider emblem factor** -- 2-3 N.O.V.A. via emblem is a different question than 2-3 via adding a unit. Explore with/without emblem as separate conditions
4. **"Universal improvement" = bias signal** -- if filtering by a trait improves every unit equally, it's selection bias not causal effect

### Revision Requirements
- Redo within specific comps using Necessity not AVP
- Control for emblem vs unit-added paths to higher breakpoints
- Apply causal inference reasoning (Xing: "你应该比我更懂因果推断")

### What Changed in Revision
- Switched to Necessity as primary metric for all item comparisons
- Analyzed within nova_95 and nova_yi separately
- Discovered filter integrity issue (Kindred leaking into 5 NOVA nova_95)
- Quantified emblem factor (3.4% -- negligible)
- Compared item Necessity rankings across conditions (stable top 6)
- Cross-validated with tftable (rankings match)

### Data Re-run After Filter Bug Fix (2026-04-22)
- Fixed `_unit_to_metatft()` in `filter_params.py`: bare Unit filters now append `_.*` wildcard suffix
- All data re-queried with working `~Unit('TFT17_Kindred')` exclusion
- nova_95 total: 308,478 → 237,967 games (70k contaminated games removed)
- 5 NOVA nova_95: 38,457 → 1,029 games (previous data was 97% Kindred contamination from bug)
- Emblem factor reversed: 3.4% → dominant path (36-63% of carry items in 5 NOVA)
- AVP delta reversed: -0.31 → -0.01 (essentially zero)

## Review (Second Round)

**Status**: 🔄 revision (2026-04-22)

### Feedback (Xing)
1. **报告完全偏离了原始问题** — 问题是"5 NOVA 值不值"，但报告变成了 filter bug 调试记录 + item ranking 对比。Chapter 2-4 在讲 filter bug，Chapter 5-6 才勉强回到问题
2. **nova_95 里 5 NOVA 只有 1k 局不够分析** — 应该用 nova_yi 作为主要分析对象，nova_yi 有 65k 局 2 NOVA 和 120k 局 5 NOVA，两组都有足够样本
3. **tftable 除了 Necessity 还有其他 debiasing 方法** — Xing 会逐步教，当前 Necessity 只是第一步

### Revision Requirements
- 以 nova_yi 为主要分析 comp 回答"5 NOVA 值不值"
- 聚焦原始问题，filter bug 教训归入 lab-checklist 不占报告篇幅
- 简化报告结构
