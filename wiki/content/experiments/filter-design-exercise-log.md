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
