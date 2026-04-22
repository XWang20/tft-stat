# Experiment: Xayah Stargazer Item Analysis
Status: 🧪 draft
Date: 2026-04-22
Module: 2, 7

## The Question

S17 Xayah comp can pair with 7 different Stargazer effects. Do different Stargazer types change Xayah's optimal itemization? And how much does Jhin's item competition distort Xayah's Necessity rankings?

## Chapter 1: Stargazer Effect on Comp Performance

Queried Xayah comp (`xayah` in compositions.py) crossed with each Stargazer (3+ units):

| Stargazer | Games | AVP | Top4% | Nec (as trait) |
|---|---|---|---|---|
| Serpent | 53,314 | 3.85 | 61.1% | **+0.075** |
| Wolf | 50,243 | 3.94 | 59.0% | +0.056 |
| Shield | 54,922 | 4.08 | 56.6% | +0.041 |
| Huntress | 46,310 | 4.35 | 51.3% | -0.003 |
| Medallion | 33,500 | 4.59 | 46.9% | -0.024 |
| Fountain | 37,110 | 4.75 | 44.1% | -0.043 |
| Mountain | 7,232 | 6.66 | 11.4% | -0.043 |

Baseline (no Stargazer filter): 395k games, AVP 4.33.

Serpent and Wolf are clearly the best Stargazer effects for Xayah. Mountain only 7k games at AVP 6.66 — data unreliable (likely a patch/API change since previous analysis showed 63k games).

## Chapter 2: Item Necessity Across Stargazers (Normal Items Only)

Excluded artifact/radiant/trait/emblem items at API level (`unit_itemtype_counts`) and Anima Squad items via regex (`item=!TFT17_AnimaSquadItem_.*`). Using `unit_items_unique` endpoint which deduplicates item variants.

Mountain excluded from analysis — insufficient data (3,333 games after normal-only filter).

Top items by average Necessity across 6 Stargazers:

| Item | Serpent | Wolf | Shield | Huntress | Medallion | Fountain |
|---|---|---|---|---|---|---|
| Kraken's Fury | +.254(#1) | +.211(#1) | +.293(#1) | +.256(#1) | +.173(#1) | +.182(#1) |
| Red Buff | +.056(#2) | +.085(#2) | +.062(#2) | +.053(#2) | +.047(#2) | +.060(#2) |
| Last Whisper | +.015(#3) | +.015(#4) | +.008(#4) | +.021(#3) | +.030(#3) | +.021(#3) |
| Deathblade | -.016(#34) | -.020(#41) | +.008(#3) | +.004(#4) | -.004(#29) | +.003(#6) |
| Giant Slayer | -.018(#35) | -.002(#31) | -.026(#37) | -.006(#32) | -.031(#36) | -.019(#37) |
| Guinsoo's | -.001(#21) | +.058(#3) | -.093(#38) | -.132(#37) | -.075(#37) | -.135(#38) |
| Striker's Flail | -.012(#33) | -.008(#39) | -.012(#35) | -.012(#35) | -.014(#34) | -.010(#35) |
| Infinity Edge | -.126(#36) | -.188(#42) | -.199(#39) | -.188(#38) | -.154(#38) | -.169(#39) |

### Key Observations

1. **Top 3 (Kraken/Red Buff/LW) stable across all Stargazers** — no need to change core items based on Stargazer type.
2. **Guinsoo's divergence**: Wolf +.058(#3) vs Huntress -.132(#37) and Fountain -.135(#38). Only positive in Wolf and near-zero in Serpent.
3. **Deathblade** mildly positive only in Shield(#3)/Huntress(#4)/Fountain(#6).
4. **Infinity Edge** strongly negative everywhere (before conflict recompute).

## Chapter 3: Conflict Recompute (Precise Per-Item Jhin Filter)

Jhin appears in 73% of Xayah comp games and competes for IE, Giant Slayer, and Last Whisper.

**Method**: For each conflicting item, filter for games where Jhin ALSO carries that specific item using positive `unit_item_unique`:

```python
Item('TFT_Item_InfinityEdge', carrier_unit_id='TFT17_Jhin')
```

This is the **precise** method — it guarantees Jhin has the contested item, so Xayah's Necessity for that item reflects true value without competition bias. Previously this returned 0 games (`unit_item` endpoint); now works via `unit_item_unique` endpoint.

### Results

| Item | Stargazer | Original | Recomputed | Games | Verdict |
|---|---|---|---|---|---|
| **Infinity Edge** | Medallion | -.154(#38) | **+.038(#1)** | 6,012 | Major flip — IE best item when Jhin has IE too |
| | Serpent | -.127(#36) | -.003(#26) | 12,342 | Near zero (was strongly negative) |
| | Wolf | -.188(#42) | -.015(#35) | 11,620 | Still negative but much less |
| | Shield | -.199(#39) | -.011(#30) | 11,460 | Still negative but much less |
| | Huntress | -.188(#38) | -.041(#33) | 8,865 | Reduced but still clearly negative |
| | Fountain | -.168(#39) | -.012(#30) | 6,441 | Still negative but much less |
| **Giant Slayer** | all | -.001 to -.031 | -.004 to -.046 | 2.7k-5.5k | No improvement; GS bias is NOT from Jhin |
| **Last Whisper** | all | +.008 to +.030 | -.008 to +.006 | 2.0k-4.3k | **Gets worse** — original LW positivity was partly from Jhin correlation |

### Interpretation

1. **IE in Medallion is the only true flip** (+.038 #1). In all other Stargazers, IE remains negative even after precise recompute. This is a major correction from the previous approximate method, which showed IE flipping positive in Serpent/Fountain too.

2. **Previous approximate method overestimated the recompute effect.** `Unit('TFT17_Jhin', item_min=3)` (Jhin has any 3 items) introduced systematic upward bias because "Jhin full" ≠ "Jhin has this specific item." The approximate filter selected for stronger teams generally, not just for resolved item competition.

3. **Last Whisper's original positive Necessity was partly a Jhin-correlation artifact.** When we control for Jhin carrying LW, Xayah's LW Necessity drops to near zero. This suggests LW's apparent value came from games where Jhin prioritized LW (indicating an already-strong AD comp), not from LW being inherently good on Xayah.

4. **Giant Slayer is genuinely weak on Xayah.** Recompute makes it slightly worse, confirming the negative Necessity is not from Jhin competition.

### Methodological Lesson

The approximate conflict recompute (`Unit(carry, item_min=3)`) is **not a valid substitute** for precise per-item recompute (`Item(item_id, carrier=carry)`). The approximate method:
- Overstates improvement for items with genuine competition (IE)
- Misses that some items benefit from correlation, not despite competition (LW)
- Should be deprecated now that `unit_item_unique` supports positive filters

## What I Learned

1. **Xayah's core itemization is Stargazer-independent**: Kraken's Fury > Red Buff > Last Whisper in all 6 types (Mountain excluded — data unreliable).
2. **Guinsoo's is the only item that truly changes by Stargazer**: positive only in Wolf (#3), near-zero in Serpent, strongly negative in all others.
3. **IE is only situationally redeemable** — precise conflict recompute shows it flips to #1 only in Medallion. Previous approximate method was too optimistic.
4. **Last Whisper's value is partly a Jhin-correlation artifact** — a surprising finding from precise recompute.
5. **Approximate conflict recompute is systematically biased** — the most important methodological lesson. Now that `unit_item_unique` works for positive filters, always use the precise method.

## Open Questions

- What mechanic makes Guinsoo's positive in Wolf but negative in Huntress/Fountain?
- Is LW's Jhin-correlation artifact seen in other dual-carry comps?
- Mountain Stargazer data collapsed (7k games, AVP 6.66) — patch change or API issue?

## Questions for Xing

- The approximate conflict recompute was systematically upward-biased. Should we add a warning to the debiasing methods page about this?
- LW's drop after precise recompute is surprising — is "correlation artifact" the right framing, or is there another explanation?
- Mountain data is broken in current patch. Should we remove it or keep it marked as unreliable?

## Review

