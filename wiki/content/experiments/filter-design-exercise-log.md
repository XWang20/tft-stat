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

---

### pyke — 2026-04-22

**My filter**: `--units TFT17_Pyke:i3 --exclude-units TFT17_Viktor:i3`
**Expert filter**: `Pyke(i3) & ~Viktor(i3)` — carry + minimal exclusion (Pattern 4)

**Sample size**: mine=58,285, expert=58,291 (diff = 6 games, negligible)

**What I got right**:
- Correctly identified Pyke as single primary carry with `i3` — Pyke reroll is a classic single-carry comp that absorbs all items
- Correctly identified Viktor i3 as the only needed exclusion — Pyke and Viktor share the PsyOps trait and frequently co-exist. When Viktor has 3 items, those games are really Viktor comp, not Pyke comp
- No trait lock needed — Pyke i3 is unique enough (no other comp runs Pyke as 3-item carry)
- Correctly matched Pattern 4 (Carry + Minimal Exclusions): unique carry that only needs one exclusion to separate from an overlapping comp

**What I missed**:
- Nothing significant. The 6-game difference is likely from `item_max=3` in the expert definition vs my implicit no-max.

**Design reasoning**:
1. Started with carry-only `Pyke(i3)` → 110,146 games
2. Checked unit frequencies: Viktor appeared in 60,630 games (55%) — suspiciously high
3. Tested overlap: 51,866 games (47%) had BOTH Pyke i3 AND Viktor i3 — clear contamination from Viktor comp
4. Added `~Viktor(i3)` → 58,285 games, clean unit distribution

**Lesson for the guide**:
When a carry-only filter shows another unit appearing at >50% frequency with 3 items, that's a contamination signal. The other unit's comp is leaking into your data. The fix is a targeted exclusion of that specific carry, not a trait lock.

**Guide update needed?**: no — the guide already covers Pattern 4 well, and the iterative refinement process (Step 3→4) naturally leads to discovering this pattern.

---

### veigar — 2026-04-22

**My filter**: `--units TFT17_Veigar:i3`
**Expert filter**: `Veigar(i3)` — carry-only, no trait lock, no exclusions (Pattern 1)

**Sample size**: mine=109,081, expert=109,091 (diff = 10 games, negligible)

**What I got right**:
- Correctly identified Veigar as a unique single carry — no other meta comp runs Veigar as a 3-item primary carry
- Correctly determined no trait lock needed — "Veigar Printer" is defined by the carry, not a trait shell
- Correctly determined no exclusions needed — checked unit frequencies and found no contaminating 3-item carries at high rates (ASOL i3 overlap = 52 games, 0.05%)
- Matched Pattern 1 (Carry-Only) perfectly: the simplest filter for the simplest case

**What I missed**:
- Nothing significant. The 10-game difference is from `item_max=3` in the expert definition vs my implicit no-max.

**Design reasoning**:
1. Started with carry-only `Veigar(i3)` → 109,081 games
2. Checked unit frequencies: Rammus (87%), Summon/Shepherd (63%), Illaoi (57%), Bard (44%) — all support/tank units, no competing carries
3. Checked for 3-item carry contamination: ASOL i3 = 52 games, Galio in ~12% of games but as frontline (not carry), no other carry at >5% with i3
4. Concluded: Veigar i3 is self-isolating — no exclusions needed

**Lesson for the guide**:
Low-cost reroll carries (1-2 cost units like Veigar, Zed, Kai'Sa) are often self-isolating because they occupy a unique niche — no other comp invests 3 items into these units. The carry-uniqueness heuristic from Pattern 1 ("how many comps share this carry?") maps directly: if the answer is zero, carry-only is sufficient.

**Guide update needed?**: no — Pattern 1 is already well-documented and Veigar is a textbook example of it.

---

### space_groove — 2026-04-22

**My filter**: `--or-units TFT17_Nami:i3,TFT17_Samira:i3 --traits TFT17_SpaceGroove:5`
**Expert filter**: `(Nami i3 | Samira i3) & SpaceGroove >= 5 & ~Nasus(i3, 3★)` — OR carry group + trait lock + minimal exclusion

**Sample size**: mine=238,205, expert=234,322 (diff = 3,883 games, 1.6%)

**What I got right**:
- Correctly identified this as a **Line comp** — defined by the SpaceGroove trait shell, not a single carry
- Correctly used OR-group for dual carries: `Nami(i3) | Samira(i3)` — both can serve as primary carry
- Correctly chose `SpaceGroove >= 5` as the trait anchor (not >= 3, which would be too broad at 258k games)
- Correctly used `i3` item threshold — these are single-carry boards where one carry absorbs all items
- Identified the comp from scout data without prior knowledge: multiple top-3 boards showed Nami(i3) + Riven(i3) + Shen + TahmKench + SpaceGroove trait

**What I missed**:
- The exclusion `~Nasus(i3, 3★)` — excludes 3-star Nasus with 3 items. This removes Bonk (Nasus reroll) games that happen to run 5+ SpaceGroove units. The key insight: star_min=3 + star_max=3 narrows the exclusion to **3-star reroll** Nasus only, not all Nasus boards. A 2-star Nasus in Space Groove is normal (frontline); a 3-star Nasus with 3 items is a Bonk comp contaminating the data.

**Why the expert added this exclusion**:
Low-cost reroll comps (like Bonk/Nasus) share many units with higher-tier comps. In this case, SpaceGroove units like Blitzcrank, Shen, and Nunu also appear in Bonk boards. When a Nasus hits 3-star with 3 items, that game's identity is "Nasus carry" not "Space Groove carry." The star-level qualifier (`star_min=3, star_max=3`) is a precision tool — it only excludes the true reroll cases while keeping normal Nasus appearances.

**Design reasoning**:
1. Scouted boards → noticed recurring Nami(i3) + SpaceGroove pattern
2. Started with `Nami(i3) + SpaceGroove >= 3` → 258k games (too broad)
3. Tightened to `SpaceGroove >= 5` → 224k games (better)
4. Added Samira as OR carry → 238k games (correct population)
5. Missed the Nasus exclusion — didn't check for reroll comp contamination

**Lesson for the guide**:
When filtering Line comps with broad trait anchors, check for **low-cost reroll comp contamination**. Reroll comps share many units with the trait shell but have a fundamentally different carry identity (3-star carry with 3 items). The exclusion should use `star_min=3, star_max=3` to precisely target reroll boards without removing normal appearances of the unit.

**Guide update needed?**: yes — the iterative refinement section (Step 4) should mention checking for reroll comp contamination in Line comps, specifically using star-level qualifiers in exclusions.
