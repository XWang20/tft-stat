# Filter Design Exercise Log

Exercises where a new agent designs a filter from scratch, then compares with the expert ground truth in `compositions.py`.

---

### conduit_mf — 2026-04-22

**My filter**: `--units TFT17_MissFortune:i3 --traits TFT17_ManaTrait:2`
**Expert filter**: `MF(i2+) & ManaTrait ≥ 2` — carry + trait lock, no exclusions

**Sample size**: mine=26,826, expert=29,863

**What I got right**:
- Correctly identified ManaTrait (Conduit) as the trait anchor — the comp's identity is MF + Conduit, not just MF
- Correctly identified MF as the primary carry
- No exclusions needed — MF + Conduit is unique enough to stand alone (Pattern 2: Carry + Trait Lock)

**What I missed**:
- Used `i3` (3 items) instead of expert's `i2+` (2+ items). This excluded ~3,000 legitimate games (11% of sample) where MF had only 2 items.

**Why the expert used i2 instead of i3**:
Conduit MF is not a pure single-carry comp where MF absorbs all 3 item slots. The comp often distributes items — MF gets 2 core items while a tank or secondary unit gets items too. Using i3 biases toward "MF got all the items" games, which may not represent typical Conduit MF gameplay. The expert's lower threshold captures the full population of games where MF is itemized as a carry.

**Lesson for the guide**:
Not all carry comps use `item_min=3`. When a comp distributes items across multiple units (dual carry, or carry + tanky frontline), the primary carry may only need 2 items to be identified as "the carry." The item threshold should match the comp's item distribution pattern, not default to 3.

**Guide update needed?**: yes — the "Step 2: Write initial filter" section should mention that `i2` is appropriate for comps where the carry shares items, and that `i3` is specifically for single-carry comps where one unit absorbs all items.
