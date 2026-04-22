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
