# Build Analysis
**Status**: ✅ verified

## Why Builds > Single Items

Single-item stats are heavily polluted by carousel bias. If someone has a Guard Breaker on their Heimer, it's likely from a late-game carousel — they were already winning.

Looking at full builds (3-item combinations) filters this out because:
- Players actively craft these combinations
- The full build is present from mid-game, not just endgame
- Dishsoap: "look at item combos and full builds — that's going to knock out a lot of the bias"

## Methods

### Full Build Comparison
Compare complete 3-item sets using `unit_builds` endpoint.

```bash
python3 metatft_query.py items TFT17_Vex --or-units "..." --traits "..."
# Then separately query unit_builds for detailed build data
```

### Control Variable (Fix 2, Vary 1)
The most powerful single-item evaluation method:
1. Group all builds by pairs (e.g., Guinsoo + Giant Slayer)
2. For each pair, rank the 3rd item by AVP
3. Compare rankings across different pairs

### Consistency Check
The validation step:
- Does the same item rank similarly across different base pairs?
- If Red Buff is #1 with Guinsoo+GSlayer AND Guinsoo+Gunblade AND Guinsoo+JG... it's likely genuinely good
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

See [[experiments/vex-nova95]] for full details.

## Sources
- [[sources/dishsoap-frodan-stats]]: "Look at item combos and full builds"
- Mochi experiments (2026-04-21): Control variable + consistency check
