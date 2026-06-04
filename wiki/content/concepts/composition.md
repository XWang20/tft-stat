# Composition Structure
**Status**: 🧪 draft

## What Makes a Comp

A composition is not just a filter — it has internal structure. Understanding that structure is prerequisite to asking the right questions.

### Primary Board

Every comp has a **primary board** — the most common board composition. Use `python3 cli.py core --comp <KEY>` to find it (freq #1).

The primary board defines:
- **Core units**: all player-placed units in the primary board
- **Level**: number of player-placed units (derived from data, not assumed from carry cost)

**Summoned units** (e.g. `TFT17_Summon` from the Summoner trait) are not player population — they don't occupy a player slot. The CLI automatically excludes them from level calculation and marks them as `(Summon)` in the output. They should never be counted as core units or +1 candidates.

**Multi-slot traits**: some traits have units that occupy extra board slots (e.g. Mecha: 3 units occupy 5 slots → 7 units on board = level 9). Level ≠ board unit count in these cases.

### Comp Variants and Flex Slots

Three composition patterns:

**1. Fixed roster (no flex)**: all core units are fixed, no substitution room. Typical of reroll comps (e.g. bonk = Nasus 3★ + fixed teammates). No +1 analysis needed.

**2. Flex slot**: N core units are fixed, but the N+1 position has multiple competing candidates. Classic +1 analysis scenario.

**3. Variant**: the comp has multiple distinct builds with different core units (**≥3 unit difference** = variant; 1-2 unit difference = flex slot substitution). Example: Mecha's Fiora variant vs Viktor variant.

Identification criteria:
- **Primary**: highest frequency board
- **Variant**: high-frequency board with ≥3 unit difference from primary
- **Flex substitution**: 1-2 unit difference (not a variant)
- **+1 board**: board with 1 more unit than primary

Analysis workflow: see [[methods/flex-slot-detection]].

### Role Taxonomy

Units serve different roles within a comp. Role determines how to analyze them:

| Role | Definition | Item Pattern | Filter Reliability | Example |
|---|---|---|---|---|
| Primary Carry | Main damage dealer, 3 items | Deliberate, optimized | High (ρ > 0.95) | Vex in nova_95 |
| Tanky Carry | Main tank, 3 items, comp identity | Deliberate tank items | High (ρ 0.93-1.00) | Nasus in bonk |
| Comp-Specific Tank | Tank whose build depends on comp | Comp items + generic | Split: comp items unstable, generic stable | Galio in mecha |
| Support | Core but rarely itemized | Leftover items | Very low (ρ ~ 0.05) | Mordekaiser in dark_star |
| Flex/Fill | Interchangeable with other units | Varies | Context-dependent | Blitzcrank/Nunu in nova_95 |

### Carry Form: Reroll vs Tempo

**A carry holding 3 items is not necessarily a reroll carry.** The same unit can be played two ways, and `Unit(X, item_min=3)` does not tell you which:

- **Reroll**: hold a low level (often 8, sometimes 7), roll gold to hit a high star (usually 3★), win on unit power. Board is a fixed roster.
- **Tempo / level-to-power**: push levels on curve, itemize the carry at a lower star (often 2★), and win on board quality + level advantage rather than star level.

Assuming "3-item low-cost carry = reroll" is a mistake. Diagnose the form with a **star × level breakdown** — split IC3 (`item_min=3`, i.e. the carry holding ≥3 items) by `star_min/star_max` across `--level 7/8/9`. **Merge lv9 and lv10 into a single "cap" row** — lv10 alone is too sparse for a 3-cost comp and isn't the steady state; lv9+10 together represent the "played it to the late game" ceiling. lv10 is not examined on its own.

| Signature | Reroll | Tempo |
|---|---|---|
| Where do the IC3 games sit? | Concentrated **low** (lv7–8) | Spread up toward the cap |
| High-star rate at low level | Already high (rolled to cap) | Lower — many stay at 2★ |
| 2★ AVP across levels | n/a (most are 3★) | **Improves as level rises** (2★ underpowered → leaning on population quality to compensate) |

**Worked example — Samira IC3 in `space_groove` (2026-06-04, SpaceGroove≥5):**

| Level | IC3 games | 2★ (AVP) | 3★ (AVP) | 3★ share |
|---|---|---|---|---|
| 7 | 74,002 | 33k (6.02) | 40k (5.08) | 55% |
| 8 | **166,794** | 57k (4.69) | 108k (2.92) | 65% |
| 9–10 (cap) | 105,741 | 42k (2.96) | 63k (1.76) | 60% |

Reading: games pile up at **lv7–8 with 55–65% already 3★** → the dominant form is reroll. But 2★-itemized Samira exists at every level in volume (33k/57k/42k) and its **AVP climbs 6.02 → 4.69 → 2.96** as the player levels up → a real tempo branch coexists. The correct description is "reroll-dominant, with a tempo branch," not "Samira reroll."

This is the [[methods/filter-strategy]] cap-state principle applied to star level: aggregating across levels blends two different game plans.

For the related question of *which* unit in a comp is the real itemization target (vs a unit that just got spare items dumped on it), see [[concepts/biases]] → "Disentangling Investment from Survivor-Dumping (IC3)" — the same end-board-only constraint applies, and the diagnostic is unit-necessity × item-necessity plus build entropy.

### Play Rate vs Necessity Decoupling

Play rate and necessity measure different things:

- **Play rate**: how often a unit appears (presence)
- **Necessity**: how much AVP changes without the unit (impact)

These can sharply decouple:

| Unit | Play Rate | Necessity | Interpretation |
|---|---|---|---|
| Akali (nova_95) | 91.5% | +0.17 | "Default fill" — always there, low impact |
| Shen (nova_95) | 86.0% | +1.40 | "Irreplaceable" — slightly less common but critical |

## Hero Augments

### S17 Hero Augment List

S17 has **8 hero augments**, each transforming a low-cost unit into a carry (changed ability + combat mode):

| Augment | Name | Unit | Cost | Comp |
|---|---|---|---|---|
| NasusCarry | Bonk! | Nasus | 1 | `bonk` |
| PoppyCarry | Termeepnal Velocity | Poppy | 1 | `termeepnal_velocity` |
| AatroxCarry | Stellar Combo | Aatrox | 1 | `stellar_combo` |
| JaxCarry | Reach for the Stars | Jax | 2 | `reach_for_the_stars` |
| IvernMinionCarry | The Big Bang | Ivern | 2 | `the_big_bang` |
| PykeCarry | Contract Killer | Pyke | 2 | `pyke` |
| GragasCarry | Self Destruct | Gragas | 2 | — |
| MordekaiserCarry | Heat Death | Mordekaiser | 3 | — |

### What Stats Can and Cannot Discover

MetaTFT API **does not track augment data** (`augments` field is `None` in match records). No direct filtering or statistics possible.

**Observable**:
- **Item split on tanky carries**: hero augment turns a tank into a carry, so item data shows both tank items (Warmog, Sunfire) and damage items (Guinsoo, Deathcap) from completely different games
- **Role ambiguity**: Nasus in bonk is both tank (without augment) and carry (with augment); both item types show positive necessity

**Not observable**: augment vs non-augment AVP difference, augment pick rate, augment impact on comp strength.

### Removing Hero Augment Influence

Use `--exclude-dmg-items` (for tank carry analysis) or `--exclude-tank-items` (for carry build analysis):

```bash
python3 cli.py items TFT17_Nasus --comp bonk --normal-only --exclude-dmg-items  # tank build
python3 cli.py items TFT17_Nasus --comp bonk --normal-only --exclude-tank-items  # carry build
```

10 hero-augment / tanky-carry comps in compositions.py annotate an `exclude_{dmg,tank,bruiser}_items_for_carriers` field (upstream `CompositionDefinition`), applied as `Not(Item(...))` constraints at query time.

## Sources
- [[experiments/2026-04-23-nova95-unit-evaluation]] — core findings
- [[experiments/2026-04-23-tank-filter-reliability]] — role taxonomy evidence
- [[experiments/2026-04-23-flex-slot-all-comps]] — 29 comp flex slot analysis
- CDragon TFT static data — S17 hero augment definitions
