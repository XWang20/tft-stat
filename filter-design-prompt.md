You are a NEW agent performing a filter design exercise. You have NO prior context — read the wiki to learn.

## Your Goal

Analyze 100 recent top-player endgame boards, cluster them into distinct comp patterns, and design filters for each. This is a classification problem: group similar boards together, separate different ones.

## Step 1: Learn the Method

Read `wiki/content/methods/filter-strategy.md` — focus on "Design a Filter From Scratch" and the expert heuristics.

**DO NOT read `tft_stat/compositions.py` or run `python3 cli.py comps` — they contain the answers.**

## Step 2: Observe All Boards

Run `python3 cli.py scout --top 3` to get ~50 top-3 boards.

Study ALL boards holistically. For each board, note:
- Which units carry 3 items (= carries)?
- What traits are active?
- What's the overall team shape?

## Step 3: Cluster Into Comp Patterns

Group boards by similarity. Ask:
- Which boards share the same carry + trait combination?
- Which boards look like variants of each other?
- How many distinct comp types can you identify?

Write down each cluster with:
- A working name you choose
- The defining features (carry, trait, core units)
- How many boards fall into this cluster
- How this cluster differs from similar-looking clusters

## Step 4: Design Filters For Each Cluster

For EACH cluster, design a filter iteratively:

1. **Initial filter** — carry (with item threshold) + trait anchor
2. **Test**: `python3 cli.py total <your filter args>` — check sample size
3. **Validate**: `python3 cli.py units <your filter args>` — check:
   - Do expected core units appear at high rate?
   - Do unexpected units appear (= contamination from other comps)?
   - What's the carry's IC3 rate?
4. **Iterate** — if contamination or sample issues:
   - Add exclusions for contaminating units/traits
   - Adjust item threshold (i2 vs i3)
   - Adjust trait bounds (≥ vs =)
5. **Record each iteration** — what you changed and why

## Step 5: Write the Report

Write to `wiki/content/experiments/YYYY-MM-DD-filter-design-exercise.md`:

```
# Filter Design Exercise: Comp Discovery from Endgame Boards
Status: 🧪 draft
Date: YYYY-MM-DD

## Observation
What I saw in the 100 boards. How many distinct patterns. What stood out.

## Clustering
For each cluster:
- Name, defining features, board count
- How it differs from similar clusters

## Filter Design Process (per cluster)
For each cluster, show the FULL iteration:
1. Initial filter → sample size, IC3, contamination check
2. What I adjusted and why
3. Final filter → sample size, IC3
Show the reasoning, not just the result.

## Comparison with Ground Truth
NOW read compositions.py. For each of my clusters:
- Does a matching expert definition exist?
- What did I get right / miss?
- Did I discover anything the expert definitions don't cover?

## Lessons for the Guide
What should be added to filter-strategy.md?

## Questions for Xing
```

## Step 6: Update Guide + Commit

If you learned something new, update `wiki/content/methods/filter-strategy.md`.
Update `wiki/content/index.md` and `wiki/content/log.md`.

```
git add wiki/ .
git commit -m "filter-design exercise: discovered N comp patterns from 100 boards

via [HAPI](https://hapi.run)

Co-Authored-By: HAPI <noreply@hapi.run>"
git push
```
