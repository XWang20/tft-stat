# Experiment: Xayah Stargazer Item Analysis
Status: 🧪 draft
Date: 2026-04-22
Module: 2, 7

## The Question

S17 Xayah comp can pair with 7 different Stargazer effects. Do different Stargazer types change Xayah's optimal itemization? And how much does Jhin's item competition distort Xayah's Necessity rankings?

## Chapter 1: Stargazer Effect on Comp Performance

Queried Xayah comp (`xayah` in compositions.py) crossed with each Stargazer (all tiers):

| Stargazer | Games | AVP | Top4% |
|---|---|---|---|
| Serpent | 57,691 | 3.88 | 60.7% |
| Boar | 61,439 | 3.97 | 58.4% |
| Alter | 55,045 | 4.08 | 56.6% |
| Huntress | 50,475 | 4.41 | 50.2% |
| Mountain | 48,729 | 4.57 | 47.0% |
| Medallion | 33,603 | 4.59 | 46.9% |
| Fountain | 39,330 | 4.78 | 43.5% |

Baseline (no Stargazer filter): 396k games, AVP 4.33.

Serpent and Boar are clearly the best Stargazer effects for Xayah. Fountain is the worst.

Note: each Stargazer has different numbers of trait tiers (Shield/Medallion=1, Serpent/Huntress=3, Boar=4, Mountain=5). All tiers included.

## Chapter 2: Item Necessity + Conflict Recompute

Excluded artifact/radiant/trait items at API level (`unit_itemtype_counts`) and Anima Squad items via regex. Mountain does NOT exclude emblem (Mountain grants emblems — excluding them kills the data). Using `unit_items_unique` endpoint.

For conflict items (IE/GS/LW), shows original Necessity and recomputed Necessity (after filtering for Jhin also carrying that specific item via positive `unit_item_unique`).

| Item | Serpent | Boar | Alter | Huntress | Mountain | Medallion | Fountain |
|---|---|---|---|---|---|---|---|
| Kraken's Fury | +.251 | +.170 | +.292 | +.249 | +.208 | +.174 | +.179 |
| Red Buff | +.056 | +.075 | +.062 | +.054 | +.050 | +.048 | +.064 |
| Last Whisper | +.018/-.001 | +.021/+.002 | +.008/-.004 | +.018/+.004 | -.007/-.001 | +.031/-.009 | +.018/-.001 |
| Guinsoo's | +.005 | +.027 | -.107 | -.096 | **+.116** | -.078 | -.121 |
| Deathblade | -.013 | -.016 | +.009 | +.004 | +.005 | -.003 | +.004 |
| Giant Slayer | -.020/-.026 | +.004/-.000 | -.026/-.048 | -.006/-.013 | +.006/-.021 | -.032/-.030 | -.020/-.033 |
| Striker's Flail | -.014 | -.006 | -.012 | -.013 | -.006 | -.014 | -.011 |
| Infinity Edge | -.128/-.004 | -.181/-.016 | -.199/-.009 | -.185/-.033 | -.135/+.007 | -.157/**+.036** | -.165/-.007 |

Format: `original/recomputed` for conflict items. Recomputed = filtered for Jhin also carrying that specific item (positive `unit_item_unique`).

### Key Observations

1. **Top 2 (Kraken/Red Buff) stable across all Stargazers** — no need to change core items.
2. **Guinsoo's extreme divergence**: Mountain +.116 and Boar +.027 vs Fountain -.121 and Alter -.107.
3. **IE only flips positive after recompute in Medallion (+.036) and Mountain (+.007)**. All others remain negative. Previous approximate method (`Unit(Jhin, item_min=3)`) overstated this — showed IE flipping in 3+ Stargazers.
4. **Last Whisper's positive Necessity is mostly a Jhin-correlation artifact**. After precise recompute, drops to near-zero or negative everywhere. LW looked good because Jhin-with-LW games = strong AD comps overall, not because LW is inherently valuable on Xayah.
5. **Giant Slayer is genuinely weak** — recompute makes it worse, confirming negative Necessity is real, not from Jhin competition.

### Methodological Lesson

The approximate conflict recompute (`Unit(carry, item_min=3)`) is **not a valid substitute** for precise per-item recompute (`Item(item_id, carrier=carry)`). The approximate method selects for stronger teams generally, not just resolved item competition. Now that `unit_item_unique` supports positive filters, always use the precise method.

## What I Learned

1. **Xayah's core itemization is Stargazer-independent**: Kraken's Fury > Red Buff everywhere.
2. **Guinsoo's is the only item that truly changes by Stargazer**: strong in Mountain/Boar, harmful in Fountain/Alter.
3. **IE is only situationally redeemable** — precise conflict recompute shows it flips only in Medallion. Previous approximate method was too optimistic.
4. **Last Whisper's value is partly a Jhin-correlation artifact** — surprising finding from precise recompute.
5. **Approximate conflict recompute is systematically biased** — most important methodological lesson.
6. **Stargazer tier counts vary** (1–5 tiers). Must query all tiers, not hardcode tier 1. Mountain also requires keeping emblem items.

## Open Questions

- What mechanic makes Guinsoo's positive in Mountain/Boar but negative in Fountain/Alter?
- Is LW's Jhin-correlation artifact seen in other dual-carry comps?
- Should conflict recompute be standard practice for all dual-carry comps?

## Questions for Xing

- LW's drop after precise recompute is surprising — is "correlation artifact" the right framing, or is there another explanation?
- The approximate conflict recompute was systematically biased. Should we add a stronger warning to the methods page?
- Mountain Guinsoo's +.116 is the strongest non-Kraken item anywhere. Worth investigating?

## Review

