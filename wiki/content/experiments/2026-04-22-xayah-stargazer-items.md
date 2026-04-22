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

<table style="border-collapse:collapse;text-align:center;font-size:14px">
<tr style="background:#f0f0f0"><th style="text-align:left;padding:4px 8px">Item</th>
<th style="padding:4px 8px">Serpent</th>
<th style="padding:4px 8px">Boar</th>
<th style="padding:4px 8px">Alter</th>
<th style="padding:4px 8px">Huntress</th>
<th style="padding:4px 8px">Mountain</th>
<th style="padding:4px 8px">Medallion</th>
<th style="padding:4px 8px">Fountain</th>
</tr>
<tr><td style="text-align:left;padding:4px 8px;font-weight:bold">Guinsoo's</td>
<td style="padding:4px 8px;background:rgb(211,240,211)">+0.014</td>
<td style="padding:4px 8px;background:rgb(194,240,194)">+0.039</td>
<td style="padding:4px 8px;background:rgb(255,171,171)">-0.092</td>
<td style="padding:4px 8px;background:rgb(255,179,179)">-0.078</td>
<td style="padding:4px 8px;background:rgb(145,240,145)">+0.113</td>
<td style="padding:4px 8px;background:rgb(255,167,167)">-0.101</td>
<td style="padding:4px 8px;background:rgb(255,158,158)">-0.117</td>
</tr>
<tr><td style="text-align:left;padding:4px 8px;font-weight:bold">Kraken's Fury</td>
<td style="padding:4px 8px;background:rgb(120,240,120)">+0.249</td>
<td style="padding:4px 8px;background:rgb(120,240,120)">+0.169</td>
<td style="padding:4px 8px;background:rgb(120,240,120)">+0.291</td>
<td style="padding:4px 8px;background:rgb(120,240,120)">+0.248</td>
<td style="padding:4px 8px;background:rgb(120,240,120)">+0.208</td>
<td style="padding:4px 8px;background:rgb(120,240,120)">+0.175</td>
<td style="padding:4px 8px;background:rgb(120,240,120)">+0.178</td>
</tr>
<tr><td style="text-align:left;padding:4px 8px;font-weight:bold">IE</td>
<td style="padding:4px 8px;background:rgb(255,218,218)">-0.005</td>
<td style="padding:4px 8px;background:rgb(255,212,212)">-0.016</td>
<td style="padding:4px 8px;background:rgb(255,217,217)">-0.007</td>
<td style="padding:4px 8px;background:rgb(255,203,203)">-0.032</td>
<td style="padding:4px 8px;background:rgb(214,240,214)">+0.010</td>
<td style="padding:4px 8px;background:rgb(196,240,196)">+0.037</td>
<td style="padding:4px 8px;background:rgb(255,218,218)">-0.005</td>
</tr>
<tr><td style="text-align:left;padding:4px 8px;font-weight:bold">Giant Slayer</td>
<td style="padding:4px 8px;background:rgb(255,209,209)">-0.021</td>
<td style="padding:4px 8px;background:rgb(217,240,217)">+0.005</td>
<td style="padding:4px 8px;background:rgb(255,207,207)">-0.026</td>
<td style="padding:4px 8px;background:rgb(255,217,217)">-0.006</td>
<td style="padding:4px 8px;background:rgb(216,240,216)">+0.006</td>
<td style="padding:4px 8px;background:rgb(255,204,204)">-0.030</td>
<td style="padding:4px 8px;background:rgb(255,210,210)">-0.020</td>
</tr>
<tr><td style="text-align:left;padding:4px 8px;font-weight:bold">Red Buff</td>
<td style="padding:4px 8px;background:rgb(182,240,182)">+0.058</td>
<td style="padding:4px 8px;background:rgb(171,240,171)">+0.074</td>
<td style="padding:4px 8px;background:rgb(180,240,180)">+0.061</td>
<td style="padding:4px 8px;background:rgb(184,240,184)">+0.054</td>
<td style="padding:4px 8px;background:rgb(187,240,187)">+0.050</td>
<td style="padding:4px 8px;background:rgb(188,240,188)">+0.048</td>
<td style="padding:4px 8px;background:rgb(178,240,178)">+0.063</td>
</tr>
<tr><td style="text-align:left;padding:4px 8px;font-weight:bold">Deathblade</td>
<td style="padding:4px 8px;background:rgb(217,240,217)">+0.005</td>
<td style="padding:4px 8px;background:rgb(255,218,218)">-0.004</td>
<td style="padding:4px 8px;background:rgb(214,240,214)">+0.009</td>
<td style="padding:4px 8px;background:rgb(210,240,210)">+0.015</td>
<td style="padding:4px 8px;background:rgb(207,240,207)">+0.020</td>
<td style="padding:4px 8px;background:rgb(208,240,208)">+0.018</td>
<td style="padding:4px 8px;background:rgb(208,240,208)">+0.019</td>
</tr>
<tr><td style="text-align:left;padding:4px 8px;font-weight:bold">Last Whisper</td>
<td style="padding:4px 8px;background:rgb(209,240,209)">+0.017</td>
<td style="padding:4px 8px;background:rgb(206,240,206)">+0.021</td>
<td style="padding:4px 8px;background:rgb(214,240,214)">+0.009</td>
<td style="padding:4px 8px;background:rgb(208,240,208)">+0.018</td>
<td style="padding:4px 8px;background:rgb(255,219,219)">-0.003</td>
<td style="padding:4px 8px;background:rgb(200,240,200)">+0.030</td>
<td style="padding:4px 8px;background:rgb(209,240,209)">+0.017</td>
</tr>
<tr><td style="text-align:left;padding:4px 8px;font-weight:bold">Striker's Flail</td>
<td style="padding:4px 8px;background:rgb(255,219,219)">-0.003</td>
<td style="padding:4px 8px;background:rgb(218,240,218)">+0.003</td>
<td style="padding:4px 8px;background:rgb(255,219,219)">-0.002</td>
<td style="padding:4px 8px;background:rgb(255,217,217)">-0.007</td>
<td style="padding:4px 8px;background:rgb(213,240,213)">+0.011</td>
<td style="padding:4px 8px;background:rgb(216,240,216)">+0.006</td>
<td style="padding:4px 8px;background:rgb(216,240,216)">+0.006</td>
</tr>
<tr><td style="text-align:left;padding:4px 8px;font-weight:bold">Hextech Gunblade</td>
<td style="padding:4px 8px;background:rgb(255,219,219)">-0.003</td>
<td style="padding:4px 8px;background:rgb(255,220,220)">-0.001</td>
<td style="padding:4px 8px;background:rgb(216,240,216)">+0.007</td>
<td style="padding:4px 8px;background:rgb(219,240,219)">+0.002</td>
<td style="padding:4px 8px;background:rgb(217,240,217)">+0.005</td>
<td style="padding:4px 8px;background:rgb(210,240,210)">+0.016</td>
<td style="padding:4px 8px;background:rgb(219,240,219)">+0.002</td>
</tr>
<tr><td style="text-align:left;padding:4px 8px;font-weight:bold">Quicksilver</td>
<td style="padding:4px 8px;background:rgb(255,220,220)">-0.001</td>
<td style="padding:4px 8px;background:rgb(214,240,214)">+0.010</td>
<td style="padding:4px 8px;background:rgb(212,240,212)">+0.013</td>
<td style="padding:4px 8px;background:rgb(216,240,216)">+0.006</td>
<td style="padding:4px 8px;background:rgb(255,218,218)">-0.004</td>
<td style="padding:4px 8px;background:rgb(219,240,219)">+0.002</td>
<td style="padding:4px 8px;background:rgb(219,240,219)">+0.002</td>
</tr>
<tr><td style="text-align:left;padding:4px 8px;font-weight:bold">Edge of Night</td>
<td style="padding:4px 8px;background:rgb(218,240,218)">+0.004</td>
<td style="padding:4px 8px;background:rgb(218,240,218)">+0.003</td>
<td style="padding:4px 8px;background:rgb(211,240,211)">+0.014</td>
<td style="padding:4px 8px;background:rgb(212,240,212)">+0.013</td>
<td style="padding:4px 8px;background:rgb(214,240,214)">+0.009</td>
<td style="padding:4px 8px;background:rgb(209,240,209)">+0.017</td>
<td style="padding:4px 8px;background:rgb(210,240,210)">+0.016</td>
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

