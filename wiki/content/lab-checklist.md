# Lab Checklist
**Read this BEFORE every experiment. No exceptions.**

---

## Pre-Experiment
- [ ] Read `wiki/content/index.md` — know current progress and experiment queue
- [ ] Read this checklist — don't skip items
- [ ] Define the question clearly before touching any data
- [ ] Check: is this question interesting? Could the answer surprise us?

## Filter (Dimension 1 — Foundation)
- [ ] Specify comp context (traits + key units), not just the unit
- [ ] Use `compositions.py` definitions when available (expert-curated baseline)
- [ ] Use `--normal-only` — 不排除光装/特殊装备会污染排名
- [ ] Use `--level` when analyzing level-up candidates — level bias 是需要预防的变量，不是需要发现的结论
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
- [ ] Control variable（固定两件看第三件）→ 用 Necessity 不用 raw AVP（退化成单件 AVP）
- [ ] Consistency check（跨 base pair 排名）→ AVP 比较是有效的

## Analysis
- [ ] **Data first, conclusions after** — don't bring conclusions to data
- [ ] Show the data, let it speak
- [ ] Acknowledge limitations and open questions
- [ ] If two methods disagree, investigate why (don't pick the one you prefer)

## Report
- [ ] Story format with chapters (see experiment template in CLAUDE.md)
- [ ] Status set to `🧪 draft` — Xing will review and set final status
- [ ] Include `## Questions for Xing` section
- [ ] Update `wiki/content/index.md` (experiments table + syllabus status)
- [ ] Append to `wiki/content/log.md`
- [ ] `git add wiki/ && git commit && git push`

## After Review
- [ ] Xing's feedback recorded in report's `## Review` section
- [ ] Knowledge findings → integrated into `concepts/` or `methods/` pages
- [ ] Process lessons → appended to Lessons Learned below

---

## Lessons Learned
Append new ones here. These are hard-won — don't repeat them.

1. **Edge ≡ AVP** — algebraically trivial, caught by Xing (2026-04-21)
2. **Shrinkage doesn't fix systematic bias** — TFT's problem is bias not variance (2026-04-21)
3. **Don't regress to AVP** — cron experiment used AVP despite proving it unreliable the same day (2026-04-22)
4. **Isolated sessions forget everything** — must re-read wiki before every experiment (2026-04-22)
5. **compositions.py 一定能筛出足够样本** — tftable 定义是专家写的。0 games = 我们的 filter 转换有 bug，不是定义的问题。vex_95 曾因缺少 `_.*` 后缀返回 0 (2026-04-22)
6. **实验不要偏离原始问题** — nova-trait-breakpoint 修订后变成 filter bug 调试报告，完全偏离了"5 NOVA 值不值"的问题 (2026-04-22)
7. **Feedback 必须立即记录** — Xing 给的 feedback 要当场写进实验报告的 Review section 和 lab-checklist，不能只存 memory 不落文档 (2026-04-22)
8. **Revise 后必须通读全文** — 修改数据后要检查全文一致性，包括引用数字、结论、章节间逻辑。不能只改数据表就提交 (2026-04-22)
9. **物品分析必须用 `--normal-only`** — 不排除光装/特殊装备会污染 Necessity 排名，光装和普通装混排无意义 (2026-04-23)
10. **固定两件看第三件 = 单件 AVP** — 控制变量分析固定 base pair 后，第三件的 raw AVP 和单件 AVP 有同样的 survivorship bias，必须用 Necessity。但 consistency check（跨 base pair 排名）用 AVP 是有效的 (2026-04-23)
11. **Level bias 是预防不是发现** — 分析 +1 挂谁时必须用 `--level` 控制人口。Sona 在 nova_95 的 Necessity 从未控制的 +0.127 降到 level-controlled 的 +0.015（下降 88%）(2026-04-23)
