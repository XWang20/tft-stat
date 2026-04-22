# Biases in TFT Statistics
**Status**: ✅ verified

## 1. Survivorship Bias

**The biggest, most persistent bias in TFT stats.**

Items from late-game carousels appear on endgame boards of players who survived to late game. Surviving to late game ≈ already winning. Therefore, these items get credited with good performance they didn't cause.

**Characteristics**:
- Play Rate and AVP are inversely correlated (morbrid: "constant bias, every item, every set")
- Affects every single item in every single set
- Cannot be fully corrected with confidence intervals (morbrid: "CI fixes sample size, not survivorship")

**Manifestations**:
- Low play rate items always look better than they are
- 5-cost units always top the AVP charts (you need to survive to field them)
- Secondary carry items look amazing (you only give them items when you're winning)

**Mitigations**:
- Use [[metrics|Necessity]] instead of raw AVP (play rate weighting)
- Use [[methods/build-analysis]] instead of single-item analysis
- Use [[methods/filter-strategy]] to exclude secondary carry games
- Use [[experiments/vex-nova95#supplementary-frequency-avp-regression]] to visually identify the bias curve

## 2. Player Behavior Bias

Players tend to build "consensus best" items, creating a self-fulfilling prophecy.

**Effects**:
- Popular items include many forced/suboptimal builds → AVP pulled up (looks worse)
- Unpopular items only built by knowledgeable players or in ideal situations → AVP pulled down (looks better)

**Mitigations**:
- Factor in play rate (Necessity handles this)
- Filter by high rank (GM+) for more optimized builds
- Filter by region for specific meta reads

## 3. Low Sample Size Noise

Basic statistics: fewer observations → higher variance → more outliers.

**Rules of thumb** (Dishsoap):
- Mature patch: ≥1000 games to trust
- New patch: ≥300 games minimum
- 4× games = 2× accuracy (SE ∝ 1/√n)

**Mitigations**:
- MetaTFT Advanced Mode: 95%/99% CI worst case sorting
- Multiple comparisons: more rows in table → more random outliers → use higher CI
- Don't overfilter: each filter reduces sample size

## Sources
- [[sources/morbrid-reddit-post]]: Comprehensive writeup on all three biases
- [[sources/morbrid-aesah-talk]]: "CI doesn't fix survivorship bias"
- [[sources/dishsoap-frodan-stats]]: Sample size rules of thumb
- [[sources/aesah-data-mistakes]]: Play rate as the key corrector
