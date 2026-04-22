You are a NEW agent performing a filter design exercise. You have NO prior context — read the wiki to learn.

## Step 1: Learn

Read `wiki/content/methods/filter-strategy.md` — focus on "Design a Filter From Scratch".

**DO NOT read `tft_stat/compositions.py` or run `python3 cli.py comps` — they contain the answers.**

## Step 2: Observe Boards and Find a Pattern

Run `python3 cli.py scout --top 3` to see top player endgame boards.

Look at MULTIPLE boards (not just one). Find a recurring pattern — boards that share similar carries, traits, and core units. Give it your own working name.

Check `wiki/content/experiments/filter-design-exercise-log.md` — skip patterns already attempted.

Write down:
- What boards you observed that share this pattern
- What defines this pattern (carry, trait, core units)
- How it differs from other boards you saw

## Step 3: Design the Filter (show your work)

Build the filter iteratively. Show EACH step:

1. **Initial filter** → `python3 cli.py total <your args>` → record sample size
2. **Check units** → `python3 cli.py units <your args>` → record carry IC3 rate, contaminating units
3. **Adjust** → what you changed and why → re-run → check again
4. **Repeat** until: target comp included + interference excluded + sample adequate

## Step 4: Compare with Ground Truth

NOW read `tft_stat/compositions.py`. Find the matching expert definition.
- What did you get right / miss?
- Run the expert filter too, compare sample sizes

## Step 5: Record Results

Append to `wiki/content/experiments/filter-design-exercise-log.md`:

```
### [your_name] → [expert_key] — [date]

**Observation**: [which boards, what pattern you saw]
**My reasoning**: [why you chose this carry/trait/exclusions]

**Filter iterations**:
1. `<args>` → X games, IC3 Y%, contamination: [units]
2. Added `--exclude-units Z` → X games, IC3 Y%, clean
3. Final: `<args>`

**Expert filter**: [description]
**Comparison**: right=[...], missed=[...]
**Lesson**: [what the guide should add]
```

If the guide needs updating, edit `wiki/content/methods/filter-strategy.md`.

## Step 6: Commit and Push

```
git add wiki/
git commit -m "filter-design exercise: [your_name] — [one-line result]

via [HAPI](https://hapi.run)

Co-Authored-By: HAPI <noreply@hapi.run>"
git push
```
