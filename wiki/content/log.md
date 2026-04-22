## [2026-04-22] cron | Carry leverage experiment + vex-cross-comp consistency check
- Giscus #7: confirmed Round 3 consistency fixes complete for [[experiments/2026-04-22-vex-cross-comp-items]]
- New experiment: [[experiments/2026-04-22-carry-leverage-necessity]] — Module 5 follow-up
- Tested 2 new comps (Space Groove Nami, Meeple Corki) to validate carry leverage theory
- Key finding: AP carry Necessity ↑ at higher tier (Nami +163% Nashor's), AD carry flat (Corki +10%)
- ΔAVP magnitude may be the real driver, not carry type per se
- Updated: [[index]] (experiments table, queue cleared)

## [2026-04-22] cron | Filter reliability experiment + vex-cross-comp revision
- Revised [[experiments/2026-04-22-vex-cross-comp-items]] — removed stale vex_95 references, fixed consistency per Xing feedback
- New experiment: [[experiments/2026-04-22-filter-reliability]] — Module 1/9
- Key finding: filter reliability depends on carry role — Vex (primary carry) ρ=0.976, Mordekaiser (tank) ρ=0.048
- Warmog's #1 in full filter but #7 in tftable — filter confound for tanks
- Deepened: [[methods/filter-strategy]] — added "Filter Reliability Depends on Unit Role" section with quantified evidence
- Updated: [[index]] (experiments table, queue)

## [2026-04-22] cron | Giscus review processing + universal bias experiment
- Giscus #9: ✅ accepted [[experiments/2026-04-22-build-vs-single-necessity]] — "没太大区别" confirmed
- Giscus #8: ✅ accepted [[experiments/2026-04-22-cross-validation-vex-nova95]]
- Giscus #7: 🔄 revision [[experiments/2026-04-22-vex-cross-comp-items]] — "通读全文检查一致性"
- Added lesson #8 to [[lab-checklist]]: revise 后必须通读全文
- New experiment: [[experiments/2026-04-22-universal-improvement-bias]] — Module 5, tested 8 traits total
- Key finding: 7/8 traits show higher tier = better AVP (selection bias); Anima Squad reverses (opportunity cost)
- Space Groove 10 = canonical selection bias example (AVP 1.10, 93% WR, 1117 games)
- Updated: [[index]] (experiments table, queue, statuses)

## [2026-04-22] cron | Multi-comp trait breakpoint experiment
- New experiment: [[experiments/2026-04-22-trait-breakpoint-multi-comp]] — Module 5 redo, tested 3 traits (DRX/DarkStar/Summon) × 3 comps (nova_yi/dark_star/shepherd)
- Key finding: trait breakpoints do not change carry itemization — universal across AD/tank/AP carries
- Unexpected: Necessity direction varies by carry role leverage (MasterYi ↓, Mordekaiser/Sona ↑ at higher tier)
- Cross-validated with tftable for Mordekaiser and Sona — item pools match
- Updated: [[index]] (experiments table, queue)
- GitHub authentication failed — skipped Giscus/issue processing

## [2026-04-22] cron | Issue processing + nova-trait-breakpoint revision
- Processed 6 GitHub issues (#1-6): 3 feedback, 2 conclusions, 1 revision
- Issue #4 (conclusion): integrated tftable debiasing info into concepts/metrics.md — new "Necessity Is Not the Final Answer" section
- Issue #3 (conclusion): integrated compositions.py trust rule into methods/filter-strategy.md — new "Trust compositions.py Definitions" section
- Issue #1 (revision): nova-trait-breakpoint third revision — switched to nova_yi as primary comp (66k 2 NOVA vs 120k 5 NOVA), focused on "does 5 NOVA change itemization?" (answer: no for MasterYi, top 3 identical)
- Issues #2, #5, #6: confirmed feedback already recorded in wiki, closed
- First cross-validation disagreement found: Edge of Night vs Giant Slayer at #1 for MasterYi

## [2026-04-22] experiment | Expert Filter Design Patterns
- Taxonomized all 29 compositions.py filters into 5 design patterns
- LeBlanc case study: Guinsoo invisible in minimal filter, #1 in full filter (92% usage)
- Nami Simpson's Paradox: Void Staff #1 globally, irrelevant within either comp
- Vex cross-comp: Striker's Flail 20× Necessity drop between nova_95 and vex_95
- Expert heuristic: 64% of exclusions target 3-item carries (boundary definition)
- Cross-validated vanguard_leblanc with tftable: top 5 match

## [2026-04-22] experiment | Build Necessity vs Single-Item Necessity
- Module 3 follow-up: compared build-level and single-item Necessity for Vex and Fiora in nova_95
- Key finding: build-implied rankings differ — Hextech Gunblade rises to #1 (from #3), Guinsoo drops to #4 (ceiling effect at 88% play rate)
- Bloodthirster on Fiora shows same pattern: #3 single-item but backbone of 9/10 top builds
- JG confirmed as trap: tftable gives negative Necessity, build score misleadingly positive (contaminated by strong partners)
- Methods are complementary: single-item for "what to prioritize," builds for "which third item"
- Cross-validated with tftable: Void Staff worst item in both methods

## [2026-04-22] experiment | N.O.V.A. Trait Breakpoints (revised)
- Redid experiment using Necessity within specific comps (nova_95, nova_yi)
- Key finding: item Necessity rankings are stable across trait tiers (Vex top 6 identical in 2 vs 5 NOVA)
- Discovered filter integrity issue: Kindred exclusion leaks when combined with DRX tier 2 trait filter (97% Kindred in "5 NOVA nova_95")
- Emblem path to 5 NOVA is negligible (~3.4% of games)
- "Universal improvement" pattern persists even within comps -- selection bias not eliminated
- Cross-validated with tftable: item Necessity rankings match
- Question remains fundamentally unanswerable from endgame snapshots

## [2026-04-22] experiment | Vex cross-comp items (revision)
- Revised experiment using standardized compositions.py filters (was ad-hoc)
- Old Shepherd filter captured 58k Vex games; standardized filter yields only 3.9k (93% drop)
- 3 items flipped Necessity sign in Dark Star (Giant Slayer, Hextech Gunblade, JG) -- ad-hoc filter artifacts
- "Jeweled Gauntlet trap" conclusion was entirely a filter artifact
- Cross-validated nova_95 against tftable: top 7 items match
- Core conclusion "filter = foundation" still holds, but dramatic sign-flip stories were overstated

## [2026-04-22] update | Project restructure
- Merged wiki into main tft-stat repo (was separate git repo)
- Restructured code: metatft_query.py → tft_stat/ package + cli.py
- Updated schema.md, index.md, course.md, lab-checklist.md
- GitHub Pages deployed at xwang20.github.io/tft-stat/

## [2026-04-22] experiment | N.O.V.A. Trait Breakpoints (cron)
- First cron-triggered experiment
- Compared 2 vs 5 N.O.V.A. using AVP (wrong metric!)
- Xing feedback: use Necessity, control variables within specific comps, consider emblem factor

## [2026-04-22] reflection | Xing feedback on cron experiment
- Regressed to AVP despite yesterday's lessons
- Added lab-checklist.md as preflight
- Learned: checklist = gate (10 items), not textbook

## [2026-04-22] update | Wiki maintenance
- Added lab-checklist.md
- Added reflections-2026-04-22.md with Xing's full feedback
- Updated index, course, cron job messages
- Metrics page fully rewritten (Edge deprecated)

## [2026-04-21] experiment | Vex cross-comp items
- Same Vex, different comps → different BIS (Giant Slayer flips sign)
- Filter = foundation validated empirically

## [2026-04-21] experiment | Vex items in Nova 95
- 5 metrics compared: AVP, Edge, Necessity, Builds, Control Variable
- Necessity + Builds converge; Red Buff/Dcap consistently best

## [2026-04-21] reflection | Day 1 learnings
- Don't bring conclusions to data
- Shrinkage ≠ debiasing (TFT's problem is bias not variance)
- Edge is algebraically equivalent to AVP

## [2026-04-21] ingest | Four source videos/posts
- morbrid Reddit post, Aesah data mistakes, morbrid+Aesah talk, Dishsoap+Frodan stats
- Created concepts/metrics, concepts/biases, concepts/framework
- Created methods/filter-strategy, methods/build-analysis
- Created tools/metatft-api
