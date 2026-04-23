# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Purpose

This repo is a **TFT (Teamfight Tactics) data science training system** — it teaches an AI agent to perform rigorous statistical analysis of TFT game data using MetaTFT as the primary tool. The goal is to produce a reusable agent that any new Claude instance can bootstrap from.

Two main components:
1. **`tft_stat/`** — Python package: MetaTFT API client, metrics, filter expression tree, 29 S17 comp definitions
2. **`wiki/`** — Quartz-based knowledge wiki (Karpathy-style) that accumulates domain knowledge across sessions

## Architecture

```
tft-stat/
├── cli.py                        # CLI entry point (subcommands: comps/total/units/items/core/scout/games)
├── tft_stat/                     # Core library (Python 3, stdlib only)
│   ├── api.py                    # MetaTFT Explorer API client
│   ├── metrics.py                # placement_stats, necessity/edge calculations
│   ├── filter_params.py          # Expression tree + CLI specs → API query params
│   ├── filter_expr.py            # Boolean expression tree (Unit/Trait/And/Or/Not)
│   ├── compositions.py           # 29 S17 comp definitions (from XWang20/tft_data)
│   ├── item_classes.py           # Item categories: TANK, DMG, BRUISER item ID sets
│   └── config/pbe/               # traits.json (breakpoints), items.json (names)
└── wiki/                         # Quartz wiki (separate git repo)
    └── content/
        ├── index.md              # Entry point — syllabus, knowledge catalog, experiments
        ├── lab-checklist.md      # MUST READ before every experiment
        ├── schema.md             # Wiki maintenance rules
        ├── concepts/             # Core ideas (metrics, biases, framework)
        ├── methods/              # Techniques (filter-strategy, build-analysis)
        ├── tools/                # API docs (metatft-api)
        ├── sources/              # Summaries of raw learning materials
        └── experiments/          # Analysis reports + reflections
```

## CLI Usage

```bash
# List all 29 compositions
python3 cli.py comps

# Query using comp definition (recommended)
python3 cli.py total --comp nova_95
python3 cli.py units --comp nova_95
python3 cli.py items TFT17_Vex --comp nova_95

# Filter by player level (all subcommands)
python3 cli.py units --comp nova_95 --level 10

# --comp and --filter stack (comp provides base filter, --filter adds on top)
python3 cli.py units --comp nova_95 --level 10 --filter "\
Unit('TFT17_Aatrox') & Unit('TFT17_Akali') & Unit('TFT17_Vex') \
& Unit('TFT17_Fiora') & Unit('TFT17_Shen') & Unit('TFT17_Graves') \
& Unit('TFT17_Morgana') & Unit('TFT17_Blitzcrank') & Unit('TFT17_Nunu')"

# Board composition detection (primary board, star levels)
python3 cli.py core --comp nova_95

# Item analysis with item class exclusion (for hero augment decontamination)
python3 cli.py items TFT17_Nasus --comp bonk --normal-only --exclude-dmg-items
python3 cli.py items TFT17_Nasus --comp bonk --normal-only --exclude-tank-items

# Cross-validate with tftable (SSH to desktop, compare necessity rankings)
python3 cli.py tftable TFT17_Vex --comp nova_95

# Cross-validate unit necessity (omit unit for unit-level comparison)
python3 cli.py tftable --comp nova_95

# Manual filter (can combine with --comp)
python3 cli.py items TFT17_Vex \
    --or-units TFT17_Fiora:i3,TFT17_Vex:i3,TFT17_Graves:i3 \
    --traits TFT17_DRX:2 \
    --exclude-units TFT17_Kindred
```

Unit spec syntax: `TFT17_Vex:s2:i3` (s=star, i=items). Trait spec: `TFT17_DRX:2` (min_units, auto-converts to tier).

### Subcommands

| Command | Purpose |
|---|---|
| `comps` | List all 29 composition definitions |
| `total` | Overall stats (games, AVP, top4%, win%) |
| `units` | Per-unit stats within a comp |
| `items` | Item stats for a specific unit |
| `core` | Board compositions via `exact_units_traits2` (primary board detection, star levels) |
| `tftable` | Cross-validate against tftable ground truth |
| `scout` | Scan top player endgame boards |
| `games` | Show sample boards matching a filter (sanity check) |

### Global Flags

| Flag | Applies To | Description |
|---|---|---|
| `--comp` | all | Use a composition definition as base filter |
| `--filter` | all | Additional filter expression (stacks with --comp) |
| `--level N` | all | Player level filter (1-10) |
| `--normal-only` | items | Exclude artifact/radiant/trait/emblem items |
| `--exclude-tank-items` | items | Exclude tank items (Warmog, Gargoyle, etc.) |
| `--exclude-dmg-items` | items | Exclude damage items (Guinsoo, IE, Dcap, etc.) |
| `--exclude-bruiser-items` | items | Exclude bruiser items (BT, GA, Gunblade, etc.) |

## Library Usage

```python
from tft_stat.api import query
from tft_stat.filter_params import build_filter_params
from tft_stat.metrics import placement_stats

params = build_filter_params(comp="nova_95")
data = query("total", params)
stats = placement_stats(data["data"][0]["placement_count"])
```

## Critical Domain Rules — Read Before Any Analysis

1. **NEVER rank items by raw AVP** — survivorship bias makes low-frequency items look artificially good. Use **Necessity** (`w/o_AVP - overall_AVP`) as primary ranking metric.
2. **Edge ≡ AVP** — algebraically trivial transformation, provides no additional information. Don't use it.
3. **Filter is foundation** — always set comp context (traits + key units) before analyzing. Without proper conditioning, all metrics analyze polluted data (Simpson's Paradox).
4. **Sample size ≥ 1000 games** for mature patches, ≥ 300 for new patches. Use 99% CI when rows > 50.
5. **Builds > single items** — three-item build analysis largely eliminates carousel survivorship bias.
6. **Data first, conclusions after** — never bring a conclusion to the data looking for confirmation.

Math relationships:
```
p = play_rate, a = item_AVP, A = overall_AVP
Necessity = p/(1-p) × (A - a)
Delta = -(A - a)/(1-p)
```

---

## Behavioral Guidelines — How to Think and Work

### 1. Bootstrap: Read the Wiki First

**Every new session starts cold. The wiki is your memory.**

Before any analysis or experiment:
- Read `wiki/content/index.md` — understand what exists
- Read `wiki/content/index.md` — understand the syllabus and current progress
- Read `wiki/content/lab-checklist.md` — internalize the rules

Don't rely on what you "know" from training. The wiki captures hard-won lessons (e.g., Edge ≡ AVP) that your training data doesn't contain.

### 2. Data First, Conclusions After

**You are a scientist, not a debater. Don't bring conclusions to data.**

- State the question before touching any data.
- Show the data. Let it speak. If it surprises you, that's good.
- If two methods disagree, investigate why — don't pick the one you prefer.
- If a result looks wrong, it might be right. Investigate before dismissing.
- Acknowledge limitations and open questions. Uncertainty is not weakness.

Ask yourself: "Am I looking for truth, or for confirmation?" If the latter, stop.

### 3. Filter Before Measure

**Without proper conditioning, all metrics are polluted. Filter is Dimension 1.**

Before analyzing any metric:
- Define the comp context (traits + key units). Never analyze a unit in isolation.
- Use `compositions.py` definitions when available — these are expert-curated.
- Check sample size. Below 1000 games on a mature patch = proceed with caution.
- Sanity check: would a real player recognize these games as "this comp"?

The three dimensions are orthogonal. But **filter comes first** because bad conditioning makes the other two dimensions meaningless.

### 4. Cross-Validate Everything

**A result from one method is a hypothesis. Convergence across methods is evidence.**

- Single-item analysis → supplement with build analysis.
- Necessity ranking → compare with control variable results.
- Our pipeline → cross-check against tftable when available.
- If methods agree → confidence increases.
- If methods disagree → that's the interesting part. Investigate.

### 5. Compound Knowledge, Don't Re-derive

**The wiki is a persistent artifact. Each experiment must leave the system more capable.**

Every experiment produces three outputs:
1. **Report** — the narrative in `experiments/`
2. **Code** — if a new method is discovered, implement it in `tft_stat/` or `cli.py`
3. **Knowledge** — substantively deepen the relevant `concepts/` or `methods/` page

Bad: "Added lesson #9 to lab-checklist: don't do X"
Good: Rewrote `concepts/biases.md` Selection Bias section with quantified examples and a decision framework.

Two self-checks:
- "Can the system do something it couldn't before?" (code)
- "Does a new agent reading the wiki understand this topic more deeply?" (knowledge)

### 6. Experiments Are Stories

**Reports are narratives, not tables. Each experiment tells a story with chapters.**

```
# Experiment: [Title]
Status: 🧪 draft
Date: YYYY-MM-DD
Module: N

## The Question          ← what are we trying to learn?
## Chapter 1-N           ← data-driven narrative, show the journey
## Cross-Validation      ← vs tftable (mandatory when available)
## What I Learned        ← synthesis
## Open Questions        ← seeds for future experiments
## Questions for Xing    ← things that need human judgment
## Review                ← Xing's feedback goes here (added after review)
```

Experiment review states: `🧪 draft` → `✅ accepted` | `🔄 revision` | `❌ rejected`.
Feedback is never deleted — it's the most valuable part of the report.

After review, route lessons:
- Knowledge findings → integrate into `concepts/` or `methods/` pages
- Process lessons ("never do X again") → append to `lab-checklist.md` Lessons Learned

### 7. Surprise Over Routine

**Experiments should teach something unexpected. Follow curiosity.**

Good experiment topics:
- Follow-ups from open questions in previous experiments
- Contradictions between methods or data sources
- Previews of upcoming course modules
- Things nobody asked about but the data hints at

Bad experiment topics:
- Repeating what we already know
- Confirming what we expect without risk of surprise
- Topics chosen because they're easy, not because they're interesting

### 8. Questions Come From Players, Not From Statistics

**You don't play the game. Find questions from people who do.**

Two sources for good questions:
1. **Community** (Reddit /r/CompetitiveTFT, Discord) — find what players debate. "Giant Slayer vs JG on Vex?" is a real question with a decision point. Data can settle the argument.
2. **Top player match history** — scan 50+ endgame boards from Challenger/GM players. Spot new comps, unusual builds, emerging meta shifts. This reveals questions like "why are top players building X on Y?" and helps improve compositions.py filters.

A good question is **decision-oriented** ("Should I build X or Y?"), not exploratory ("What's the relationship between X and Y?"). Every question should map to a player decision point.

### 9. Filter = Controlling Variables

**Filter is not data preprocessing. It defines what question you're asking.**

- Every unit is either primary carry (主C) or secondary (副C) — itemization differs completely between these roles
- Primary carry vs secondary is determined by the comp context
- `Unit('TFT17_Vex', item_min=3)` means "Vex is the primary carry" not "games with Vex"
- Your question determines what to control for → filter is the implementation of that control
- Poorly defined question = poorly defined filter = unreliable conclusions

---

## Wiki Maintenance

The wiki follows a three-layer architecture (see `wiki/content/schema.md`):
- **Layer 1** (immutable): `sources/*.txt` — raw transcripts, never edit
- **Layer 2** (maintained): `concepts/`, `methods/`, `tools/`, `experiments/` — integrate new knowledge
- **Layer 3**: `schema.md` — rules

Conventions: wikilinks `[[folder/page]]`, status tags (✅ 🧪 ❌), kebab-case filenames.

## Cross-Validation

tftable data (ground truth) is at `wangxing@DESKTOP-QTEB3KH:/home/wangxing/project/tft_data/analysis/team_comp_sections`. Comp definitions are in `compositions.py` at `XWang20/tft_data` on GitHub.

## Daily Cronjob Experiments

3 experiments per day (crontab: 9:00, 14:00, 20:00). Each run:
1. **Process GitHub Issues first** — feedback, conclusions, revisions, new topics
2. Pick experiment from queue → run → write report → update wiki → commit & push

### GitHub Issues as Feedback Pipeline

Xing creates issues on `XWang20/tft-stat` with labels:
- **feedback** → record in experiment's `## Review` section + lab-checklist if process lesson
- **conclusion** → integrate into `concepts/` or `methods/` wiki pages
- **revision** → revise the specified experiment
- **topic** → add to Experiment Queue in index.md

Agent processes all open issues before starting new experiments, then closes them with a summary comment.

### Giscus Comments as Review Pipeline

Xing reviews experiments via Giscus comments directly on wiki pages (backed by GitHub Discussions).

- **"accept"** → update status to ✅ in report and index.md
- **feedback text** → record in report's `## Review` section, update status to 🔄
- **conclusion** → integrate into concepts/ or methods/ pages

Agent checks Discussions for XWang20 comments each cron run.
