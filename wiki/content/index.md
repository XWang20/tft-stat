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
| 4 | Unit Evaluation | Which units matter most in a comp? | 🧪 | Shen most irreplaceable; level 10 Sona best; play rate ≠ necessity |
| 5 | Trait Breakpoints | When is 4->6 trait worth the cost? | 🧪 | Item rankings stable across tiers; selection bias persists within comps; filter leakage issue |
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
| [[concepts/metrics]] | ✅ | AVP, Necessity, Delta — definitions, math, when to use each |
| [[concepts/biases]] | ✅ | Three systematic biases: survivorship (biggest), player behavior, sample size |
| [[concepts/framework]] | ✅ | Question → filter → dimensions; primary carry vs secondary; question sourcing |

### Methods

| Page | Status | Summary |
|---|---|---|
| [[methods/filter-strategy]] | ✅ | Filter = control variables; primary carry/secondary; 5 expert patterns; design-from-scratch loop; Simpson's Paradox |
| [[methods/build-analysis]] | ✅ | Three-item builds, control variable, consistency check |
| [[methods/item-analysis-debiasing]] | 🧪 | Exclude special items (artifact/radiant/anima) + conflict recompute for shared-carry bias |

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

### Review Status
- 🧪 **draft** — agent submitted, not yet reviewed
- 🔄 **revision** — needs rework (feedback attached)
- ✅ **accepted** — conclusions reliable, findings integrated into wiki
- ❌ **rejected** — conclusions not trustworthy

| Page | Date | Module | Status | Summary |
|---|---|---|---|---|
| [[experiments/2026-04-21-vex-nova95-items]] | 2026-04-21 | 2 | ✅ | 5 metrics compared; Necessity + Builds converge; Red Buff/Dcap best |
| [[experiments/2026-04-22-vex-cross-comp-items]] | 2026-04-22 | 1 | 🧪 | Revised: Vex BIS across 4 comps with standardized filters; NOVA vs Vex 95 shows 4x Guinsoo's Nec gap; ad-hoc filters caused 3 sign flips in Dark Star |
| [[experiments/2026-04-22-cross-validation-vex-nova95]] | 2026-04-22 | 9 | ✅ | Spearman 0.993 — top 9 items match; Necessity values differ but rankings robust |
| [[experiments/2026-04-22-nova-trait-breakpoint]] | 2026-04-22 | 5 | 🧪 | Third revision: nova_yi focus (66k/120k); 5 NOVA doesn't change MasterYi itemization; AVP gap is selection bias |
| [[experiments/2026-04-22-build-vs-single-necessity]] | 2026-04-22 | 3 | ✅ | Build-implied rankings differ from single-item: Gunblade rises to #1, Guinsoo drops (ceiling effect); methods complementary |
| [[experiments/2026-04-22-filter-design-patterns]] | 2026-04-22 | 1 | 🧪 | 29 comp filters → 5 design patterns; LeBlanc Guinsoo invisible without filter; Nami Simpson's Paradox |
| [[experiments/2026-04-22-trait-breakpoint-multi-comp]] | 2026-04-22 | 5 | 🧪 | 3 traits × 3 comps: itemization stable across breakpoints; Necessity direction depends on carry leverage |
| [[experiments/2026-04-22-universal-improvement-bias]] | 2026-04-22 | 5 | 🧪 | 8 traits tested: 7/8 show higher tier = better AVP (selection bias); Anima Squad reverses (opportunity cost > trait value) |
| [[experiments/2026-04-22-filter-reliability]] | 2026-04-22 | 1/9 | 🧪 | Filter reliability depends on carry role: Vex ρ=0.976 (stable), Morde ρ=0.048 (unstable); tanks need cross-validation |
| [[experiments/2026-04-22-carry-leverage-necessity]] | 2026-04-22 | 5 | 🧪 | 5 comps tested: AP carry Necessity ↑ at higher tier, AD carry flat/↓; ΔAVP magnitude may be confound |
| [[experiments/2026-04-22-filter-design-clustering]] | 2026-04-22 | 1 | 🧪 | Discovered 7 comp patterns from 38 boards; compared with 29 expert definitions; carry uniqueness determines filter complexity |
| [[experiments/2026-04-22-xayah-stargazer-items]] | 2026-04-22 | 2, 7 | 🧪 | Xayah items × 7 Stargazers; core items stable; Guinsoo's diverges by Stargazer; IE negative is Jhin selection bias (conflict recompute) |
| [[experiments/2026-04-23-vex-third-item-build]] | 2026-04-23 | 2, 3 | 🧪 | GS+Guinsoo 后第三件：nova_95 Red Buff 最优，vex_95 Dcap 最优；Gunblade 被严重高估(32% play rate 排#8)；Void Staff 极度 comp 依赖 |
| [[experiments/2026-04-23-nova95-unit-evaluation]] | 2026-04-23 | 4 | 🧪 | Module 4 开篇：Shen Necessity 最高(+1.40)；十人口 Sona 是明确首选(3x Jhin)；Akali 高 play rate 低 Necessity |
| [[experiments/2026-04-23-tank-filter-reliability]] | 2026-04-23 | 1, 9 | 🧪 | 纠正前实验：真正带装的 tank(Nasus/Poppy/Cho) ρ=0.929-1.000，与 carry 一样稳定；Galio 揭示 comp-specific 物品反转现象 |

### Experiment Queue

(empty — generate from open questions)

### Experiment Lifecycle

```
agent writes draft → status: 🧪 draft
Xing reviews       → status: ✅ accepted | 🔄 revision | ❌ rejected
                      feedback written in report's "## Review" section
if 🔄 revision     → agent revises or creates follow-up experiment
```

Every experiment report includes a **## Review** section at the end. Xing's feedback goes there regardless of status. Feedback is never deleted — it's the most valuable part.

**Lesson routing** after review:
- Knowledge findings → integrate into `concepts/` or `methods/` pages
- Process lessons ("never do X again") → append to `lab-checklist.md` Lessons Learned

---

**Maintenance**: [[schema]] (rules) · [[log]] (timeline) · [[lab-checklist]] (preflight)
**Last updated**: 2026-04-23 · **Contributors**: Xing (teacher), Agent (learner)
