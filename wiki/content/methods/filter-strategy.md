# Filter Strategy
**Status**: ✅ verified

## Why Filtering is the Foundation

TFT match data is high-dimensional: comp, items, traits, rank, server, stage, augments...

Directly comparing aggregate statistics across these dimensions produces **Simpson's Paradox**: the same item can be BIS in one comp and terrible in another (e.g., Zoe's BIS flips between Rebel and Sorc — Dishsoap example).

In econometrics terms: you can't run an OLS regression without controlling for confounders and expect meaningful coefficients.

**Filter = controlling for confounders.**

## Filter Checklist

```
□ Lock composition: add trait + key unit filters
□ Exclude interference: secondary carry 3-item, special game modes
□ Sanity check: Games tab — look at real games, verify no garbage
□ Preserve sample: don't overfilter below 1000 games
□ Consider rank: Plat+ for general, GM+ for optimization questions
□ Consider region: KR/NA/VN have different metas
```

## Filter Sources

### Option 1: Use tftable compositions.py (Expert-Curated)
tftable maintains `compositions.py` with human-expert-written filter definitions for all meta comps. These use OR groups, trait requirements, and unit exclusions. Available at the tft_data GitHub repo. This is the gold standard.

### Option 2: Build Filters Yourself
Tips from Dishsoap and Aesah:

**Dishsoap’s approach** ([[sources/dishsoap-frodan-stats]]):
- Start with the comp identity (trait + key carry), not the unit
- "Don’t search Zoe items. Search 7 Rebel Zoe items or 6 Sorc Zoe items."
- Use MetaTFT Explorer: add units one by one, check Units tab for frequency + delta
- Use Traits tab: search trait names, compare breakpoints
- Filter by rank (GM+) and region (KR/NA) for granular reads
- Augment proxy trick: search for item patterns that imply augments (e.g., 4× Rageblade = Anger Issues)

**Aesah’s approach** ([[sources/aesah-data-mistakes]]):
- Add comp context (e.g., 3+ Prodigy, 5 Battle Academia) to narrow down
- Use “or more” for traits to capture more variants and increase sample size
- Exclude secondary carries (e.g., exclude Katarina 3) to see primary carry’s true items
- Don’t add too many filters — 92 games = noise

**morbrid’s approach** ([[sources/morbrid-aesah-talk]]):
- Games tab sanity check after every filter change
- Click suspicious outliers → add to filter → look at games → exclude if garbage
- Exclude Golden Ox, cash out games
- Don’t specify star level (introduces selection bias)
- Use bookmarks to A/B compare two filter sets
- “Exclude → Toggle On” to measure category importance (anti-heal, shred)

## Techniques

### Add Context First (Dishsoap)
Don't search "Zoe items". Search "7 Rebel Zoe items" or "6 Sorc Zoe items".

### Exclude → Toggle On (morbrid)
To measure how important a category of items is (e.g., anti-heal):
1. Exclude all anti-heal items (Red Buff, Morello, Sunfire)
2. Note the AVP without any anti-heal
3. Toggle them back on one by one
4. The AVP jump = importance of that category

### Games Tab Sanity Check (morbrid)
After setting filters, always check the Games tab:
- Are these the kinds of games you want to analyze?
- Any Golden Ox / cash out / disconnected boards?
- Is the rank distribution what you expect?

Click a suspicious outlier → add to filter → look at its games → exclude if garbage.

### Don't Overfilter
Every filter reduces sample size. Three filters might be enough. Seven filters might leave you with 200 games and pure noise.

**The art is finding the minimum filters that isolate what you want to study.**

## Trust compositions.py Definitions

tftable 的阵容定义是专家手写的，保证有足够对局数量。如果我们的 filter 转换返回 0 或极少 games，**一定是代码 bug**，不是定义的问题。不要怀疑 compositions.py。

案例：`vex_95` 曾返回 0 games，排查发现是 bare Unit 缺少 `_.*` 通配符后缀（`filter_params.py` 已修复）。

## Common Filters

| Filter | Purpose |
|---|---|
| Trait (e.g., N.O.V.A. ≥2) | Lock composition |
| Key units with 3 items | Ensure primary carry setup |
| Exclude specific units | Remove comp variants you don't want |
| Exclude 3-item secondary carry | Remove "winning so hard I itemize everyone" games |
| Rank (GM+) | See what good players do |
| Star level (don't specify) | morbrid: specifying stars introduces bias |

## Sources
- [[sources/dishsoap-frodan-stats]]: "Add context first", don't just put the unit in
- [[sources/morbrid-aesah-talk]]: Games tab, exclude→toggle, don't overfilter
- [[sources/aesah-data-mistakes]]: Filter to see primary carry items
