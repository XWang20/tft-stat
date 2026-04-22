# Analysis Framework
**Status**: ✅ verified

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

## Sources
- Xing + Agent framework (2026-04-21, updated 2026-04-22)
- Informed by all [[sources/morbrid-reddit-post|references]]
