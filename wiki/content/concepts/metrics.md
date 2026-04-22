# Metrics
**Status**: ✅ standard (AVP, Delta) / 🧪 tftable (Necessity)

## Definitions

| Metric | Formula | Sign Convention | Source | Status |
|---|---|---|---|---|
| **AVP** | raw average placement | lower = better | industry standard | ✅ |
| **Delta** | `item_AVP - w/o_AVP` | negative = good | MetaTFT, TacticsTools | ✅ standard |
| **Necessity** | `w/o_AVP - overall_AVP` | positive = important | tftable | 🧪 |
| ~~Edge~~ | `overall_AVP - item_AVP` | positive = good | Mochi (deprecated) | ≡ AVP |

**Edge ≡ AVP**: `Edge = constant - AVP`, so sorting by Edge is identical to sorting by AVP. It's a readability improvement (positive = good) but provides no additional analytical power. Deprecated as a separate metric.

## Mathematical Relationships

```
Let: p = play_rate, a = item_AVP, A = overall_AVP

w/o_AVP = (A - p×a) / (1-p)

Delta      = a - w/o = a - (A - p×a)/(1-p) = (a - A)/(1-p)
Necessity  = w/o - A = p/(1-p) × (A - a)
```

Key relationships:
- **Delta = -(A - a) / (1-p)** — AVP gap divided by (1 - play_rate)
- **Necessity = p/(1-p) × (A - a)** — AVP gap scaled by play_rate ratio
- **Delta × p = -Necessity** — they are proportional with opposite signs

## What Each Metric Captures

| Metric | Measures | Handles Survivorship Bias? | Play Rate Aware? |
|---|---|---|---|
| **AVP** | "How good is placement when this item is present?" | ❌ No | ❌ No |
| **Delta** | "How much better/worse vs not having it?" | Partially — but w/o baseline shifts with play rate | ⚠️ Indirectly (w/o depends on p) |
| **Necessity** | "How much would overall suffer if nobody built this?" | ✅ Better — play rate weighting suppresses carousel items | ✅ Directly |

## When to Use What

| Question | Use | Why |
|---|---|---|
| Quick overview of what's being built | **AVP** sorted by play rate | See what's popular and how it performs |
| "Is this item better than that one?" (similar play rates) | **Delta** | w/o baselines are comparable when play rates are close |
| "What's the most important item for this comp?" | **Necessity** | Weights by play rate — core items rank high, carousel items rank low |
| "What should I build?" (practical) | **Builds** (not a single-item metric) | See [[methods/build-analysis]] — avoids single-item bias entirely |

## Known Limitations

### AVP
- Play rate and AVP are inversely correlated (constant bias, every set — morbrid)
- Low play rate items always look better due to carousel/late-game acquisition

### Delta
- w/o baseline is **not fixed** — it shifts with play rate
- High play rate item (e.g., Guinsoo 87%): w/o group is tiny and weak → Delta inflated
- Low play rate item (e.g., Red Buff 7%): w/o group ≈ overall → Delta ≈ raw AVP gap
- Cross-item comparison is structurally unfair when play rates differ significantly

### Necessity
- Suppresses low play rate items — this is usually correct (carousel bias) but could hide genuinely good niche items
- High play rate items dominate — an "okay" item that everyone builds gets high Necessity
- Does not fully solve survivorship bias — just uses play rate as a proxy

### Bayesian Shrinkage
- Tested and found ineffective for TFT item analysis ([[experiments/vex-nova95]])
- TFT's problem is systematic bias, not variance
- Most items have 4k-183k games — sample size is already sufficient
- Shrinkage doesn't change rankings

### Necessity Is Not the Final Answer
- tftable 除了 Necessity 还使用了进阶 debiasing 方法，这解释了我们的 Necessity 数值和 tftable 有系统性差异（排名一致但量级不同）
- Xing 会逐步教这些方法。当前阶段：用 Necessity 做分析，和 tftable 交叉验证排名一致性
- 不要把 Necessity 当作最终答案 — 它是学习路径上的一步，后续会更新 metrics 体系

### No Single Perfect Metric
- **Necessity + Build Analysis** converging is currently our best signal for confidence
- Each metric answers a different question — use the right tool for the right question
- See [[concepts/framework]] for the three-dimensional approach

## Sources
- [[sources/aesah-data-mistakes]]: Play rate weighted formula, Heimer example
- [[sources/morbrid-reddit-post]]: CI, sample size, constant frequency-AVP bias
- [[sources/morbrid-aesah-talk]]: Graph view (frequency vs AVP), tier algorithm = frequency + place change
- [[sources/dishsoap-frodan-stats]]: Play rate as confidence signal, builds > single items
- [[experiments/vex-nova95]]: Empirical comparison of all metrics on Vex in Nova 95
