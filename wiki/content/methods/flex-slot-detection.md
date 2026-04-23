# Flex Slot Detection
**Status**: 🧪 draft

## When to Use

Analyze a comp's standard board composition and flex slot (+1 unit candidates).

## Method

### Step 1: Find Primary Board

```bash
python3 cli.py core --comp <KEY>
```

Queries `exact_units_traits2` API for all board compositions (size 6-11), sorted by frequency with average star levels. **freq #1 = primary board**.

The primary board tells you:
- **Core units**: all units in the primary board (excluding summoned units)
- **Level**: number of player-placed units (derived from data, not assumed from carry cost)

**Summoned units** (e.g. `TFT17_Summon`) don't count as player population — they are automatically excluded from level calculation and core unit lists. The CLI marks them as `(Summon)` in the output.

**Multi-slot traits** (e.g. Mecha: 3 units occupy 5 slots) mean board unit count ≠ player level. The `core` command handles Summon automatically; Mecha-style adjustments require manual correction.

### Step 2: +1 Control Variable Analysis

Fix the primary board's core units + control level:

```bash
# The core command auto-generates this command
python3 cli.py units --comp <KEY> --level <LEVEL+1> --filter "\
Unit('unit1') & Unit('unit2') & ... & Unit('unitN')"
```

Rank non-core units by **frequency**, then evaluate with **AVP** (primary metric) and **Necessity** (supplementary):
- **AVP**: valid for complete boards (no survivorship bias). Lower AVP with high frequency = good pick.
- **Necessity**: measures marginal impact, but compressed at high levels (small AVP range).

Summoned units should not appear as +1 candidates — they are trait-generated, not player choices.

### Step 3: Cross-Validation

`python3 cli.py tftable --comp <COMP>` — compare with tftable's unit necessity. Note: our unit necessity (existence value) and tftable's IC3 necessity (likely carry value) measure different things.

## Known Limitations

1. **Primary ≠ only playstyle**: variant-heavy comps (e.g. pyke) may have a primary board representing only 15% of games.
2. **Level bias**: without `--level` control, +1 candidate Necessity is inflated (Sona in nova_95 dropped 88% after level control).
3. **Compressed AVP**: at high levels, AVP range is small — differences between candidates may be noise.
4. **Multi-slot traits**: Mecha units occupy extra slots; level needs manual adjustment.

## Example: Nova 95

**Step 1**: `python3 cli.py core --comp nova_95`
→ primary = 9 units (Aatrox, Akali, Blitzcrank, Fiora, Graves, Morgana, Nunu, Shen, Vex), 82k games (46%), AVP 3.95, level 9

**Step 2**: control variable analysis
```bash
python3 cli.py units --comp nova_95 --level 10 --filter "\
Unit('TFT17_Aatrox') & Unit('TFT17_Akali') & Unit('TFT17_Vex') \
& Unit('TFT17_Fiora') & Unit('TFT17_Shen') & Unit('TFT17_Graves') \
& Unit('TFT17_Morgana') & Unit('TFT17_Blitzcrank') & Unit('TFT17_Nunu')"
```
→ Sona (+0.027) ≈ Rhaast (+0.021) ≈ Jhin (+0.019)

## Sources
- [[experiments/2026-04-23-nova95-unit-evaluation]] — method development
- [[experiments/2026-04-23-flex-slot-all-comps]] — all 29 comps analyzed
- [[concepts/composition]] — comp structure definitions
