# Composition Structure
**Status**: 🧪 draft

## What Makes a Comp

A composition is not just a filter — it has internal structure. Understanding that structure is prerequisite to asking the right questions.

### Standard Board Size

Every comp has a **standard board size** — the number of units that appear together in > 70% of games. This is the "natural" level for the comp:

| Comp Type | Typical Board Size | Example |
|---|---|---|
| 5-cost carry | 9 units | nova_95: 9 units > 70% play rate |
| 4-cost carry | 8 units | compositions.py 多数定义 8 个 unit |
| Reroll (1-3 cost) | 7-8 units | bonk: Nasus-centric, 7-8 units |

Standard board size determines:
- **At what level the comp "comes online"** — level 9 for nova_95
- **What the level-up question is** — nova_95 asks "who is the 10th unit", not the 9th
- **How to interpret unit necessity** — core units (> 70%) measure irreplaceability; non-core units measure marginal value

### Core vs Flex

Within a comp's standard board:

**Core units** (play rate > 70%): Always present. Their necessity measures **irreplaceability** — how much the comp suffers without them.

**Flex slots**: Positions where multiple units compete. Example: nova_95 at level 9 includes both Blitzcrank (73%) and Nunu (73%), but at level 8 players choose between them.

**Level-up candidates**: Units below the core threshold (< 20% play rate) that appear when players reach higher levels. Their necessity measures **marginal value** but is inflated by level bias.

### Role Taxonomy

Units serve different roles within a comp. Role determines how to analyze them:

| Role | Definition | Item Pattern | Filter Reliability | Example |
|---|---|---|---|---|
| Primary Carry (主C) | Main damage dealer, 3 items | Deliberate, optimized | High (rho > 0.95) | Vex in nova_95 |
| Tanky Carry | Main tank, 3 items, comp identity | Deliberate tank items | High (rho 0.93-1.00) | Nasus in bonk |
| Comp-Specific Tank | Tank whose build depends on comp | Comp items + generic | Split: comp items unstable, generic stable | Galio in mecha |
| Support | Core but rarely itemized | Leftover items | Very low (rho ~ 0.05) | Mordekaiser in dark_star |
| Flex/Fill | Interchangeable with other units | Varies | Depends on context | Blitzcrank/Nunu in nova_95 |

### Play Rate vs Necessity Decoupling

Play rate and necessity measure different things:

- **Play rate**: how often a unit appears (presence)
- **Necessity**: how much AVP changes without the unit (impact)

These can sharply decouple:

| Unit | Play Rate | Necessity | Interpretation |
|---|---|---|---|
| Akali (nova_95) | 91.5% | +0.17 | "Default fill" — always there, low impact |
| Shen (nova_95) | 86.0% | +1.40 | "Irreplaceable" — slightly less common but critical |

High play rate + low necessity = the unit is easy to include but doesn't drive results.
Low play rate + high necessity = the unit is hard to find/fit but strongly improves outcomes (or level bias inflates it).

### Level Bias in Level-Up Analysis

Analyzing non-core units (level-up candidates) suffers from **level bias**: reaching higher levels correlates with winning. Any unit that appears as "the Nth unit" has inflated AVP because the player was already ahead.

**Mitigation**: Level bias affects all candidates equally at the same level, so **relative rankings** (Sona > Jhin > Rhaast at level 10) are more reliable than absolute necessity values.

**Open problem**: No standard method to fully remove level bias from unit necessity analysis. Possible approaches:
- Control for board size (only compare games with exactly N units)
- Use tftable's IC3 method (measures different thing — carry value, not existence value)

## Sources
- [[experiments/2026-04-23-nova95-unit-evaluation]] — core findings
- [[experiments/2026-04-23-tank-filter-reliability]] — role taxonomy evidence
