# Filter Design Exercise Log

Tracking all filter-design exercises for learning and comparison.

---

### xayah_carry → xayah — 2026-04-22

**Observation**: From `cli.py scout --top 3`, observed a VN2 Master board with Xayah(i3) + Zed(i3) as dual carries alongside Jhin, Nunu(i3), Rammus(i3), Shen, Jax, Mordekaiser, Morgana. The Xayah carry pattern appears broadly — Xayah with 3 AD items (Guinsoo, IE, crossbow variants) supported by Jhin, Bard, and a tanky frontline (Nunu, Rammus, Mordekaiser). Multiple boards showed Xayah(i3) as the primary ranged carry.

**My reasoning**: Xayah appears to be a unique enough carry for a carry-only filter (Pattern 4). She doesn't share a comp identity with other carries the way Vex does across NOVA/Vex95/DarkStar. The main concern is contamination from other 3-item carries appearing alongside Xayah in "winning too hard" boards.

**Filter iterations**:
1. `--or-units TFT17_Xayah:i3` → 431,066 games, AVP 4.27, Top4 53.3%. Contamination: Samira(i3) 11k, Fiora(i3) in top 30
2. `--or-units TFT17_Xayah:i3 --exclude-units TFT17_Samira:i3,TFT17_Fiora:i3,TFT17_Vex:i3,TFT17_Zed:i3` → 385,671 games, AVP 4.34, Top4 52.0%. Core units clean: Nunu 94%, Jax 83%, Mordekaiser 79%, Jhin 72%, Rammus 69%
3. Final: `--or-units TFT17_Xayah:i3 --exclude-units TFT17_Samira:i3,TFT17_Fiora:i3,TFT17_Vex:i3,TFT17_Zed:i3`

**Expert filter**: `Xayah(i3, i_max=3) & ~Lulu(i3) & ~Samira(i3) & ~Jax(i3) & ~DarkStar>=4 & ~Ezreal(i3)` → 362,055 games, AVP 4.33, Top4 52.0%

**Comparison**:
- right: carry-only approach (Pattern 4), Samira exclusion
- missed: Lulu(i3) exclusion (reroll contamination), Jax(i3) exclusion (reroll contamination), Ezreal(i3) exclusion, DarkStar >= 4 exclusion (Xayah in DarkStar is a different comp context), item_max=3 precision
- over-excluded: Fiora(i3), Vex(i3), Zed(i3) — expert doesn't need these because their contamination rate is low enough to not matter, or they represent legitimate Xayah-primary games

**Lesson**: For carry-only filters, the expert's exclusions focus on **reroll comps** (Lulu, Jax, Ezreal — all low-cost reroll carries) and **trait-based variants** (DarkStar >= 4). I over-focused on excluding high-cost carries (Fiora, Vex, Zed) which rarely overlap, while missing the low-cost reroll carries that are the real contamination risk. The reroll carry exclusion pattern (Pattern 5 from the guide) applies even within carry-only filters.

### darkstar_graves → dark_star — 2026-04-22

**Observation**: From `cli.py scout --top 3`, a KR Master #2 board showed Graves(i3) with Dark Star Emblem + Last Whisper + HoJ, alongside Karma(i3) with JG/Nashor's/Striker's, in a DarkStar_3 comp with Chogath, Galio, Jhin, TahmKench, Mordekaiser, Nunu. I named it "darkstar_graves" — Graves as carry in a DarkStar shell.

**My reasoning**: The board had DarkStar_3 as the dominant trait with Graves as the primary AD carry. I assumed this was a carry + trait lock comp (Pattern 2), with Graves(i3) + DarkStar as the defining features. I tried to exclude contaminating carries (Xayah, Vex, Fiora) from other comps.

**Filter iterations**:
1. `--or-units TFT17_Graves:i3 --traits TFT17_DarkStar:2` → 39,690 games, AVP 4.06, Top4 56.9%. Way too broad — Xayah 30%, Vex 24%, Fiora 12% contamination. DarkStar >= 2 captures any comp splashing 2 DarkStar units.
2. `--or-units TFT17_Graves:i3 --traits TFT17_DarkStar:4` → 3,951 games, AVP 4.22, Top4 54.3%. Much cleaner — core units Mordekaiser 96%, Karma 88%, Cho'gath 85%, Jhin 77%. Still some Xayah 19%.
3. `--or-units TFT17_Graves:i3 --traits TFT17_DarkStar:4 --exclude-units TFT17_Xayah:i3,TFT17_Vex:i3,TFT17_Fiora:i3` → 3,460 games, AVP 4.27, Top4 53.3%.
4. Final: `--or-units TFT17_Graves:i3 --traits TFT17_DarkStar:4 --exclude-units TFT17_Xayah:i3,TFT17_Vex:i3,TFT17_Fiora:i3`

**Expert filter**: `Trait(DarkStar, min_units=4) & ~Kaisa(★3) & ~Chogath(★3)` — **no carry specified at all**. 116,218 games, AVP 4.38, Top4 52.1%.

**Comparison**:
- right: DarkStar >= 4 as the correct trait threshold (matched expert exactly)
- missed:
  - **Dark Star is a "Line" comp, not a carry comp.** The expert defines it purely by trait (DarkStar >= 4) with no carry unit. By anchoring on Graves(i3), I captured only 3% of the actual comp (3,460 vs 116,218 games). Dark Star boards have flexible carries — Graves, Karma, Jhin, Kai'Sa, or others can all be the primary carry.
  - **Star-level exclusions**: expert excludes Kai'Sa★3 and Cho'gath★3 (reroll variants that are fundamentally different comps). I didn't consider star-level as an exclusion dimension.
  - **Over-excluded**: my Xayah/Vex/Fiora exclusions were unnecessary — the trait threshold alone is distinctive enough.

**Lesson**: Not every comp is defined by a carry. Some comps are defined purely by their trait shell — the carry slot is flexible. Recognizing comp "type" (single carry vs flex carry vs Line) from scout data is critical BEFORE designing the filter. When boards sharing a trait have different carries, that's a signal it's a Line/trait-shell comp, not a carry comp. Also learned: star-level (★3) exclusions are a tool for separating reroll variants from standard comps, a dimension I hadn't considered.

### corki_astronaut → meeple_corki — 2026-04-22

**Observation**: From `cli.py scout --top 3`, two boards showed Corki(i3) as primary AD carry: a GM EUW board (Corki/Bard/Riven/Rammus/Fizz/Milio/Poppy/Shen/TahmKench, Astronaut_2/Timebreaker_1) and a Master JP board (Corki/Bard/Riven/Rammus/Mordekaiser/Fizz/Milio/Poppy/Rhaast, Astronaut_2/Timebreaker_2). Both featured Corki as the ranged AD carry with Astronaut units (Fizz/Milio/Poppy) and Riven as bruiser.

**My reasoning**: Both boards shared a Timebreaker trait shell alongside Astronaut units. I named it "corki_astronaut" and tried Timebreaker >= 2 as the trait anchor (since both boards displayed Timebreaker). The carry seemed unique enough that a carry + trait lock (Pattern 2) would work. I expected minimal contamination since Corki as primary 3-item carry is specific.

**Filter iterations**:
1. `--or-units TFT17_Corki:i3 --traits TFT17_Astronaut:2` → 169,130 games, AVP 4.31, Top4 51.7%. Too broad — generic splash units (Shen 19%, Aatrox 12%) dominate, meaning Astronaut >= 2 is too low a breakpoint.
2. `--or-units TFT17_Corki:i3 --traits TFT17_Timebreaker:2` → 84,744 games, AVP 3.99, Top4 58.7%. Tighter. Core units: Talon 17%, Caitlyn 18%, TF 18%, Jax 19%, Aatrox 19%. Low contamination from other carries (<0.5% from Nami/Samira/LeBlanc).
3. Checked exclusions: `--exclude-units TFT17_Nami:i3,TFT17_Samira:i3,TFT17_Leblanc:i3` → 84,307 games — only 437 games removed, confirming minimal contamination.
4. Final: `--or-units TFT17_Corki:i3 --traits TFT17_Timebreaker:2`

**Expert filter**: `Corki(i3, i_max=3) & Astronaut >= 5 & ~Veigar(i3) & ~IvernMinion(i3,★3) & ~Poppy(i3)` → 103,981 games, AVP 4.48, Top4 47.5%

**Comparison**:
- right: identified Corki as primary carry with 3 items, recognized the comp is a trait-shell comp (Pattern 2)
- missed:
  - **Wrong trait anchor**: expert uses **Astronaut >= 5** (the comp is literally called "Meeple Corki / 木灵族"), not Timebreaker. I was misled by a secondary trait visible in the two boards I observed. The comp's identity IS the deep Astronaut shell.
  - **Breakpoint matters**: Astronaut >= 2 (my first try) was too low; expert uses >= 5. The high breakpoint is what defines this as "the Astronaut comp" vs "any comp that splashes 2 Astronauts."
  - **Reroll exclusions**: expert excludes Veigar(i3), IvernMinion(i3,★3), Poppy(i3) — low-cost reroll carries that share the Astronaut trait and contaminate the filter. Same pattern as xayah_carry: reroll carries are the main contamination risk.
  - **item_max=3**: expert uses exact 3 items, not just minimum 3.
- wrong: my Timebreaker filter was accidentally stricter (85k games) AND captured a different population than the expert (104k games at worse performance). My filter selected high-performing Timebreaker boards that happened to include Corki, rather than the actual Corki-in-Astronaut comp.

**Lesson**: When scouting boards, secondary traits can be misleading — two boards both showing Timebreaker didn't mean Timebreaker defines the comp. The comp name and high trait breakpoint (Astronaut >= 5) reveal the true identity. Also reinforced: high breakpoints (>= 5 vs >= 2) serve a filtering purpose — they narrow to the actual deep-trait comp, not random splashes. Finally, reroll carry exclusions (Veigar, IvernMinion★3, Poppy) are essential when the trait shell overlaps with reroll comps — the same lesson from the xayah exercise.

### spacegroove_nami → space_groove — 2026-04-22

**Observation**: From `cli.py scout --top 3`, two boards showed Nami(i3) as primary AP carry in a SpaceGroove shell: a #1 VN2 board (Nami(i3)/Riven(i3)/Nunu(i3)/TahmKench(i3), SpaceGroove_3) and a #2 EUW1 board (Nami(i3)/Riven(i3)/Nunu(i3), SpaceGroove_3). Both featured Ornn/Shen/Pantheon/Blitzcrank as tanky frontline. Named it "spacegroove_nami."

**My reasoning**: I observed Nami as the primary AP carry with SpaceGroove as the defining trait. Both scout boards showed SpaceGroove_3, but I reasoned that a higher breakpoint would separate the dedicated SpaceGroove comp from random splashes. I treated it as a carry + trait lock comp (Pattern 2), with Nami(i3) + SpaceGroove as the filter core. I excluded Samira(i3) as contamination — and Lissandra(i3)/Teemo(i3) as reroll carries.

**Filter iterations**:
1. `--or-units TFT17_Nami:i3 --traits TFT17_SpaceGroove:3` → 260,020 games, AVP 4.21, Top4 55.3%. SpaceGroove >= 3 too low — Blitz 78%, Shen 52%, but Illaoi 8%, Mordekaiser 7% leaking in from other comps. Still very broad.
2. `--or-units TFT17_Nami:i3 --traits TFT17_SpaceGroove:5` → 225,469 games, AVP 4.10, Top4 57.0%. Tighter — Blitz 84%, Shen 56%, Nunu 32%, Morgana 12%. Less contamination. Riven(i3) only 118 games — she's not as common as scout suggested.
3. `--or-units TFT17_Nami:i3 --traits TFT17_SpaceGroove:5 --exclude-units TFT17_Samira:i3,TFT17_Lissandra:i3,TFT17_Teemo:i3` → 216,828 games, AVP 4.12, Top4 56.8%. Removed ~8.6k games. Core units stable: Blitz 85%, Shen 57%, Nunu 31%.
4. Final: `--or-units TFT17_Nami:i3 --traits TFT17_SpaceGroove:5 --exclude-units TFT17_Samira:i3,TFT17_Lissandra:i3,TFT17_Teemo:i3`

**Expert filter**: `(Nami(i3,i_max=3) | Samira(i3,i_max=3)) & SpaceGroove >= 5 & ~Nasus(★3,i3,i_max=3)` → 235,417 games, AVP 4.11, Top4 56.9%

**Comparison**:
- right: SpaceGroove >= 5 breakpoint (matched expert exactly), Nami(i3) as carry, trait-shell comp identification
- missed:
  - **Samira is a co-carry, not contamination.** Expert uses OR(Nami(i3) | Samira(i3)) — Space Groove is a flex carry Line comp where either Nami or Samira can be the primary carry. I excluded Samira, losing ~18k legitimate games.
  - **Nasus(★3,i3) exclusion**: the correct reroll exclusion is Nasus★3 (a low-cost reroll carry in SpaceGroove), not Lissandra/Teemo. My reroll exclusions were misguided.
  - **item_max=3**: expert uses exact 3 items, not just minimum 3.
- over-excluded: Lissandra(i3), Teemo(i3) — expert doesn't need these within SpaceGroove >= 5.

**Lesson**: When scouting a trait-shell comp, identifying the comp type (Line vs single carry) determines whether alternative carries are contamination or legitimate flex options. Both scout boards happened to feature Nami, but Samira is equally valid as the primary carry in SpaceGroove. **Two boards showing the same carry doesn't mean the comp has a fixed carry** — need to look at more boards or check whether other units in the same trait shell also appear with 3 items. Also: reroll exclusions must target units that actually appear at ★3 with 3 items in this specific trait context (Nasus), not generically "reroll carries" from other comps (Lissandra/Teemo).

### primordian_belveth → primordian — 2026-04-22

**Observation**: From `cli.py scout --top 3`, 5 boards showed Belveth★3(i3) + RekSai★3(i3) in a Primordian shell with DRX_2: JP1 #2 (Belveth/Kindred/RekSai), VN2 #3 (Belveth/Kindred/RekSai/Maokai), EUN1 #3 (Akali★3(i3)/Belveth/RekSai), TR1 #3 (Akali/Belveth/RekSai), KR #3 (Akali/Belveth/RekSai). All featured Aatrox, Briar, Caitlyn, Maokai as supporting units. In 3/5 boards, Akali★3(i3) appeared as a co-carry alongside Belveth.

**My reasoning**: This is a reroll comp defined by Primordian trait + Belveth/Akali dual carry. Primordian >= 2 is the trait anchor. Unlike NOVA (which shares DRX trait), Primordian is niche enough that I expected minimal contamination from other comps. I identified Akali as a flex co-carry by iteration 2.

**Filter iterations**:
1. `--or-units TFT17_Belveth:i3 --traits TFT17_Primordian:2` → 214,396 games, AVP 4.11, Top4 59.3%. Core units clean: Maokai 93.6%, Kindred 87.7%, Caitlyn 75.0%. No 3-item carry contamination visible.
2. `--or-units TFT17_Belveth:i3,TFT17_Akali:i3 --traits TFT17_Primordian:2 --exclude-units TFT17_Fiora:i3,TFT17_Vex:i3,TFT17_Graves:i3` → 213,785 games. Exclusions removed only 611 games (0.3%), confirming minimal contamination. Core units unchanged.
3. Added `--exclude-units TFT17_Samira:i3,TFT17_Xayah:i3,TFT17_Nami:i3` → 213,600 games. Only 185 more removed. Confirmed: no exclusions needed.
4. Final: `--or-units TFT17_Belveth:i3,TFT17_Akali:i3 --traits TFT17_Primordian:2`

**Expert filter**: `(Belveth(i3,i_max=3) | Akali(i3,i_max=3)) & Primordian >= 2` — no exclusions. 220,933 games, AVP 4.13, Top4 58.8%.

**Comparison**:
- right: Belveth as primary carry, Primordian >= 2 as trait anchor, Akali as co-carry (dual carry pattern), no exclusions needed
- missed: item_max=3 (exact 3 items vs minimum 3), didn't include Akali in final filter initially
- over-excluded: iterations 2-3 tested NOVA carry exclusions (Fiora/Vex/Graves/Samira/Xayah/Nami i3) — all unnecessary, each removing <0.3% of games

**Lesson**: When a trait is niche enough (Primordian only has ~220k games total), the trait anchor alone provides sufficient boundary — no exclusions needed. This is Pattern 3 (OR-Carry + Trait) without the exclusion component. Cross-reference: `nova_yi` explicitly excludes `~Primordian >= 2`, confirming the trait boundary works bidirectionally. Also: spending iterations testing exclusions that remove <1% of games is a signal that the initial filter is already clean — recognize this early and stop iterating.

### mecha_asol_galio → mecha — 2026-04-22

**Observation**: From `cli.py scout --top 3`, 3 boards showed ASOL(i3) + Galio(i3) as dual carries in a Mecha shell: KR GM #1 (ASOL★3(i3)/Galio★3(i3)/Karma★3(i3)/TahmKench(i3)/Urgot, Mecha_3), VN2 Master #1 (ASOL★2(i3)/Bard★2(i3)/Fiora★2(i3)/Galio★2(i3)/TahmKench/Urgot, Mecha_3), EUN1 Master #1 (ASOL★2(i3)/Fiora★2(i3)/Galio★2(i3)/Karma★2(i3)/TahmKench/Urgot, Mecha_3). All featured TahmKench and Urgot as supporting units.

**My reasoning**: Identified ASOL + Galio as dual carries with Mecha as the defining trait. Scout boards showed Mecha_3, which I interpreted as `Mecha >= 3`. I used OR(ASOL_i3, Galio_i3) because CLI `--units` (AND) returned 0 games (likely a bug). I expected this to be a Pattern 2 (carry + trait lock) comp.

**Filter iterations**:
1. `--or-units TFT17_AurelionSol:i3,TFT17_Galio:i3 --traits TFT17_Mecha:3` → 273,339 games, AVP 4.60, Top4 47.2%. Too broad — captures any game with ASOL or Galio with 3 items + any Mecha splash. Fiora-1 at 103k (37.8%), Bard-1 at 83k (30.4%) — heavy contamination from NOVA/other comps.
2. Tried `--or-units TFT17_AurelionSol:i2,TFT17_Galio:i2 --traits TFT17_Mecha:6` → 15,323 games, AVP 6.65. Terrible — using OR instead of AND means only one carry is present, and Mecha >= 6 without both carries captures losing/incomplete boards.
3. Tried `--traits TFT17_Mecha:6` alone → 235,389 games, AVP 4.56. ASOL only appears in ~2% (4,646/235k), Galio ~2% (4,884/235k). Mecha >= 6 is dominated by non-ASOL/Galio boards — the trait shell alone is too broad without requiring both carries.
4. Could not make `--units` AND work (returned 0), so stopped iterating. Final: `--or-units TFT17_AurelionSol:i3,TFT17_Galio:i3 --traits TFT17_Mecha:3`

**Expert filter**: `ASOL(i2+) AND Galio(i2+) AND Mecha = 6 (exact)` → 225,068 games, AVP 4.50, Top4 48.8%

**Comparison**:
- right: identified ASOL + Galio as dual carries, Mecha as defining trait
- missed:
  - **AND not OR**: dual carry comps require both carries simultaneously (AND), not either-or (OR). My OR filter captured 48k extra games where only one carry was present.
  - **i2 not i3**: dual carry = items distributed between two units. Using i3 requires 3 full items on each carry, but in practice items are split (e.g., ASOL gets 3, Galio gets 2, or vice versa). i2 captures the full population.
  - **Mecha = 6 (exact) not >= 3**: trait ceiling prevents contamination from other comps that splash a few Mecha units. The "3" in scout data (Mecha_3) was the trait tier/breakpoint, not a min_units threshold for filtering.
  - **CLI `--units` AND returned 0 games**: I hit a possible bug and gave up instead of investigating. Should have tried alternative approaches or checked if the API params were correct.

**Lesson**: Dual carry comps require fundamentally different filter logic than single/flex carry comps: (1) AND both carries, not OR; (2) lower item threshold (i2) because items are split; (3) trait ceiling (exact match like `= 6`) is critical to prevent splash contamination. Also: when a CLI command returns unexpected 0 results, investigate the cause rather than abandoning the approach — it's likely a parameter issue, not proof that the filter is wrong.

### psyops_viktor → viktor — 2026-04-22

**Observation**: From `cli.py scout --top 3`, 4 boards showed Viktor(i3) as primary AP carry with PsyOps trait and Summon units: VN2 #1 (Viktor★3(i3)/Nami(i3)/Rhaast(i3)/Illaoi★3(i3)), VN2 #2 (Viktor★3(i3)/Sona(i3)/Illaoi(i3)), SG2 #3 (Viktor★2(i3)/Pyke★3(i3)/Mordekaiser★3(i3)), TW2 #3 (Viktor★3(i3)/Nami(i3)/Illaoi★3(i3)). All featured PsyOps_1 and most had SummonTrait_1 with low-cost frontline units (Mordekaiser, Pyke, Illaoi, Rhaast, IvernMinion, Lissandra).

**My reasoning**: Viktor appeared as a unique carry — no other comp uses Viktor as primary 3-item carry. The comp looked like a carry-only filter (Pattern 1). PsyOps trait was present in all boards but Viktor alone provides PsyOps, so the trait isn't a useful discriminator. Core units (Pyke 86%, Mordekaiser 86%, Illaoi 85%) all >80% confirmed a clean carry-only pattern with minimal contamination from other 3-item carries.

**Filter iterations**:
1. `--or-units TFT17_Viktor:i3` → 347,290 games, AVP 4.09, Top4 58.4%. Core units: Pyke 86%, Mordekaiser 86%, Illaoi 85%, IvernMinion 83%, Rhaast 81%, Lissandra 76%. 3-item carry contamination negligible (Nami-3: 186, Galio-2: 137). Very clean.
2. `--or-units TFT17_Viktor:i3 --traits TFT17_PsyOps:2` → 341,388 games, AVP 4.07. PsyOps >= 2 only removed 6k games — Viktor auto-provides PsyOps, so the trait is not a useful filter. Abandoned this direction.
3. Tested carry exclusions (Galio i3, ASOL i3) individually — each removed <13k games (<4%). Concluded carry-only filter is sufficient.
4. Final: `--or-units TFT17_Viktor:i3`

**Expert filter**: `Viktor(i3, i_max=3) & ~MissFortune & ~Pyke(i3, i_max=3) & ~MasterYi(i3, i_max=3)` → 254,478 games, AVP 4.06, Top4 59.0%

**Comparison**:
- right: carry-only approach (Pattern 1), identified Viktor as unique carry, no trait lock needed
- missed:
  - **~MissFortune (no item requirement)**: MF's presence indicates Conduit MF comp contamination, even without 3 items on MF. This is a "unit presence = comp identity" exclusion, not a "3-item carry" exclusion.
  - **~Pyke(i3)**: Pyke appeared at 86% in my filter and I assumed it was a core unit. But Pyke WITH 3 items is Pyke Reroll — a different comp. The expert excludes Pyke-as-carry while keeping Pyke-as-support.
  - **~MasterYi(i3)**: NOVA Yi comp shares low-cost units with Viktor comp.
  - **item_max=3**: exact 3 items, not minimum 3.
- over-included: 93k extra games (347k vs 254k) from MF/Pyke(i3)/Yi(i3) contamination.

**Lesson**: A unit appearing at >80% in a carry filter does NOT mean it shouldn't be excluded. Pyke at 86% was mostly Pyke-as-support (1 item), but the Pyke(i3) subset is contamination from Pyke Reroll. The distinction is: **exclude the unit-as-carry (i3), keep the unit-as-support (i1)**. Also: exclusions don't always require an item threshold — MissFortune is excluded entirely (any item count) because her presence signals a different comp direction regardless of itemization. The lesson: exclusion criteria should match the contamination signal, not a fixed template.

### leblanc_vanguard → vanguard_leblanc — 2026-04-22

**Observation**: From `cli.py scout --top 3`, 3 boards showed LeBlanc(i3) as primary AP carry in a Vanguard + Summon shell: VN2 #1 (LeBlanc★3(i3)/Blitz(i3)/Illaoi(i3)/IvernMinion/Nunu(i3)/Mordekaiser, ShieldTank_3, SummonTrait_1), EUW1 #2 (LeBlanc★3(i3)/Illaoi/IvernMinion/Nunu(i3)/Mordekaiser/Zoe(i3), ShieldTank_2, SummonTrait_1), VN2 #3 (LeBlanc★2(i3)/Illaoi(i3)/IvernMinion(i1)/Nunu(i3)/Mordekaiser/Morgana, ShieldTank_2, SummonTrait_1). All featured Mordekaiser, IvernMinion, Illaoi, Nunu as core frontline. Named it "leblanc_vanguard."

**My reasoning**: LeBlanc appeared as a unique AP carry in a Vanguard (ShieldTank) + Summon shell. I treated this as a carry + trait lock comp (Pattern 2), with LeBlanc(i3) + ShieldTank >= 2 + SummonTrait >= 3 as the filter core. I expected contamination from other AP carries (Viktor, Nami, Vex) and reroll carries (Teemo, Nasus, Lissandra) sharing the Summon trait shell.

**Filter iterations**:
1. `--or-units TFT17_Leblanc:i3 --traits TFT17_ShieldTank:2` → 273,657 games, AVP 4.44. Way too broad — ShieldTank >= 2 is too generic, captures many comps.
2. `--or-units TFT17_Leblanc:i3 --traits TFT17_ShieldTank:2,TFT17_SummonTrait:3` → 251,280 games, AVP 4.32. Adding SummonTrait >= 3 barely narrowed. Teemo 39k (15%), Lissandra 48k (19%), Nasus 33k (13%) — massive reroll contamination.
3. Added exclusions for known carries (Vex/Viktor/Nami/Samira/Xayah/Lissandra/Teemo/Nasus/Aurora i3) → 211,283 games, AVP 4.47. Core units clearer: Illaoi 98%, IvernMinion 91%, Mordekaiser 90%, Nunu 88%, Leona 86%, Karma 83%. But still very broad.
4. Aggressive exclusions (17 carries excluded) → 167,226 games, AVP 4.64. Core units stable but over-excluded with brute force.
5. Final: `--or-units TFT17_Leblanc:i3 --traits TFT17_ShieldTank:2,TFT17_SummonTrait:3 --exclude-units TFT17_Vex:i3,TFT17_Viktor:i3,TFT17_Nami:i3,TFT17_Samira:i3,TFT17_Xayah:i3,TFT17_Lissandra:i3,TFT17_Teemo:i3,TFT17_Nasus:i3,TFT17_Aurora:i3,TFT17_Bard:i3,TFT17_Sona:i3,TFT17_Galio:i3,TFT17_Fiora:i3,TFT17_Graves:i3,TFT17_Zed:i3,TFT17_MasterYi:i3,TFT17_Jhin:i3`

**Expert filter**: `LeBlanc(i3, i_max=3) & ShieldTank >= 2 & SummonTrait = 3 (exact) & ~Diana(i3) & ~Nasus(i3) & ~Zoe(i3) & ~Teemo(i3) & ~Vex(i3)` → 162,218 games, AVP 4.62

**Comparison**:
- right: LeBlanc(i3) as carry, ShieldTank >= 2, SummonTrait >= 3 as starting point, Vex(i3)/Teemo(i3)/Nasus(i3) exclusions
- missed:
  - **Summon = 3 (exact, not >= 3)**: the expert uses `max_units=3` to cap Summon at exactly 3, preventing overlap with Shepherd (Summon >= 5). This is the **trait ceiling** concept — without it, the filter captures Shepherd games where LeBlanc has items. My CLI only supports `>=`, so I couldn't express this.
  - **Diana(i3) and Zoe(i3) exclusions**: Diana is the Anima Diana carry; Zoe is an ADMIN carry. Both contaminate when given 3 items within the Summon/Vanguard shell. I missed these targeted exclusions.
  - **item_max=3**: expert uses exact 3 items
- over-excluded: I used 17 exclusions when the expert needs only 5 (Diana/Nasus/Zoe/Teemo/Vex). Samira, Xayah, Lissandra, Aurora, Bard, Sona, Galio, Fiora, Graves, Zed, MasterYi, Jhin — all unnecessary because their contamination rate in LeBlanc + ShieldTank + Summon=3 is negligible.

**Lesson**: **Trait ceilings (`max_units`) are as important as trait floors (`min_units`).** When a comp lives at a specific trait breakpoint (Summon = 3 for vanguard_leblanc), using `>= 3` captures all higher breakpoints too (Shepherd at >= 5). The ceiling is a surgical tool that one `max_units=3` parameter replaces dozens of exclusions — it removes Shepherd contamination at the trait level instead of unit-by-unit. Also: when faced with a filter that's too broad, the instinct to add more exclusions is a brute-force approach. The expert's method is to first identify the RIGHT trait constraints (including ceilings), then add only the targeted exclusions that the trait constraints can't handle.

### tf_jax_reroll → tf — 2026-04-22

**Observation**: From `cli.py scout --top 3`, 3 boards showed Jax★3(i3) + TwistedFate★3(i3) as dual reroll carries: SG2 #1 (Jax★3(i3)/TF★3(i3)/Aatrox★3/Caitlyn★3/Corki★2/Milio★2/Riven★2/Shen/Talon★3, Fateweaver_2), VN2 #3 (Jax★3(i3)/TF★3(i3)/Aatrox★3/Caitlyn★3/Gwen★2/Milio/Talon★3, Fateweaver_1), EUN1 #3 (Jax★3(i3)/TF★3(i3)/Corki★2(i3)/Aatrox★3/Caitlyn★3/Milio★2/Riven★2/Talon★3, Fateweaver_2). All shared Aatrox★3, Caitlyn★3, Talon★3 as low-cost reroll core. Named it "tf_jax_reroll."

**My reasoning**: Identified TF + Jax as dual reroll carries linked by Fateweaver trait. Tried Fateweaver >= 2 as trait anchor with OR(TF_i3, Jax_i3), then AND(TF_i3, Jax_i3). The main contamination source was Meeple Corki (Corki + Astronaut comp also runs TF+Jax). Attempted to exclude Corki(i3) and other carries, but the CLI couldn't express "exclude Corki regardless of items," so contamination persisted. The `--units` AND for 3+ units returned 0 games, blocking my attempt to add Aatrox as required core.

**Filter iterations**:
1. `--or-units TFT17_TwistedFate:i3,TFT17_Jax:i3 --traits TFT17_Fateweaver:2` → 218,877 games, AVP 4.29. Corki-1 at 129k (59%), Milio at 145k (66%) — overwhelmingly Meeple Corki contamination. OR captures single-carry boards.
2. `--units TFT17_TwistedFate:i3,TFT17_Jax:i3 --traits TFT17_Fateweaver:2` → 155,299 games, AVP 3.97. AND helped but Corki-1 still 100k (64%), Milio 110k (71%). Fateweaver trait is not distinctive — both reroll and Meeple Corki comps use it.
3. `--units TFT17_TwistedFate:i3,TFT17_Jax:i3 --traits TFT17_Fateweaver:2 --exclude-units TFT17_Corki:i3` → 133,421 games, AVP 4.14. Only excluded 3-item Corki; Corki-1 at 78k (59%), Milio still dominant. CLI `--exclude-units X:i3` only blocks 3-item version.
4. Tried TF(i3) only + various carry exclusions → 165k+ games, still Corki/Milio dominated. Could not find a unit/trait combination to isolate the reroll comp.
5. Final: stuck at `--units TFT17_TwistedFate:i3,TFT17_Jax:i3 --traits TFT17_Fateweaver:2 --exclude-units TFT17_Corki:i3` — 133k games, heavily contaminated.

**Expert filter**: `TF(i2+) AND Jax(i2+) & ~BT_on_Aatrox & ~Titan's_on_Jax` → 174,888 games, AVP 4.16, Top4 57.5%

**Comparison**:
- right: identified TF + Jax as dual carries, recognized they must be AND-linked
- missed:
  - **i2 not i3**: like the Mecha comp, dual carry = items distributed. Using i2 captures the full population. I defaulted to i3 because I saw scout boards with 3 items on each carry, but in practice items split between them.
  - **No trait anchor at all**: the expert uses NO Fateweaver trait — TF+Jax together are already distinctive enough. I wasted iterations trying to use Fateweaver as a discriminator, when it actually pulled in Meeple Corki contamination.
  - **Item-based exclusions (Pattern 5)**: the expert uses `~BT_on_Aatrox` and `~Titan's_on_Jax` — signature items that identify overlapping reroll comps (Aatrox reroll, Jax reroll). I never considered item-based exclusions. This is the most subtle pattern: when unit/trait overlap is unavoidable between reroll comps, specific item-on-unit combos serve as negative identifiers.
  - **The filter coexists with Corki boards**: Corki-1 at 108k (62%) in the expert filter too. The expert doesn't exclude Corki because TF+Jax+Corki boards ARE legitimate TF reroll games (the comp often includes Corki as a secondary unit). My assumption that Corki = contamination was wrong.

**Lesson**: **Low-cost reroll comps sharing the same unit pool can only be separated by item patterns, not by unit/trait filters.** TF reroll, Jax reroll, and Aatrox reroll all share Aatrox/Caitlyn/Talon/Jax/TF — you can't exclude units without destroying your own comp. The expert's solution is Pattern 5: signature items as negative identifiers (BT on Aatrox = Aatrox comp, Titan's on Jax = Jax comp). Also learned: dual carry comps use i2 not i3, and sometimes no trait anchor is needed when the unit combination itself is sufficiently distinctive. Finally: a unit appearing at high frequency in your filtered data (Corki at 62%) is not automatically contamination — it may be a legitimate secondary unit in the comp.

### nova_yi_carry → nova_yi — 2026-04-22

**Observation**: From `cli.py scout --top 3`, 3 boards showed MasterYi(i3) as primary melee carry with DRX trait and Kindred as secondary/co-carry: EUW1 #1 (MasterYi(i3)/Kindred(i3)/Graves(i3)/TahmKench(i3), DRX_1), VN2 #1 (MasterYi(i3)/Fiora(i3)/Kindred(i3)/Shen(i3)/TahmKench(i3), DRX_2, MeleeTrait_2), TW2 #2 (MasterYi(i3)/Kindred(i3)/Fiora(i3)/Maokai(i3)/Shen(i3), DRX_1, MeleeTrait_2). All featured Aatrox, Akali, Maokai as supporting units. Named it "nova_yi_carry."

**My reasoning**: MasterYi appeared as the primary melee carry with DRX as the defining trait — a NOVA variant. I treated it as a carry + trait lock comp (Pattern 2), starting carry-only then adding DRX >= 2. The main contamination concern was Primordian comp (Belveth/Akali carries) which shares most DRX units. I excluded individual carries (Belveth i3, Akali i3, Viktor i3) rather than the Primordian trait itself.

**Filter iterations**:
1. `--or-units TFT17_MasterYi:i3` → 202,612 games, AVP 4.44. Very dispersed — Belveth 38%, Sona 23%, many different comps using Yi as carry. No trait identity.
2. `--or-units TFT17_MasterYi:i3 --traits TFT17_DRX:2` → 131,731 games, AVP 4.34. Belveth still 56% — Primordian comp shares DRX trait. Akali 93%, Maokai 90%, core units present but heavily contaminated.
3. `--or-units TFT17_MasterYi:i3 --traits TFT17_DRX:2 --exclude-units TFT17_Belveth:i3,TFT17_Akali:i3,TFT17_Viktor:i3` → 120,718 games, AVP 4.36. Belveth still 55% as i1 support. Core units: Akali 93%, Maokai 90%, Aatrox 84%, Kindred 86%, TahmKench 66%, Fiora 60%.
4. Tested aggressive carry exclusions (added Fiora/Vex/Nami/Samira i3) → 79,254 games, AVP 4.90. Over-excluded — Fiora and Vex are legitimate NOVA flex carries. Abandoned.
5. Final: `--or-units TFT17_MasterYi:i3 --traits TFT17_DRX:2 --exclude-units TFT17_Belveth:i3,TFT17_Akali:i3,TFT17_Viktor:i3`

**Expert filter**: `(MasterYi(i3,i_max=3) | Kindred(i3,i_max=3)) & DRX >= 2 & ~Primordian >= 2 & ~Aatrox(i3,★3)` → 189,240 games, AVP 4.45

**Comparison**:
- right: MasterYi(i3) as primary carry, DRX >= 2 as trait anchor, recognized Primordian as main contamination source
- missed:
  - **Kindred is a co-carry (OR group)**: expert uses `MasterYi(i3) | Kindred(i3)`. I only used MasterYi(i3), losing ~68k games where Kindred was the primary carry and Yi was support. All 3 scout boards showed Kindred(i3), but I treated it as secondary rather than flex carry.
  - **~Primordian >= 2 (trait-level exclusion)**: expert excludes the entire Primordian trait (>= 2), not individual units. This is cleaner and more comprehensive — any board with 2+ Primordian units is excluded regardless of item counts. My unit-level exclusions (Belveth i3, Akali i3) only caught carry versions while missing support-item Primordian boards.
  - **~Aatrox(i3, ★3)**: excludes 3-star Aatrox reroll — a reroll variant sharing low-cost DRX units.
  - **item_max=3**: exact 3 items.
- over-excluded: Viktor(i3) — unnecessary because ~Primordian >= 2 already handles Viktor comp contamination (Viktor comp doesn't run Primordian trait, but the exclusion is redundant since Viktor games are a tiny fraction).

**Lesson**: **Trait-level exclusions (`~Trait >= N`) are more powerful than unit-level exclusions (`~Unit(i3)`) when two comps share the same unit pool but differ by trait identity.** NOVA Yi and Primordian share Aatrox, Akali, Maokai, Kindred, RekSai — excluding individual units as carries (i3) misses the contamination from support-item versions. `~Primordian >= 2` cleanly separates the two comps at the trait boundary. Also: when a unit (Kindred) appears at 86% with 3 items in the filtered data AND appears as i3 in all scout boards, it's a co-carry signal — should be in an OR-group, not treated as secondary.

### admin_teemo_reroll → teemo — 2026-04-22

**Observation**: From `cli.py scout --top 3`, 2 boards showed Teemo★3(i3) as primary AP carry alongside Leona★3(i3) and Zoe in a Summon shell: BR1 #2 (Leona★3(i3)/Lissandra★3(i3)/Teemo★3(i3)/Zoe★2, ADMIN_1, SummonTrait_1, with Illaoi/Mordekaiser/Nasus frontline) and TW2 #2 (Leona★3(i3)/Teemo★3(i3)/Zoe★2(i3), ADMIN_1, SummonTrait_1, with Illaoi/Mordekaiser/Blitzcrank/Nami). Both featured ADMIN trait (Teemo + Zoe) and a Summon-heavy frontline (Illaoi, Mordekaiser, Nasus, Lissandra). Named it "admin_teemo_reroll."

**My reasoning**: Teemo appeared as the primary AP carry with ADMIN as a potentially defining trait (Teemo + Zoe both ADMIN). I treated it as a carry + trait lock comp (Pattern 2), with Teemo(i3) + ADMIN >= 2 as the filter core. I expected contamination from vanguard_leblanc (LeBlanc shares Summon units) and other AP carries (Viktor, Nami, Aurora). I added carry exclusions to clean up.

**Filter iterations**:
1. `--or-units TFT17_Teemo:i3` → 106,821 games, AVP 4.17, Top4 57.6%. Core units: Leona 95%, Nasus 94%, Mordekaiser 93%, Illaoi 92%, Summon 91%, Zoe 68%, Lissandra 69%, LeBlanc-1 37%, Nunu 38%. Very clean already.
2. `--or-units TFT17_Teemo:i3 --traits TFT17_ADMIN:2` → 92,250 games, AVP 4.09, Top4 59.3%. ADMIN >= 2 only removed ~14k games. LeBlanc still 42%. Trait not very discriminating.
3. `--or-units TFT17_Teemo:i3 --traits TFT17_ADMIN:2 --exclude-units TFT17_Leblanc:i3,TFT17_Nami:i3,TFT17_Viktor:i3,TFT17_Aurora:i3` → 73,770 games, AVP 4.26, Top4 55.6%. LeBlanc-1 (support) still 36%. Core units clean but over-excluded.
4. Tested OR-carry with Leona: `--or-units TFT17_Teemo:i3,TFT17_Leona:i3 --traits TFT17_ADMIN:2 --exclude-units ...` → 96,140 games. Leona expanded too much — Teemo dropped to 83%, IvernMinion appeared at 11%. Leona is a co-tank, not an independent carry. Abandoned.
5. Final: `--or-units TFT17_Teemo:i3 --traits TFT17_ADMIN:2 --exclude-units TFT17_Leblanc:i3,TFT17_Nami:i3,TFT17_Viktor:i3,TFT17_Aurora:i3`

**Expert filter**: `Teemo(i3, i_max=3) & ~Guinsoo's_on_Nasus` → 106,883 games, AVP 4.17, Top4 57.6%

**Comparison**:
- right: Teemo(i3) as primary carry, identified it as a unique carry
- missed:
  - **No trait lock needed**: Teemo is unique enough — no ADMIN, no Summon, no trait anchor at all. This is Pattern 1 (carry-only), not Pattern 2. My ADMIN >= 2 removed 14k legitimate games for no benefit.
  - **Item-based exclusion (Pattern 5)**: expert uses `~Guinsoo's_on_Nasus` to separate from Nasus reroll, which shares the identical unit pool. Guinsoo's on Nasus signals Nasus-carry, not Teemo-carry. Same logic as `tf` exercise (BT on Aatrox, Titan's on Jax).
  - **item_max=3**: exact 3 items.
- over-excluded: ADMIN >= 2 (-14k), LeBlanc(i3)/Nami(i3)/Viktor(i3)/Aurora(i3) exclusions (-19k more). Total: 33k legitimate games lost (31% of expert sample). LeBlanc(i3) appearing in 37% of Teemo games isn't contamination — it's boards that legitimately run both Teemo and LeBlanc as carries (different item slots in a Summon shell).

**Lesson**: **When a carry is unique, the carry-only filter IS the answer.** Adding trait locks to a unique carry doesn't improve accuracy — it just shrinks sample size. The instinct to "add context" (Dishsoap method) must be calibrated: context helps when carries are shared across comps, but HURTS when the carry is already distinctive. Teemo is like Viktor or Zed — no other comp runs Teemo(i3) as primary carry. Also reinforced: for low-cost reroll comps sharing unit pools, **item-based exclusions are the only way** to separate them (Nasus reroll vs Teemo reroll share Nasus/Leona/Mordekaiser/Illaoi/Lissandra). The item on a shared unit identifies which reroll variant the board belongs to.

### stargazer_samira → two_tanky_samira — 2026-04-22

**Observation**: From `cli.py scout --top 3`, 3 boards showed Samira★3(i3) with Ornn★3(i3) and a tanky frontline (Nunu, Rhaast, Blitzcrank, Jax): KR Master #1 (Samira★3(i3)/Ornn★3(i3)/Nunu(i3)/Xayah(i3), Stargazer_Mountain_4), VN2 Master #2 (Samira★3(i3)/Ornn★3(i3)/Rhaast★3(i3)/Blitz(i3), Stargazer_Wolf_1), VN2 Master #3 (Samira★3(i3)/Ornn★3(i3)/Nunu(i3)/Rhaast★3, Stargazer_Serpent_1). I named it "stargazer_samira" based on the Stargazer trait visible across all boards.

**My reasoning**: Samira appeared as a unique-ish carry — I assumed Samira(i3) would be a carry-only filter (Pattern 1). The Stargazer traits present in all boards seemed potentially useful as a trait anchor. I expected SpaceGroove (Nami/Samira as flex carries) to be the main contamination source and tried excluding Nami(i3) and Lissandra(i3).

**Filter iterations**:
1. `--or-units TFT17_Samira:i3` → 123,159 games, AVP 4.38, Top4 51.5%. Core units: Ornn 94%, Nunu 86%, Jax 80%, Xayah 79%, Blitzcrank 41%. Minimal 3-item carry contamination. Very clean already.
2. `--or-units TFT17_Samira:i3 --exclude-units TFT17_Nami:i3,TFT17_Riven:i3` → 112,686 games, AVP 4.42, Top4 50.6%. Nami/Riven exclusions only removed 10k games (8%). Unit profile unchanged — SpaceGroove contamination negligible at i3 level.
3. `--or-units TFT17_Samira:i3 --exclude-units TFT17_Nami:i3,TFT17_Lissandra:i3` → 114,861 games, AVP 4.42, Top4 50.7%. Same story — exclusions barely moved the needle. Carry-only filter is already clean.
4. Final: `--or-units TFT17_Samira:i3` (carry-only, no exclusions needed)

**Expert filter**: `Samira(count=2)` — requires only Samira★2+ (2 copies on board). No item requirement, no trait, no exclusions. 241,374 games, AVP 4.48, Top4 49.8%.

**Comparison**:
- right: identified Samira as a unique-enough carry with no trait lock or exclusions needed
- missed:
  - **Completely different filter paradigm**: expert uses `count=2` (star level ★2+), not `item_min=3`. This is NOT Pattern 1 (carry-only with items). The comp is defined by having a 2-star Samira, regardless of whether she has 0, 1, 2, or 3 items. My i3 filter captured 123k games; the expert captures 241k — nearly double.
  - **"Two Tanky Samira" is not a carry comp**: the comp name ("成双莎弥拉") implies Samira★2 as a presence marker, not an itemized carry. The expert's unit profile includes Riven at 25%, Nami at 35%, Pantheon at 22% — much broader than a carry comp.
  - **Star-level = comp identity for some comps**: this is a comp where having Samira★2 on board defines the comp, similar to how reroll comps are defined by ★3 units. The item count is irrelevant — what matters is whether you committed to Samira (by 2-starring her).
  - **Misread the scout data**: I focused on Samira's items (i3) and Stargazer traits from the scout boards. But the scout boards were top-3 finishes — of course they have items on their carry. The comp's IDENTITY is simpler than what top boards show.

**Lesson**: **Not all comps are defined by items or traits — some are defined by star level.** The 5 patterns in the guide (carry-only, carry+trait, OR-carry+trait+exclusions, carry+exclusions, item-based exclusions) all assume items are part of the comp identity. "Two Tanky Samira" introduces a 6th paradigm: **star-level presence** (`count=N`). The comp is "any board that committed to Samira★2+", and adding an item requirement (i3) artificially excludes half the legitimate games. This is a blindspot in the current guide. Also: scout board observations are biased toward winning boards — the carries always look itemized in top-3 finishes, which can mislead you into thinking item count is definitional when it's not.

### veigar_reroll → veigar — 2026-04-22

**Observation**: From `cli.py scout --top 3`, 4 boards showed Veigar★3(i3) as primary AP carry: JP1 #1 (Veigar★3(i3)/Ornn★3(i3)/Poppy★3, Astronaut_1, SummonTrait_1), KR #2 (Veigar★3(i3)/Bard★2(i3)/Rammus★2(i3), Astronaut_2), TW2 #2 (Veigar★3(i3)/Poppy★3(i3)/Lissandra★2(i3)/Gnar★2(i3), Astronaut_3), VN2 #3 (Veigar★3(i3)/Corki★2(i3)/Rammus★2(i3), Astronaut_2). All featured Veigar★3 as the AP reroll carry with JG/Nashor/SoS builds. The secondary units varied widely (Ornn, Bard, Poppy, Corki) — no consistent trait shell or co-carry.

**My reasoning**: Veigar appeared as a reroll AP carry across multiple boards, but with no consistent trait shell (Astronaut breakpoints ranged 1-3, secondary carries varied). I initially treated it as a carry-only filter (Pattern 1), which was correct. However, I then second-guessed myself because no core unit exceeded 80% besides Rammus (a generic tank) — I interpreted the dispersed unit profile as contamination rather than recognizing that Veigar's comp is genuinely flexible in supporting units. This led me to over-exclude in subsequent iterations.

**Filter iterations**:
1. `--or-units TFT17_Veigar:i3` → 112,267 games, AVP 4.35, Top4 52.2%. Rammus 87%, Illaoi 57%, Bard 44%, Galio 12%. No 3-item carry contamination visible. **This was already the answer.**
2. `--or-units TFT17_Veigar:i3 --exclude-units TFT17_Poppy:i3` → 59,904 games, AVP 4.53, Top4 48.5%. Lost 47% of games — massive over-exclusion. Poppy(i3) is a co-present carry in Veigar boards, not contamination.
3. `--or-units TFT17_Veigar:i3 --exclude-units TFT17_Poppy:i3,TFT17_Corki:i3,TFT17_Galio:i3` → 39,197 games, AVP 4.80, Top4 43.4%. Destroyed the filter — removed 65% of legitimate games. Performance collapsed.

**Expert filter**: `Veigar(i3, i_max=3)` — pure carry-only, no exclusions, no trait. 112,325 games, AVP 4.35, Top4 52.2%.

**Comparison**:
- right: Iteration 1 was the correct answer — carry-only filter (Pattern 1), no trait lock, no exclusions needed
- missed: item_max=3 (exact 3 items vs minimum 3) — a minor precision detail
- over-excluded: iterations 2-3 added Poppy(i3), Corki(i3), Galio(i3) exclusions that destroyed the filter. Each of these units legitimately co-exists with Veigar in the same boards

**Lesson**: **When iteration 1 is already clean, stop iterating.** The absence of >80% core units (besides Rammus) is not a contamination signal — it's a signal that Veigar's comp is genuinely flexible in its supporting cast. Different boards pair Veigar with Astronaut units, Summon units, or generic tanks, but they're all legitimately "the Veigar comp." The instinct to "clean up" a dispersed unit profile by adding exclusions is dangerous when the carry is already unique. A unique carry with a flexible support shell = carry-only filter, full stop. Also: when exclusions remove >10% of games and AVP gets worse (not better), that's a clear signal you're cutting real games, not contamination.

### vex_summon → vex_95 — 2026-04-22

**Observation**: From `cli.py scout --top 3`, 5 boards showed Vex(i3) as primary AP carry with Blitzcrank and Mordekaiser in a Summon/Vanguard shell — NOT in DRX/NOVA context: VN2 #2 (Vex(3)/Blitz(3)/Nunu(3), ShieldTank_2, SummonTrait_1), VN2 #2 (Vex(3)/Sona(3)/Blitz(3)/Nunu(3), SummonTrait_3), EUW1 #1 (Vex(3)/Zoe★3(3)/Leona★3(3), ShieldTank_3). These boards shared Vex as AP carry with a tanky Summon/Vanguard frontline (Blitzcrank, Mordekaiser, Illaoi, IvernMinion, Nunu), distinct from NOVA boards which feature DRX trait + Fiora/Graves flex carries. Named it "vex_summon."

**My reasoning**: Vex appeared as a shared carry across multiple comps (NOVA, DarkStar, vex_95, vanguard_leblanc). I needed to isolate the specific "Vex in Summon/Vanguard shell" variant. Starting carry-only would be far too broad (526k games). The key distinguishing features were: (1) no DRX trait (separates from NOVA), (2) Blitzcrank + Mordekaiser as frontline anchors, (3) no LeBlanc (separates from vanguard_leblanc).

**Filter iterations**:
1. `--or-units TFT17_Vex:i3` → 525,870 games, AVP 4.12, Top4 56.4%. Way too broad — Vex appears as carry in NOVA (Fiora 48%, Graves 46%), DarkStar, vanguard_leblanc, and vex_95 simultaneously. No core unit >80%. Carry-only is insufficient for a shared carry.
2. `--or-units TFT17_Vex:i3 --exclude-units TFT17_Fiora:i3,TFT17_Graves:i3,TFT17_Leblanc:i3,TFT17_Jhin:i3 --exclude-traits TFT17_DRX:2` → 237,626 games, AVP 4.33, Top4 52.5%. Better — excluded NOVA flex carries and DRX trait. But still very dispersed: Blitzcrank 76%, Mordekaiser 73%, IvernMinion 69%, no unit >80%. The filter is "Vex in non-DRX, non-NOVA everything" — still too broad.
3. Could not add `--units TFT17_Blitzcrank,TFT17_Mordekaiser` AND condition (CLI returned 0 when mixing `--units` AND with `--or-units`). Stopped iterating due to CLI limitation.

**Expert filter**: `Vex(i3, i_max=3) & Blitzcrank & Mordekaiser & ~LeBlanc & ~DRX >= 2 & ~Jhin(i3)` → 143,811 games, AVP 3.81, Top4 62.1%

**Comparison**:
- right: identified need for DRX exclusion (`~DRX >= 2`), recognized Vex is a shared carry requiring more than carry-only, excluded Jhin(i3) and LeBlanc as contamination sources
- missed:
  - **Blitzcrank & Mordekaiser as AND conditions (Pattern 4)**: the expert requires BOTH Blitzcrank and Mordekaiser to be present on the board — they define the comp's frontline identity, not just the carry. My filter was 66% larger (238k vs 144k) because I couldn't enforce this AND condition. Blitz+Morde at 100% in the expert filter confirms they ARE the comp's definition alongside Vex.
  - **~LeBlanc (no item requirement)**: expert excludes LeBlanc entirely (any item count), not just LeBlanc(i3). LeBlanc's presence signals vanguard_leblanc regardless of itemization — same pattern as MissFortune in the Viktor filter.
  - **item_max=3**: exact 3 items
- over-excluded: Fiora(i3) and Graves(i3) — the expert doesn't need these because `~DRX >= 2` already handles NOVA contamination. My carry exclusions were redundant with the trait exclusion.

**Lesson**: **When a carry appears in 4+ different comps, carry-only filtering is useless.** Vex is the most shared carry in S17 — she appears in NOVA, DarkStar, vex_95, vanguard_leblanc. The expert solves this not with trait locks (Vex doesn't have a unique trait) but with **unit AND conditions** (Blitzcrank + Mordekaiser = this specific Vex comp) plus **comp-boundary exclusions** (~DRX >= 2 for NOVA, ~LeBlanc for vanguard_leblanc, ~Jhin(i3) for DarkStar). This is a **hybrid of Pattern 4 (carry + minimal exclusions) and trait-level exclusion**. Also learned: when `--exclude-traits` removes contamination and `--exclude-units` targeting the same comps' carries is redundant — prefer the trait-level exclusion (fewer parameters, same effect). Finally: some units (LeBlanc, MissFortune) are excluded entirely regardless of items because their mere presence signals a different comp direction.
