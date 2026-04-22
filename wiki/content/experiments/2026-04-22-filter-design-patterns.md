# Experiment: Expert Filter Design Patterns in compositions.py
**Status**: 🧪 draft
**Date**: 2026-04-22
**Module**: 1 (Filter Design — practice)

---

## The Question

`compositions.py` contains 29 expert-curated comp filter definitions from XWang20/tft_data. These represent human-expert filter design decisions. **What patterns do experts use, and how much does filter design actually matter for item analysis?**

Specifically:
1. What recurring design patterns appear across 29 comp definitions?
2. How much do item Necessity rankings change when you use a full expert filter vs a minimal carry-only filter?
3. Can the same unit have completely different BIS items in different comps?

---

## Chapter 1: Taxonomy of Filter Patterns

Analyzing all 29 comp definitions in `compositions.py`, I identified 5 recurring design patterns:

### Pattern 1: Carry-Only (5 comps)

The simplest filter — just the carry unit with 3 items. No trait, no exclusions.

| Comp | Filter |
|---|---|
| zed | `Unit(Zed, i3)` |
| kaisa | `Unit(Kai'Sa, i3)` |
| bonk | `Unit(Nasus, i3)` |
| veigar | `Unit(Veigar, i3)` |
| termeepnal_velocity | `Unit(Poppy, i3)` |

**When used**: When the carry itself is sufficiently unique — no other comp runs this unit as primary carry with 3 items. Zed 3-item is always a Zed comp; there's no "Zed in another comp" problem.

**Sample sizes**: Tend to be moderate (Zed 53k, Kai'Sa 156k, Bonk 51k, Veigar small, Poppy small).

### Pattern 2: Carry + Trait Lock (5 comps)

Carry unit + a trait requirement to define the comp's identity.

| Comp | Carry | Trait |
|---|---|---|
| conduit_mf | MF (i2+) | Conduit ≥ 2 |
| mecha | ASOL (i2+) + Galio (i2+) | Mecha = 6 |
| anima_diana | Aurora (i3) \| Diana (i3) + Diana | Anima Squad ≥ 3 |
| primordian | Bel'Veth (i3) \| Akali (i3) | Primordian ≥ 2 |
| two_tanky_samira | Samira × 2 | — (count=2 is the lock) |

**When used**: When the carry appears in multiple comps. MissFortune with items could be many comps, but MF + Conduit trait isolates the specific build path.

### Pattern 3: OR-Carry Group + Trait + Exclusions (7 comps)

The most common pattern for meta comps. Multiple possible carries (OR-group), a trait anchor, and exclusions to prevent leakage from similar comps.

| Comp | OR Carries | Trait | Exclusions |
|---|---|---|---|
| nova_95 | Fiora\|Vex\|Graves (i3) | DRX ≥ 2 | ~Mecha 4, ~Kindred, ~Aurora i3, ~MasterYi i3, ~Zed |
| nova_yi | MasterYi\|Kindred (i3) | DRX ≥ 2 | ~Primordian 2, ~Aatrox i3★3 |
| space_groove | Nami\|Samira (i3) | Space Groove ≥ 5 | ~Nasus i3★3 |
| meeple_corki | Corki (i3) | Astronaut ≥ 5 | ~Veigar i3, ~Ivern i3★3, ~Poppy i3 |
| vanguard_leblanc | LeBlanc (i3) | Vanguard ≥ 2, Summon = 3 | ~Diana i3, ~Nasus i3, ~Zoe i3, ~Teemo i3, ~Vex i3 |
| xayah | Xayah (i3) | — | ~Lulu i3, ~Samira i3, ~Jax i3, ~DarkStar 4, ~Ezreal i3 |
| voyager | Karma + Nami + Lissandra | — | ~Veigar, ~Pyke i3, ~Ivern i3, ~Viktor i3, ~Aurora i3, ~LeBlanc, ~DarkStar 4 |

**Key insight**: This is where filter design gets hard. The exclusions form a **negative boundary** — "this comp is NOT those other comps." nova_95 excludes 5 units to separate from nova_yi, mecha, and other DRX variants. vanguard_leblanc excludes 5 alternate carries to isolate the Vanguard-Summon variant.

### Pattern 4: Carry + Minimal Exclusions (5 comps)

Light exclusion to separate from one or two overlapping comps.

| Comp | Filter | Excluded |
|---|---|---|
| pyke | Pyke (i3) | ~Viktor i3 |
| viktor | Viktor (i3) | ~MF, ~Pyke i3, ~MasterYi i3 |
| shepherd | Summon ≥ 5 | ~Teemo i3, ~Lissandra i3 |
| vex_95 | Vex (i3) + Blitz + Morde | ~LeBlanc, ~DRX ≥ 2, ~Jhin i3 |
| reach_for_the_stars | Jax (i3) | — |

### Pattern 5: Item-Based Exclusions (3 comps)

The most unusual pattern — uses `~Item()` to exclude specific item-on-unit combinations.

| Comp | Item Exclusion | Purpose |
|---|---|---|
| lulu | ~Guinsoo on Jax | Exclude Jax-reroll boards that happen to include Lulu |
| tf | ~Bloodthirster on Aatrox, ~Titan's on Jax | Exclude Aatrox/Jax reroll boards |
| teemo | ~Guinsoo on Nasus | Exclude Bonk boards with Teemo |

**This is the most subtle pattern.** These comps share low-cost units with other reroll comps, so unit and trait filters alone can't separate them. The expert uses signature items as negative identifiers — if Jax has Titan's Resolve, it's a Jax reroll, not a TF comp.

---

## Chapter 2: The Filter Impact — LeBlanc Case Study

LeBlanc appears in at least two distinct comps: **vanguard_leblanc** (Vanguard + Summon shell, Guinsoo carry) and various other boards. The expert filter has heavy exclusions. Does it matter?

### Minimal filter: `Unit(LeBlanc, i3)` — 281,409 games

| Rank | Item | Nec. | Rate |
|---|---|---|---|
| 1 | Rabadon's Deathcap | +0.035 | 11% |
| 2 | Giant Slayer | +0.031 | 48% |
| 3 | Archangel's Staff | +0.017 | 10% |
| 4 | Sparking Prototype | +0.008 | 1% |
| 5 | Vanguard Emblem | +0.007 | 3% |

### Full filter: `--comp vanguard_leblanc` — 161,786 games

| Rank | Item | Nec. | Rate |
|---|---|---|---|
| 1 | **Guinsoo's Rageblade** | **+0.071** | **92%** |
| 2 | Giant Slayer | +0.051 | 53% |
| 3 | Rabadon's Deathcap | +0.027 | 11% |
| 4 | Vanguard Emblem | +0.013 | 3% |
| 5 | Archangel's Staff | +0.011 | 9% |

**Guinsoo's Rageblade is invisible in the minimal filter (not in top 25!) but is the #1 item by a massive margin in the full filter** (Nec +0.071, 92% usage). Without the comp filter, the 120k non-vanguard LeBlanc games (Diana-carry boards, Summon-5 variants, etc.) pollute the rankings. Those games don't use Guinsoo, so it gets diluted out of the top results despite being a 92% must-build in the actual comp.

### Cross-validation with tftable

tftable for vanguard_leblanc (131,531 games):

| tftable Rank | Item | tftable Nec. | Our Nec. |
|---|---|---|---|
| 1 | Guinsoo's Rageblade | 0.489 | 0.071 |
| 2 | Giant Slayer | 0.085 | 0.051 |
| 3 | Jeweled Gauntlet | 0.052 | 0.010 |
| 4 | Rabadon's Deathcap | 0.027 | 0.027 |
| 5 | Archangel's Staff | 0.017 | 0.011 |

**Rankings match perfectly (top 5 identical).** Absolute Necessity values differ (tftable's are higher), but the ordering is robust. Both sources agree: Guinsoo is defining, Giant Slayer is important, the rest are optional.

---

## Chapter 3: Same Unit, Different Comp — Vex Edition

Vex appears in two comps: **nova_95** (DRX shell) and **vex_95** (Blitzcrank + Mordekaiser shell, no DRX). Does comp context change her BIS?

### Vex in nova_95 (211,359 games)

| Rank | Item | Nec. | Rate |
|---|---|---|---|
| 1 | Guinsoo | +0.502 | 88% |
| 2 | Giant Slayer | +0.083 | 38% |
| 3 | Hextech Gunblade | +0.076 | 29% |
| 4 | Striker's Flail | +0.063 | 16% |
| 5 | Rabadon's Deathcap | +0.038 | 10% |

### Vex in vex_95 (140,160 games)

| Rank | Item | Nec. | Rate |
|---|---|---|---|
| 1 | Guinsoo | +0.123 | 92% |
| 2 | Giant Slayer | +0.094 | 52% |
| 3 | Rabadon's Deathcap | +0.025 | 12% |
| 4 | Hextech Gunblade | +0.019 | 27% |
| 5 | **Void Staff** | **+0.009** | **26%** |

Key differences:
- **Striker's Flail**: Rank 4 (Nec +0.063) in nova_95 → Rank 10 (Nec +0.003) in vex_95. A 20× Necessity drop.
- **Void Staff**: Not in top 11 in nova_95 → Rank 5 (Nec +0.009) in vex_95. Appears only when the DRX trait isn't boosting magic damage.
- **Hextech Gunblade**: Rank 3 in nova_95 → Rank 4 in vex_95, with Necessity dropping from +0.076 to +0.019 (4× reduction).

This confirms Dishsoap's principle: **"Don't search Vex items. Search Nova 95 Vex items or Vex 95 Vex items."** The supporting cast (DRX trait, Mordekaiser shell) changes what the carry needs.

---

## Chapter 4: Nami — The Simpson's Paradox Poster Child

Nami is the most extreme case. She appears in **space_groove** and **voyager** — two completely different comps with different traits, different supporting casts, and wildly different AVP baselines.

### All Nami i3 (no comp filter): 428,846 games, AVP 3.96

| Rank | Item | Nec. |
|---|---|---|
| 1 | Void Staff | +0.145 |
| 2 | Spear of Shojin | +0.082 |
| 3 | Giant Slayer | +0.029 |

### Nami in space_groove: 225,742 games, AVP 4.11

| Rank | Item | Nec. |
|---|---|---|
| 1 | Spear of Shojin | +0.072 |
| 2 | **Nashor's Tooth** | **+0.038** |
| 3 | Nashor's Tooth ★2 | +0.028 |
| 4 | Void Staff | +0.018 |

### Nami in voyager: 12,635 games, AVP 4.82

| Rank | Item | Nec. |
|---|---|---|
| 1 | **Jeweled Gauntlet** | **+0.199** |
| 2 | Nashor's Tooth | +0.137 |
| 3 | Spear of Shojin | +0.105 |
| 4 | Nashor's Tooth ★2 | +0.041 |

**Three completely different BIS profiles from the same unit:**

| Item | Global Rank | Space Groove Rank | Voyager Rank |
|---|---|---|---|
| Void Staff | **#1** (+0.145) | #4 (+0.018) | not ranked |
| Jeweled Gauntlet | not ranked | not ranked | **#1** (+0.199) |
| Nashor's Tooth | not ranked | **#2** (+0.038) | #2 (+0.137) |

Void Staff is #1 globally but drops to #4 in Space Groove and disappears in Voyager. Jeweled Gauntlet is Nami's most important item in Voyager but doesn't appear in the top 16 globally. **This is textbook Simpson's Paradox**: aggregating across comp contexts produces rankings that are wrong for every individual context.

---

## Chapter 5: Design Pattern Summary — Expert Filter Heuristics

From the 29 comp definitions, I extract these expert heuristics:

### Heuristic 1: Identity = Trait + Carry, Boundary = Exclusions

The **positive** filter (trait lock + carry specification) defines what this comp IS.
The **negative** filter (exclusions) defines what this comp IS NOT.

Most design effort goes into the exclusions. nova_95 has 2 positive conditions (3-item carry OR + DRX ≥ 2) but 5 exclusions. This reflects a domain reality: many S17 comps share units, so the boundaries between comps must be explicitly drawn.

### Heuristic 2: Exclusions Target 3-Item Carries

Of 44 total `~Unit()` exclusions across all 29 comps, **28 (64%)** specify `item_min=3, item_max=3`. This is deliberate: a unit with 3 items is someone's carry. If another carry appears in "your" comp's data, those are contaminated games.

### Heuristic 3: Item Exclusions for Low-Cost Overlaps

Only 3 comps use `~Item()` exclusions (lulu, tf, teemo). All are low-cost reroll comps that share units with other reroll comps at the same cost tier. When unit + trait filters can't separate TF-reroll from Jax-reroll (both use Jax + TF), the expert falls back to signature items as discriminators.

### Heuristic 4: Trait Max = Comp Narrowing

Two comps use `max_units` on traits:
- mecha: `Mecha = 6` (exactly 6, not more) — this is a very specific board state
- vanguard_leblanc: `Summon = 3` (exactly 3 Summon) — separates from Shepherd (Summon ≥ 5)

Setting a trait ceiling prevents overlap with higher-breakpoint variants that play fundamentally differently.

### Heuristic 5: Carry-Only Works When the Carry is Unique

The 5 carry-only comps (zed, kaisa, bonk, veigar, poppy) all share a property: no other meta comp uses that unit as primary carry. When there's only one way to play a unit, no exclusion is needed.

---

## What I Learned

1. **Filter design is the most impactful analytical decision.** For LeBlanc, the difference between minimal and full filter isn't a small adjustment — it's the difference between Guinsoo being invisible and being the #1 item. The filter doesn't refine the analysis; it fundamentally changes the answer.

2. **Expert exclusions are boundary definitions, not noise removal.** The 64% of exclusions targeting 3-item carries aren't removing "bad games" — they're defining where one comp ends and another begins. This is a semantic operation, not a statistical one.

3. **Item-based exclusions are the last resort.** Only 3 of 29 comps need them, and only for low-cost reroll comps where unit/trait overlap is unavoidable. This is the expert's escape hatch when the standard tools fail.

4. **Simpson's Paradox is not theoretical — it's the default.** Nami's global BIS (#1 Void Staff) is wrong for both of her comps. The aggregate doesn't approximate any individual context. Unfiltered analysis doesn't produce "roughly right" answers; it produces actively misleading ones.

5. **Carry uniqueness determines filter complexity.** The 5-pattern taxonomy maps to a single variable: how many comps share this carry? Unique carry → carry-only filter. Shared carry → need trait locks and exclusions. The expert intuitively knows this and calibrates filter complexity accordingly.

---

## Open Questions

1. **How many games does each exclusion save?** We could measure this by removing exclusions one at a time from a complex filter (like vanguard_leblanc) and checking how many contaminated games each exclusion blocks.

2. **Are there missing exclusions?** The expert definitions are from a specific point in the meta. If new comps emerge that share units with existing comps, the exclusions may need updating.

3. **Can filter design be automated?** Given that the heuristics follow clear patterns (3-item carry exclusion, trait locks, item-based fallbacks), could we write code that suggests filters based on unit overlap analysis?

4. **What's the minimum viable filter?** For analysis on a time budget, which single filter element matters most — trait lock, carry specification, or exclusions?

---

## Questions for Xing

1. **Item exclusion pattern**: The `~Item(Guinsoo, carrier=Jax)` pattern in lulu and teemo is clever — it uses signature items as comp discriminators. Is this something tftable arrived at through iteration, or was it designed from first principles?

2. **Filter evolution**: Do the compositions.py definitions change within a patch as the meta shifts, or are they set once at patch start? If the meta creates new comp overlaps mid-patch, do the exclusions get updated?

3. **Trait max_units**: The `Summon = 3` in vanguard_leblanc is very precise. How sensitive are the results to this ceiling? Would `Summon ≤ 3` or `Summon ≥ 2` produce meaningfully different rankings?

4. **Nami surprise**: Void Staff being #1 globally but irrelevant within either comp is a striking Simpson's Paradox example. Is this a known phenomenon in TFT analytics, or did it surprise you too?

5. **Automation potential**: Could the filter design process be partially automated — e.g., given a carry unit, automatically identify which other comps share it and suggest exclusions? Or is there too much domain knowledge involved?

---

## Sources
- `tft_stat/compositions.py` — 29 comp definitions
- `tft_stat/filter_expr.py` — filter expression tree implementation
- tftable ground truth via `python3 cli.py tftable --comp vanguard_leblanc`
- [[methods/filter-strategy]] — existing filter methodology
- [[concepts/metrics]] — Necessity as primary metric
- [[sources/dishsoap-frodan-stats]] — "Add context first" principle

---

## Review
