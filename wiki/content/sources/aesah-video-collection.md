# Source: Aesah — Video Collection (13 Videos)
**Type**: YouTube video transcripts
**Author**: AesahTFT
**Channel**: https://www.youtube.com/@Aesah
**Ingested**: 2026-04-24

Comprehensive study of Aesah's data analysis methodology across 13 videos spanning Set 14–17. Videos grouped by theme.

---

## Theme 1: Data Explorer Methodology

### "Stop Making These Mistakes When Looking at Data | How to Use MetaTFT Explorer Like a Pro" (WxRRHtQeKoU)

**Core thesis**: Raw item stats are misleading without comp context. Data Explorer filters are essential.

**Key examples**:
- **Indomitable artifact trap**: Globally top-ranked tank artifact, but within 5 Battle Academia Prodigy (Leona with 3 items), it's actually the **worst** of the six main tank artifacts. Locket and Light Shield perform better.
- **Gwen dual-comp problem**: Gwen is played in both 6 Sorcerer and 8 Soul Fighter. In 6 Sorc (no strong frontline), Edge of Night is critical for survival. In 8 Soul Fighter (trait gives 650 HP), Gunblade becomes viable because Gwen is already tanky enough. Same unit, different comps, completely different BIS.
- **Yumi primary vs secondary carry**: Without filters, anti-heal/void staff look great on Yumi. After excluding Katarina 3-star (which makes Yumi a secondary carry), real damage items (Striker + JG) become clearly superior. Support items only look good because secondary-carry Yumi inherits leftover items from a winning board.
- **Overfiltering warning**: Too many filters (specific emblems + specific 5-costs + specific board states) reduces sample size to <100 games. One player's habits can then dominate the stats.

**Practical rules**:
1. Always set comp context before evaluating items
2. Use "3 or more" trait filters (not exact) to capture comp variants
3. Don't specify unnecessary filters that don't affect the carry
4. Check sample size — under 200 games is noise

### "The Secret Behind Accurate TFT Stats" (Ost7eDrUUzw) — with morbrid

Already documented in [[sources/morbrid-aesah-talk]]. Key additions from this re-study:

- **Bookmark A/B testing**: Save two filter configurations, toggle between them to see how a single variable (e.g., adding/removing a unit) changes item rankings
- **Games tab as ground truth**: Before trusting any statistical result, click through 10-20 actual games to verify the filter captures what you intended
- **Star level warning (morbrid)**: Specifying star level in filters introduces selection bias — 3-star unit games are already winning

### "99% of TFT Players Don't Know How to Use Advanced Stats" (tlk6eeh4qk8)

**Core thesis**: Advanced Mode's confidence intervals solve the low-sample-size problem.

**Key methods**:
- **95% CI as default**: Industry standard; 99% is overly conservative
- **Worst Case sorting**: Upper bound of CI — penalizes low sample sizes automatically. A 3.97 AVP with 153 games has CI [3.97, 4.57]; a 4.21 AVP with 2000 games has CI [4.17, 4.25]. Worst Case correctly ranks the second item higher.
- **Sampling bias detection**: Edge of Night on Brand looks great in raw stats, but clicking into games reveals Brand isn't the primary carry — he gets leftover defensive items in late-game winning boards
- **Tier list algorithm**: Combines frequency and AVP. High frequency + good AVP = S-tier. Low frequency + good AVP = survivorship bias signal, not strength signal.

### "Avoid These Data Mistakes in TFT!" (RLmtiQRWREI)

Already partially documented in [[sources/aesah-data-mistakes]]. Key reinforcement:

- **Relative Delta formula**: `no_item_AVP = (overall - p × item_AVP) / (1 - p)` — this is the play-rate weighted correction
- **Heimer example**: Guard Breaker (5% rate, 4.01 AVP) vs Archangels (39.1% rate, 4.21 AVP). Raw AVP says Guard Breaker is much better. Relative Delta shows Archangels has 3.5x more real impact.
- **Component economy**: Giant Slayer uses sword+bow (bad for AP comps) vs Rabadon uses rod+rod. Item evaluation must consider component opportunity cost.

---

## Theme 2: Item Evaluation Frameworks

### "How to Use TFT Data the Right Way – Item Selection Tips with Adjusted Placement" (FF1fS_NNV-s)

**Core thesis**: "Adjusted Placement" (= Necessity/Delta) is the correct metric for item comparison, not raw AVP.

**Method**: Demonstrates the full workflow of using MetaTFT Explorer's adjusted placement view to compare items within a comp context. Reinforces that high play rate items always look worse in raw AVP due to inclusion of forced/suboptimal builds.

### "How to Choose the Right Items – The Math Behind Blue Buff vs Shojin" (vSob_g9LZFg)

**Core thesis**: Community consensus can be mathematically wrong. Verify with parametric analysis.

**Parametric analysis framework**:
```
Mana generation = (1 + AS_bonus) × base_AS × mana_per_attack + mana_regen/sec

Shojin on Caitlyn: 12.9 mana/sec (10% AS bonus)
Blue Buff on Caitlyn: 13.8 mana/sec (same 10% AS)
```

**Hidden advantages of Blue Buff**:
1. **Walking phase**: Units moving can't auto-attack but still get mana regen → Blue Buff still generates mana
2. **CC duration**: Stunned/disarmed units can't auto-attack → Blue Buff still works
3. **Component economy**: Shojin uses Sword (contested resource); Blue Buff saves Sword for carry items

**Lesson**: Popularity ≠ optimality. Parametric math can overturn community consensus.

### "TFT Power Budget Guide" (V-yn_BoPGBA)

**Core concept: Power Budget** — every item has a fixed "power budget" distributed across stats (AD, AP, AS, HP, resist, utility). A unit that can't use all stats wastes part of the budget.

**Examples**:
- Crown Guard (45 AP) on a non-AP unit: wastes ~30% of power budget
- Bloodthirster's defensive stats (shield, MR) on a backline carry: wasted
- Teamwide AS augment: almost all units benefit (high budget utilization)
- Teamwide AD augment: many units can't use AD (low budget utilization)

**Power-up evaluation**:
- Scaling power-ups (e.g., Infernal Speed: 2%→10%+ AS over game) → only valuable on units you keep all game
- Instant power-ups (e.g., Cyclone Rush: flat 15% AS) → fine on temporary units

**Relevance to our project**: Power Budget explains WHY certain items have low Necessity on certain units — it's not that the item is bad, it's that the unit wastes part of its power. This is a causal framework complementing our statistical measures.

---

## Theme 3: Augment Evaluation

### "Teamwide Combat vs Items | When to Pick Which Augment" (UTI0-urZloE)

**Core thesis**: Item augments are better early (multiplicative scaling on few units); teamwide augments are better late (8 units all benefit, bypass 3-item cap).

**Stage-dependent value**:
- **Early (4 units)**: 1 extra item on 2-star carry >>> tiny buff to 4 units (3 of which are 1-star supports)
- **Late (8 units, carries maxed)**: Item augment has diminishing returns (3-item cap reached); teamwide buff scales with unit count
- **1st vs 2nd place**: When two players have identical comps and items, the **teamwide augments** determine the winner

**Decision framework**:
- High-rolling → prefer teamwide augments (invest in ceiling)
- Low-rolling → prefer item augments (need immediate power to survive)
- Mid-rolling → context-dependent

### "How to Evaluate Econ Augments Correctly" (V5B4MdtDhKQ)

**Core method: Gold-equivalent conversion** — translate all augment effects into equivalent gold value for comparison.

| Augment | Gold Equivalent | Notes |
|---|---|---|
| Get 21 Gold | 21g | Baseline — actually weakest, not "balanced" |
| Explosive Growth (7XP×4) | 28g | Delayed delivery; reroll-comp restricted |
| Epic Carousel (23 rerolls at 8) | 46g | Conditional; non-reroll only |
| Epoch Plus (8XP+3 rerolls recurring) | 42g | Most delayed but most total value |
| Poor Thinking (lose all, gain +70) | 45g theoretical | Time cost makes actual value lower (lose econ breakpoint) |

**Key insight**: "Get 21 Gold" is universally overrated as the "balanced baseline." It's actually the weakest econ augment. Players should be much more willing to take conditional augments.

**Time-value discount**: Delayed gold < immediate gold because losing the 50-gold interest breakpoint even temporarily costs compounding interest.

---

## Theme 4: Game Strategy (Stat-Related)

### "TFT Strategy: Playing for 1st vs Playing for Top 4" (XjAZy5kJhHA)

**Decision point**: 4-2 rolldown — aggressive (roll to 10g for immediate power) vs conservative (maintain 50g for interest).

**Data-backed insight**: The 30g interest differential over a full game ≈ 1 augment worth of power. Players underestimate how much "playing for 1st" costs in expected placement.

**Stat relevance**: Explains why filtering by rank tier matters — playing-for-1st vs playing-for-top4 produce structurally different boards, introducing a hidden confound in comp-level AVP data.

### "Top 5 Best Artifacts & How to Play Around Them" (hTuNaiIA5dQ)

**Evaluation method**: Artifact value = base stat benefit × unit synergy. Not all "top" artifacts are best on all units.

**Example**: Flickerblade is S-tier globally but only S-tier on high-AS units (Gameplan). On low-AS units, the AS multiplier yields less absolute benefit.

**Stat relevance**: Reinforces Power Budget — global artifact rankings are misleading without unit-specific context (same principle as Indomitable on Leona).

---

## Cross-Cutting Insights (Synthesized)

### 1. The Filter-First Principle
Every video reinforces: raw stats are polluted. Always condition on comp context before drawing conclusions. This is Aesah's #1 rule.

### 2. Survivorship Bias is Everywhere
- Low play rate items look artificially good (carousel acquisition)
- Secondary carry items look good (inherited from winning boards)
- Higher trait tiers look better (only strong boards reach them)
- 5-cost units top AVP charts (only survivors field them)

### 3. Parametric Verification
When data conflicts with theory, do the math. Blue Buff vs Shojin, Power Budget analysis — these complement statistical analysis with causal reasoning.

### 4. Stage-Dependent Value
Items, augments, and strategies have different values at different game stages. No single metric captures this. Context is everything.

---

## Appendix: Game Knowledge (Not Directly Stat-Related)

These videos teach TFT game mechanics and economy. They provide domain context for interpreting data but don't introduce stat analysis methods.

### "The Stage 2 Econ Framework EVERY TFT Player Needs" (seGNtdrgf2w)

- Win/loss streaks are overrated; base gold + interest dominate Stage 2 economy
- Full win-streak (4 wins): only +1 extra gold over breaking even
- Full loss-streak (4 losses): +2 extra gold but -20+ HP
- **1 gold ≈ 3 HP** (Aesah's rule of thumb)
- Conclusion: Almost always upgrade at 2-1 and 2-5 to play strongest board

### "Even vs Odd Components on 4-2" (Kt2Lp25-BZU)

- After 5-1, no more components drop. Odd component count = 1 wasted component = half an item lost.
- In 85% of games, you get 4 additional components through Stage 4. Track parity at 4-2 augment selection.

### "TFT Shop Odds Explained | When To Roll vs Level" (tn_NNceutMg)

- **120g looking for 5-cost at level 8**: Stay 8, roll 100g = 50 shops. Don't level to 9 (only 20g left = 10 shops despite 4x better odds).
- **150+g**: Level to 9 — enough gold remaining to exploit the better odds.
- **Gold sufficiency > probability differential**: Having enough rolls matters more than the per-shop odds improvement from leveling.

---

## Wiki Pages Updated
- This file is a new comprehensive source document
- Related: [[sources/aesah-data-mistakes]], [[sources/morbrid-aesah-talk]]
