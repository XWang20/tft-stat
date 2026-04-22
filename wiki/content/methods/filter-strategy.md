# Filter Strategy
**Status**: ✅ verified

## Why Filtering is the Foundation

TFT match data is high-dimensional: comp, items, traits, rank, server, stage, augments...

**Filter = controlling variables.** Not data preprocessing — it defines what question you're asking.

Every filter condition controls a variable:
- Fixed comp (trait + carry) = controls team composition
- `item_min=3` on a unit = controls role (primary carry vs secondary)
- Exclude specific units = controls comp boundaries
- Rank/region = controls player skill

**Your question determines your filter.** "What's Vex's BIS as primary carry?" → filter must isolate games where Vex IS the primary carry. "What's the best 9th unit for Nova 95?" → filter must lock the 8-unit core.

### Primary Carry vs Secondary — The Most Important Variable

Every unit is either **primary carry (主C)** or **secondary/support (副C)** in a given game. Itemization differs completely between these roles:
- Primary carry: optimized item builds, 3 items, items chosen deliberately
- Secondary: leftover items, late carousel pickups, survivorship bias at maximum

Whether a unit is primary carry is determined by comp context. `Unit('TFT17_Vex', item_min=3)` in compositions.py means "games where Vex is the primary carry." Without this distinction, you're mixing two completely different populations.

**Not all comps have a single primary carry.** Comp types:
- **Single carry**: one clear 主C (e.g., Zed, Kai'Sa) — simple
- **Flex carry**: carry slot rotates between units (e.g., nova_95: Fiora/Vex/Graves) — use OR-group
- **Dual carry**: items distributed across two units (e.g., mecha: ASOL + Galio) — lower item threshold
- **Line**: a flexible path defined by a trait shell, not a fixed board (e.g., Space Groove) — harder to filter, more contamination expected

### Simpson's Paradox Is Not Theoretical — It's the Default

Nami demonstrates this with real data. Her global item rankings (all 428k Nami-i3 games) show Void Staff as the #1 item (Nec +0.145). But within either of her actual comps:

| Item | Global | Space Groove | Voyager |
|---|---|---|---|
| Void Staff | **#1** (Nec +0.145) | #4 (Nec +0.018) | not ranked |
| Jeweled Gauntlet | not ranked | not ranked | **#1** (Nec +0.199) |

Void Staff is globally #1 but irrelevant within either comp. Jeweled Gauntlet is Nami's most important item in Voyager but invisible in global data. The aggregate doesn't approximate any individual context — it produces actively misleading rankings.

### Measured Impact: Filter Changes Conclusions, Not Just Precision

These are not hypothetical scenarios. Measured across S17 comps:

- **Giant Slayer** on Vex: Necessity +0.084 in nova_95, +0.026 in dark_star — same item, same champion, 3x difference depending on comp context.
- **Striker's Flail** on Vex: Necessity +0.063 in nova_95, +0.003 in vex_95 — a **20x drop** between two comps that both feature Vex as primary carry.
- **Guinsoo's Rageblade** on LeBlanc: invisible in top 25 with a carry-only filter (281k games), but **#1 item at 92% usage** with the full vanguard_leblanc filter (162k games). The filter doesn't refine the answer — it fundamentally changes it.

The filter is not a statistical refinement. It determines which question you're answering.

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

tftable maintains `compositions.py` with 29 expert-curated filter definitions for all meta comps. Available at the tft_data GitHub repo. **This is the gold standard — always prefer these over ad-hoc filters.**

Analysis of all 29 definitions reveals 5 recurring design patterns:

#### Pattern 1: Carry-Only (5 comps)
Just the carry unit with 3 items. No trait, no exclusions.
Examples: `zed` = `Unit(Zed, i3)`, `kaisa` = `Unit(Kai'Sa, i3)`, `bonk` = `Unit(Nasus, i3)`

**When it works**: when the carry is unique — no other comp runs this unit as primary carry with 3 items. There is no "Zed in another comp" problem.

**Carry-only ≠ no exclusions.** Even carry-only comps may need exclusions — not for other carries sharing the slot, but for units whose 3-item presence signals a different comp. Example: `viktor` excludes `~Pyke(i3)` and `~MasterYi(i3)` (reroll/NOVA carries that share low-cost units), plus `~MissFortune` entirely (her presence signals Conduit MF regardless of items). A unit at 86% appearance (Pyke in Viktor) can still be an exclusion target when it's the *3-item carry version* that's contamination — the support version (1 item) stays.

#### Pattern 2: Carry + Trait Lock (5 comps)
Carry unit plus a trait requirement to define the comp's identity.
Examples: `conduit_mf` = MF (i2+) + Conduit >= 2; `mecha` = ASOL (i2+) + Galio (i2+) + Mecha = 6

**When it works**: when the carry appears in multiple comps. MF with items could be many things, but MF + Conduit isolates the specific build path.

#### Pattern 3: OR-Carry Group + Trait + Exclusions (7 comps)
The most common pattern for meta comps. Multiple possible carries (OR-group), a trait anchor, and exclusions to prevent leakage from similar comps.
Examples: `nova_95` = Fiora|Vex|Graves (i3) + DRX >= 2, excluding Mecha 4, Kindred, Aurora i3, MasterYi i3, Zed. `vanguard_leblanc` = LeBlanc (i3) + Vanguard >= 2 + Summon = 3, excluding 5 alternate carries.

**Key insight**: most design effort goes into the exclusions. nova_95 has 2 positive conditions but 5 exclusions. The exclusions form a **negative boundary** — "this comp is NOT those other comps."

#### Pattern 4: Carry + Minimal Exclusions (5 comps)
Light exclusion to separate from one or two overlapping comps.
Examples: `pyke` = Pyke (i3), excluding Viktor i3; `vex_95` = Vex (i3) + Blitz + Morde, excluding LeBlanc, DRX >= 2, Jhin i3

#### Pattern 5: Item-Based Exclusions (3 comps)
The most subtle pattern — uses `~Item()` to exclude specific item-on-unit combinations.
Examples: `lulu` excludes Guinsoo on Jax (separates from Jax-reroll boards); `tf` excludes Bloodthirster on Aatrox and Titan's on Jax (separates from Aatrox/Jax reroll boards)

**When it works**: only for low-cost reroll comps where unit/trait overlap is unavoidable. The expert uses signature items as negative identifiers — if Jax has Titan's Resolve, it's a Jax reroll, not a TF comp.

#### Expert Heuristics Extracted from These Patterns

1. **Identity = Trait + Carry; Boundary = Exclusions.** The positive filter defines what the comp IS; the negative filter defines what it IS NOT.
2. **64% of exclusions target 3-item carries.** A unit with 3 items is someone's carry. If another carry appears in "your" comp's data, those are contaminated games.
3. **Trait ceilings narrow comps.** `Summon = 3` (not >= 3) in vanguard_leblanc prevents overlap with Shepherd (Summon >= 5). Setting a max prevents leakage into higher-breakpoint variants.
4. **Carry uniqueness determines filter complexity.** Unique carry = carry-only filter. Shared carry = need trait locks and exclusions. The taxonomy maps to one variable: how many comps share this carry?

### Option 2: Design a Filter From Scratch

When compositions.py doesn't have the comp you want to study, or when you discover a new comp pattern, build the filter iteratively:

#### Step 1: Scout top player boards
Run `python3 cli.py scout --top 3` to scan recent top-3 endgame boards from Challenger/GM. Identify recurring board patterns — groups of units that appear together. These are candidate comps.

**Beware single-carry bias**: seeing the same carry across 2-3 boards doesn't prove the comp has a fixed carry. In Line/flex comps (e.g., Space Groove), different carries can fill the same slot. If the boards share a trait shell but the 3-item carry could plausibly rotate (e.g., Nami or Samira in SpaceGroove), treat alternative carries as co-carries (OR-group), not contamination. Check whether other units in the same trait shell also appear with 3 items before excluding them.

#### Step 2: Write initial filter (Dishsoap method)
Start with the comp's identity, not a single unit. Different comp types need different approaches:

**Single carry comp** (e.g., `zed`): trait anchor + carry with 3 items. Straightforward.

**Flex carry comp** (e.g., `nova_95`): the carry slot is flexible — Fiora, Vex, or Graves can all be the primary carry. Use an OR-group for the carries: `(Fiora i3 | Vex i3 | Graves i3) & DRX ≥ 2`. The comp is defined by the trait shell, not a single carry.

**Carry + trait lock comp** (e.g., `conduit_mf`): carry unit + trait requirement. Use `i2` (not `i3`) when the carry routinely shares items with frontline or secondary units — `MF(i2) + Conduit ≥ 2`. Using `i3` here drops ~11% of legitimate games where MF had only 2 items.

**Dual/multi carry comp** (e.g., `mecha`): multiple units share items. `ASOL(i2) + Galio(i2) + Mecha = 6`. Three key differences from single/flex carry comps: (1) use AND to require both carries simultaneously — OR captures single-carry games from other comps; (2) lower the item threshold (i2 instead of i3) because items are distributed between carries; (3) use exact trait match (`= 6` not `>= 6`) as a trait ceiling to prevent splash contamination from other comps running a few Mecha units.

**Line (not comp)** (e.g., `space_groove`): a flexible path defined by a trait, not a fixed board. `(Nami i3 | Samira i3) + Space Groove ≥ 5`. These are harder to filter because the endgame boards vary more. Expect lower IC3 rates and more contamination — add exclusions carefully.

Don't add exclusions yet in this step — start broad.

#### Step 3: Validate with data
Run `python3 cli.py total` and `python3 cli.py units` with your filter. Check:
- **Total games**: is the sample size reasonable (≥1000)?
- **Carry IC3 rate**: what % of games have the carry with 3 items? Should be high (>50%) if this is truly a carry comp
- **Unit frequency**: do the expected core units appear at high rates? Do unexpected units appear (= contamination)?

#### Step 4: Iteratively refine
Based on Step 3 results:
- **Unexpected units at high frequency** → they're from a different comp leaking in. Add exclusion (`~Unit()`)
- **IC3 rate too low** → your carry definition might be wrong, or the trait anchor is too broad
- **Sample too small** → your filter is too narrow. Relax a condition (e.g., remove an exclusion, lower trait threshold)
- **Sample too large with mixed boards** → add a trait ceiling or more exclusions
- **Low-cost reroll contamination in Line comps** → when a trait-anchored filter (e.g., SpaceGroove >= 5) overlaps with a reroll comp's units, check for 3-star carries with 3 items leaking in. Use `~Unit(X, item_min=3, star_min=3, star_max=3)` to exclude only the true reroll cases while keeping normal appearances of that unit.
- **Too many exclusions needed** → if you find yourself adding 10+ exclusions to clean the filter, you likely need a **trait ceiling** (`max_units`) rather than more exclusions. A single `Summon = 3` (not `>= 3`) replaces a dozen carry exclusions by cutting off overlap with higher-breakpoint variants (e.g., Shepherd at Summon >= 5). Fix the constraint first, then add only the targeted exclusions the constraint can't handle.

#### Step 5: Cross-validate
Compare your filter's item Necessity rankings against tftable (`python3 cli.py tftable`) if the comp exists there. If rankings diverge significantly, your filter boundary may be wrong.

#### The Loop
```
scout → initial filter → check IC3/games/units → adjust → re-check → ...
→ converge when: target comp included + interference excluded + sample adequate
→ output: a reliable filter definition
```

This is how compositions.py definitions are written — the same iterative process, formalized.

### Tips from Experts

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

### Filter Reliability Depends on Unit Role

Not all units benefit equally from careful filtering. Filter reliability depends on the unit's **carry role** within the comp.

| Unit Role | Filter Sensitivity | Example |
|-----------|-------------------|---------|
| **Primary carry** (3-item, >80% appearance) | Low — rankings stable across filter levels (ρ ≥ 0.89) | Vex in NOVA: full vs minimal ρ = 0.893, full vs no-filter ρ = 0.976 |
| **Tank / secondary** | Extreme — rankings invert across filter levels (ρ ≈ 0.05) | Mordekaiser in Dark Star: full vs tftable ρ = 0.048, Warmog's rank swings #1↔#7 |

**Why**: The primary carry IS the comp's identity. Filter changes mostly add/remove non-carry games, but carry-specific games stay similar. A tank's optimal build depends on the surrounding team context — different filters select different contexts.

**Practical rule**: For primary carries, even a minimal filter (carry + 3 items) produces reliable Necessity rankings. For tanks and secondary carries, cross-validate with tftable before trusting any ranking. See [[experiments/2026-04-22-filter-reliability]].

## Ad-hoc vs Standardized Filters

**Always use standardized compositions.py definitions. Never construct ad-hoc filters when an expert definition exists.**

### The Shepherd Cautionary Tale

An ad-hoc "Shepherd" filter (agent-constructed on the fly) captured 58,817 Vex games. The standardized Shepherd definition (Summon >= 5, excluding Teemo/Lissandra carries) has only 3,901 Vex games — a **93% sample collapse**.

The old filter was defining "any game with Vex in a summon-ish context" rather than the actual Shepherd comp. Of the 49,432 total Shepherd games, Vex only appears in 8%. She is not the Shepherd carry. The ad-hoc filter was analyzing a fundamentally different population while calling it by the same name.

### Three Sign Flips in Dark Star

Ad-hoc filters for Vex in Dark Star produced three Necessity sign flips compared to standardized filters:

| Item | Ad-hoc Necessity | Standardized Necessity | Conclusion change |
|---|---|---|---|
| Giant Slayer | -0.003 | **+0.026** | "avoid" -> "useful" |
| Hextech Gunblade | -0.007 | **+0.022** | "avoid" -> "useful" |
| Jeweled Gauntlet | -0.067 | **+0.003** | "trap item" -> "neutral" |

The original experiment called Jeweled Gauntlet a "trap item" in Dark Star. That conclusion was entirely a filter artifact — the item is neutral with proper conditioning.

### Why This Happens

Ad-hoc filters are dangerous because they feel reasonable. "Vex + some Summon units" sounds like a reasonable proxy for Shepherd, but it captures a superset that includes many non-Shepherd games. The resulting metrics are a weighted average of real Shepherd games and contaminating games — Simpson's Paradox at the filter level.

**Rule**: If compositions.py has a definition, use it. If it doesn't, your analysis question may be ill-defined.

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
- [[experiments/2026-04-22-vex-cross-comp-items]]: Quantified filter impact — 3 sign flips from ad-hoc vs standardized, Shepherd 93% sample collapse
- [[experiments/2026-04-22-filter-design-patterns]]: 5 expert filter patterns from 29 comp definitions, LeBlanc case study, Nami Simpson's Paradox
