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
