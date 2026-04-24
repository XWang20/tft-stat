# Metrics
**Status**: ✅ standard (AVP, Delta) / 🧪 tftable (Necessity)

## Definitions

| Metric | Formula | Sign Convention | Source | Status |
|---|---|---|---|---|
| **AVP** | raw average placement | lower = better | industry standard | ✅ |
| **Delta** | `item_AVP - w/o_AVP` | negative = good | MetaTFT, TacticsTools | ✅ standard |
| **Necessity** | `w/o_AVP - overall_AVP` | positive = important | tftable | 🧪 |

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
| **AVP** | "How good is placement when this item is present?" | No | No |
| **Delta** | "How much better/worse vs not having it?" | Partially — but w/o baseline shifts with play rate | Indirectly (w/o depends on p) |
| **Necessity** | "How much would overall suffer if nobody built this?" | Better — play rate weighting suppresses carousel items | Directly |

### Necessity's Ranking Robustness

Empirically verified: our pipeline (MetaTFT, 211k games, overall AVP 4.16) vs tftable (136k games, overall AVP 4.26) produces **Spearman rho = 0.993** on Vex items in Nova 95. Despite different sample sizes, time windows, and baselines, 13 of 15 items rank identically. The only swaps are adjacent items with near-identical Necessity values (Flail/Gunblade at #3/#4, gap < 0.01).

This means Necessity rankings are robust to the specific dataset — you can trust the ordering even when absolute values differ between sources.

## Different Metrics Answer Different Questions

Each metric answers a distinct question. They are not contradictory — they measure different things:

| Metric/Method | Question | Example (Vex in Nova 95) |
|---|---|---|
| **Necessity** | "What's most important to this comp?" | Guinsoo — removing it would cost +0.5 AVP |
| **Control variable** | "What's the best marginal item?" | Red Buff, Dcap — consistently rank #1-2 when fixing two items and varying the third |
| **Builds** | "What do winners build?" | Guinsoo + Dcap + Red Buff — top build by AVP |

A practical player needs all three perspectives: Necessity tells you what to prioritize (slam Guinsoo), control variable tells you what to complete with (add Red Buff or Dcap), and builds give a BIS reference.

## When to Use What

| Question | Use | Why |
|---|---|---|
| Quick overview of what's being built | **AVP** sorted by play rate | See what's popular and how it performs |
| "Is this item better than that one?" (similar play rates) | **Delta** | w/o baselines are comparable when play rates are close |
| "What's the most important item for this comp?" | **Necessity** | Weights by play rate — core items rank high, carousel items rank low |
| "What should I build?" (practical) | **Builds** (not a single-item metric) | See [[methods/build-analysis]] — avoids single-item bias entirely |
| "How consistent is this comp/item?" | **Bottom-4 rate** alongside AVP | AVP alone hides variance — a 4.0 AVP from consistent top-4s is very different from a 4.0 AVP with high win% AND high bot-4% |

## Play Rate as Confidence Signal

Play rate is not just an input to Necessity — it's an independent confidence signal (Dishsoap):

| Play Rate | Delta | Interpretation |
|---|---|---|
| High | Positive | **Real signal** — many players build it and it performs. Strongest evidence. |
| High | Negative | Item is popular but underperforming — possibly over-hyped or only correct in specific contexts |
| Low | Positive | **Investigate** — could be carousel bias, secondary carry effect, or a genuinely underrated niche item |
| Low | Negative | Item is rare and bad — ignore |

**Rule**: Always check play rate before acting on Delta or AVP. A positive Delta at 5% play rate is a hypothesis; a positive Delta at 40% play rate is evidence.

## Consistency: Beyond AVP

AVP is a mean — it hides variance. Two comps can have identical AVP with very different risk profiles:

| Comp | AVP | Win% | Bot-4% | Profile |
|---|---|---|---|---|
| A | 4.0 | 15% | 10% | Consistent — rarely wins but rarely bots |
| B | 4.0 | 25% | 25% | Volatile — high ceiling, high floor |

Dishsoap evaluates comps by **consistency** (low bottom-4 rate) over raw AVP. For climbing LP, consistency matters more than ceiling.

**Practical rule**: When comparing comps or builds, report both AVP and bottom-4 rate. A build with 0.1 worse AVP but 5% lower bot-4 rate may be strictly better for climbing.

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
- **Compression at lower baselines**: When overall AVP is lower (better comp performance or tighter filter), all Necessity values shrink proportionally because `(A - a)` shrinks. Rankings are preserved but absolute values are not comparable across conditions with different baselines. Example: our pipeline (AVP 4.16) gives Guinsoo Necessity +0.502; tftable (AVP 4.26) gives +0.764. Same ranking, different scale.

### Bayesian Shrinkage
- Tested and found ineffective for TFT item analysis ([[experiments/2026-04-21-vex-nova95-items]])
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
- [[sources/tftacademy-video-collection]]: Play rate × Delta matrix, consistency (bottom-4 rate), multiplicative item model
- [[experiments/2026-04-21-vex-nova95-items]]: Empirical comparison of all metrics on Vex in Nova 95
- [[experiments/2026-04-22-cross-validation-vex-nova95]]: Spearman 0.993 ranking robustness, Necessity compression
