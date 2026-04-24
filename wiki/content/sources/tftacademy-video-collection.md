# Source: TFTAcademy — Video Collection (7 Videos)
**Type**: YouTube video transcripts (podcast / guide)
**Authors**: Dishsoap + Frodan (hosts), guests vary
**Channel**: https://www.youtube.com/@TFTAcademyy
**Ingested**: 2026-04-24

TFTAcademy is a podcast-style channel by Dishsoap (high-Challenger analyst) and Frodan (caster/educator). Study Hall episodes are ~1hr discussions; standalone guides are 15-30min. 7 videos studied, grouped by stat relevance.

---

## Theme 1: Using Stats to Climb

### "Patch 13.7 & How to Climb with Stats" (RjZ58unIe_0)

The most stat-relevant TFTAcademy episode. Dishsoap walks through his actual workflow for using MetaTFT/Tactics.tools.

**Dishsoap's analysis workflow**:
1. Look at **unit AVP first**, not individual items
2. Filter by **player rank** (GM+ for optimized builds)
3. Sort by **Delta** as initial direction, but immediately check **play rate**
4. High play rate + positive Delta = real signal. Low play rate + high Delta = carousel bias.
5. Compare **item combos** not single items — single-item stats are polluted by carousel/secondary carry effects

**Key rules (Dishsoap)**:
- **Sample size thresholds**: 1000 games (mature patch), 300 games (new patch) — same as morbrid's numbers
- **Region filtering matters**: Korea meta ≠ NA meta. Different regions have different preferences.
- **Stats are a question-asking tool, not an answer tool** — data raises questions, game knowledge answers them

**Carousel bias mechanism (detailed)**:
- Late-game carousel items appear on boards of players who already survived → inflated AVP
- These players pick first on carousel (higher HP = later pick in some sets, earlier in others depending on mechanic)
- Low play rate items are disproportionately from carousel → bias is strongest for rare items

**Three-tier stat usage framework**:
- **Gold-Plat**: Follow guides, use basic explorer
- **Diamond-Master**: Learn sample size filtering, check play rate alongside Delta, compare combos
- **GM+**: Use Advanced Explorer with region/rank filters, understand bias mechanisms, use stats to ask questions not find answers

### "You're Building Items Wrong!" (7D1Fj883120)

**Item economy math**:
- Total components per game: 11-15
- Each stage adds 1 unique component to the "component bag"
- Carousel draws from separate pool (not the bag) → higher duplicate rate from carousel

**Hidden item formula (multiplicative model)**:
```
Tank effectiveness = HP × Resist × Damage Reduction
Physical DPS = Attack Speed × AD × Damage Modifier
Magic DPS = Cast Speed × AP × Damage Modifier

Rule: pick one from each column → multiplicative, not additive
```

This means: two items from the same column (e.g., two AS items) give diminishing returns. One from each column gives multiplicative scaling. This is a parametric framework that complements Necessity rankings.

**Stat analysis warnings**:
- Item Delta high ≠ item is good → could be Stage 5-6 carousel survivorship bias
- Must check play rate + Delta together
- 3-star unit item data is nearly always misleading → reaching 3-star already means you won

### "Your Augment Choice Is Losing You LP!" (0fm9AKfIlH8)

**Augment evaluation framework (Dishsoap's checklist)**:
1. Do I have an econ engine? (can I reach the level I need?)
2. Are my items complete? (carry + tank equipped?)
3. Do I have utility items? (anti-heal, shred?)
4. If all 3 → take combat augment. Otherwise → fill the gap.

**Direction as hidden value**: A clear direction (knowing your comp early) saves ~10-15g in wasted bench units over a game. Augments that give direction are worth more than their raw power suggests.

**Stat limitation**: Augment performance data can't distinguish between "this augment is strong" and "this augment is only taken when already winning." Same survivorship bias as items, but harder to correct because augments aren't acquired from carousel.

---

## Theme 2: Decision Frameworks (Stat-Related)

### "Line Selection and How to Think like a Pro!" (rhC-tO6obXE)

**Line ≠ Comp**: A comp is a destination; a line is the path to get there. Multiple lines can lead to the same comp.

**Comp tier list factors (stat-relevant)**:
- **Raw power**: AVP and win rate
- **Consistency**: Top 4 rate vs bottom 4 rate (not just win rate)
- **Flexibility**: How few conditions are needed (fewer = stronger)

This maps to our analysis: a comp with high AVP but high bottom-4 rate is risky (high variance). A comp with moderate AVP but very low bottom-4 rate is consistent.

**Five-scan framework (every game)**:
1. What is the patch encouraging? (→ meta read from stats)
2. What are my items telling me? (→ component analysis)
3. What is my board telling me? (→ win/loss/even)
4. What are my augments telling me? (→ direction)
5. What is the lobby telling me? (→ contestation)

**Contestation impact**: Dishsoap notes that contested comps lose AVP proportionally. If 3 players contest the same comp, expected placement shifts by ~0.5-1.0 places. This is a measurable effect in our data — filtering by lobby competition could reveal this.

### "When to Stay 8 vs Go 9" (ia1Lki3YSf8)

**HP as hidden currency**: Fast 9 requires an HP buffer. Below 50 HP at 4-1, fast 9 is rarely correct — the risk of dying before rolling is too high.

**Key data insight**: "Playing to 9" ≠ "fast 9." You can reach level 9 by playing strong 4-cost boards at 8, stabilizing, then leveling when safe. Stats that compare "level 9 games" lump together fast-9-with-HP and desperate-9-at-20-HP — very different game states.

---

## Appendix: Game Knowledge (Not Directly Stat-Related)

### "Your Econ Is Holding You Back!" (VnwiiG4Ke_I)

- Gold compounds: 1 extra gold/round × 25 rounds = 25g total = more than a gold augment
- Interest breakpoints: hitting 10/20/30/40/50 gold thresholds 1 round earlier compounds over the entire game
- Six econ-killing behaviors: rolling to 0, over-contesting, losing win streaks early, non-interval leveling, holding expensive units, upgrading unnecessary units
- **1 gold ≈ 3 HP** (same rule as Aesah's estimate)

### "How to Optimize Encounters" (eDwX8wv0bl8)

- Patch balance discussion (15.7b rated best of set because Mech was removed)
- Rocket Grab + Darius interaction: 20% base HP shield per proc → 8-9k shields/fight without tank items
- Poppy 3-star is weakest 4-cost 3-star (58% win rate vs 70%+ for others)

---

## Cross-Cutting Insights

### 1. Stats as Questions, Not Answers
Both Dishsoap and Frodan repeatedly emphasize: data should make you ask "why does this look this way?" — not tell you what to build. This is the same philosophy as Aesah's "data is a tool, not truth."

### 2. Play Rate is the Missing Dimension
Every stat discussion returns to play rate. High play rate + good performance = real signal. Low play rate + good performance = investigate for bias. This aligns exactly with our Necessity metric (play rate weighting).

### 3. Multiplicative Item Model
The hidden item formula (HP × Resist × DmgReduction for tanks; AS × AD × Modifier for carries) explains why diversified item builds outperform stacking. This is a parametric framework that can predict which 3-item builds should perform best — testable against our build analysis data.

### 4. Consistency > Raw Power
Dishsoap consistently evaluates comps by consistency (low bottom-4 rate) over raw AVP. This suggests our analyses should report both AVP and bottom-4 rate, not just AVP alone.

---

## Wiki Pages Updated
- This file is a new source document
- Related: [[sources/dishsoap-frodan-stats]] (earlier Dishsoap content)
