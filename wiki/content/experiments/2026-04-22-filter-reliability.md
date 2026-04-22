# Experiment: Filter Reliability — When Does Filter Definition Matter?
**Status**: 🧪 draft
**Date**: 2026-04-22
**Module**: 1 (Filter Design) / 9 (Cross-Validation)

## The Question

We know filter is foundation — ad-hoc filters caused 3 sign flips in the Vex cross-comp experiment. But **how much does filter precision matter**, and **for whom**? Can we quantify filter reliability?

Specifically: if we progressively degrade a filter from "expert compositions.py definition" to "no filter at all", how much do Necessity rankings shift? And does the answer depend on the unit's role?

---

## Chapter 1: Experimental Design

We test **four filter levels** on two units in different roles:

| Level | Description | Controls |
|-------|-------------|----------|
| **Full** | compositions.py definition (trait + carry + exclusions) | Maximum |
| **Partial** | Carry 3-item + primary trait only (no exclusions) | Moderate |
| **Minimal** | Carry 3-item only | Minimal |
| **None** | All games with unit, no filter | Zero |

**Test units**:
- **Vex in nova_95**: Primary AP carry, appears in 88% of comp games
- **Mordekaiser in dark_star**: Tank/secondary carry, itemized in a broader comp context

**Ground truth**: tftable Necessity rankings (expert-curated with advanced debiasing).

**Metric**: Spearman rank correlation (ρ) between filter levels and against tftable.

---

## Chapter 2: Vex — The Primary Carry

### Data by Filter Level

| Filter Level | Games | Overall AVP | Top Item Nec |
|-------------|-------|-------------|--------------|
| Full (nova_95) | 215,021 | 4.16 | Guinsoo's 0.496 |
| Partial (carry+DRX) | 242,432 | 4.12 | Guinsoo's 0.426 |
| Minimal (Vex 3-item) | 514,300 | 4.12 | Guinsoo's 0.169 |
| None (all Vex) | 630,110 | 4.33 | Guinsoo's 0.314 |
| tftable (ground truth) | 135,798 | 4.26 | Guinsoo's 0.764 |

### Ranking Stability (8 items: Guinsoo, Giant Slayer, Hextech, Striker, Rabadon, Red Buff, Archangel, JG)

| Comparison | Spearman ρ |
|-----------|------------|
| Full vs Partial | **1.000** |
| Full vs None | 0.976 |
| Full vs tftable | 0.976 |
| Partial vs None | 0.976 |
| Full vs Minimal (7 items) | 0.893 |
| tftable vs Minimal (7 items) | 0.857 |

### Rank Comparison

| Item | Full | Partial | Minimal | None | tftable |
|------|------|---------|---------|------|---------|
| Guinsoo's | 1 | 1 | 1 | 1 | 1 |
| Giant Slayer | 2 | 2 | 2 | 2 | 2 |
| Hextech Gunblade | 3 | 3 | 4 | 3 | 4 |
| Striker's Flail | 4 | 4 | 5 | 4 | 3 |
| Rabadon's Deathcap | 5 | 5 | 3 | 5 | 5 |
| Red Buff | 6 | 6 | 6 | 6 | 6 |
| Archangel's Staff | 7 | 7 | 7 | 8 | 7 |
| Jeweled Gauntlet | 8 | 8 | — | 7 | 8 |

**Finding**: Vex's item rankings are remarkably stable across filter levels. The top 2 items (Guinsoo's, Giant Slayer) never move. Even the "no filter" condition produces ρ = 0.976 against the full expert filter. The only instability is at positions #3-#5 (Hextech/Striker/Rabadon swap), and this is the exact same zone where tftable and MetaTFT also disagree.

---

## Chapter 3: Mordekaiser — The Tank

### Data by Filter Level

| Filter Level | Games | Overall AVP | Description |
|-------------|-------|-------------|-------------|
| Full (dark_star) | 108,027 | 4.40 | DarkStar 4+ with exclusions |
| Partial (carry+trait) | 12,223 | 4.18 | Morde 3-item + DarkStar 4 |
| Minimal (Morde 3-item) | 78,468 | 4.23 | Morde 3-item only |
| tftable (ground truth) | 49,266 | 4.54 | Expert definition |

### Ranking Stability (8 items: Warmog, Crownguard, Steadfast, Evenshroud, Ionic, Protector, Adaptive, Bramble)

| Comparison | Spearman ρ |
|-----------|------------|
| Full vs tftable | **0.048** |
| Full vs Partial | 0.357 |
| Full vs Minimal | -0.286 |
| tftable vs Minimal | 0.607 |

### Rank Comparison

| Item | Full | Partial | Minimal | tftable |
|------|------|---------|---------|---------|
| Warmog's Armor | 1 | 5 | 7 | 7 |
| Crownguard | 2 | 2 | 1 | 1 |
| Steadfast Heart | 3 | 4 | 3 | 2 |
| Evenshroud | 4 | 1 | — | 8 |
| Ionic Spark | 6 | 3 | 2 | 6 |
| Protector's Vow | 5 | 6 | 6 | 4 |
| Adaptive Helm | 7 | 7 | 4 | 3 |
| Bramble Vest | 8 | — | 5 | 5 |

**Finding**: Mordekaiser's rankings are **catastrophically unstable** across filter levels. The full dark_star filter gives ρ = 0.048 against tftable — essentially zero correlation. Warmog's is #1 with full filter but #7 in both tftable and minimal filter. The rankings invert depending on filter choice.

---

## Chapter 4: Why the Difference?

### The Carry Leverage Hypothesis

Vex is the **primary carry** in nova_95. She appears in 88% of games and receives 3 items in the comp definition. Her item choices are the **decisive variable** — the comp's performance rises or falls on Vex's items. This means:
- Filter changes mostly add/remove **non-Vex games** (other carries in the same trait space)
- The Vex-specific games remain similar regardless of what comp context we define
- Her item Necessity is driven by her own carry performance, not by team composition nuance

Mordekaiser is a **tank** in dark_star. He receives items, but the comp's performance depends more on the actual carries (Jhin, etc.). His item choices are **secondary variables**:
- Filter changes alter which **carries and traits surround him**
- Different filter definitions select fundamentally different team contexts
- Warmog's being #1 in the full filter but #7 in tftable suggests the full filter is capturing a specific subpopulation where tanky builds happen to correlate with winning — likely a confound, not a causal effect

### Quantitative Summary

| Metric | Vex (Primary Carry) | Mordekaiser (Tank) |
|--------|--------------------|--------------------|
| Full vs tftable ρ | 0.976 | 0.048 |
| Full vs Minimal ρ | 0.893 | -0.286 |
| Rank volatility (max rank change) | 2 positions | 6 positions |
| Top item stable? | Yes (Guinsoo's always #1) | No (Warmog #1→#7) |

### Implication

**Filter reliability is a property of the unit-role, not the filter.** A well-defined carry's item rankings are robust to filter variation because the carry IS the comp's identity. A tank's item rankings are fragile because the tank's optimal build depends on what else is happening in the comp — information that different filters capture differently.

---

## Cross-Validation

### Vex (nova_95)
MetaTFT full filter vs tftable: ρ = 0.976. Top 7 items match. The only swap is Hextech (#3) ↔ Striker (#4), which is within noise. **Strong convergence.**

### Mordekaiser (dark_star)
MetaTFT full filter vs tftable: ρ = 0.048. Complete divergence. Notably, **tftable vs MetaTFT minimal** gives ρ = 0.607 — tftable is actually closer to the minimal filter than to the full expert filter. This suggests the full dark_star compositions.py filter may be selecting a biased subpopulation for Mordekaiser specifically, even though it correctly defines the Dark Star comp overall.

---

## What I Learned

1. **Filter reliability depends on carry role.** Primary carries (Vex: ρ = 0.976) have stable Necessity rankings regardless of filter precision. Tanks (Mordekaiser: ρ = 0.048) have unstable rankings that invert with filter changes. This is because carries ARE the comp's identity — their performance is the thing being measured. Tanks are context-dependent — their optimal build changes with team composition.

2. **You can skip careful filtering for primary carries — but you MUST filter carefully for tanks.** Paradoxically, the units that need filtering most (tanks, secondary carries) are the units for which filtering is hardest to get right. For Vex, even "no filter" gives ρ = 0.976 against expert definition. For Mordekaiser, even the expert filter diverges from tftable.

3. **tftable vs MetaTFT divergence is systematic for tanks.** ρ = 0.048 means our full dark_star filter and tftable's definition are selecting different Mordekaiser populations. This isn't a calculation difference — it's a fundamental filter difference. tftable's advanced debiasing methods may matter more for tanks than for carries.

4. **Warmog's Armor is the canary.** It's #1 with full filter, #7 with tftable and minimal. High play rate (30%) + marginal AVP gap (+0.02 Edge in minimal) = it looks important by Necessity only when the filter artificially creates a population where it correlates with winning. This is exactly the kind of confound that Necessity alone can't fix.

## Open Questions

- Is there a threshold of "carry-ness" (% of comp games where unit appears with 3 items) below which filter reliability drops sharply?
- Can we develop a filter reliability diagnostic? E.g., compute ρ between filter and filter-minus-one-condition as a stability test.
- Why does tftable's Mordekaiser ranking agree more with our minimal filter (ρ = 0.607) than our full filter (ρ = 0.048)? Is the dark_star compositions.py definition suboptimal for Mordekaiser analysis?

## Questions for Xing

1. **Tank item analysis** — Is Mordekaiser item analysis even meaningful from endgame snapshots? The ρ = 0.048 against tftable suggests we might be measuring noise for tanks.
2. **tftable debiasing** — Does tftable use a different method for tank items vs carry items? The divergence is dramatic (ρ = 0.976 for Vex vs 0.048 for Morde).
3. **Warmog's paradox** — Is #1 (full filter) or #7 (tftable) closer to the truth? Or is this fundamentally unanswerable from endgame snapshots?
4. **Practical implication** — Should we restrict item analysis to primary carries only, or is there a way to make tank analysis reliable?

---

## Review

*(pending Xing review)*
