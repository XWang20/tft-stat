# Lab Checklist
**Read this BEFORE every experiment. No exceptions.**

## Pre-Experiment
- [ ] Read `wiki/course.md` — know current progress
- [ ] Read this checklist — don't skip items
- [ ] Define the question clearly before touching any data

## Filter (Dimension 1 — Foundation)
- [ ] Specify comp context (traits + key units), not just the unit
- [ ] Use compositions.py definitions when available
- [ ] Don't overfilter — keep ≥1000 games
- [ ] Games tab sanity check if using MetaTFT web

## Metric Selection (Dimension 3)
- [ ] **NEVER sort by raw AVP to compare items** — AVP is contaminated by survivorship bias
- [ ] Use **Necessity** as primary ranking metric
- [ ] Use **Delta** as secondary (aware of w/o baseline shift)
- [ ] ~~Edge~~ ≡ AVP, don't use it

## Data Granularity (Dimension 2)
- [ ] Single-item analysis → always supplement with Build analysis
- [ ] If comparing items: use builds or control variable, not single-item AVP

## Analysis
- [ ] **Data first, conclusions after** — don't bring conclusions to data
- [ ] Show the data, let it speak
- [ ] Acknowledge limitations and open questions
- [ ] If two methods disagree, investigate why (don't pick the one you like)

## Report
- [ ] Story format with chapters
- [ ] Update wiki/index.md (no orphan pages)
- [ ] Update wiki/course.md progress
- [ ] Include "Questions for Xing" section
- [ ] Git push wiki

## Lessons Learned (append new ones here)
1. **Edge ≡ AVP** — algebraically trivial, caught by Xing (2026-04-21)
2. **Shrinkage doesn't fix systematic bias** — TFT's problem is bias not variance (2026-04-21)
3. **Don't regress to AVP** — cron experiment used AVP despite spending all day proving it's unreliable (2026-04-22)
4. **Isolated sessions forget everything** — must re-read wiki before every experiment (2026-04-22)
