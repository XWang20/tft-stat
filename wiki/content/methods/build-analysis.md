# Build Analysis
**Status**: ✅ verified

## Why Builds > Single Items

Single-item stats are heavily polluted by carousel bias. If someone has a Guard Breaker on their Heimer, it's likely from a late-game carousel — they were already winning.

Looking at full builds (3-item combinations) filters this out because:
- Players actively craft these combinations
- The full build is present from mid-game, not just endgame
- Dishsoap: "look at item combos and full builds — that's going to knock out a lot of the bias"

## Methods

### Build Necessity

Compute Necessity at the build level rather than the single-item level:

1. Query all 3-item builds via `unit_builds` endpoint, filtered to the comp
2. Filter to builds with >=200 games (significance threshold)
3. Compute weighted-average AVP across all qualifying builds (= overall build AVP)
4. For each item X, compute weighted-average AVP of builds *containing* X
5. Derive `w/o_X_AVP` and apply: `Build_Necessity = w/o_AVP - overall_build_AVP`

Same formula as single-item Necessity, applied to the build population instead of the game population. Items appearing in ~100% of builds (e.g., Guinsoo on Vex) have undefined Build Necessity and must be excluded.

### Full Build Comparison
Compare complete 3-item sets using `unit_builds` endpoint.

```bash
python3 cli.py items TFT17_Vex --comp nova_95
# Then separately query unit_builds for detailed build data
```

### Control Variable (Fix 2, Vary 1)
The most powerful single-item evaluation method:
1. Group all builds by pairs (e.g., Guinsoo + Giant Slayer)
2. For each pair, rank the 3rd item by **Necessity within the pair** (not raw AVP)
3. Compare rankings across different pairs

**Why Necessity, not AVP**: Fixing two items and varying the third degenerates to single-item analysis within the subpopulation. Low-frequency third items have the same survivorship bias as single-item AVP. Compute Build Necessity within the fixed-pair subset:

```
p = games_with_X / total_pair_games
Build Necessity = p/(1-p) × (pair_baseline_AVP - X_AVP)
```

Example: in nova_95 GS+Guinsoo subset, Red Buff had the best raw AVP (3.58) but ranked #2 by Necessity (+0.017) behind Striker's Flail (+0.027), because Red Buff's 4.2% play rate limited its weighted impact.

### Consistency Check
The validation step — here, comparing AVP across base pairs is valid because you're using many builds to triangulate a single item's value, not ranking within a fixed pair:
- Does the same item rank similarly across different base pairs?
- If Dcap is #1 with Guinsoo+GSlayer AND Guinsoo+Gunblade AND Guinsoo+Flail... it's genuinely good
- If it's #1 in one pair but #5 in another, it's context-dependent

## Our Experiment Results (Vex in Nova 95)

Consistency check across 7-8 base pairs:
```
Red Buff    10.9% avg rank → ✅ Consistently strong
Dcap        17.4% → ✅ Consistently strong  
Flail       38.5% → ⚠️ Above average
Gunblade    63.7% → Average (despite being most popular)
JG          83.3% → ❌ Consistently weak
Void Staff  95.1% → ❌ Consistently weak
```

See [[experiments/2026-04-21-vex-nova95-items]] for full details.

## When Methods Disagree

Build Necessity and single-item Necessity largely agree (Spearman rho = 0.75-0.94 across three carries), but divergences are informative:

**Ceiling effect**: When a core item (e.g., Guinsoo at 88% play rate) appears in nearly 100% of builds, Build Necessity can't measure it — it hits a ceiling. This reshuffles rankings below: Hextech Gunblade rises from #3 (single-item) to #1 (build) on Vex because Guinsoo drops out of the comparison entirely.

**Thief's Gloves**: Rises in Build Necessity because it *is* a complete build. Single-item Necessity undervalues it since it can't capture the "3 random items" package effect.

**Sustain redundancy**: Bloodthirster drops from #3 to #5 on Fiora because it overlaps with Sterak's Gage (both sustain) — builds containing both don't gain much from doubling up.

**Top-N build counts are misleading**: Red Buff appears in 6/10 top Vex builds but ranks only #5 by Build Necessity. Infinity Edge appears in 2/10 top Graves builds but has *negative* Build Necessity. Frequency in top builds != marginal importance.

## Complementary Use

Single-item Necessity and build analysis answer different questions:

| Method | Question It Answers | Best For |
|---|---|---|
| **Single-item Necessity** | "What's most important to this comp?" | Prioritizing which items to slam early |
| **Build Necessity** | "Which items contribute most across all builds?" | Evaluating items when core is already decided |
| **Control variable** | "What's the best marginal item given my current two?" | Choosing the third item — **use Necessity within the pair, not raw AVP** |
| **Top build AVP** | "What do the best-performing boards look like?" | BIS reference (but beware survivorship bias on low-frequency builds) |
| **Consistency check** | "Is this item's strength robust across contexts?" | Triangulating item value across base pairs — AVP comparison is valid here |

In practice: use single-item Necessity to identify core items (slam Guinsoo first), then control variable analysis to pick the best third item given what you already have.

## Pitfalls

### JG Trap: Contamination by Strong Partners

An item can have negative tftable Necessity (the comp performs *worse* when it's present) but show misleadingly positive Build Necessity — because it appears in builds alongside strong partner items. The strong partners carry the build AVP, making JG look better than it is.

Detection: compare the item's single-item Necessity (negative = bad sign) with its Build Necessity. If Build Necessity is positive but single-item is negative, the build score is likely contaminated by partner item strength. Cross-validate with control variable analysis: if JG consistently ranks last when you fix two strong items and vary the third, it confirms the trap.

## Sources
- [[sources/dishsoap-frodan-stats]]: "Look at item combos and full builds"
- [[experiments/2026-04-21-vex-nova95-items]]: Control variable + consistency check
- [[experiments/2026-04-22-build-vs-single-necessity]]: Build Necessity vs single-item comparison across 3 carries
