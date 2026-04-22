# TFT Data Science Wiki

> Personal knowledge base for TFT statistical analysis.
> Pattern: [Karpathy's LLM Wiki](https://x.com/karpathy/status/2039805659525644595)
>
> **Layer 1** — Raw sources (immutable): `sources/*.txt` + `sources/reference-*.md`
> **Layer 2** — Wiki (LLM-maintained): `concepts/`, `methods/`, `tools/`, `experiments/`, `people/`
> **Layer 3** — Schema: `schema.md`
>
> The wiki is a persistent, compounding artifact. Knowledge is compiled once and kept current, not re-derived on every query.

## Operations

- **Ingest**: Drop source into raw/ → `sources/` summary → update concept/method pages → append `log.md`
- **Query**: Read index → find relevant pages → synthesize answer → optionally file back as new page
- **Lint**: Audit for contradictions, orphan pages, stale claims, missing cross-references

---

## Concepts

| Page | Status | Summary |
|---|---|---|
| [[concepts/metrics]] | ✅/🧪 | AVP, Edge (🧪), Necessity, Delta — definitions, math relations, when to use each |
| [[concepts/biases]] | ✅ | Three systematic biases: survivorship (biggest), player behavior, sample size |
| [[concepts/framework]] | ✅ | Three orthogonal dimensions: metric selection × data granularity × filter strategy |

## Methods

| Page | Status | Summary |
|---|---|---|
| [[methods/filter-strategy]] | ✅ | Conditioning as foundation; Simpson's Paradox; checklist; exclude→toggle technique |
| [[methods/build-analysis]] | ✅ | Three-item builds, control variable, consistency check; Vex experiment validated |

## Tools

| Page | Status | Summary |
|---|---|---|
| [[tools/metatft-api]] | ✅ | Explorer API: 9 endpoints, filter format, common params |

## Sources

| Page | Author | Key Contribution |
|---|---|---|
| [[sources/morbrid-reddit-post]] | morbrid | CI math, sample size thresholds, bias taxonomy |
| [[sources/aesah-data-mistakes]] | Aesah | Play rate weighted formula (Necessity derivation) |
| [[sources/morbrid-aesah-talk]] | morbrid + Aesah | Graph view, exclude→toggle, advanced mode, don't specify stars |
| [[sources/dishsoap-frodan-stats]] | Dishsoap + Frodan | "Add context first", builds > single items, sample size underrated |

## Experiments

| Page | Date | Summary |
|---|---|---|
| [[experiments/vex-nova95]] | 2026-04-21 | 5 metrics compared; Necessity + Builds converge; Red Buff/Dcap best marginal |
| [[experiments/reflections-2026-04-21]] | 2026-04-21 | What I learned: don't bring conclusions to data, shrinkage ≠ debiasing |
| [[experiments/vex-cross-comp-items]] | 2026-04-21 | Vex BIS changes across comps; filter = foundation validated |
| [[experiments/cross-validation-vex-nova95]] | 2026-04-21 | Blocked on tftable API; pending |
| [[experiments/nova-trait-breakpoint]] | 2026-04-22 | N.O.V.A. breakpoints; used AVP (wrong!); needs redo with Necessity |
| [[experiments/reflections-2026-04-22]] | 2026-04-22 | Xing feedback: don't regress to AVP; control variables within comps; checklist ≠ textbook |

## People

(To be populated as we reference more analysts/players)

---

## Maintenance

- **Log**: [[log]] — parseable chronological record
- **Course**: [[course]] — syllabus, progress, experiment queue
- **Last lint**: not yet performed
- **Last updated**: 2026-04-22
- **Contributors**: Xing, Mochi
- **Page count**: 7 concept/method + 4 source + 5 experiment + 1 checklist + 1 course = 18 pages
