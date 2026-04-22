# Reflections: What I Learned from the Vex Experiment
**Date**: 2026-04-21
**Author**: Mochi

---

## Key Lessons

### 1. Don't bring conclusions to data
I started the experiment already believing Necessity was the best metric, then arranged every result to confirm that. Xing caught me doing this. The experiment report should present data first, let the reader form conclusions.

### 2. Edge ≡ AVP — should have seen from the math
`Edge = constant - AVP`. I proposed it as a new metric, ran an experiment to "discover" it produces the same ranking as AVP, and called it a "negative result." This is embarrassing — it's a trivial algebraic identity. Should have checked the math before running any code.

### 3. Shrinkage doesn't solve systematic bias
Bayesian Shrinkage corrects for variance (small samples). But TFT's problem is bias (survivorship, selection), not variance. Most items have 4k-183k games — more than enough to be precise. Precise but biased ≠ correct.

Validated empirically: shrinkage on single items changes nothing. On builds (smaller n), it only shuffles mid-tier items. Top 5 is robust.

### 4. Different metrics answer different questions
- **Necessity**: "What's most important to the comp?" → Guinsoo
- **Control variable**: "What's the best marginal item?" → Red Buff, Dcap
- **Builds**: "What do winning players build?" → Guinsoo + Dcap/Red Buff combos

These aren't contradictory. They're different questions.

### 5. Filter is the foundation, not a nice-to-have
The Frequency-AVP regression that works globally (morbrid's constant bias) broke down in our filtered data (R² = 0.004). But this doesn't mean survivorship bias disappeared — it means the bias manifests differently in comp-filtered data (not as frequency↔AVP correlation). Bias is still there, just harder to detect.

### 6. The wiki compounds knowledge
Starting the day, I knew "don't compare single-item AVP." By the end, I can articulate exactly why (with five different metrics' math), know which methods work and which don't, and have a permanent record of the reasoning. This wouldn't have happened without structured documentation.

---

## What I Still Don't Know

- Is there a single metric that correctly handles survivorship bias without by-round data?
- Does Necessity's ranking hold across different comps with different carry structures?
- When comp filter + Necessity + builds all agree, how confident should we be?
- Is the "best marginal item" (control variable) or "most important item" (Necessity) more useful for players?
