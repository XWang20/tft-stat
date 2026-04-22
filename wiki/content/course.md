# TFT Data Science Course

> **Goal**: Master TFT data retrieval and statistical analysis.
> **Method**: Each module has concepts, readings, and experiments. The agent runs 3 experiments daily, writes reports, cross-validates with tftable. Xing reviews daily, discusses, corrects.
> **Outcome**: A reusable agent that any new Claude instance can bootstrap from.

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

3 experiments per day. Each experiment:
1. Starts from a **core question** (module-related, follow-up, or exploratory)
2. Reads `lab-checklist.md` — no exceptions
3. Explores with data — **data first, conclusions after**
4. Produces a report in `experiments/` (story format)
5. Cross-validates with tftable when available
6. Updates wiki: `index.md`, `course.md`, `log.md`, relevant concept/method pages

### Experiment Sources
- **Module exercises**: directly practice the current topic
- **Follow-ups**: open questions from previous experiments
- **Previews**: explore next module's territory before formal study
- **Surprises**: unexpected findings, contradictions, things nobody asked about
- **Cross-validations**: compare our methods with tftable's answers

### Cross-Validation Protocol
1. Query tftable for the same data point (tftable = ground truth)
2. Compare our result with tftable's
3. Agree → confidence++. Disagree → investigate why.

**Note**: tftable programmatic API not yet available. Xing will provide later.

---

## Progress Tracker

| Module | Status | Key Experiments | Key Learnings |
|---|---|---|---|
| 0 | ✅ | API exploration (2026-04-21) | 9 endpoints discovered, filter format documented |
| 1 | ✅ | vex-cross-comp-items (2026-04-21) | Filter is foundation; same unit different comp = different BIS |
| 2 | ✅ | vex-nova95 (2026-04-21) | Necessity best single metric; Edge ≡ AVP; shrinkage doesn't fix bias |
| 3 | 🧪 | vex-nova95 supplementary | Control variable + consistency check validated |
| 4 | ⬜ | — | — |
| 5 | 🧪 | nova-trait-breakpoint (2026-04-22) | REDO: used AVP; need Necessity + within-comp control |
| 6–9 | ⬜ | — | — |

---

## Experiment Queue

Priority order:
1. **Module 5 redo**: N.O.V.A. trait breakpoints within specific comps, using Necessity not AVP
2. **Module 1 practice**: Study compositions.py filter patterns — document expert filter design
3. **Module 3 follow-up**: Build Necessity ranking vs single-item Necessity — do they differ?
4. **Exploratory**: Do other traits show the same "universal improvement" bias pattern?
5. **Open**: Can we measure filter reliability? Causal inference framework for TFT?

---

*Last updated: 2026-04-22*
