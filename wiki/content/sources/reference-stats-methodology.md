# TFT Stats 方法论 — 三视频学习笔记

## 来源
1. **AesahTFT — Stop Making These Mistakes When Looking at Data** (WxRRHtQeKoU)
2. **AesahTFT + morbrid (MetaTFT dev) — The Secret Behind Accurate TFT Stats** (Ost7eDrUUzw)
3. **TFT Academy — How to Climb with Stats (Dishsoap & Frodan)** (RjZ58unIe_0)

---

## Aesah 的 Play Rate 加权公式

直接用 play rate 反推 "有 vs 没有" 某件装备的真实影响:

```
整体 AVP = play_rate × item_AVP + (1 - play_rate) × no_item_AVP
→ no_item_AVP = (整体AVP - play_rate × item_AVP) / (1 - play_rate)
→ marginal_value = no_item_AVP - item_AVP
```

- 高 play rate + 高 marginal value = **真正的 BIS**
- 低 play rate + 低 marginal value = **carousel bias 假象**
- 高 play rate + 低 marginal value = **过度使用** (player behavior bias)
- Relative Delta (MetaTFT) ≈ 这个概念的简化版

---

## 核心原则

### 1. 永远加上下文 Filter (Context Matters)
- **不要只看全局 item stats** — 同一个装备在不同阵容里表现完全不同
- 例: Gwen 在 6 Sorc 里需要 Edge of Night 保命,在 8 Soul Fighter 里 Gunblade 就够了
- 例: Yumi 作为主C vs 副C,装备优先级完全不同 — 排除 Katarina 3 后数据翻转
- **Filter 不要太多** — 太多 filter 会让 sample size 降到噪声级别 (如 92 games)

### 2. 幸存者偏差 (Survivorship Bias) — 最大的陷阱
- **后期 Carousel 装备看起来都很强** — 因为你能活到后期 = 你本来就强
- **副C 装备 stats 天然好看** — 因为你只有在 super late game / Urgot farming 才会给副C 上装备
- **低频装备 AVP < 高频装备不代表更好** — play rate 和 AVP 成反比是系统性规律
- **morbrid**: "最大的对抗幸存者偏差的方法是构建正确的 filter — 排除那些你不想看的局"

### 3. Sample Size 是最被低估的因素
- **Dishsoap**: "我跟很多 pro player 聊过,几乎没人真正理解 sample size 的重要性"
- **成熟 patch: ≥1000 games**, 新 patch: ≥300 games
- **行数越多,outlier 越多** — 20+ 行的表格至少有几行是纯随机噪声
- **4x games = 2x accuracy** (标准误差与样本量的平方根成反比)

### 4. Play Rate + Delta 组合看
- 不要只看 Delta (Place Change) — 低 play rate 的好 Delta 可能是假的
- 不要只看 Play Rate — 高 play rate 可能被 forced builds 拉低
- **Frequency vs AVP 散点图** (MetaTFT Graph view): 左上角 = OP,右下角 = underperforming
- 可以画对角线,线上方 = 好于预期,线下方 = 差于预期

### 5. Advanced Mode / CI 使用时机
- **morbrid**: "Advanced mode 最适合低 sample size 查询 — 如三件套 builds、artifacts"
- **95% Worst Case 排序** = 去掉低 sample noise,让高 sample 可靠数据浮上来
- **99% CI** 当行数 50+ 时用
- **但 CI 不修复幸存者偏差** — 只解决 sample size 问题

---

## 实操技巧

### Filter 策略
1. 先确定你在分析什么阵容 (不是什么棋子)
2. 加足够的 trait/unit filter 来锁定阵容
3. **排除干扰**: Golden Ox 局、副C 三件套局、特殊 cash out 局
4. 不要 overfilter — 保持 1000+ sample
5. **Exclude 比 Include 更强大** — 排除不想要的比指定想要的灵活

### 装备分析
- **看 builds (两件/三件组合)** 比看单件更可靠 — 消除 carousel bias
- Primary carry items ≠ secondary carry items — 一定要区分
- **base stats matter** — 不只看效果,30% 攻速在坦克上是死属性
- **Items tab + 指定 unit + 搜索** 比全局 items 页面有用 100 倍

### 棋子/等级分析
- 用 Units tab 看每级最佳棋子 (设置 level filter)
- **一费在高费段位的异常表现** → 说明 reroll 线或某个 trait 被 break 了
- 比较 "有 vs 没有" 某个棋子: 构造两组 filter,toggle between

### 羁绊分析
- Items tab 搜 trait 名可以看激活频率 vs AVP
- 找断点: 2→3→4 的 Delta 变化帮你判断是否值得投资

### Augment "曲线救国"
- 没有直接 augment stats,但可以间接查:
  - Anger Issues → 搜多个 Rageblade
  - Build Different → 搜不常见的 unit 组合 + 排除正常 traits
  - Hero Augments → 搜该 unit 的特殊 items/builds
  - 装备类 Augments (Artifacts/Radiants) → 直接搜 item

### Frequency vs AVP 散点图 (Graph View) — morbrid 推荐
- X轴 = AVP, Y轴 = Frequency
- **画对角线**: 线上方 = 好于预期 (OP), 线下方 = 差于预期
- 直接对抗幸存者偏差: 低频装备天然 AVP 好, 但如果在线下方就是真的差
- Tier list 算法 = frequency + place change 混合, 本质上就是量化这条对角线
- 同 frequency 的装备之间才能直接比 AVP (如 IE vs Gargoyle), 不同 frequency 不能直接比 (如 IE vs Steraks)
- **"Exclude → Toggle On" 方法**: 排除所有减甲装备 → 看 AVP 恶化多少 → 判断该效果在阵容中的重要性
- 这也适用于判断反甲 vs 减抗 vs 减攻的相对价值

### 高级技巧
- **Filter by region** (KR/NA/VN) — 不同区域 meta 不同
- **Filter by rank** (GM+) — 高段位数据更有参考价值
- **Games tab sanity check** — 看真实对局确认 filter 没捕到垃圾数据
- **Bookmarks** — 保存常用查询,toggle 对比
- **Plus-one traits** (MetaTFT) — 看阵容最佳第 N 个 emblem

---

## 关键教训

> "Stats 不能直接告诉你答案,它们提出重要的问题。Stats 是对话的起点,不是结论。" — Dishsoap

> "如果一个数据看起来不对劲,investigate it。如果调查完还是找不到原因,那也许 stats 是对的。" — Dishsoap

> "Advanced mode 不修复幸存者偏差。它只修复低 sample size 问题。" — morbrid

> "Frequency vs AVP 的反比关系是系统性的,因为 Stage 5/6 Carousel。这不是小问题,是每个 item 每个 set 都存在的 constant bias。" — Dishsoap

> "个人能先发现未优化的线,然后数据会反映出来。Patch 早期信个人,后期信数据。" — morbrid + Dishsoap
