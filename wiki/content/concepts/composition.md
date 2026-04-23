# Composition Structure
**Status**: 🧪 draft

## What Makes a Comp

A composition is not just a filter — it has internal structure. Understanding that structure is prerequisite to asking the right questions.

### Primary Board

每个 comp 有一个 **primary board** — 最常见的 board composition。通过 `python3 cli.py core --comp <KEY>` 查询，freq #1 就是 primary board。

Primary board 定义了：
- **Core units**: primary board 中的所有 unit
- **Core size**: unit 数（不从 carry cost 推断 — 从数据读）
- **Level**: 需考虑多 slot trait（如 Mecha 3 unit 占 5 slot → 7 units = level 9）

### Comp Variants and Flex Slots

Comp 的构成有三种模式：

**1. 固定阵容（无灵活位）**：所有核心 unit 确定，没有替换空间。多见于 reroll comp（如 bonk = Nasus 3★ + 固定队友）。

**2. 存在灵活位**：核心 N 个 unit 固定，第 N+1 个位置有多个候选竞争。

**3. 存在 Variant**：同一个 comp 有多个变体，核心阵容本身不同（**≥3 个 unit 差异**才算 variant，1-2 个差异属于灵活位）。例如 Mecha 的 Fiora 版 vs Viktor 版。

判读标准：
- **Primary**: freq 最高的 board
- **Variant**: 和 primary 有 ≥3 unit 差异的高频 board
- **灵活位替换**: 1-2 unit 差异（不算 variant）
- **+1 board**: 比 primary 多 1 unit

分析流程见 [[methods/flex-slot-detection]]。

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

### 通过 Stat 能发现什么

MetaTFT API **不追踪 augment 数据**（match 记录中 `augments` 字段为 `None`），无法直接过滤。但可间接观察影响：

**可发现的**：
- **Tanky carry 的装备分裂**：hero augment 让 tank 变 carry，item 数据中同时出现 tank 装和 dmg 装（来自不同游戏）
- **Unit 的角色模糊性**：Nasus 在 bonk 中既是 tank 又是 carry，两类装备都有正 necessity

**不可发现的**：有无 augment 的 AVP 差异、augment 出现率、augment 对 comp 强度的影响

### 去除 Hero Augment 影响

使用 `--exclude-dmg-items`（tank carry 排除 dmg 装）或 `--exclude-tank-items`（看 carry build）：

```bash
python3 cli.py items TFT17_Nasus --comp bonk --normal-only --exclude-dmg-items  # tank build
python3 cli.py items TFT17_Nasus --comp bonk --normal-only --exclude-tank-items  # carry build
```

compositions.py 中 6 个 hero augment comp 标注了 `exclude_dmg_items_for` 字段。

## Sources
- [[experiments/2026-04-23-nova95-unit-evaluation]] — core findings
- [[experiments/2026-04-23-tank-filter-reliability]] — role taxonomy evidence
- [[experiments/2026-04-23-flex-slot-all-comps]] — 29 comp flex slot 分析
- CDragon TFT static data — S17 hero augment definitions
