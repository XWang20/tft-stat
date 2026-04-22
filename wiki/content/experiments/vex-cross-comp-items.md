# Experiment: Vex Items Across Different Comps (Revised)
**Status**: 🧪 draft
**Date**: 2026-04-22 (revised from 2026-04-21)
**Module**: 1 (Filter Design)

## The Question

Does Vex's BIS change depending on what comp she's in? If the same champion has different optimal items in different compositions, then **filter = foundation** -- you can't analyze items without specifying the comp first.

This is a revision of the original experiment. The original used ad-hoc filters (agent-constructed on the fly). This time we use **standardized compositions.py definitions** -- expert-curated filters ported from XWang20/tft_data.

We compare Vex's item metrics in three comp contexts plus unfiltered:
1. **NOVA 95** (`nova_95`) -- the dominant Vex comp (231k Vex games)
2. **Dark Star** (`dark_star`) -- trait-focused comp where Vex sometimes appears (5.6k Vex games)
3. **Shepherd** (`shepherd`) -- Summon-focused comp where Vex sometimes appears (3.9k Vex games)
4. **Unfiltered** -- all Vex games (616k games)

**Note**: `vex_95` returned 0 games -- this comp definition (Vex 3-item + Blitzcrank + Mordekaiser, excluding DRX/LeBlanc/Jhin) is too narrow for current data availability. It may have been defined for a different patch window.

---

## Chapter 1: The Data (Standardized Filters)

### NOVA 95 (231,363 Vex games, AVP 4.12)

Comp total: 308,499 games (AVP 4.21). Vex appears in 75% of nova_95 games.

| Item | Games | Rate | AVP | Edge | Necessity |
|------|-------|------|-----|------|-----------|
| Guinsoo's Rageblade | 202,505 | 88% | 4.06 | +0.06 | **+0.452** |
| Giant Slayer | 84,906 | 37% | 3.99 | +0.13 | +0.075 |
| Hextech Gunblade | 65,854 | 28% | 3.95 | +0.17 | +0.068 |
| Striker's Flail | 36,202 | 16% | 3.78 | +0.34 | +0.063 |
| Rabadon's Deathcap | 22,247 | 10% | 3.76 | +0.36 | +0.038 |
| Red Buff | 16,899 | 7% | 3.68 | +0.44 | +0.035 |
| Archangel's Staff | 22,320 | 10% | 3.95 | +0.17 | +0.018 |
| Jeweled Gauntlet | 51,457 | 22% | 4.11 | +0.01 | +0.003 |

### Dark Star (5,633 Vex games, AVP 4.21)

Comp total: 110,814 games (AVP 4.39). Vex appears in only 5% of dark_star games -- she is not the primary carry.

| Item | Games | Rate | AVP | Edge | Necessity |
|------|-------|------|-----|------|-----------|
| Guinsoo's Rageblade | 3,762 | 67% | 4.08 | +0.13 | **+0.260** |
| Dark Star Emblem | 2,201 | 39% | 3.98 | +0.23 | +0.149 |
| Void Staff | 751 | 13% | 3.94 | +0.27 | +0.041 |
| Giant Slayer | 1,061 | 19% | 4.10 | +0.12 | +0.027 |
| Rabadon's Deathcap | 408 | 7% | 3.89 | +0.32 | +0.025 |
| Hextech Gunblade | 634 | 11% | 4.03 | +0.18 | +0.023 |
| Archangel's Staff | 404 | 7% | 3.92 | +0.29 | +0.022 |
| Jeweled Gauntlet | 1,400 | 25% | 4.20 | +0.01 | +0.004 |

### Shepherd (3,892 Vex games, AVP 3.38)

Comp total: 49,295 games (AVP 4.02). Vex appears in only 8% of shepherd games.

| Item | Games | Rate | AVP | Edge | Necessity |
|------|-------|------|-----|------|-----------|
| Guinsoo's Rageblade | 2,858 | 73% | 3.27 | +0.11 | **+0.298** |
| Giant Slayer | 1,200 | 31% | 3.12 | +0.25 | +0.113 |
| Void Staff | 662 | 17% | 3.16 | +0.22 | +0.044 |
| Jeweled Gauntlet | 1,280 | 33% | 3.32 | +0.06 | +0.027 |
| Striker's Flail | 268 | 7% | 3.09 | +0.29 | +0.021 |
| Hextech Gunblade | 746 | 19% | 3.29 | +0.09 | +0.020 |
| Rabadon's Deathcap | 296 | 8% | 3.14 | +0.23 | +0.019 |
| Red Buff | 182 | 5% | 3.06 | +0.32 | +0.015 |

Notable negative-Necessity items in Shepherd:
- Shepherd Emblem: Nec -0.034 (the comp's own emblem hurts Vex!)
- Spear of Shojin: Nec -0.025

### Unfiltered (616,448 games, AVP 4.33)

| Item | Games | Rate | AVP | Edge | Necessity |
|------|-------|------|-----|------|-----------|
| Guinsoo's Rageblade | 497,853 | 81% | 4.25 | +0.08 | **+0.315** |
| Giant Slayer | 220,625 | 36% | 4.12 | +0.21 | +0.115 |
| Hextech Gunblade | 143,339 | 23% | 4.12 | +0.21 | +0.063 |
| Striker's Flail | 64,814 | 11% | 3.99 | +0.34 | +0.040 |
| Rabadon's Deathcap | 56,201 | 9% | 3.95 | +0.38 | +0.038 |
| Red Buff | 32,745 | 5% | 3.89 | +0.44 | +0.025 |
| Void Staff | 102,176 | 17% | 4.22 | +0.11 | +0.021 |
| Jeweled Gauntlet | 158,536 | 26% | 4.29 | +0.04 | +0.014 |

---

## Chapter 2: What Changes Across Comps

### The Constant -- Guinsoo's Rageblade
Guinsoo's is #1 in every context by a massive margin. Play rate varies (67-88%), but it is always the highest-Necessity item. This is a **comp-independent truth** about Vex.

### Necessity Rankings Side-by-Side

| Rank | NOVA 95 | Dark Star | Shepherd |
|------|---------|-----------|----------|
| #1 | Guinsoo's (0.452) | Guinsoo's (0.260) | Guinsoo's (0.298) |
| #2 | Giant Slayer (0.075) | **Dark Star Emblem** (0.149) | Giant Slayer (0.113) |
| #3 | Hextech Gunblade (0.068) | **Void Staff** (0.041) | **Void Staff** (0.044) |
| #4 | Striker's Flail (0.063) | Giant Slayer (0.027) | Jeweled Gauntlet (0.027) |
| #5 | Rabadon's Deathcap (0.038) | Rabadon's Deathcap (0.025) | Striker's Flail (0.021) |
| #6 | Red Buff (0.035) | Hextech Gunblade (0.023) | Hextech Gunblade (0.020) |

Key differences (bolded items shift significantly across comps):

1. **Dark Star Emblem** is #2 in Dark Star (Nec 0.149) -- obvious comp-specific synergy. Does not appear in other comps.

2. **Void Staff** is #3 in Dark Star (0.041) and Shepherd (0.044) but only Nec +0.007 in NOVA (not even in the top 8). Comp-dependent value.

3. **Giant Slayer** is #2 in NOVA (0.075) and Shepherd (0.113), but drops to #4 in Dark Star (0.027). Still positive everywhere -- see Chapter 3 for how this differs from the old ad-hoc result.

4. **Jeweled Gauntlet** is essentially neutral in NOVA (+0.003) and Dark Star (+0.004), but moderately useful in Shepherd (+0.027, #4). Not a trap anywhere with standardized filters.

5. **Striker's Flail** matters in NOVA (#4, 0.063) but is marginal elsewhere.

### Giant Slayer: The Cross-Comp Comparison

| Context | Rate | AVP | Edge | Necessity |
|---------|------|-----|------|-----------|
| NOVA 95 | 37% | 3.99 | +0.13 | +0.075 |
| Dark Star | 19% | 4.10 | +0.12 | +0.027 |
| Shepherd | 31% | 3.12 | +0.25 | +0.113 |
| Unfiltered | 36% | 4.12 | +0.21 | +0.115 |

Giant Slayer is positive everywhere, but its Necessity varies 4x (0.027 in Dark Star to 0.113 in Shepherd). The comp context changes both the play rate and the marginal value.

---

## Chapter 3: Old Ad-Hoc vs New Standardized Filters

This is the core of the revision. How much did the filter definition matter?

### Sample Size Changes

| Comp | Old Vex Games | New Vex Games | Change |
|------|--------------|---------------|--------|
| NOVA 95 | 210,392 | 231,363 | +10% |
| Dark Star | 3,692 | 5,633 | **+53%** |
| Shepherd | 58,817 | 3,892 | **-93%** |
| Unfiltered | 460,602 | 616,448 | +34% |

The **Shepherd change is dramatic**: the old ad-hoc filter captured 58k Vex games, while the standardized Shepherd definition (Summon 5+, excluding Teemo/Lissandra carries) only has 3.9k Vex games. The old filter was likely defining "any game with Vex in a summon-ish context" rather than the actual Shepherd comp. 49,295 total Shepherd games exist, but Vex only appears in 8% of them -- she is not the Shepherd carry.

### Metric Changes That Matter

| Item | Comp | Old Necessity | New Necessity | Direction Change? |
|------|------|--------------|---------------|-------------------|
| Giant Slayer | Dark Star | **-0.003** | **+0.027** | YES (neg -> pos) |
| Hextech Gunblade | Dark Star | -0.007 | **+0.023** | YES (neg -> pos) |
| Jeweled Gauntlet | Dark Star | **-0.067** | +0.004 | YES (neg -> neutral) |
| Giant Slayer | Shepherd | +0.034 | **+0.113** | Same, 3x magnitude |
| Shepherd Emblem | Shepherd | (not reported) | **-0.034** | New finding |

**Three items flipped sign in Dark Star.** The old ad-hoc filter was polluting Dark Star data with non-Dark Star games (or excluding valid ones), producing artificial negative Necessity values.

The biggest casualty: **Jeweled Gauntlet was called a "trap item"** in the original report (Nec -0.067 in Dark Star). With standardized filters, it's Nec +0.004 -- essentially neutral. The "trap" was an artifact of bad filtering, not a real property of the item.

### What Survived the Revision

Despite the specific numbers changing, the **core structural conclusions hold**:
- Guinsoo's is universally #1 (comp-independent)
- Dark Star Emblem is uniquely valuable in Dark Star (comp-specific)
- Void Staff matters more in Dark Star and Shepherd than in NOVA
- Item rankings shift meaningfully across comps

But the dramatic claims about items "flipping sign" between comps were partially artifacts. With standardized filters, the differences are more about **magnitude** (Giant Slayer 4x more valuable in Shepherd than Dark Star) than about **sign** (positive vs negative).

---

## Chapter 4: Cross-Validation with tftable

tftable ground truth was available for **NOVA 95 only**. For Dark Star and Shepherd, tftable does not track Vex as an itemized unit (Vex is not the carry in those comps).

### NOVA 95: MetaTFT vs tftable

| Item | MetaTFT Nec | tftable Nec | MetaTFT Rank | tftable Rank |
|------|------------|-------------|--------------|--------------|
| Guinsoo's Rageblade | +0.452 | +0.764 | 1 | 1 |
| Giant Slayer | +0.075 | +0.092 | 2 | 2 |
| Hextech Gunblade | +0.068 | +0.078 | 3 | 4 |
| Striker's Flail | +0.063 | +0.080 | 4 | 3 |
| Rabadon's Deathcap | +0.038 | +0.049 | 5 | 5 |
| Red Buff | +0.035 | +0.046 | 6 | 6 |
| Archangel's Staff | +0.018 | +0.017 | 7 | 7 |
| Jeweled Gauntlet | +0.003 | -0.002 | 8 | 11 |

**Top 7 items match between MetaTFT and tftable.** Rankings are nearly identical, with only a Hextech/Striker's swap at #3/#4. The absolute Necessity values differ (tftable Guinsoo's is 0.764 vs MetaTFT 0.452), likely due to different data collection periods or filter implementation details. But the rankings converge strongly.

tftable sample: 135,798 games (vs MetaTFT 231,363 Vex games). Different data windows likely explain the absolute value differences.

---

## What I Learned

1. **Filter definition matters as much as filter existence.** The original experiment proved "you need a filter." This revision proves "the filter must be standardized." Ad-hoc filters produced three sign flips in Dark Star -- Giant Slayer, Hextech Gunblade, and Jeweled Gauntlet all appeared negative with ad-hoc filters but are positive/neutral with standardized ones. The "Jeweled Gauntlet is a trap" conclusion was entirely an artifact.

2. **Shepherd sample size collapsed 93%.** The old ad-hoc "Shepherd" filter was capturing a superset that happened to include 58k Vex games. The real Shepherd comp only has 3.9k Vex games because Vex is not the Shepherd carry. This is the clearest example of why compositions.py matters -- an ad-hoc filter can look reasonable but define a fundamentally different population.

3. **Core conclusion survived, dramatic details didn't.** "Same item, different comp = different BIS" is still true. But the exciting stories (Giant Slayer flipping negative, Jeweled Gauntlet as a trap) were filter artifacts. The truth is more nuanced: items vary in **magnitude** across comps (Giant Slayer 4x stronger in Shepherd than Dark Star) rather than flipping sign.

4. **Cross-validation works for NOVA 95.** Top 7 items match between MetaTFT and tftable. This gives confidence that the standardized nova_95 filter is correct. We cannot cross-validate Dark Star and Shepherd because tftable does not track Vex in those comps.

5. **Vex is a secondary unit in Dark Star and Shepherd.** She appears in only 5% and 8% of those comp's games respectively. Item analysis on a non-carry unit in a comp is inherently noisier -- the 5.6k and 3.9k game samples are still below the ideal 10k+ threshold for stable Necessity estimates.

## Open Questions

- Why did Guinsoo's Necessity differ so much between MetaTFT (0.452) and tftable (0.764)? Is it data window, filter implementation, or calculation methodology?
- Can we cross-validate Dark Star and Shepherd Vex items through any other method, given tftable doesn't track them?
- The vex_95 comp definition returned 0 games -- is this comp definition outdated, or does it target a specific patch window?
- Is it meaningful to analyze Vex items in comps where she appears in <10% of games? At what point does she become "incidental" rather than "part of the comp"?

## Questions for Xing

1. **vex_95 returned 0 games** -- is this definition stale/broken, or was it designed for a different data window? Should we report this as a bug?
2. **Shepherd definition** -- the old ad-hoc filter gave 58k Vex games, but compositions.py Shepherd only has 3.9k. Is the standardized filter correct for studying "Vex in Shepherd"? Or should we also define a "Vex-carry Shepherd" variant?
3. **Cross-comp analysis of a non-carry** -- Vex appears in only 5-8% of Dark Star/Shepherd games. Is it still scientifically valid to compare her item rankings across comps where she is incidental vs where she is the carry?
4. **Necessity magnitude gap** between MetaTFT and tftable for Guinsoo's (0.452 vs 0.764) -- is this expected, or a concern?

---

## Review

### Original Review (2026-04-22)

**Status**: 🔄 revision

#### Feedback (Xing)
1. **Comp filter 未标准化** -- "Dark Star"、"Shepherd" 是 agent 自己临时拼的 filter，没有使用 compositions.py 的专家定义。filter 定义不一致导致数据可能包含错误的局（如 Vex 在 "Dark Star" 里可能混入了非暗星阵容）
2. **结论方向对，但具体数据不可靠** -- "filter matters" 这个大方向是对的，Giant Slayer 在不同阵容表现不同也符合直觉，但具体数字（如 Dark Star 只有 3692 局）需要用标准化 filter 重跑

#### Revision Requirements
- 用 compositions.py 的标准 filter 定义重跑所有阵容的 Vex 装备数据
- 对比标准 filter vs 当时 ad-hoc filter 的差异，量化 filter 定义对结论的影响

### Revision Notes (2026-04-22)

All data re-collected using `python3 cli.py items TFT17_Vex --comp <key>` with standardized compositions.py definitions. Chapter 3 directly compares old vs new results. Key finding: 3 items flipped Necessity sign in Dark Star due to ad-hoc filter pollution. The "Jeweled Gauntlet trap" was an artifact. Cross-validated nova_95 against tftable (top 7 match).
