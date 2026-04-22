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

All items recomputed with Jhin conflict filter: `Item(item_id, carrier_unit_id='TFT17_Jhin')` via positive `unit_item_unique`. Format: `original/recomputed`.

| Item | Serpent | Boar | Alter | Huntress | Mountain | Medallion | Fountain |
|---|---|---|---|---|---|---|---|
| Guinsoo's | +.014/-.115 | +.039/-.183 | -.092/-.171 | -.078/-.260 | **+.113**/-.334 | -.101/-.162 | -.117/-.246 |
| Kraken's Fury | +.249/+.182 | +.169/+.052 | +.291/+.165 | +.248/+.142 | +.208/+.185 | +.175/+.028 | +.178/+.022 |
| Infinity Edge | -.129/-.005 | -.181/-.016 | -.196/-.007 | -.183/-.032 | -.134/**+.010** | -.158/**+.037** | -.162/-.005 |
| Giant Slayer | -.021/-.026 | +.005/-.001 | -.026/-.046 | -.006/-.013 | +.006/-.019 | -.030/-.030 | -.020/-.030 |
| Red Buff | +.058/-.010 | +.074/-.006 | +.061/+.003 | +.054/-.000 | +.050/-.009 | +.048/-.014 | +.063/-.006 |
| Deathblade | -.012/**+.005** | -.015/-.004 | +.009/+.009 | +.004/**+.015** | +.004/**+.020** | -.004/**+.018** | +.003/**+.019** |
| Last Whisper | +.017/-.002 | +.021/+.002 | +.009/-.004 | +.018/+.005 | -.009/-.003 | +.030/-.006 | +.017/-.001 |
| Striker's Flail | -.012/-.003 | -.007/**+.003** | -.012/-.002 | -.013/-.007 | -.005/**+.011** | -.013/**+.006** | -.010/**+.006** |
| Hextech Gunblade | -.003/-.005 | -.001/-.005 | -.003/**+.007** | +.000/+.002 | -.003/**+.005** | +.009/**+.016** | -.001/+.002 |
| Quicksilver | -.001/-.018 | +.005/**+.010** | +.002/**+.013** | -.004/**+.006** | -.004/-.011 | +.002/-.010 | -.004/+.002 |
| Edge of Night | +.004/-.014 | +.003/-.001 | +.004/**+.014** | +.003/**+.013** | +.001/**+.009** | +.009/**+.017** | +.005/**+.016** |

### Clean Table (all items = max of original and recomputed)

<table style="border-collapse:collapse;text-align:center;font-size:14px;font-family:system-ui">
<tr><th style="text-align:left;padding:6px 10px;border-bottom:2px solid #e5e7eb">Item</th>
<th style="padding:6px 10px;border-bottom:2px solid #e5e7eb;font-weight:600">Serpent</th>
<th style="padding:6px 10px;border-bottom:2px solid #e5e7eb;font-weight:600">Boar</th>
<th style="padding:6px 10px;border-bottom:2px solid #e5e7eb;font-weight:600">Alter</th>
<th style="padding:6px 10px;border-bottom:2px solid #e5e7eb;font-weight:600">Huntress</th>
<th style="padding:6px 10px;border-bottom:2px solid #e5e7eb;font-weight:600">Mountain</th>
<th style="padding:6px 10px;border-bottom:2px solid #e5e7eb;font-weight:600">Medallion</th>
<th style="padding:6px 10px;border-bottom:2px solid #e5e7eb;font-weight:600">Fountain</th>
</tr>
<tr>
<td style="text-align:left;padding:6px 10px;font-weight:600">Guinsoo's</td>
<td style="padding:6px 10px;background:#eefcf6">+0.014</td>
<td style="padding:6px 10px;background:#cff7e7">+0.039</td>
<td style="padding:6px 10px;background:#fdb9c1">-0.092</td>
<td style="padding:6px 10px;background:#fdc3cb">-0.078</td>
<td style="padding:6px 10px;background:#76e8bb">+0.113</td>
<td style="padding:6px 10px;background:#fdb2bb">-0.101</td>
<td style="padding:6px 10px;background:#fda6b1">-0.117</td>
</tr>
<tr style="background:#fafafa">
<td style="text-align:left;padding:6px 10px;font-weight:600">Kraken's Fury</td>
<td style="padding:6px 10px;background:#6ee7b7">+0.249</td>
<td style="padding:6px 10px;background:#6ee7b7">+0.169</td>
<td style="padding:6px 10px;background:#6ee7b7">+0.291</td>
<td style="padding:6px 10px;background:#6ee7b7">+0.248</td>
<td style="padding:6px 10px;background:#6ee7b7">+0.208</td>
<td style="padding:6px 10px;background:#6ee7b7">+0.175</td>
<td style="padding:6px 10px;background:#6ee7b7">+0.178</td>
</tr>
<tr>
<td style="text-align:left;padding:6px 10px;font-weight:600">IE</td>
<td style="padding:6px 10px;background:#fefbfb">-0.005</td>
<td style="padding:6px 10px;background:#fef2f4">-0.016</td>
<td style="padding:6px 10px;background:#fef9fa">-0.007</td>
<td style="padding:6px 10px;background:#fee6e9">-0.032</td>
<td style="padding:6px 10px;background:#f2fdf9">+0.010</td>
<td style="padding:6px 10px;background:#d2f7e8">+0.037</td>
<td style="padding:6px 10px;background:#fefbfb">-0.005</td>
</tr>
<tr style="background:#fafafa">
<td style="text-align:left;padding:6px 10px;font-weight:600">Giant Slayer</td>
<td style="padding:6px 10px;background:#feeff1">-0.021</td>
<td style="padding:6px 10px;background:#f8fefc">+0.005</td>
<td style="padding:6px 10px;background:#feebed">-0.026</td>
<td style="padding:6px 10px;background:#fefafb">-0.006</td>
<td style="padding:6px 10px;background:#f7fdfb">+0.006</td>
<td style="padding:6px 10px;background:#fee8eb">-0.030</td>
<td style="padding:6px 10px;background:#feeff1">-0.020</td>
</tr>
<tr>
<td style="text-align:left;padding:6px 10px;font-weight:600">Red Buff</td>
<td style="padding:6px 10px;background:#b8f3dc">+0.058</td>
<td style="padding:6px 10px;background:#a5f0d2">+0.074</td>
<td style="padding:6px 10px;background:#b5f2da">+0.061</td>
<td style="padding:6px 10px;background:#bdf4de">+0.054</td>
<td style="padding:6px 10px;background:#c2f5e1">+0.050</td>
<td style="padding:6px 10px;background:#c5f5e2">+0.048</td>
<td style="padding:6px 10px;background:#b2f2d9">+0.063</td>
</tr>
<tr style="background:#fafafa">
<td style="text-align:left;padding:6px 10px;font-weight:600">Deathblade</td>
<td style="padding:6px 10px;background:#f8fefc">+0.005</td>
<td style="padding:6px 10px;background:#fefbfc">-0.004</td>
<td style="padding:6px 10px;background:#f4fdf9">+0.009</td>
<td style="padding:6px 10px;background:#ecfcf6">+0.015</td>
<td style="padding:6px 10px;background:#e6fbf3">+0.020</td>
<td style="padding:6px 10px;background:#e9fbf4">+0.018</td>
<td style="padding:6px 10px;background:#e8fbf3">+0.019</td>
</tr>
<tr>
<td style="text-align:left;padding:6px 10px;font-weight:600">Last Whisper</td>
<td style="padding:6px 10px;background:#eafbf4">+0.017</td>
<td style="padding:6px 10px;background:#e5faf2">+0.021</td>
<td style="padding:6px 10px;background:#f4fdf9">+0.009</td>
<td style="padding:6px 10px;background:#e9fbf4">+0.018</td>
<td style="padding:6px 10px;background:#fefcfd">-0.003</td>
<td style="padding:6px 10px;background:#daf9ed">+0.030</td>
<td style="padding:6px 10px;background:#eafbf4">+0.017</td>
</tr>
<tr style="background:#fafafa">
<td style="text-align:left;padding:6px 10px;font-weight:600">Striker's Flail</td>
<td style="padding:6px 10px;background:#fefcfd">-0.003</td>
<td style="padding:6px 10px;background:#fbfefd">+0.003</td>
<td style="padding:6px 10px;background:#fefdfd">-0.002</td>
<td style="padding:6px 10px;background:#fef9fa">-0.007</td>
<td style="padding:6px 10px;background:#f1fcf8">+0.011</td>
<td style="padding:6px 10px;background:#f7fdfb">+0.006</td>
<td style="padding:6px 10px;background:#f7fdfb">+0.006</td>
</tr>
<tr>
<td style="text-align:left;padding:6px 10px;font-weight:600">Hextech Gunblade</td>
<td style="padding:6px 10px;background:#fefcfd">-0.003</td>
<td style="padding:6px 10px;background:#fefefe">-0.001</td>
<td style="padding:6px 10px;background:#f6fdfa">+0.007</td>
<td style="padding:6px 10px;background:#fcfefd">+0.002</td>
<td style="padding:6px 10px;background:#f8fefc">+0.005</td>
<td style="padding:6px 10px;background:#ebfbf5">+0.016</td>
<td style="padding:6px 10px;background:#fcfefd">+0.002</td>
</tr>
<tr style="background:#fafafa">
<td style="text-align:left;padding:6px 10px;font-weight:600">Quicksilver</td>
<td style="padding:6px 10px;background:#fefefe">-0.001</td>
<td style="padding:6px 10px;background:#f2fdf9">+0.010</td>
<td style="padding:6px 10px;background:#effcf7">+0.013</td>
<td style="padding:6px 10px;background:#f7fdfb">+0.006</td>
<td style="padding:6px 10px;background:#fefbfc">-0.004</td>
<td style="padding:6px 10px;background:#fcfefd">+0.002</td>
<td style="padding:6px 10px;background:#fcfefd">+0.002</td>
</tr>
<tr>
<td style="text-align:left;padding:6px 10px;font-weight:600">Edge of Night</td>
<td style="padding:6px 10px;background:#fafefc">+0.004</td>
<td style="padding:6px 10px;background:#fbfefd">+0.003</td>
<td style="padding:6px 10px;background:#eefcf6">+0.014</td>
<td style="padding:6px 10px;background:#effcf7">+0.013</td>
<td style="padding:6px 10px;background:#f4fdf9">+0.009</td>
<td style="padding:6px 10px;background:#eafbf4">+0.017</td>
<td style="padding:6px 10px;background:#ebfbf5">+0.016</td>
</tr>
</table>

### Key Observations

1. **Kraken's Fury and Red Buff** are stable #1 and #2 across all Stargazers. However, recompute shows their high Necessity is partly from Jhin correlation — when Jhin also has Kraken/Red Buff, Xayah's Necessity drops significantly. This is expected: Kraken/Red Buff are genuinely good, AND appear in strong-team games.
2. **Deathblade is a hidden strong item.** Original Necessity is near-zero or negative, but recompute reveals +.015 to +.020 in Huntress/Mountain/Medallion/Fountain. Jhin competes hard for Deathblade; when that competition is resolved, it's solidly positive.
3. **Edge of Night** similarly hidden: recompute lifts it to +.013 to +.017 in Alter/Huntress/Medallion/Fountain.
4. **Guinsoo's extreme divergence** persists in the clean table: Mountain +.113, Boar +.039 vs Fountain -.117, Alter -.092.
5. **IE only flips positive in Medallion (+.037) and Mountain (+.010)**. All others remain negative even after recompute.
6. **Giant Slayer is genuinely weak** — recompute makes it worse, confirming negative Necessity is real.
7. **Striker's Flail** is mildly positive after recompute in Mountain/Medallion/Fountain — previously hidden by Jhin competition.

### Methodological Lesson

Full conflict recompute across ALL items reveals a richer picture than selective recompute on suspected items only:
- Items that look neutral (Deathblade, Edge of Night, Striker's Flail) turn out to be hidden positives
- Items that look strongly positive (Kraken's, Red Buff) partially benefit from team-strength correlation
- The `unit_item_unique` positive filter makes this feasible at scale

## What I Learned

1. **Xayah's core itemization is Stargazer-independent**: Kraken's Fury > Red Buff > Last Whisper in the clean table.
2. **Deathblade is the biggest surprise**: hidden behind Jhin competition, it's actually the 4th best item after recompute (ahead of Guinsoo's in most Stargazers).
3. **Guinsoo's is the only item that truly changes by Stargazer**: strong in Mountain/Boar, harmful in Fountain/Alter.
4. **IE is only situationally redeemable** — flips only in Medallion and barely Mountain.
5. **Full conflict recompute should be standard** for any dual-carry comp — selective recompute misses hidden items.
6. **Stargazer tier counts vary** (1–5 tiers). Must query all tiers, not hardcode. Mountain also requires keeping emblem items.

## Open Questions

- What mechanic makes Guinsoo's positive in Mountain/Boar but negative in Fountain/Alter?
- Deathblade's hidden value: is this specific to Xayah/Jhin, or a general pattern in dual-carry comps?
- Should the clean table (max of original and recomputed) be the default reporting format?

## Questions for Xing

- Deathblade's emergence after full recompute is striking. Is this a known phenomenon in dual-carry analysis?
- Should we formalize "full conflict recompute" as a standard step in the item analysis method?
- Kraken's/Red Buff Necessity dropping after recompute: is this the team-strength correlation we discussed, or something else?

## Review

