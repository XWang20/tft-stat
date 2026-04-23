# Plus-One Discovery
**Status**: 🧪 draft

## When to Use

When the question is about **what to add at the next level** — the +1 unit for a comp. Typical questions:
- "Nova 95 到 level 10 应该挂谁？"
- "Mecha 到 level 9 加什么？"

## Method

### Step 1: Find Primary Board

```bash
python3 cli.py core --comp nova_95
```

`core` 子命令查询 `exact_units_traits2`，显示所有 board compositions（6-11 人口混排）按频率排序 + 平均星级。freq #1 = primary board。

从 primary board 读出：
- **Core units**: primary board 中的所有 unit
- **Board size**: unit 数量（注意 level ≠ board unit 数，Mecha 等 trait 的 unit 占多个 slot）
- **Level**: board unit 数 + 额外 trait slot（如 Mecha 3 unit 占 5 slot → level = board units + 2）

### Step 2: Find +1 Boards

在 `core` 输出中，比 primary 多 1 个 unit 的 board 就是 +1 候选。

**AVP 在这里是有效的主指标**：和单件分析不同，完整 board 的 AVP 不受 survivorship bias 污染（每个 board 是一个完整的游戏状态）。按 freq 往下排，同时看 AVP（越低越好）和 Necessity。

### Step 3: Control Variable 精细分析

如果需要更精确的 +1 排名，用两层控制：

**Layer 1 — Control level**: `--level` 消除 level bias。

**Layer 2 — Fix core units**: 固定 primary board 的所有 core unit。这是 build 分析 "固定两件看第三件" 的 unit 版本。

```bash
# nova_95: 固定 9 核心 + level 10
python3 cli.py units --comp nova_95 --level 10 --filter "\
Unit('TFT17_Aatrox') & Unit('TFT17_Akali') & Unit('TFT17_Vex') \
& Unit('TFT17_Fiora') & Unit('TFT17_Shen') & Unit('TFT17_Graves') \
& Unit('TFT17_Morgana') & Unit('TFT17_Blitzcrank') & Unit('TFT17_Nunu')"
```

`core` 子命令会自动生成这个命令。

对非 core unit 按 freq 排列，看 AVP 和 Necessity：
1. **AVP**: 完整 board 的主指标，freq 高且 AVP 低 = 好选择
2. **Necessity**: 补充指标，衡量 "有这个 unit vs 没有" 的边际影响
3. Check **trait activation** — 是否触发新 breakpoint？
4. Check **sample size** — play rate < 1% 的可能是噪声
5. Check **competition** — 候选之间是互斥还是互补？

**Critical**: 不控制 level 时，+1 候选的 Necessity 被 level bias 严重膨胀。Sona 在 nova_95 从未控制的 +0.127 降到 level-controlled 的 +0.015（下降 88%）。

### Step 4: Cross-Validation

Compare with tftable: `python3 cli.py tftable --comp <COMP>`

**Warning**: 我们的 unit necessity 和 tftable 的 IC3 necessity 衡量不同的东西：
- 我们的: 存在价值（unit 在不在场）
- IC3: 可能是 carry 价值（unit 带 3 件装备的贡献）
- Spearman rho = -0.476 in nova_95 — 近乎反向

两个指标互补而非互相验证。

## Known Limitations

1. **w/o sample**: 核心 unit (90%+ play rate) 的 "without" 样本很小，可能不具代表性。
2. **No causal claim**: 负 Necessity（Maokai, TahmKench）不代表 unit 有害，而是出现在弱势局面（selection bias）。即使控制 level 后仍成立。
3. **Emblem/spatula**: 未控制。高 Necessity 可能依赖纹章。
4. **Compressed AVP**: Level 10 的 AVP 很低（nova_95 = 2.08），所有 Necessity 值都小，候选间差异可能在噪声范围内。

## Example: Nova 95

**Step 1**: `python3 cli.py core --comp nova_95` → primary = 9 units (Aatrox, Akali, Blitzcrank, Fiora, Graves, Morgana, Nunu, Shen, Vex), 82k games, 46%

**Step 2**: +1 boards in core output → 10-unit boards with Sona (14k), Jhin (3k), etc.

**Step 3**: Control variable (30k games, all 9 core fixed at level 10, AVP 1.95):
- Sona (+0.027) ≈ Rhaast (+0.021) ≈ Jhin (+0.019) — nearly equal
- Maokai (+0.002) nearly zero; TahmKench (-0.013) negative

Three levels of analysis yield increasingly refined conclusions:
1. No control: "Sona is 3x better" (level bias artifact)
2. `--level 10` only: "Jhin ≈ Rhaast ≈ Sona" (level controlled)
3. `--level 10` + fix core 9: "Sona slightly ahead, all three viable" (fully controlled)

## Sources
- [[experiments/2026-04-23-nova95-unit-evaluation]] — method development
- [[concepts/composition]] — comp structure, variants, flex slots
