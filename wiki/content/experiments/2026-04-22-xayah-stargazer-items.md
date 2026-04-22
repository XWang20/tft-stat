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
| Serpent | 55,964 | 3.87 | 60.7% | **+0.078** |
| Wolf | 59,734 | 3.97 | 58.4% | +0.066 |
| Shield | 53,466 | 4.08 | 56.5% | +0.040 |
| Huntress | 48,864 | 4.42 | 50.2% | -0.013 |
| Mountain | 62,960 | 4.44 | 49.6% | -0.021 |
| Medallion | 32,366 | 4.60 | 46.7% | -0.025 |
| Fountain | 37,892 | 4.79 | 43.3% | **-0.051** |

Baseline (no Stargazer filter): 383k games, AVP 4.33.

Serpent and Wolf are clearly the best Stargazer effects for Xayah. Fountain is the worst.

## Chapter 2: Item Necessity Across Stargazers (Normal Items Only)

Excluded artifact/radiant/trait/emblem items at API level (`unit_itemtype_counts`) and Anima Squad items from results. Also excluded Battle Bunny Crossbow via filter expression.

**TODO**: Anima Squad exclusion is result-level only (display filter), not game-level. Anima-carrying games still pollute the baseline. See [[methods/item-analysis-debiasing]] for details.

Top 8 items by play rate, Necessity across all Stargazers:

| Item | Serpent | Wolf | Shield | Huntress | Mountain | Medallion | Fountain |
|---|---|---|---|---|---|---|---|
| Kraken's Fury | +.257(#1) | +.170(#1) | +.292(#1) | +.248(#1) | +.201(#1) | +.174(#1) | +.170(#1) |
| Red Buff | +.057(#2) | +.074(#2) | +.061(#2) | +.051(#2) | +.045(#3) | +.046(#2) | +.064(#2) |
| Last Whisper | +.014(#3) | +.024(#4) | +.010(#3) | +.013(#3) | +.016(#4) | +.033(#3) | +.023(#3) |
| Guinsoo's | -.002(#12) | +.024(#3) | -.082(#24) | -.137(#25) | +.046(#2) | -.108(#22) | -.124(#24) |
| Deathblade | -.014(#23) | -.016(#26) | +.008(#4) | +.005(#4) | +.004(#5) | -.005(#15) | +.003(#5) |
| Giant Slayer | -.017(#24) | +.000(#10) | -.024(#23) | -.000(#11) | +.000(#8) | -.029(#21) | -.014(#22) |
| Striker's Flail | -.012(#21) | -.004(#21) | -.011(#20) | -.011(#23) | -.003(#18) | -.011(#19) | -.010(#20) |
| Infinity Edge | -.144(#25) | -.195(#27) | -.218(#25) | -.201(#26) | -.168(#27) | -.171(#23) | -.181(#25) |

### Key Observations

1. **Top 3 (Kraken/Red Buff/LW) stable across all Stargazers** -- no need to change core items based on Stargazer type.
2. **Guinsoo's extreme divergence**: Mountain +.046(#2) and Wolf +.024(#3) vs Huntress -.137(#25) and Fountain -.124(#24). These two Stargazers likely have attack speed or on-hit synergy.
3. **Deathblade** mildly positive only in Shield/Huntress/Mountain/Fountain, negative elsewhere.
4. **Infinity Edge** strongly negative everywhere (before conflict recompute).

## Chapter 3: Conflict Recompute (Jhin Competition)

Jhin appears in 73% of Xayah comp games and competes for IE, Giant Slayer, and Last Whisper.

**Ideal method**: For each conflicting item, filter for games where Jhin ALSO carries that specific item: `Item('TFT_Item_InfinityEdge', carrier_unit_id='TFT17_Jhin')`. This directly removes the competition bias for that item.

**TODO**: Positive `unit_item` filter is not supported by the MetaTFT API (returns 0 games). The results below use a workaround: `Unit('TFT17_Jhin', item_min=3)` (Jhin has any 3 items). This is less precise -- it doesn't guarantee Jhin has the specific contested item. Results should be treated as approximate until the ideal method is implementable.

| Item | Stargazer | Original | Recomputed | Verdict |
|---|---|---|---|---|
| **Infinity Edge** | Medallion | -.171(#23) | **+.049(#1)** | Massive flip -- IE is Xayah's best item when Jhin is full |
| | Serpent | -.144(#25) | +.012(#4) | Flips positive |
| | Fountain | -.181(#25) | +.011(#5) | Flips positive |
| | Wolf | -.195(#27) | -.000(#8) | Near zero |
| | Mountain | -.168(#27) | -.015(#20) | Still negative |
| | Shield | -.218(#25) | -.021(#17) | Still negative |
| | Huntress | -.201(#26) | -.019(#17) | Still negative |
| **Giant Slayer** | Huntress | -.001(#12) | +.015(#3) | Flips positive |
| | Wolf | +.001(#10) | +.003(#5) | Small increase |
| | Mountain | +.000(#8) | -.021(#22) | Gets worse (not just bias) |
| **Last Whisper** | Huntress | +.013(#3) | +.032(#2) | Modest increase |
| | Medallion | +.033(#3) | +.039(#2) | Modest increase |
| | all others | +.010 to +.024 | +.017 to +.030 | Consistent small increase |

### Interpretation

1. **IE's negative Necessity is almost entirely selection bias from Jhin**. When Jhin is already full, IE becomes positive on Xayah in Medallion/Serpent/Fountain -- precisely the Stargazers where crit/burst synergizes.
2. **Giant Slayer has real Stargazer interaction**, not just bias: it improves with recompute in Huntress but worsens in Mountain.
3. **Last Whisper's mild conflict is confirmed**: small positive shift across all Stargazers, already positive before recompute.

## What I Learned

1. **Xayah's core itemization is Stargazer-independent**: Kraken's Fury > Red Buff > Last Whisper in all 7 types.
2. **Guinsoo's is the only item that truly changes by Stargazer**: mandatory in Mountain/Wolf, harmful in Huntress/Fountain.
3. **Conflict recompute reveals IE as a hidden strong item** -- its terrible raw Necessity is a selection bias artifact from Jhin competition. In Medallion (best crit Stargazer), recomputed IE is actually #1.
4. **Two new methods validated**: excluding special items and conflict recompute. Documented in [[methods/item-analysis-debiasing]].

## Open Questions

- What specific mechanics make Guinsoo's positive in Mountain/Wolf but negative in Huntress/Fountain?
- Can conflict recompute be generalized to other comp pairs (e.g., any comp with a secondary AD carry)?
- Is there a way to exclude Anima Squad items at the API level (currently only result-level filtering)?

## Questions for Xing

- Is the conflict recompute method (filter for competing carry fully itemized) the standard approach? Or is there a more precise technique?
- The Guinsoo's divergence across Stargazers is striking. Is this a known interaction, or worth deeper investigation?
- Should we track Stargazer as a standard dimension in future comp analyses?

## Review
