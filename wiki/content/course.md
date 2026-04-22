# TFT Data Science Course

> Goal: Master TFT data retrieval and analysis. Become better than the teacher.
> Method: Each module has concepts, readings, and experiments. Mochi runs 3 experiments daily (cronjob), writes reports, cross-validates with tftable.
> Xing reviews daily, discusses, corrects.

---

## Syllabus

| Module | Topic | Core Question | Concepts | Readings | Experiments |
|---|---|---|---|---|---|
| 0 | Foundations | What data do we have and where does it come from? | Endgame snapshots, API endpoints, filter params | [[sources/morbrid-reddit-post]], [[tools/metatft-api]] | Explore all MetaTFT API endpoints; compare MetaTFT vs tftable data |
| 1 | Filter Design | How do we define "this comp" precisely? | Conditioning, Simpson's Paradox, overfiltering | [[sources/dishsoap-frodan-stats]], [[methods/filter-strategy]] | Same unit different comps (Zoe in Rebel vs Sorc); filter sensitivity analysis |
| 2 | Item Metrics | Given a comp, what metric tells us if an item is good? | AVP, Delta, Necessity, survivorship bias | [[sources/aesah-data-mistakes]], [[concepts/metrics]] | **[[experiments/vex-nova95]]** ✅ |
| 3 | Build Analysis | How do item combinations interact? | Builds, control variable, consistency check | [[sources/dishsoap-frodan-stats]], [[methods/build-analysis]] | Top builds vs top single items; when do they disagree? |
| 4 | Unit Evaluation | Which units matter most in a comp? | Unit Necessity, carry vs support, cap boards | [[sources/morbrid-aesah-talk]] | Best 9th unit for a comp; Poppy vs Sejuani type questions |
| 5 | Trait Breakpoints | When is 4→6 trait worth the cost? | Trait Delta, opportunity cost, marginal unit value | [[sources/dishsoap-frodan-stats]] | Compare 4 vs 6 N.O.V.A.; when does vertical pay off? |
| 6 | Comp Comparison | How do we compare two different comps? | Strength, AVP distribution, matchups | tftable comps data | Rank all S17 comps; compare our ranking with tftable |
| 7 | Emblem & Augment | What's the best emblem/augment for a comp? | Plus-one traits, augment proxies, exclude→toggle | [[sources/morbrid-aesah-talk]] | Best emblem for Nova 95; anti-heal importance by comp |
| 8 | Temporal Analysis | How does the meta shift within a patch? | Day-over-day trends, early vs late patch | — | Track a comp's AVP over 7 days; does "solved meta" exist? |
| 9 | Cross-Validation | When should we trust our results? | Convergence of methods, tftable cross-check, confidence | All prior modules | Systematic cross-validation: our pipeline vs tftable on 5 comps |

---

## Daily Experiment Protocol

### Schedule
3 experiments per day via cronjob. Each experiment:
1. Starts from a **core question** (can be Module-related, exploratory, or follow-up)
2. Explores with data — **data first, conclusions after**
3. Produces a report in `experiments/` (story format, with chapters)
4. Cross-validates with tftable when applicable
5. Updates relevant wiki concept/method pages

### Report Format
```
# Experiment: [Title]
Status: 🧪 In Progress | ✅ Complete
Date: YYYY-MM-DD
Module: N (or "Exploratory")

## The Question
## Chapter 1-N: (story-driven, data first)
## Cross-Validation (vs tftable) ← MANDATORY for every experiment
## What I Learned
## Open Questions → feed into next experiments
```

### Cross-Validation Protocol
Every experiment SHOULD include cross-validation when tftable API is available:
1. Query tftable for the same data point (tftable = baseline / ground truth)
2. Compare our result with tftable's
3. If they agree → confidence++
4. If they disagree → investigate why

**Note**: tftable API not yet available for programmatic access. Xing will provide API later. For now, qualitative comparison only.

### Experiment Sources
- **Module exercises**: directly practice the current topic
- **Follow-ups**: open questions from previous experiments
- **Previews**: explore next module's territory before formal study
- **Surprises**: unexpected findings, things I'm curious about
- **Cross-validations**: compare our methods with tftable's answers

---

## Progress Tracker

| Module | Status | Key Experiments | Key Learnings |
|---|---|---|---|
| 0 | ✅ | API exploration (2026-04-21) | 9 endpoints discovered, filter format documented |
| 1 | ✅ | vex-cross-comp-items (2026-04-21) | Filter is foundation; same unit different comp = different BIS; Giant Slayer flips sign between NOVA and Dark Star |
| 2 | ✅ | vex-nova95 (2026-04-21) | Necessity best single metric; Edge ≡ AVP; shrinkage doesn't fix bias |
| 3 | 🧪 | vex-nova95 supplementary | Control variable + consistency check validated |
| 4 | ⬜ | — | — |
| 5 | 🧪 | nova-trait-breakpoint (2026-04-22) | REDO needed: used AVP (Xing feedback); universal improvement = bias; need Necessity + within-comp control |

---

## Experiment Queue

### Next experiments (priority: respond to Xing's feedback first):
1. **Module 5 redo**: N.O.V.A. trait breakpoints within specific comps (Nova 95, Nova Yi), with/without emblem. Use Necessity not AVP. Apply causal inference. (Xing feedback 2026-04-22)
2. **Open questions**: Can we measure filter reliability? How does causal inference framework apply to TFT?
3. **Module 1 practice**: Study compositions.py filter patterns — document what expert-written filters look like
4. **Module 3 follow-up**: Build AVP ranking vs Build Necessity ranking — do they differ?
5. **Exploratory**: Do other traits show the same "universal improvement" bias pattern?

---

*Last updated: 2026-04-22*
