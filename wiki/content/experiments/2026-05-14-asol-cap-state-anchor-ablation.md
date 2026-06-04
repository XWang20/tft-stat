---
title: "Asol comps: cap-state lens + anchor ablation by gained set"
date: 2026-05-14
module: 1
status: 🧪 draft
---

# Experiment: Asol Comps — Cap-State Lens & Anchor Ablation by Gained Set

**Status**: 🧪 draft
**Date**: 2026-05-14 (data re-verified 2026-06-04)
**Module**: 1 (Filter Design)

> Note on numbers: this report's board counts and AVPs come from a 2026-06-04
> re-run on the live patch. The earlier 2026-05-14 pass produced the same
> *qualitative* verdicts with different magnitudes (patch drift). Every verdict
> below was reproduced; only the digits moved.

## The Question

Two filter-design questions surfaced while trying to write `compositions.py`
definitions for the Aurelion Sol family:

1. **The Asol Mecha=3 comp looked weak** — aggregate AVP ~4.3, top4 ~54%. Is it
   actually a bad comp, or is the aggregate lying?
2. **Which units belong in an Asol filter as anchors?** Asol shows up in at least
   two distinct shells (a Summon-trait board and a Galio/Morde frontline board).
   How do we decide which co-occurring units to pin as constraints — and how do we
   know an anchor isn't just smuggling in contamination from a neighboring comp?

Both turn out to be the same lesson from two angles: **aggregate numbers blend
sub-populations, and you cannot design a filter by watching a scalar move. You
have to look at the boards.**

## Chapter 1 — The Aggregate Lies: Cap-State vs Transition-Death

The `mecha` comp (`Mecha>=3 & Asol i2 & Galio i2`) by aggregate:

| Slice | Games | AVP | Top4 |
|---|---|---|---|
| Aggregate (all levels) | 147,196 | 4.31 | 53.7% |
| Level 9 cap | 63,503 | 3.62 | 68.4% |
| Level 10 cap | 18,865 | **2.17** | **93.2%** |

The 4.31 aggregate is a weighted average of two completely different
sub-populations:
- **Transition-death boards**: players who ran the comp but died at level 7–8 with
  it half-assembled. These dominate the count and pull the mean toward 5–6.
- **Cap-state boards**: players who reached level 10 and assembled the full board.
  These place 2.17 — an excellent comp.

Calling this comp "weak" by its 4.31 aggregate is a category error. The comp's
*ceiling* is elite; it's just hard to execute (many runs die in transition). The
aggregate measures **execution difficulty blended with comp strength**, and you
cannot separate them without conditioning on level.

**Rule extracted**: always run `--level 9` and `--level 10` separately. Aggregate
AVP and aggregate unit-frequency are both diluted by transition deaths. A unit at
30% aggregate frequency can be 85% at cap — only the cap number reflects comp
identity.

## Chapter 2 — Two Asol Shells

At cap, Asol resolves into two distinct comps, not one flex blob:

**summon_asol** — `Asol i3 & Summon>=3`. Cap-state lv10: 7,628 games, AVP **1.99**,
top4 95.4%. Primary board:
```
AurelionSol Bard Blitzcrank Illaoi IvernMinion Karma Mordekaiser Nunu Sona (Summon)
```

**flex_asol** — `Asol i3 & Galio & Morde & ~Summon>=3 & ~Mecha>=6`. Cap-state lv10:
9,762 games, AVP **2.09**, top4 94.3%. Primary board:
```
AurelionSol Bard Blitzcrank Illaoi Leona Mordekaiser Nasus Nunu Viktor Zoe
```

Same carry (Asol i3), entirely different frontline and trait shell. A naive
`(Asol i3)` filter would merge them and any per-unit metric would be a Simpson's-
Paradox average of two comps. The shells must be split.

## Chapter 3 — Anchor Ablation: Look at the Gained Set, Not the AVP Delta

To split the shells we pin unit anchors. The question for each candidate anchor:
**is this unit defining the comp, or is it replaceable filler?** The wrong way to
answer is "remove it and see if cap AVP changes" — cap AVP can stay flat for two
opposite reasons:

- the anchor was redundant (gained boards are same-comp variants) → safe to remove
- the anchor was protective (gained boards are *contamination* that happens to
  place similarly) → removing it silently pollutes the comp

You cannot tell these apart from a scalar. **You must inspect the boards that join
the filter when the anchor is removed** — the *gained set*. Procedure: remove the
anchor, append `& ~Unit(anchor)` to isolate exactly the gained boards, run
`cli.py core --level 10`, and read the trait shell / identity.

### flex_asol anchors

| Anchor removed | Gained set (lv10 `core`) | Identity | Verdict |
|---|---|---|---|
| **Galio** | 591 games; primary = `Leona★2.8 Nasus Illaoi Blitzcrank Nunu Zoe` | Darkstar/heavy-armor frontline — a **different comp** | **KEEP** |
| **Mordekaiser** | 413 games; primary = `Fiora Jhin Urgot TahmKench Bard` at lv8 | 5-Mecha **cap-incomplete boards** leaking in | **KEEP** |
| **Karma** | 265 games; same `Galio+Morde+Leona` shell minus Karma, Viktor fills slot | **Same comp**, Karma replaceable | **REMOVE** |

The Galio and Morde gained sets are *not* flex_asol — they're a darkstar comp and a
mecha-line remnant respectively. Both anchors are doing real boundary work. Karma's
gained set is the same shell with the 5-cost caster slot filled by a substitute, so
Karma is filler.

### summon_asol anchors

| Anchor removed | Gained set (lv10 `core`) | Identity | Verdict |
|---|---|---|---|
| **Sona** | 547 games; Summon trait still active, `Lissandra` fills Sona's slot | **Same comp**, Sona replaceable | **REMOVE** |
| **Mordekaiser** | 256 games; Summon trait still active, same shell | **Same comp** | **REMOVE** |

Both summon_asol candidates are filler: the Summon trait shell survives intact when
they're removed, with substitutes (Lissandra, LeBlanc) sliding into the slot. So
summon_asol needs **no unit anchor beyond the carry** — `Asol i3 & Summon>=3` is the
whole definition.

### The punchline

Across all five ablations the cap AVP delta was small (within roughly ±0.1). An
**AVP-based ablation rule would have removed all five anchors** — and let a darkstar
comp and a mecha-line remnant flood into flex_asol. The gained-set inspection is the
only test that distinguishes "redundant" from "protective." Cost-based heuristics
("5-costs are flex, skip them") fail for the same reason: they never look at the
boards.

## Final Definitions

```python
"summon_asol": Asol i3 & Summon>=3
"flex_asol":   Asol i3 & Galio & Morde & ~Summon>=3 & ~Mecha>=6
```

Both validated at cap (lv10 AVP 1.99 / 2.09, top4 ~95%). The standalone `ap_flex`
sketch — `(Asol i3 | Karma i3) & ~Mecha>=3` — was discarded: it overlaps almost
entirely with summon_asol and has no shell discipline.

## What I Learned

1. **Aggregate metrics are a blend of comp strength and execution difficulty.**
   Condition on cap level to separate them. This is universal, not Asol-specific.
2. **Anchor ablation is decided by the gained set, never by the AVP delta.** A flat
   AVP is necessary but not sufficient evidence that an anchor is redundant.
3. **"Obviously required" 4-cost frontliners still need ablation.** High
   co-occurrence ≠ comp identity. Galio co-occurs with Asol constantly, yet removing
   it gains an entirely different comp — proving it's load-bearing, which a frequency
   table alone wouldn't show.

## Cross-Validation

Not run against tftable (these two Asol shells are not split the same way there).
Internal convergence instead: both comps independently hit ~95% top4 at cap with
clean, recognizable primary boards — a real player would name these boards on sight.

## Open Questions

- summon_asol overlaps `shepherd` (Summon>=5) at the high-breakpoint tail. Should
  summon_asol carry a `Summon max_units` ceiling, or is the Asol-i3 carry constraint
  enough separation?
- flex_asol's `~Mecha>=6` ceiling vs the `mecha` comp's `Mecha>=3` floor leaves the
  Mecha 3–5 band shared. Is that band genuinely flex, or a third distinct comp?

## Questions for Xing

- Are summon_asol / flex_asol the right names, or do you have canonical labels?
- Should the cap-state lens become a standing preflight step for *every* comp
  definition (it's now in lab-checklist), or only when a comp looks weak by aggregate?

## Review

_(Xing's feedback goes here.)_
