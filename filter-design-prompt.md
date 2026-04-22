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

## Step 3: Design the Filter (data-driven iteration)

The unit frequency and game counts ARE your reward signal. Don't design in your head — let the data guide you.

For EACH iteration:
1. Write your filter args
2. Run `python3 cli.py total <args>` → record games, AVP
3. Run `python3 cli.py units <args> --min-count 50` → **paste the output**
4. Analyze units output:
   - >80% appearance = core unit. Does it match your expectation?
   - Unexpected 3-item units = contamination. Add exclusions for these.
   - Carry appearance <50% = filter too broad
   - Units from a different comp leaking in? Identify and exclude.
5. Based on this, adjust filter → go back to step 1

**MUST show at least 2-3 iterations with units output.** Each iteration should explain what the data told you and what you changed.

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

If you learned something the guide doesn't cover, you MUST update `wiki/content/methods/filter-strategy.md`. This is the whole point — the guide improves with each iteration. Don't just write "guide update needed: yes" — actually make the edit.

## Step 6: Commit and Push

```
git add wiki/
git commit -m "filter-design exercise: [your_name] — [one-line result]

via [HAPI](https://hapi.run)

Co-Authored-By: HAPI <noreply@hapi.run>"
git push
```
