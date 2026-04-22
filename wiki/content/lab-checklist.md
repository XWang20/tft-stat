# Lab Checklist
**Read this BEFORE every experiment. No exceptions.**

---

## Pre-Experiment
- [ ] Read `wiki/content/course.md` — know current progress and queue
- [ ] Read this checklist — don't skip items
- [ ] Define the question clearly before touching any data
- [ ] Check: is this question interesting? Could the answer surprise us?

## Filter (Dimension 1 — Foundation)
- [ ] Specify comp context (traits + key units), not just the unit
- [ ] Use `compositions.py` definitions when available (expert-curated baseline)
- [ ] Don't overfilter — keep ≥1000 games
- [ ] Sanity check: would a real player recognize these games as "this comp"?

## Metric Selection (Dimension 3)
- [ ] **NEVER sort by raw AVP to compare items** — survivorship bias contaminates it
- [ ] Use **Necessity** as primary ranking metric
- [ ] Use **Delta** as secondary (aware of w/o baseline shift)
- [ ] ~~Edge~~ ≡ AVP — don't use it

## Data Granularity (Dimension 2)
- [ ] Single-item analysis → always supplement with build analysis
- [ ] If comparing items: use builds or control variable, not single-item AVP

## Analysis
- [ ] **Data first, conclusions after** — don't bring conclusions to data
- [ ] Show the data, let it speak
- [ ] Acknowledge limitations and open questions
- [ ] If two methods disagree, investigate why (don't pick the one you prefer)

## Report
- [ ] Story format with chapters (see `course.md` for template)
- [ ] Update `wiki/content/index.md` (no orphan pages)
- [ ] Update `wiki/content/course.md` progress
- [ ] Append to `wiki/content/log.md`
- [ ] Include "Questions for Xing" section
- [ ] `git add wiki/ && git commit && git push`

---

## Lessons Learned
Append new ones here. These are hard-won — don't repeat them.

1. **Edge ≡ AVP** — algebraically trivial, caught by Xing (2026-04-21)
2. **Shrinkage doesn't fix systematic bias** — TFT's problem is bias not variance (2026-04-21)
3. **Don't regress to AVP** — cron experiment used AVP despite proving it unreliable the same day (2026-04-22)
4. **Isolated sessions forget everything** — must re-read wiki before every experiment (2026-04-22)
