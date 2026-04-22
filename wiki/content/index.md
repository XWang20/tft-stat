# TFT Data Science Wiki

> **Purpose**: Persistent knowledge base for TFT statistical analysis.
> **Pattern**: [Karpathy's LLM Wiki](https://x.com/karpathy/status/2039805659525644595) — compiled once, kept current, not re-derived.
> **Audience**: Any new agent instance bootstraps from here.

**New agent?** Read: this page → [[course]] → [[lab-checklist]] → start working.
**Returning?** Check [[log]] for what changed since last session.

---

## Concepts

| Page | Status | Summary |
|---|---|---|
| [[concepts/metrics]] | ✅/🧪 | AVP, Necessity, Delta — definitions, math, when to use each |
| [[concepts/biases]] | ✅ | Three systematic biases: survivorship (biggest), player behavior, sample size |
| [[concepts/framework]] | ✅ | Three orthogonal dimensions: filter strategy × data granularity × metric selection |

## Methods

| Page | Status | Summary |
|---|---|---|
| [[methods/filter-strategy]] | ✅ | Conditioning as foundation; Simpson's Paradox; exclude→toggle; filter checklist |
| [[methods/build-analysis]] | ✅ | Three-item builds, control variable, consistency check |

## Tools

| Page | Status | Summary |
|---|---|---|
| [[tools/metatft-api]] | ✅ | Explorer API: 9 endpoints, filter format, common params |

## Sources

| Page | Author | Key Contribution |
|---|---|---|
| [[sources/morbrid-reddit-post]] | morbrid | CI math, sample size thresholds, bias taxonomy |
| [[sources/aesah-data-mistakes]] | Aesah | Play rate weighted formula → Necessity derivation |
| [[sources/morbrid-aesah-talk]] | morbrid + Aesah | Graph view, exclude→toggle, advanced mode, don't specify stars |
| [[sources/dishsoap-frodan-stats]] | Dishsoap + Frodan | "Add context first", builds > single items, sample size underrated |

## Experiments

| Page | Date | Module | Summary |
|---|---|---|---|
| [[experiments/vex-nova95]] | 2026-04-21 | 2 | 5 metrics compared; Necessity + Builds converge; Red Buff/Dcap best |
| [[experiments/vex-cross-comp-items]] | 2026-04-21 | 1 | Vex BIS changes across comps; filter = foundation validated |
| [[experiments/cross-validation-vex-nova95]] | 2026-04-21 | 9 | Blocked on tftable API; pending |
| [[experiments/nova-trait-breakpoint]] | 2026-04-22 | 5 | Used AVP (wrong!); needs redo with Necessity |
| [[experiments/reflections-2026-04-21]] | 2026-04-21 | — | Don't bring conclusions to data; shrinkage ≠ debiasing |
| [[experiments/reflections-2026-04-22]] | 2026-04-22 | — | Don't regress to AVP; control variables within comps |

---

**Maintenance**: [[schema]] (rules) · [[log]] (timeline) · [[course]] (syllabus) · [[lab-checklist]] (preflight)
**Last updated**: 2026-04-22 · **Contributors**: Xing (teacher), Agent (learner)
