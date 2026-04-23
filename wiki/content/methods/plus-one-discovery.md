# Plus-One Discovery
**Status**: 🧪 draft

## When to Use

When the question is about **which units matter** in a comp, not which items. Typical questions:
- "Who is the most important unit in this comp?"
- "What should I add at level 10?"
- "Can I replace Akali with something better?"

## Method

### Step 1: Identify Standard Board

Use `python3 cli.py core --comp <COMP>` to detect the primary board automatically. The `core` subcommand queries `exact_units_traits2` and shows board compositions ranked by frequency, with average star levels. The #1 board is the primary board.

Alternatively, run `python3 cli.py units --comp <COMP> --level <N>` and find all units with play rate > 70%. These form the **standard board**.

Use `--level` to control for player level. The standard board level is typically 9 for most comps:
- `--level 9` for standard board analysis
- `--level 10` for level-up candidate analysis

The count of standard-board units tells you the comp's natural level:
- 9 units > 70% → level 9 comp (e.g., nova_95)
- 8 units > 70% → level 8 comp
- 7 units > 70% → level 7 comp (typical reroll)

### Step 2: Compute Unit Necessity

Same formula as item necessity, applied to units:

```
Necessity = p/(1-p) * (overall_AVP - unit_AVP)
```

Where `p` = unit play rate, `unit_AVP` = AVP in games containing this unit.

**Interpretation differs by role**:

| Unit Category | Necessity Measures | Caveat |
|---|---|---|
| Core (play rate > 70%) | Irreplaceability | w/o AVP is from small minority of games without the unit |
| Level-up candidate (< 20%) | Marginal value at higher level | Inflated by level bias |
| Negative necessity | Appears in losing boards | Usually selection bias, not causation |

### Step 3: Level-Up Analysis (Control Variable Method)

For the "who to add at level N+1" question, use **two layers of control**:

**Layer 1 — Control level**: `--level` eliminates level bias.

**Layer 2 — Fix core units**: Require all core units present in the filter. This is the unit-level analogue of "fix 2 items, vary the 3rd" in build analysis.

```bash
# comp filter (nova_95 定义) + fix all 9 core units + level 10
python3 cli.py units --comp nova_95 --level 10 --filter "\
Unit('TFT17_Aatrox') & Unit('TFT17_Akali') & Unit('TFT17_Vex') \
& Unit('TFT17_Fiora') & Unit('TFT17_Shen') & Unit('TFT17_Graves') \
& Unit('TFT17_Morgana') & Unit('TFT17_Blitzcrank') & Unit('TFT17_Nunu')"
```

`--comp` and `--filter` stack: comp provides the base filter (traits + carry + exclusions), `--filter` adds the fixed core unit requirements on top.

This ensures:
- All data is from level 10 (no level bias)
- All 9 core units are present (no incomplete boards)
- The only variable is which 10th unit was chosen

Then compute necessity for each candidate within this controlled population.

1. Look at non-core units with positive necessity
2. Rank by necessity
3. Check **trait activation** — does the unit trigger a new breakpoint?
4. Check **sample size** — units below 1% play rate may be noise
5. Check **competition** — are top candidates mutually exclusive or complementary?

**Critical**: Without `--level`, level-up candidates have inflated necessity because reaching higher levels is correlated with winning. Sona in nova_95 went from +0.127 (uncontrolled) to +0.015 (level-controlled) — an 88% drop.

### Step 4: Cross-Validation

Compare with tftable: `python3 cli.py tftable --comp <COMP>`

**Warning**: Our unit necessity and tftable's IC3 necessity measure different things:
- Ours: existence value (is the unit present or not?)
- IC3: likely carry value (unit with 3 items as carry)
- Spearman rho between them was -0.476 in nova_95 — nearly inverted

This means cross-validation for units is **not** the same as for items (where rho = 0.993). The two metrics complement rather than validate each other.

## Known Limitations

1. **w/o sample**: For core units (90%+ play rate), the "without" sample is small and potentially unrepresentative — these are games where the player couldn't find the unit.
2. **No causal claim**: Negative necessity (Maokai, TahmKench) does not mean "this unit hurts the comp" — it means the unit appears in weaker game states (selection bias). Note: this holds even after controlling for level.
3. **Emblem/spatula**: Not controlled. A unit's high necessity might depend on having an emblem that's not always available.
4. **Compressed AVP at high levels**: At level 10, overall AVP is very low (2.08 for nova_95), so all Necessity values are small. Differences between candidates may be within noise.

## Example: Nova 95 (Level-Controlled + Core-Fixed)

Standard board (9 units at level 9): Aatrox, Akali, Vex, Fiora, Shen, Graves, Morgana, Blitzcrank, Nunu

Level 9 (199k games, AVP 4.67):
- Shen (+0.95) most irreplaceable, Akali (0.00) least

Level 10 — control variable (30k games, all 9 core fixed, AVP 1.95):
- Rhaast (+0.019) ≈ Sona (+0.017) ≈ Jhin (+0.016) — nearly equal
- Zed (+0.008) is a surprise 4th candidate
- Maokai (+0.001) nearly zero; Blitzcrank★2 (-0.001) slightly negative

Three levels of analysis yield increasingly refined conclusions:
1. No control: "Sona is 3x better" (level bias artifact)
2. `--level 10` only: "Jhin ≈ Rhaast ≈ Sona" (level controlled)
3. `--level 10` + fix core 9: "Rhaast slightly ahead" (fully controlled)

Key insight: Shen (+0.95 necessity) is far more irreplaceable than Akali (+0.00) despite similar play rates. Tanks can be more critical than carries in comp structure.

## Sources
- [[experiments/2026-04-23-nova95-unit-evaluation]] — method development
- [[concepts/composition]] — role taxonomy, comp variants
