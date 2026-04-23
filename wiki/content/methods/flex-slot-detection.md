# Flex Slot Detection
**Status**: 🧪 draft

## When to Use

分析一个 comp 的标准阵容构成和灵活位（+1 unit）。

## Method

### Step 1: Find Primary Board

```bash
python3 cli.py core --comp <KEY>
```

从 `exact_units_traits2` API 获取所有 board compositions（6-11 人口混排），按 freq 排序 + 显示平均星级。**freq #1 = primary board**。

Primary board 告诉你：
- **Core units**: primary board 中的所有 unit
- **Core size**: primary board 的 unit 数（不是从 carry cost 推断，因为不一定符合 "5-cost=9, 4-cost=8" 的规律）
- **Level**: 需要考虑多 slot trait（如 Mecha 3 unit 占 5 slot → 7 units on board = level 9）

### Step 2: +1 控制变量分析

固定 primary board 的 core units + 控制 level：

```bash
# core 命令会自动生成这个命令
python3 cli.py units --comp <KEY> --level <CORE_LEVEL+1> --filter "\
Unit('unit1') & Unit('unit2') & ... & Unit('unitN')"
```

对非 core unit 按 freq 排列，看 **AVP**（主指标）和 **Necessity**（补充）：
- **AVP**: 完整 board 的 AVP 不受 survivorship bias 污染，freq 高且 AVP 低 = 好选择
- **Necessity**: 衡量边际影响，但在高 level 时数值被压缩（AVP 空间小）

### Step 3: Cross-Validation

`python3 cli.py tftable --comp <COMP>` 对比 tftable 的 unit necessity（注意两者衡量不同东西：我们的是存在价值，IC3 可能是 carry 价值）。

## Known Limitations

1. **Primary board ≠ 唯一玩法**: variant-heavy comp（如 pyke）的 primary 可能只占 15%，不具代表性
2. **Level bias**: 不控制 level 时 +1 候选 Necessity 被膨胀（Sona 在 nova_95 下降 88%）
3. **Compressed AVP**: 高 level 时 AVP 空间小，+1 候选间差异可能在噪声范围内
4. **多 slot trait**: Mecha、Summon 等 trait 的 unit 占多个 slot，level 需要手动修正

## Example: Nova 95

**Step 1**: `python3 cli.py core --comp nova_95`
→ primary = 9 units (Aatrox, Akali, Blitzcrank, Fiora, Graves, Morgana, Nunu, Shen, Vex), 82k games (46%), AVP 3.95

**Step 2**: +1 boards visible in core output (10-unit boards with Sona 14k, Jhin 3k, etc.)

**Step 3**: Control variable
```bash
python3 cli.py units --comp nova_95 --level 10 --filter "\
Unit('TFT17_Aatrox') & Unit('TFT17_Akali') & Unit('TFT17_Vex') \
& Unit('TFT17_Fiora') & Unit('TFT17_Shen') & Unit('TFT17_Graves') \
& Unit('TFT17_Morgana') & Unit('TFT17_Blitzcrank') & Unit('TFT17_Nunu')"
```
→ Sona (+0.027) ≈ Rhaast (+0.021) ≈ Jhin (+0.019)

## Sources
- [[experiments/2026-04-23-nova95-unit-evaluation]] — method development
- [[experiments/2026-04-23-flex-slot-all-comps]] — 29 comp 全量分析
- [[concepts/composition]] — comp structure definitions
