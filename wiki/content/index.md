# TFT Data Science Wiki

> **Purpose**: Persistent knowledge base for TFT statistical analysis.
> **Pattern**: [Karpathy's LLM Wiki](https://x.com/karpathy/status/2039805659525644595) — compiled once, kept current, not re-derived.
> **Goal**: Master TFT data retrieval and analysis. Become better than the teacher.

**New agent?** Read: this page → [[lab-checklist]] → start working.
**Returning?** Check [[log]] for what changed since last session.

---

## Syllabus

| Module | Topic | Core Question | Status | Key Learnings |
|---|---|---|---|---|
| 0 | Foundations | What data do we have and where does it come from? | ✅ | 9 endpoints discovered, filter format documented |
| 1 | Filter Design | How do we define "this comp" precisely? | ✅ | Filter is foundation; same unit different comp = different BIS |
| 2 | Item Metrics | Given a comp, what metric tells us if an item is good? | ✅ | Necessity best single metric; Edge ≡ AVP; shrinkage doesn't fix bias |
| 3 | Build Analysis | How do item combinations interact? | 🧪 | Control variable + consistency check validated |
| 4 | Unit Evaluation | Which units matter most in a comp? | ⬜ | — |
| 5 | Trait Breakpoints | When is 4→6 trait worth the cost? | 🧪 | REDO: used AVP; need Necessity + within-comp control |
| 6 | Comp Comparison | How do we compare two different comps? | ⬜ | — |
| 7 | Emblem & Augment | What's the best emblem/augment for a comp? | ⬜ | — |
| 8 | Temporal Analysis | How does the meta shift within a patch? | ⬜ | — |
| 9 | Cross-Validation | When should we trust our results? | ⬜ | — |

### Readings by Module

| Module | Concepts | Readings |
|---|---|---|
| 0 | Endgame snapshots, API endpoints | [[sources/morbrid-reddit-post]], [[tools/metatft-api]] |
| 1 | Conditioning, Simpson's Paradox | [[sources/dishsoap-frodan-stats]], [[methods/filter-strategy]] |
| 2 | AVP, Delta, Necessity, survivorship bias | [[sources/aesah-data-mistakes]], [[concepts/metrics]] |
| 3 | Builds, control variable, consistency check | [[sources/dishsoap-frodan-stats]], [[methods/build-analysis]] |
| 4 | Unit Necessity, carry vs support | [[sources/morbrid-aesah-talk]] |
| 5 | Trait Delta, opportunity cost | [[sources/dishsoap-frodan-stats]] |
| 6 | Strength, AVP distribution, matchups | tftable comps data |
| 7 | Plus-one traits, augment proxies | [[sources/morbrid-aesah-talk]] |
| 8 | Day-over-day trends, early vs late patch | — |
| 9 | Convergence of methods, confidence | All prior modules |

---

## Knowledge Base

### Concepts

| Page | Status | Summary |
|---|---|---|
| [[concepts/metrics]] | ✅/🧪 | AVP, Necessity, Delta — definitions, math, when to use each |
| [[concepts/biases]] | ✅ | Three systematic biases: survivorship (biggest), player behavior, sample size |
| [[concepts/framework]] | ✅ | Three orthogonal dimensions: filter strategy × data granularity × metric selection |

### Methods

| Page | Status | Summary |
|---|---|---|
| [[methods/filter-strategy]] | ✅ | Conditioning as foundation; Simpson's Paradox; exclude→toggle; filter checklist |
| [[methods/build-analysis]] | ✅ | Three-item builds, control variable, consistency check |

### Tools

| Page | Status | Summary |
|---|---|---|
| [[tools/metatft-api]] | ✅ | Explorer API: 9 endpoints, filter format, common params |

### Sources

| Page | Author | Key Contribution |
|---|---|---|
| [[sources/morbrid-reddit-post]] | morbrid | CI math, sample size thresholds, bias taxonomy |
| [[sources/aesah-data-mistakes]] | Aesah | Play rate weighted formula → Necessity derivation |
| [[sources/morbrid-aesah-talk]] | morbrid + Aesah | Graph view, exclude→toggle, advanced mode, don't specify stars |
| [[sources/dishsoap-frodan-stats]] | Dishsoap + Frodan | "Add context first", builds > single items, sample size underrated |

---

## Experiments

| Page | Date | Module | Summary |
|---|---|---|---|
| [[experiments/vex-nova95]] | 2026-04-21 | 2 | 5 metrics compared; Necessity + Builds converge; Red Buff/Dcap best |
| [[experiments/vex-cross-comp-items]] | 2026-04-21 | 1 | Vex BIS changes across comps; filter = foundation validated |
| [[experiments/cross-validation-vex-nova95]] | 2026-04-21 | 9 | Blocked on tftable API; pending |
| [[experiments/nova-trait-breakpoint]] | 2026-04-22 | 5 | Used AVP (wrong!); needs redo with Necessity |
| [[experiments/reflections-2026-04-21]] | 2026-04-21 | — | Don't bring conclusions to data; shrinkage ≠ debiasing |
| [[experiments/reflections-2026-04-22]] | 2026-04-22 | — | Don't regress to AVP; control variables within comps |

### Experiment Queue

1. **Module 5 redo**: N.O.V.A. trait breakpoints within specific comps, using Necessity not AVP
2. **Module 1 practice**: Study compositions.py filter patterns — document expert filter design
3. **Module 3 follow-up**: Build Necessity ranking vs single-item Necessity — do they differ?
4. **Exploratory**: Do other traits show the same "universal improvement" bias pattern?
5. **Open**: Can we measure filter reliability? Causal inference framework for TFT?

### Experiment Protocol

3 experiments per day. Each experiment:
1. Read [[lab-checklist]] — no exceptions
2. Start from a core question → explore with data → produce report in `experiments/`
3. Cross-validate with tftable when available
4. Update this page (experiments table + syllabus status) and [[log]]

---

**Maintenance**: [[schema]] (rules) · [[log]] (timeline) · [[lab-checklist]] (preflight)
**Last updated**: 2026-04-22 · **Contributors**: Xing (teacher), Agent (learner)
