# Item Analysis Debiasing
**Status**: 🧪 exploring

Two techniques for cleaning item Necessity analysis: (1) exclude non-craftable items at query level, (2) conflict recompute for shared-carry item competition.

## Problem 1: Non-Craftable Item Pollution

When querying single-item Necessity, the results mix craftable items with special items (artifacts, radiant, Anima Squad, trait/emblem items). These special items have extreme AVP (e.g., Battle Bunny Crossbow AVP 2.4 on Xayah) and distort the baseline, play rates, and Necessity of normal items.

### Solution: Exclude at Query Level

Use MetaTFT API's `unit_itemtype_counts` parameter to exclude games where the carry has non-craftable items:

```
unit_itemtype_counts=!{unit}-1|artifact_1,2,3
unit_itemtype_counts=!{unit}-1|radiant_1,2,3
unit_itemtype_counts=!{unit}-1|trait_1,2,3
unit_itemtype_counts=!{unit}-1|emblem_1,2,3
```

The `|` and `,` must be URL-encoded. The `!` prefix means "exclude games where this unit has 1, 2, or 3 of this type."

**CLI**: `python3 cli.py items TFT17_Xayah --comp xayah --normal-only`

### TODO: Anima Squad Exclusion

`unit_itemtype_counts` has no type for Anima Squad items. Current workaround:
- Result-level filter by item ID prefix (`AnimaSquadItem`) -- **only hides items from display, does NOT exclude Anima-carrying games from the baseline**
- Specific items (e.g., Battle Bunny Crossbow) can be excluded via `~Item(carrier_unit_id=...)` in the filter expression, but this only works for `unit_item` negation, not game-level filtering on `total` endpoint

**This is incomplete**: Anima-carrying games still pollute the baseline AVP and other items' play rates. Need to find the correct `unit_itemtype_counts` type name for Anima, or an alternative API-level exclusion.

### Impact

Xayah comp: 387k games -> 255k games (34% excluded for artifact/radiant/trait/emblem). Normal item rankings become cleaner: Kraken's Fury(#1) > Red Buff(#2) > Last Whisper(#3).

## Problem 2: Carry Item Competition (Conflict Recompute)

When two carries in the same comp share item preferences, the secondary carry "steals" items from the primary carry, creating selection bias in Necessity.

### The Mechanism

Example: Xayah and Jhin both want Infinity Edge. When the team has only one IE, it usually goes to Jhin (better use). Xayah with IE = games where Jhin didn't get IE = Jhin suboptimal = team underperforms. This makes IE look bad on Xayah, even though it's genuinely good when both carries are full.

This is the same pattern as Dishsoap's Zoe/Jinx Shojin example: Zoe's Shojin looks terrible because when there's only one Shojin, Jinx gets it. Filter for Jinx having her startup items, and Zoe's Shojin Necessity jumps to match Guinsoo's.

### Ideal Solution: Per-Item Competing Carry Filter

For each conflicting item, filter for games where the competing carry ALSO has that specific item:

```python
# Recompute IE on Xayah: filter for games where Jhin also has IE
filt_recomp_ie = xayah_base & Item('TFT_Item_InfinityEdge', carrier_unit_id='TFT17_Jhin')

# Recompute GS on Xayah: filter for games where Jhin also has GS
filt_recomp_gs = xayah_base & Item('TFT_Item_MadredsBloodrazor', carrier_unit_id='TFT17_Jhin')
```

When Jhin also has IE, Xayah's IE is not at Jhin's expense -- both carries have the item, so Necessity reflects true value without competition bias.

### Implementation: Positive `unit_item_unique` Filter

The `unit_item_unique` endpoint supports positive carrier-item filters:

```python
# Filter for games where Jhin carries IE
Item('TFT_Item_InfinityEdge', carrier_unit_id='TFT17_Jhin')
# → unit_item_unique=TFT17_Jhin-1%26TFT_Item_InfinityEdge-1
```

### WARNING: Approximate Method is Biased

A previously used workaround `Unit('TFT17_Jhin', item_min=3)` (Jhin has any 3 items) introduces **systematic upward bias**. "Jhin is full" selects for stronger teams generally, not just for resolved item competition. In the Xayah experiment, the approximate method showed IE flipping positive in 3 Stargazers, while the precise method shows only 1 (Medallion). Worse, it masked that Last Whisper's positive Necessity was partly a Jhin-correlation artifact — precise recompute showed LW dropping to near-zero.

**Always use `Item(item_id, carrier_unit_id=carry)` for conflict recompute. Do not use `Unit(carry, item_min=3)`.**

### How to Identify Conflict Items

Items that meet ALL of:
1. High play rate on the primary carry (>10%)
2. Also used by a secondary carry in the same comp
3. Strongly negative Necessity on the primary carry despite being a "good" item type

### Reporting Format

For items with meaningful conflict recompute change:

```
+0.014(#3) / +0.014->+0.023(#3)    # small change, same rank
-0.144(#25) / -0.144->+0.012(#4)   # major flip: negative -> positive
```

Left side: original Necessity and rank. Right side: original -> recomputed Necessity and new rank. Only show recompute when the change exceeds 0.002.

## When to Apply

1. **Exclude special items**: Always, when analyzing craftable item choices. Use `--normal-only`.
2. **Conflict recompute**: When the comp has a secondary carry sharing AD/AP item pool. Check if any high-play-rate items have suspiciously negative Necessity.

## Sources
- [[experiments/2026-04-22-xayah-stargazer-items]] -- first application of both techniques
- [[sources/dishsoap-frodan-stats]] -- Zoe/Jinx Shojin example (the original insight)
