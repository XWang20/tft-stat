# TFT Data Science Wiki — Schema

> Layer 3: Rules for how this wiki is maintained.
> This is the meta-document — it tells the agent how to operate the wiki.

## Wiki Location

`wiki/content/` within the `tft-stat` repo.

Deployed via GitHub Pages: https://xwang20.github.io/tft-stat/

## Folder Structure

```
wiki/content/
├── index.md          # Entry point — syllabus, knowledge catalog, experiments
├── lab-checklist.md  # MUST READ before every experiment
├── log.md            # Append-only chronological record
├── schema.md         # THIS FILE — rules and conventions
├── concepts/         # Core ideas, definitions, frameworks
├── methods/          # Techniques, workflows, how-tos
├── tools/            # Software, APIs, scripts
├── sources/          # Layer 1→2 bridge: one summary per raw source
│   └── *.txt         # Layer 1: immutable raw transcripts
└── experiments/      # Analysis reports, reflections
```

## Three-Layer Architecture

| Layer | Contents | Mutability |
|---|---|---|
| 1 | `sources/*.txt` — raw transcripts, notes | **Immutable** — never edit after creation |
| 2 | `concepts/`, `methods/`, `tools/`, `experiments/` | **Maintained** — integrate new knowledge |
| 3 | `schema.md` — this file | **Rules** — update when workflow changes |

## Page Format

```markdown
# Title
**Status**: ✅ verified | 🧪 exploring | ❌ deprecated

(content with [[wikilinks]])

## Sources
- [[sources/source-name]] — what it contributed
```

## Workflows

### Ingest (new source material)
1. Drop raw source into `sources/` as `.txt` (immutable, never edit after)
2. Create `sources/<name>.md` — metadata, key takeaways, pages updated
3. Update all relevant concept/method/tool pages — **integrate, don't just append**
4. Update `index.md` — add/update entry with one-line summary
5. Append `log.md`
6. Target: 5-15 pages touched per source

### Experiment
1. Read `lab-checklist.md` — no exceptions
2. Write report in `experiments/<name>.md` using story format, status: `🧪 draft`
3. Update `index.md` (experiments table + syllabus status), `log.md`
4. After Xing review → update status to `✅ accepted` | `🔄 revision` | `❌ rejected`
5. Write feedback in report's `## Review` section — feedback is never deleted
6. Route lessons: knowledge → `concepts/` or `methods/`; process → `lab-checklist.md` Lessons Learned
7. `git push`

### Query
1. Read `index.md` → find relevant pages by summary
2. Read those pages → synthesize answer
3. Cite with `[[page]]` links
4. If answer is valuable → offer to file as new page

### Lint
- [ ] Contradictions between pages
- [ ] Orphan pages (no inbound links from index)
- [ ] Concepts mentioned but missing own page
- [ ] Stale claims superseded by newer sources
- [ ] Missing cross-references

## Log Format

Parseable: `grep "^## \[" log.md | tail -5`

Every log entry MUST include `[[wikilinks]]` to all files modified. Example:

```
## [2026-04-22] cron | Issue processing + experiment
- Issue #1 (revision): revised [[experiments/2026-04-22-nova-trait-breakpoint]] — switched to nova_yi
- Issue #3 (conclusion): updated [[methods/filter-strategy]] — added "Trust compositions.py" section
- New experiment: [[experiments/unit-eval-nova95]] — Module 4
- Updated: [[lab-checklist]] (lesson #8), [[index]] (experiments table, syllabus)

## [YYYY-MM-DD] ingest | Source Title
- Created [[sources/source-name]], updated [[concepts/metrics]], [[methods/filter-strategy]]

## [YYYY-MM-DD] experiment | Experiment Name
- Created [[experiments/name]], updated [[index]] (table + syllabus)
```

## Conventions

- Wikilinks: `[[folder/page-name]]`
- Status tags: ✅ verified, 🧪 exploring, ❌ deprecated
- File names: kebab-case
- Raw sources: NEVER modify after initial drop
- Sign convention: positive = good (Necessity), lower = better (AVP)
