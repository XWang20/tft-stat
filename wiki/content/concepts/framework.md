# Analysis Framework
**Status**: ✅ verified

## Stats Are Priors, Not Truths

**Stats tell you what works on average across 200k games. Your game is one game.** The fundamental gap between statistical analysis and TFT decision-making:

| | Statistical Analysis | In-Game Decision |
|---|---|---|
| **Scope** | Population average (200k games) | This specific game |
| **Timing** | Retrospective (endgame snapshots) | Real-time (evolving board state) |
| **Context** | Controlled by filter | Uncontrollable (opponents, shop RNG, HP) |
| **Output** | "Guinsoo is the most important item" | "Should I slam Guinsoo now with these components against this lobby?" |

Stats give you **priors** — default knowledge before the game starts. In-game context provides **updates** that can override the prior. The decision is the combination of both.

**Three layers of TFT knowledge**:

1. **Population priors (our domain)**: "In Nova 95, Guinsoo has +0.5 Necessity." This is what our pipeline produces. It's the starting point — what's true *on average* across all games.

2. **Conditional priors (partially our domain)**: "When playing for 1st vs top 4, itemization changes." "In contested lobbies, AVP shifts by 0.5-1.0." Stage-dependent value, contestation effects, econ state — these narrow the population prior toward your game state. Some of this we can measure (Aesah's filter-by-comp, Dishsoap's consistency metrics); some we can't (your specific HP/econ at 4-2).

3. **Real-time adaptation (not our domain)**: "My opponent just pivoted to the same comp — I should adjust." This requires game sense, not stats. No dataset captures this because it's specific to one lobby, one game, one moment.

**What this means for our work**: Our pipeline produces Layer 1 (population priors) and reaches into Layer 2 (conditional priors via filters, stage analysis, consistency metrics). We should never claim our analysis tells you what to do in a specific game — it tells you what's *generally* true, which is the foundation for in-game decisions.

**Prior quality varies with patch age**: Patch early → trust top players over data (sample size too small, meta unstable). Patch late → trust data over individuals (large sample, meta settled). Our pipeline is most valuable in the second half of a patch cycle. (morbrid + Aesah)

Aesah: *"Data is a tool, not truth."*
Dishsoap: *"Stats are a question-asking tool, not an answer tool."*

Both are saying the same thing: stats provide the prior, not the posterior.

## The Core Principle

**Your question determines everything.** The question you ask defines what variables to control (= filter), what granularity to use, and what metric to apply. A vague question produces vague results.

Good questions are **decision-oriented**: "Should I build Giant Slayer or JG on Vex in Nova 95?" — this maps directly to a specific filter (nova_95), granularity (single-item or builds), and metric (Necessity).

Bad questions are abstract: "What's the relationship between items and comps?" — no specific filter, no decision point, no actionable conclusion.

### Where Questions Come From

You don't play the game. Find questions from people who do:
1. **Community** (Reddit /r/CompetitiveTFT) — what players debate. Data can settle arguments.
2. **Top player match history** (`cli.py scout`) — what Challenger/GM players are building right now. New patterns, emerging comps, unusual builds.

## Three Orthogonal Dimensions

TFT stats analysis operates on three independent axes. Each can be set independently. Best results come from maximizing all three.

### Dimension 1: Filter Strategy (What games to include) — FOUNDATION

**Filter = controlling variables.** Every filter condition controls a confounding variable. The most important variable to control: **primary carry (主C) vs secondary (副C)** — itemization is completely different between these roles.

Your question determines which variables to control → filter is the implementation.

See [[methods/filter-strategy]].

### Dimension 2: Data Granularity (What to compare)

| Granularity | Method | Corrects |
|---|---|---|
| Single item | unit_items_unique | nothing |
| Two-item combo | pair analysis | partial carousel bias |
| Three-item build | unit_builds | most carousel bias |
| Control variable | fix 2, vary 1 | isolates single item contribution |
| Consistency check | cross-pair ranking | validates robustness |

Higher granularity = less carousel bias. See [[methods/build-analysis]].

### Dimension 3: Metric Selection (What to measure)

Progression: AVP → Delta → Necessity

Each step corrects one more bias. See [[concepts/metrics]] for details.

### Combining Dimensions

Best practice = all three maxed:
```
Precise Filter (Dim 1) + Build Analysis (Dim 2) + Necessity (Dim 3)
```

But any improvement on any dimension helps. Don't let perfect be the enemy of good.

## Reaching Into Layer 2: Context-Aware Analysis

The three dimensions produce Layer 1 priors. The tools below push toward Layer 2 — conditional priors that account for context our filters can't capture.

### Parametric Verification

Statistical analysis tells you WHAT works. Parametric analysis tells you WHY — and knowing WHY lets you predict when the prior will hold vs. break.

When data surprises you, verify with math. Aesah demonstrates this with Blue Buff vs Shojin: community consensus said Shojin was better on Caitlyn, but parametric mana-generation math shows Blue Buff generates 7% more mana/sec — and the gap widens during movement and CC phases.

**Power Budget** is a parametric framework for understanding item-unit fit. Every item has a fixed "power budget" across stats (AD, AP, AS, HP, resist). If a unit can't use a stat, that budget is wasted. This explains why:
- The same item has different Necessity on different units (budget utilization differs)
- Globally top-ranked items can be worst-in-slot for specific units (Indomitable on Leona)
- Component economy matters (Rabadon uses rod+rod = good for AP comp; Giant Slayer uses sword+bow = bad for AP comp)

**Multiplicative item model** (Dishsoap) predicts which 3-item builds should synergize best:

```
Tank: HP × Resist × DamageReduction   → pick one from each column
Phys: AttackSpeed × AD × DamageModifier
Magic: CastSpeed × AP × DamageModifier
```

Two items from the same column (e.g., two AS items) give diminishing returns. One from each column gives multiplicative scaling. This predicts that diversified builds outperform stacked builds — testable against our build analysis data.

**When to use parametric verification**:
- Data conflicts with game theory → do the math
- Two items have similar Necessity but one "should" be better → check budget utilization
- Community consensus conflicts with your data → parametric analysis can break the tie
- Build analysis shows a surprising combo → check if it exploits multiplicative scaling

### Stage-Dependent Value

Item and augment value is not constant across game stages — a Layer 2 factor that population stats can't fully capture:

| Resource | Early (4 units) | Late (8 units, carries maxed) |
|---|---|---|
| Item augments | High (multiplicative on carry) | Low (3-item cap reached) |
| Teamwide augments | Low (few units benefit) | High (8 units, bypasses cap) |
| Econ augments | Context-dependent | Auto-accumulate |
| Component parity | Doesn't matter yet | Odd = half item wasted |

**1st vs 2nd place**: When two players have identical comps and items, teamwide augments determine the winner. This means ceiling-oriented play (high-rolling) should favor teamwide augments.

### Consistency Over Raw Power

AVP is a mean — it hides variance. Dishsoap consistently evaluates comps by consistency (low bottom-4 rate) over raw AVP. For climbing LP, a comp with 0.1 worse AVP but 5% lower bot-4 rate may be strictly better.

This is a Layer 2 insight: the "best" comp depends on your goal (1st place vs consistent LP gain), which our population-level AVP doesn't distinguish. See [[concepts/metrics#consistency-beyond-avp]].

## Sources
- Xing + Agent framework (2026-04-21, updated 2026-04-22)
- [[sources/aesah-video-collection]] — parametric verification, power budget, stage-dependent value
- [[sources/tftacademy-video-collection]] — multiplicative item model, stats-as-questions philosophy
- Informed by all [[sources/morbrid-reddit-post|references]]
