# Unit Evaluation
**Status**: 🧪 draft

## When to Use

When the question is about **which units matter** in a comp, not which items. Typical questions:
- "Who is the most important unit in this comp?"
- "What should I add at level 10?"
- "Can I replace Akali with something better?"

## Method

### Step 1: Identify Standard Board

Run `python3 cli.py units --comp <COMP>` and find all units with play rate > 70%. These form the **standard board**.

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

### Step 3: Level-Up Analysis

For the "who to add at level N+1" question:

1. Look at non-core units with positive necessity
2. Rank by necessity (relative ranking is reliable despite level bias)
3. Check **trait activation** — does the unit trigger a new breakpoint?
4. Check **sample size** — units below 1% play rate may be noise
5. Check **competition** — are top candidates mutually exclusive (Sona vs Jhin) or complementary?

### Step 4: Cross-Validation

Compare with tftable: `python3 cli.py tftable --comp <COMP>`

**Warning**: Our unit necessity and tftable's IC3 necessity measure different things:
- Ours: existence value (is the unit present or not?)
- IC3: likely carry value (unit with 3 items as carry)
- Spearman rho between them was -0.476 in nova_95 — nearly inverted

This means cross-validation for units is **not** the same as for items (where rho = 0.993). The two metrics complement rather than validate each other.

## Known Limitations

1. **Level bias**: Level-up candidates have inflated absolute necessity. Use relative rankings only.
2. **w/o sample**: For core units (90%+ play rate), the "without" sample is small and potentially unrepresentative — these are games where the player couldn't find the unit.
3. **No causal claim**: Negative necessity (Maokai, TahmKench) does not mean "this unit hurts the comp" — it means the unit appears in weaker game states (selection bias).
4. **Emblem/spatula**: Not controlled. A unit's high necessity might depend on having an emblem that's not always available.

## Example: Nova 95

Standard board (9 units): Aatrox, Akali, Vex, Fiora, Shen, Graves, Morgana, Blitzcrank, Nunu

Level 10 ranking: Sona (+0.127) > Jhin (+0.043) > Rhaast (+0.016)

Key insight: Shen (+1.40 necessity) is far more irreplaceable than Akali (+0.17) despite similar play rates. Tanks can be more critical than carries in comp structure.

## Sources
- [[experiments/2026-04-23-nova95-unit-evaluation]] — method development
- [[concepts/composition]] — role taxonomy, level bias
