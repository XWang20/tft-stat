# Analysis Framework
**Status**: ✅ verified

## Three Orthogonal Dimensions

TFT stats analysis operates on three independent axes. Each can be set independently. Best results come from maximizing all three.

### Dimension 1: Filter Strategy (What games to include) — FOUNDATION

TFT match data is high-dimensional panel data. Viewing aggregate statistics without proper conditioning produces Simpson's Paradox — conclusions reverse when you stratify.

Filter = conditioning = controlling for confounders.

**Without correct conditioning, no metric can produce correct conclusions.**

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

Each step corrects one more bias. See [[metrics]] for details.

### Combining Dimensions

Best practice = all three maxed:
```
Precise Filter (Dim 1) + Build Analysis (Dim 2) + Necessity (Dim 3)
```

But any improvement on any dimension helps. Don't let perfect be the enemy of good.

## Sources
- Xing + Mochi framework (2026-04-21)
- Informed by all [[sources/morbrid-reddit-post|references]]
