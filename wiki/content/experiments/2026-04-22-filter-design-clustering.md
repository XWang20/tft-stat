# Filter Design Exercise: Comp Discovery from Endgame Boards
Status: 🧪 draft
Date: 2026-04-22
Module: 1

## The Question

Can we discover the meta comp landscape from scratch by observing top-player endgame boards, clustering them into patterns, and designing filters for each — without looking at expert definitions?

## Observation

Ran `cli.py scout --top 3` and collected **38 top-3 boards** from Challenger/GM/Master across VN2, KR, EUW1, EUN1, SG2. Key observations:

1. **Carries are visible**: 3-item units clearly mark the comp identity. Most boards have 1-2 primary carries with 3 items, plus 1-2 tanks with 3 defensive items.
2. **Trait shells matter**: the same carry in different trait contexts means different comps (e.g., Vex in DRX vs Vex in Vanguard shell).
3. **Reroll comps stand out**: 3-star units with 3 items are unmistakable (Belveth★3, Akali★3, Pyke★3).
4. **Some boards are hybrid**: e.g., Viktor(i3) + Vex(i3) in the same Dark Star shell — which comp is this?

## Clustering

### Cluster A: "NOVA" — DRX Flex Carry (5 boards)
**Defining features**: MasterYi(i3) and/or Kindred(i3) and/or Fiora(i3) with DRX trait. Melee-heavy with Aatrox, Akali, Shen, TahmKench support.
**Boards**: 5 boards across VN2.
**Key pattern**: carry slot rotates between MasterYi, Fiora, Kindred. DRX trait is the anchor. TahmKench often appears as tank with 3 items.
**Distinct from**: Mecha (no Galio/ASol), Primordian (no Belveth/RekSai).

### Cluster B: "Viktor Voyager" — Dark Star / Voyager Shell (5 boards)
**Defining features**: Viktor(i3) as carry, with Illaoi, IvernMinion, Mordekaiser, Lissandra, Rhaast, Pyke. DarkStar + Voyager traits.
**Boards**: 5 boards across EUN1, EUW1, VN2, KR.
**Key pattern**: Viktor is the AP carry. Illaoi often has 3 tank items. Rhaast appears frequently. Nami sometimes present but as support.
**Distinct from**: Vanguard LeBlanc (no LeBlanc, different trait shell). Some boards also have Nami(i3) as secondary carry.

### Cluster C: "Space Groove" — Riven + Nami (5 boards)
**Defining features**: Riven(i3) + Nami(i3) + Blitzcrank, SpaceGroove ≥ 3. Often with Pantheon, Shen, Gwen, Ornn.
**Boards**: 5 boards across VN2, SG2, KR.
**Key pattern**: Riven carries AD items (Bloodthirster, Edge of Night), Nami carries AP items (JG, Nashor's, Spear). Blitzcrank often has 3 items too. SpaceGroove emblem on Riven is common.
**Distinct from**: Space Groove Nami (different SpaceGroove breakpoint, different carry identity).

### Cluster D: "Vanguard LeBlanc" — LeBlanc + Vanguard/Summon (3 boards)
**Defining features**: LeBlanc★3(i3) as primary carry, Vanguard (ShieldTank) ≥ 2, Nunu(i3) frontline. IvernMinion, Mordekaiser support.
**Boards**: 3 boards across EUW1, SG2, KR.
**Key pattern**: LeBlanc is always 3-star with 3 items. ADMIN trait (Arbiter) appears in 2/3 boards. Summon trait present. Leona as secondary tank.
**Distinct from**: Viktor (different carry, different trait shell).

### Cluster E: "Jhin/Xayah Sniper" — Ranged Carry Duo (3 boards)
**Defining features**: Jhin(i3) + Xayah(i3), Sniper (RangedTrait) ≥ 2, Nunu(i3) + Rammus(i3) tank pair.
**Boards**: 3 boards in VN2.
**Key pattern**: dual AD carry — both Jhin and Xayah have 3 items. Morgana often present. Bard, Gnar, Sona as support. Nunu always has 3 tank items.
**Distinct from**: Pure Xayah (different support structure).

### Cluster F: "Mecha" — ASol + Galio (2 boards)
**Defining features**: AurelionSol(i3) + Galio(i3), Mecha trait.
**Boards**: 2 boards (EUN1, VN2).
**Key pattern**: ASol is AP carry, Galio is tank carry. Dual-item distribution. Fiora and Urgot appear as support.
**Distinct from**: NOVA (no DRX, different unit shell entirely).

### Cluster G: "Primordian Belveth" — Belveth Reroll (2 boards)
**Defining features**: Belveth★3(i3), Primordian ≥ 2. Often with RekSai★3, Akali★3, Maokai★3.
**Boards**: 2 boards in VN2.
**Key pattern**: heavy reroll comp — multiple 3-star units. Kindred sometimes present as secondary carry.
**Distinct from**: NOVA (Primordian trait vs DRX, reroll vs level-up).

### Minor Patterns (1 board each)
- **Bard + Veigar Summon**: Astronaut shell with Bard(i3) + Veigar(i3)
- **Pyke Reroll**: Pyke★3(i3) + Gwen★3(i3) + Milio★3(i3)
- **Aurora Flex**: Aurora★3(i3) + Viktor★3(i3), Voyager trait
- **Ezreal Reroll**: Chogath★3(i3) + Ezreal★3(i3), Timebreaker
- **Kaisa Reroll**: Fizz★3(i3) + Kaisa★3(i3)
- **Dark Star Kaisa**: Jhin(i3) + Kaisa(i3) + DarkStar ≥ 3

## Filter Design Process

### Cluster A: NOVA

**v1**: `--or-units TFT17_MasterYi:i3,TFT17_Fiora:i3,TFT17_Kindred:i3 --traits TFT17_DRX:2`
- Games: 416,076 | AVP: 4.01 | Top4: 59.7%
- Core units present: Shen (213k), Fiora (226k), Graves (108k), Vex (96k), Blitzcrank (88k) — all expected
- **Contamination**: Zed (9.6k), Belveth (208k high freq = support not carry ok), Kaisa (1.8k)
- IC3: Fiora 226k/416k ≈ 54%, but OR-group so checking any carry — reasonable

**v2**: Added `--exclude-units TFT17_Kindred:i3,TFT17_Aurora:i3,TFT17_Zed:i3 --exclude-traits TFT17_Mecha:3`
- Games: 248,957 | AVP: 4.14 | Top4: 56.0%
- Removed Kindred (could be own carry comp), Zed (separate comp), Aurora (Anima), Mecha overlap
- Core units still present: Shen 192k, Fiora 206k, Vex 174k, Graves 188k — clean
- **Decision**: Kindred exclusion was a judgment call. In the boards, some NOVA boards DO run Kindred(i3). This splits NOVA from what might be "nova_yi."

**Reflection**: I initially grouped MasterYi+Kindred+Fiora together. The expert might separate MasterYi/Kindred (lower cost, DRX carry) from Fiora/Vex/Graves (5-cost flex carry).

### Cluster B: Viktor Voyager

**v1**: `--or-units TFT17_Viktor:i3 --traits TFT17_DarkStar:2`
- Games: 279,248 | AVP: 3.86 | Top4: 63.0%
- Core: Nami (196k), Rhaast (244k), IvernMinion (264k), Summon (260k) — these are comp units
- **Contamination**: too many non-Viktor things. Viktor only 3,359 games within this filter — he's rare! DarkStar ≥ 2 is too broad.

**v2**: Added Voyager trait — `--traits TFT17_DarkStar:2,TFT17_FlexTrait:2`
- Games: 267,111 | AVP: 3.81 | Top4: 64.2%
- Core: Nami (188k), Sona (14k), Blitzcrank (6.4k), Galio (11k), Fiora (3.7k) — matches the boards
- **Still broad**: Viktor is only ~2k of 267k. The filter captures the Voyager + DarkStar *shell*, but Viktor is one carry option within it.

**Reflection**: This comp might be better defined as "Viktor carry-only" since the shell is used by many carries. The expert definition confirms this — `viktor` is `Unit(Viktor, i3)` minus MF, Pyke, MasterYi. Much simpler.

### Cluster C: Space Groove

**v1**: `--or-units TFT17_Nami:i3,TFT17_Riven:i3 --traits TFT17_SpaceGroove:3`
- Games: 283,792 | AVP: 4.31 | Top4: 53.4%
- Core units: Shen (145k), Blitzcrank (219k), Mordekaiser (18k), Leona (12k) — reasonable
- **Contamination**: LeBlanc (3.3k), Viktor (5.9k), Vex (7.4k) — other carries leaking in

**v2**: Added `--exclude-units TFT17_Leblanc:i3,TFT17_Viktor:i3`
- Games: 281,931 | AVP: 4.32 | Top4: 53.3%
- Minimal change — LeBlanc/Viktor were small. Shen still 145k.
- The filter is reasonable. Riven + Nami as flex carries in SpaceGroove ≥ 3 captures the pattern.

**Reflection**: The expert uses SpaceGroove ≥ 5 (not ≥ 3) with `(Nami i3 | Samira i3)`. Two differences: (1) I missed Samira as a carry option, (2) the expert uses a higher trait threshold. SpaceGroove ≥ 5 is a "Line" comp — the trait shell matters more than specific units.

### Cluster D: Vanguard LeBlanc

**v1**: `--or-units TFT17_Leblanc:i3 --traits TFT17_ShieldTank:2`
- Games: 272,890 | AVP: 4.44 | Top4: 51.2%
- **Major contamination**: Aurora (16k), Jinx (11k), Vex (17k) — other carries in Vanguard shell

**v2**: Added exclusions for Aurora, Jinx, Vex, Jhin; excluded DRX
- Games: 247,909 — barely changed. Teemo (37k), Nasus (37k) still present.
- The Vanguard shell is too broad without Summon constraint.

**v3**: Added `--traits TFT17_SummonTrait:3` to lock Shepherd = 3
- Games: 240,598 | AVP: 4.36
- Better but still broad. Aurora (15k), Jinx (11k) still present.
- LeBlanc appears in varying frequencies — the comp exists but isn't dominant in this shell.

**Reflection**: The expert uses `Summon = 3` (exact, not ≥ 3) to prevent Shepherd (Summon ≥ 5) overlap, plus 5 carry exclusions. My approach was directionally correct but insufficient — I needed exact trait matching and more carry exclusions.

### Cluster E: Jhin/Xayah Sniper

**v1**: `--or-units TFT17_Jhin:i3,TFT17_Xayah:i3 --traits TFT17_RangedTrait:2`
- Games: 495,986 | AVP: 4.18 | Top4: 55.2%
- **Contamination**: Samira (11k), Kaisa (27k), Riven (64k) — other carries
- Bard (204k), Jax (173k) — lots of non-Jhin/Xayah games

**v2**: Excluded Samira, LeBlanc, Nami
- Games: 460,258 — barely changed. Still very broad.

**v3**: Jhin only (without Xayah in OR-group) + Sniper
- Games: 254,765 | AVP: 3.52 — much better! Jax (173k), Rhaast (96k), Bard (121k) as support.
- This is actually a "Jhin Sniper" comp, not "Jhin+Xayah." Xayah appears as secondary.

**Reflection**: The expert has `xayah` as a separate comp (Xayah i3, carry-only pattern with many exclusions). There's no combined "Jhin+Xayah" — they're treated separately. My cluster was artificially merged. The expert doesn't even have a "Jhin" comp — Jhin appears as support in many comps via his unique Eradicator trait.

### Cluster F: Mecha

**v1**: `--units TFT17_AurelionSol:i2,TFT17_Galio:i2 --traits TFT17_Mecha:3`
- Games: 1,494 | AVP: 7.39 — terrible performance, tiny sample

**v2**: Without trait lock (just ASol + Galio with items)
- Games: 1,525 | AVP: 7.38 — almost identical. The unit pair IS the comp.

**Reflection**: Expert uses `Mecha = 6` (highest breakpoint), which is even more restrictive. The comp exists but performs very poorly on this patch (AVP 7.39). Only 1,525 games total — far below the 1000-game minimum for reliable analysis. The comp is identifiable but not meta-viable.

### Cluster G: Primordian Belveth

**v1**: `--or-units TFT17_Belveth:i3 --traits TFT17_Primordian:2`
- Games: 212,978 | AVP: 4.11 | Top4: 59.3%
- Shen (43k), MasterYi (10k), Fiora (11k) leaking from NOVA.

**v2**: Excluded MasterYi i3, DRX ≥ 2
- Games: 3,794 | AVP: 5.36 — much smaller. The DRX exclusion killed most games.
- Core units present: Belveth 3.7k, Fiora (726), Kindred (533), Urgot (1.1k)

**Reflection**: Expert uses `(Belveth i3 | Akali i3) & Primordian ≥ 2` — I missed Akali as a carry option! The boards showed Akali★3(i3) in one Primordian board. Also, the expert doesn't exclude DRX — the Primordian trait lock alone is sufficient to separate.

## Comparison with Ground Truth

| My Cluster | Expert Comp | Match Quality | Key Differences |
|---|---|---|---|
| A: NOVA | `nova_95` + `nova_yi` | **Partial** | Expert splits into two: nova_95 (Fiora/Vex/Graves, excludes MasterYi/Kindred) and nova_yi (MasterYi/Kindred, excludes Primordian). I merged them. |
| B: Viktor Voyager | `viktor` | **Wrong approach** | Expert uses carry-only pattern (`Viktor i3`, minus MF/Pyke/MasterYi). I tried to capture the shell (DarkStar + Voyager), which is far too broad. Viktor is unique enough for carry-only. |
| C: Space Groove | `space_groove` | **Close** | Expert uses SpaceGroove ≥ 5 (not ≥ 3) and includes Samira as carry. I missed Samira and used too low a trait threshold. |
| D: Vanguard LeBlanc | `vanguard_leblanc` | **Directionally correct** | Expert uses Summon = 3 (exact) + 5 carry exclusions. I identified the need for Summon but couldn't refine enough. |
| E: Jhin/Xayah Sniper | `xayah` (separate) | **Wrong cluster** | Expert treats Xayah as standalone carry-only comp. No "Jhin comp" exists — Jhin is support. My cluster was artificially merged. |
| F: Mecha | `mecha` | **Correct but weak** | Expert uses Mecha = 6 (stricter). Both find the same tiny, poorly-performing comp. |
| G: Primordian Belveth | `primordian` | **Close** | Expert includes Akali as carry option. I missed this. Expert doesn't exclude DRX — Primordian trait alone suffices. |

### What I Missed Entirely
- **`vex_95`**: Vex in non-DRX, non-Vanguard context (Vex + Blitz + Morde). I didn't see enough boards to identify this pattern.
- **`voyager`** (Nami): separate from Space Groove. Nami + Karma + Lissandra without Viktor/Pyke/LeBlanc.
- **`shepherd`**: Summon ≥ 5 comp — I saw hints but couldn't distinguish from LeBlanc's Summon = 3.
- **`dark_star`**: DarkStar ≥ 4 as its own comp. I saw some DarkStar boards but merged them into Viktor.
- **Reroll comps** (`pyke`, `kaisa`, `bonk`, `lulu`, `tf`, `teemo`, `ez_chogath`, etc.): only 38 boards is too few to catch rare reroll comps reliably.

### What I Got Right
1. **NOVA is a flex carry comp** — I correctly identified the OR-carry-group + DRX pattern.
2. **Mecha is ASol + Galio** — correct carry pair and dual-item distribution concept.
3. **Space Groove is a Line comp** — I identified Riven + Nami + SpaceGroove trait as the shell.
4. **Primordian is a reroll comp** — correct identification of Belveth + Primordian.
5. **Vanguard LeBlanc needs Summon** — I discovered this through iteration, matching the expert insight.

## Lessons for the Guide

1. **Carry uniqueness is the first question.** Before designing any filter, ask: "Does this carry appear in other comps?" Viktor doesn't (it's unique) → carry-only filter works. Vex does (NOVA, Vex 95, Dark Star, Shepherd) → needs trait locks and exclusions. This determines filter complexity.

2. **Start with carry-only, add complexity only if needed.** My biggest mistake with Viktor was trying to define the "comp shell" instead of just filtering on Viktor(i3). The expert's Pattern 1 (carry-only) should be the default starting point.

3. **Don't merge carries too eagerly.** I grouped Jhin+Xayah as one cluster and MasterYi+Kindred+Fiora as another. The expert separates them (nova_95 vs nova_yi, xayah standalone). Different carries = potentially different comps, even with similar support.

4. **38 boards is marginal for meta discovery.** I identified 7 clusters but missed ~15 comps from the expert list. Reroll comps (low play rate, 3-star carries) need more observations. 100+ boards would be more reliable.

5. **Trait thresholds matter more than I expected.** SpaceGroove ≥ 3 vs ≥ 5 makes a big difference. The higher threshold captures the "Line" identity; the lower one is just "has some Space Groove units."

6. **Exclusions are about 3-item carries, not traits.** I initially tried to exclude by trait (e.g., exclude DRX from Primordian). The expert primarily excludes other carries with 3 items — that's the sharper boundary.

## Questions for Xing

1. When scouting, is there a systematic way to determine the right number of boards to observe? 38 feels too few for rare comps but adequate for popular ones.
2. For Viktor — the comp shell (DarkStar + Voyager + Summon) seems more meaningful than just "Viktor i3." Is carry-only truly better, or does it depend on the analysis question?
3. Should the scout command output trait breakpoint levels instead of raw counts? That would make clustering easier.
