# TFT Data Science Wiki — Schema

> Layer 3: Rules and conventions for how this wiki is maintained.
> This file is the "CLAUDE.md" equivalent — it tells the LLM how to behave.

## Wiki Location
`comp-retrieval/wiki/`

## Folder Structure

```
wiki/
├── index.md          # Content catalog, one-line summaries, entry point
├── log.md            # Append-only chronological record
├── schema.md         # THIS FILE — rules and conventions
├── raw/              # Layer 1: immutable source transcripts/notes
├── sources/          # Layer 1→2 bridge: one summary per raw source
├── concepts/         # Core ideas, definitions, frameworks
├── methods/          # Techniques, workflows, how-tos
├── tools/            # Software, APIs, scripts
├── experiments/      # Analysis results, comparisons
└── people/           # Notable individuals
```

## Page Format

```markdown
# Title
**Status**: ✅ verified | 🧪 exploring | ❌ deprecated

(content with [[wikilinks]])

## Sources
- [[sources/source-name]] — what it contributed
```

## Log Format

Parseable: `grep "^## \[" log.md | tail -5`

```
## [YYYY-MM-DD] ingest | Source Title
## [YYYY-MM-DD] query | Question summary
## [YYYY-MM-DD] lint | Health check
## [YYYY-MM-DD] experiment | Name
## [YYYY-MM-DD] concept | New concept
```

## Ingest Workflow

1. Drop raw source into `raw/` (immutable, never edit after)
2. Create `sources/<name>.md` — metadata, key takeaways, pages updated
3. Update all relevant concept/method/tool pages — integrate, don't just add
4. Update `index.md` — add/update entry with one-line summary
5. Append `log.md`
6. Target: 5-15 pages touched per source

## Query Workflow

1. Read `index.md` → find relevant pages by summary
2. Read those pages → synthesize answer
3. Cite with `[[page]]` links
4. If answer is valuable → offer to file as new page

## Lint Checklist

- [ ] Contradictions between pages
- [ ] Orphan pages (no inbound links)
- [ ] Concepts mentioned but missing own page
- [ ] Stale claims superseded by newer sources
- [ ] Missing cross-references

## Conventions

- Wikilinks: `[[folder/page-name]]`
- Status tags: ✅ verified, 🧪 exploring, ❌ deprecated
- File names: kebab-case
- Raw sources: NEVER modify after initial drop
- Sign convention: positive = good (Edge), lower = better (AVP)

## Deployment

```bash
cd /home/xing/projects/tft-data-science-wiki && ./update-wiki.sh
```
→ Syncs to GitHub → Quartz builds → GitHub Pages deploys
→ URL: https://xwang20.github.io/tft-data-science-wiki/
