# Composition Structure
**Status**: 🧪 draft

## What Makes a Comp

A composition is not just a filter — it has internal structure. Understanding that structure is prerequisite to asking the right questions.

### Standard Board Size

Every comp has a **standard board size** — the number of units that appear together in > 70% of games. This is the "natural" level for the comp:

| Comp Type | Core Size | Flex Pop | Example |
|---|---|---|---|
| 5-cost carry | 9 units | 10 (看第 10 人) | nova_95 |
| 4-cost carry | 8 units | 9 (看第 9 人) | dark_star, mecha |
| Reroll (1-3 cost) | — | — (无灵活位) | bonk, termeepnal_velocity |

Standard board size determines:
- **At what level the comp "comes online"** — level 9 for 5-cost, level 8 for 4-cost
- **What the +1 question is** — 5-cost asks "who is the 10th unit", 4-cost asks "who is the 9th"
- **How to interpret unit necessity** — core units measure irreplaceability; +1 candidates measure marginal value

### Comp Variants and Flex Slots

Comp 的构成有三种模式：

**1. 固定阵容（无灵活位）**：所有核心 unit 都是确定的，没有替换空间。多见于 reroll comp（如 bonk = Nasus 3★ + 固定队友）。这类 comp 不需要 +1 分析。

**2. 存在灵活位**：核心 N 个 unit 固定，但第 N+1 个位置有多个候选互相竞争。这是 +1 分析的经典场景：
- 5-cost comp: 固定 9 核心，10 人口时选第 10 人（如 nova_95: Sona vs Jhin vs Rhaast）
- 4-cost comp: 固定 8 核心，9 人口时选第 9 人

**3. 存在 Variant**：同一个 comp 有多个变体，核心阵容本身就不同（**3 个以上 unit 差异**才算 variant，1-2 个差异属于灵活位）。例如 Mecha 的 Fiora 版 vs Viktor 版，核心 carry 不同。tftable 通过 `comp_variants.py` 自动检测 variant — 对同一 comp 的所有 board 做聚类，variant 之间的差异用 symmetric difference 衡量。

### 如何识别 Primary、Variant 和灵活位

使用 `core` 子命令查看一个 comp 的 board compositions（`python3 cli.py core --comp <COMP>`），按频率排序。判读标准：

- **Primary**: freq 最高的 board
- **Variant**: 和 primary 有 **≥3 个 unit 差异**的高频 board
- **灵活位替换**: 和 primary 只有 1-2 个 unit 差异的 board（不算 variant）
- **+1 board**: 比 primary 多 1 个 unit 的 board

**Level ≠ board 上的 unit 数**：有些 trait 的 unit 占多个 slot（如 Mecha 3 个 unit 占 5 个 slot），实际 level = board unit 数 + 额外 slot。

具体分析流程见 [[methods/plus-one-discovery]]。

### Core vs Flex

Within a comp's standard board:

**Core units** (play rate > 70%): Always present. Their necessity measures **irreplaceability** — how much the comp suffers without them.

**Flex slots**: Positions where multiple units compete. In the +1 analysis, flex candidates are non-core units that appear in the controlled population.

**Level-up candidates**: Units below the core threshold (< 20% play rate) that appear when players reach higher levels. Use `--level` + fix core to control for level bias and board completeness.

### Role Taxonomy

Units serve different roles within a comp. Role determines how to analyze them:

| Role | Definition | Item Pattern | Filter Reliability | Example |
|---|---|---|---|---|
| Primary Carry (主C) | Main damage dealer, 3 items | Deliberate, optimized | High (rho > 0.95) | Vex in nova_95 |
| Tanky Carry | Main tank, 3 items, comp identity | Deliberate tank items | High (rho 0.93-1.00) | Nasus in bonk |
| Comp-Specific Tank | Tank whose build depends on comp | Comp items + generic | Split: comp items unstable, generic stable | Galio in mecha |
| Support | Core but rarely itemized | Leftover items | Very low (rho ~ 0.05) | Mordekaiser in dark_star |
| Flex/Fill | Interchangeable with other units | Varies | Depends on context | Blitzcrank/Nunu in nova_95 |

### Play Rate vs Necessity Decoupling

Play rate and necessity measure different things:

- **Play rate**: how often a unit appears (presence)
- **Necessity**: how much AVP changes without the unit (impact)

These can sharply decouple:

| Unit | Play Rate | Necessity | Interpretation |
|---|---|---|---|
| Akali (nova_95) | 91.5% | +0.17 | "Default fill" — always there, low impact |
| Shen (nova_95) | 86.0% | +1.40 | "Irreplaceable" — slightly less common but critical |

High play rate + low necessity = the unit is easy to include but doesn't drive results.
Low play rate + high necessity = the unit is hard to find/fit but strongly improves outcomes (or level bias inflates it).

### Level Bias in Level-Up Analysis

Analyzing non-core units (level-up candidates) suffers from **level bias**: reaching higher levels correlates with winning. Any unit that appears as "the Nth unit" has inflated AVP because the player was already ahead.

**Solution**: Use `--level` to control for player level. Example: `python3 cli.py units --comp nova_95 --level 10` only analyzes level 10 games, eliminating level bias entirely.

Without `--level`, Sona's Necessity in nova_95 was +0.127 ("3x better than Jhin"). With `--level 10`, it dropped to +0.015 — nearly equal to Jhin (+0.021) and Rhaast (+0.019). The 88% drop proves level bias was the dominant signal.

## Hero Augments

### S17 Hero Augment 列表

S17 有 **8 个 hero augment**，每个将一个低费 unit 变成 carry（改变技能 + 战斗模式）：

| Augment | 名称 | Unit | Cost | 对应 Comp |
|---|---|---|---|---|
| NasusCarry | Bonk! | Nasus | 1 | `bonk` |
| PoppyCarry | Termeepnal Velocity | Poppy | 1 | `termeepnal_velocity` |
| AatroxCarry | Stellar Combo | Aatrox | 1 | `stellar_combo` |
| JaxCarry | Reach for the Stars | Jax | 2 | `reach_for_the_stars` |
| IvernMinionCarry | The Big Bang | Ivern | 2 | `the_big_bang` |
| PykeCarry | Contract Killer | Pyke | 2 | `pyke` |
| GragasCarry | Self Destruct | Gragas | 2 | — |
| MordekaiserCarry | Heat Death | Mordekaiser | 3 | — |

共同特征：都是将低费 tank/fighter 变成 carry，使其成为 3 件套主 C。有对应 comp 定义的 6 个 augment，其 comp filter 就是 `Unit(unit_id, item_min=3, item_max=3)`。

### 通过 Stat 能发现什么

MetaTFT API **不追踪 augment 数据**（match 记录中 `augments` 字段为 `None`），所以无法直接过滤或统计 hero augment。但可以通过间接手段观察其影响：

**可发现的**：
- **Tanky carry 的装备分裂**：hero augment 将 tank 变成 carry 后，玩家会给它 dmg 装备。在 bonk comp（Nasus i3）的 item 数据中，同时出现 tank 装（Warmog、Sunfire）和 dmg 装（Guinsoo、Deathcap），这两组来自完全不同的游戏——有 augment 的给 dmg 装，没有的给 tank 装
- **Unit 的角色模糊性**：Nasus 在 bonk 中既是 tank（无 augment 时）又是 carry（有 augment 时）。这在 item necessity 中表现为两类装备都有正 necessity

**不可发现的**：
- 有 augment 和无 augment 的 AVP 差异
- Augment 的出现率
- Augment 对 comp 强度的影响

### 普通 Comp 中去除 Hero Augment 影响

Hero augment 污染 item 分析的机制：选了 Nasus hero augment 的玩家会给 Nasus 带 dmg 装（Guinsoo 等）。这些 dmg 装混入 bonk comp 的 item 数据中，扭曲了真正 tank carry 的 BIS 排名。

**解决方法**：使用 `--exclude-dmg-items` 过滤掉 dmg 装备，只看 tank 装排名：

```bash
# 只看 tank 装备（排除 hero augment 玩家带的 dmg 装）
python3 cli.py items TFT17_Nasus --comp bonk --normal-only --exclude-dmg-items
```

compositions.py 中 6 个 hero augment comp 都标注了 `exclude_dmg_items_for` 字段。

反过来，如果想分析 hero augment carry build（只看 dmg 装），可以排除 tank 装：

```bash
# 只看 carry 装备（hero augment 玩家的 build）
python3 cli.py items TFT17_Nasus --comp bonk --normal-only --exclude-tank-items
```

## Sources
- [[experiments/2026-04-23-nova95-unit-evaluation]] — core findings, level bias quantification, control variable method
- [[experiments/2026-04-23-tank-filter-reliability]] — role taxonomy evidence
- CDragon TFT static data — S17 hero augment definitions
- `tft_data/analysis/team_comp/flex_slot.py` — tftable flex slot analysis implementation
- `tft_data/analysis/team_comp/comp_variants.py` — variant detection logic
