You are a NEW agent performing a filter design exercise. You have NO prior context — read the wiki to learn.

## Your Task

Design a TFT composition filter from scratch, then compare with the expert ground truth.

## Step 1: Learn the Method

Read these files in order:
1. `wiki/content/methods/filter-strategy.md` — the filter design guide
2. `wiki/content/concepts/framework.md` — core principles

Focus on the "Design a Filter From Scratch" section.

## Step 2: Discover a Comp Pattern from Board Data

Run `python3 cli.py scout --top 3` to scan top player endgame boards.

Study the boards. Look for recurring patterns:
- Which units appear together frequently?
- Which units carry 3 items in these boards?
- What traits are active?

Identify ONE comp pattern you can describe (e.g., "boards with a DRX trait carry holding 3 items alongside Shen and Morgana as frontline"). Give it your own working name based on what you observe.

Check `wiki/content/experiments/filter-design-exercise-log.md` — if a similar pattern was already attempted, find a different one.

**DO NOT read `tft_stat/compositions.py` or run `python3 cli.py comps` — they contain the answers. You will compare in Step 4 only.**
- Easy: single carry comps (zed, kaisa, bonk, veigar, etc.)
- Medium: carry + trait comps (conduit_mf, mecha, dark_star)
- Hard: OR-group + exclusion comps (nova_95, vanguard_leblanc, nova_yi)

## Step 3: Design Your Filter (WITHOUT looking at the answer)

DO NOT read the comp's filter definition in compositions.py yet. Instead:

1. Run `python3 cli.py scout --top 3` to see what top players are running
2. Based on the comp name and your understanding, design a filter using the guide's method:
   - What is the carry? (or carry group?)
   - What trait defines this comp?
   - What exclusions might be needed?
3. Write your filter as CLI args: `--comp` is NOT allowed. Use `--units`, `--or-units`, `--traits`, `--exclude-units`, `--exclude-traits`.
4. Test your filter: `python3 cli.py total <your filter args>`
5. Check units: `python3 cli.py units <your filter args>` — do the expected core units appear?
6. Iterate if needed (sample too small, contamination, etc.)

## Step 4: Compare with Ground Truth

NOW read `tft_stat/compositions.py` and run `python3 cli.py comps`. Find the expert definition that matches your discovered pattern (if one exists). Compare:
- What conditions did you get right?
- What did you miss? (exclusions, trait bounds, OR-groups)
- What did the expert include that you didn't think of? Why?
- Run both filters and compare sample sizes and carry IC3 rates

## Step 5: Record Results

Append your results to `wiki/content/experiments/filter-design-exercise-log.md`:

```
### [comp_key] — [date]
**My filter**: [CLI args]
**Expert filter**: [description]
**Sample size**: mine=X, expert=Y
**What I got right**: ...
**What I missed**: ...
**Lesson for the guide**: ...
**Guide update needed?**: yes/no — if yes, what specifically
```

## Step 6: Update the Guide (if needed)

If you learned something that the guide doesn't cover, update `wiki/content/methods/filter-strategy.md` with the specific insight. Make it actionable — not "be careful with X" but "when you see pattern P, do action A because reason R."

## Step 7: Commit and Push

```
git add wiki/ .
git commit -m "filter-design exercise: [comp_key] — [one-line result]

via [HAPI](https://hapi.run)

Co-Authored-By: HAPI <noreply@hapi.run>"
git push
```
