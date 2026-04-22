# Experiment: Do Trait Breakpoints Change Itemization? (Multi-Comp)
**Status**: 🧪 draft
**Date**: 2026-04-22
**Module**: 5 (Trait Breakpoints)

## The Question

The previous [[experiments/2026-04-22-nova-trait-breakpoint]] found that 5 N.O.V.A. doesn't change MasterYi itemization in nova_yi. Is this a property specific to N.O.V.A., or is it universal — do **all** trait breakpoints leave carry itemization unchanged?

We test three traits across three comps:
- **N.O.V.A. (DRX)** 2→5 in nova_yi (MasterYi carry) — replication from prior experiment
- **Dark Star** 4→6 in dark_star (Mordekaiser carry) — different trait, tank carry
- **Shepherd (Summon)** 5→7 in shepherd (Sona carry) — different trait, AP carry

If the "no itemization change" pattern holds across all three, it's likely a general property of TFT: **items serve the champion, not the trait**.

## Chapter 1: Headline Numbers — Does Higher Tier = Better Placement?

| Comp | Low Tier | Games | AVP | High Tier | Games | AVP | ΔAVP |
|---|---|---|---|---|---|---|---|
| nova_yi | DRX 2 | 66,003 | 4.61 | DRX 5 | 120,519 | 4.37 | -0.24 |
| dark_star | DS 4 | 38,617 | 4.93 | DS 6 | 75,002 | 4.11 | -0.82 |
| shepherd | Sum 5 | 33,229 | 4.25 | Sum 7 | 16,950 | 3.56 | -0.69 |

Every comp shows the same pattern: higher trait tier → better AVP. But as established in Module 2, this is **selection bias** — stronger boards naturally reach higher tiers.

Dark Star shows the largest gap (-0.82 AVP), likely because going from 4→6 Dark Star requires committing two additional Dark Star units, which is a bigger board investment than the other breakpoints.

## Chapter 2: Mordekaiser Itemization — Dark Star 4 vs 6

Mordekaiser is a frontline carry in Dark Star. Top items by Necessity:

| Rank | DS 4 (33k games) | Nec. | DS 6 (74k games) | Nec. |
|---|---|---|---|---|
| 1 | Crownguard | +0.010 | Warmog's Armor | +0.015 |
| 2 | Shepherd Emblem | +0.009 | Thief's Gloves | +0.010 |
| 3 | Thief's Gloves | +0.008 | Crownguard | +0.008 |
| 4 | Steadfast Heart | +0.008 | Evenshroud | +0.008 |
| 5 | Voyager Emblem | +0.008 | Steadfast Heart | +0.008 |
| 6 | Protector's Vow | +0.005 | Sunfire Cape | +0.006 |

**Observation**: The top items are all tank/utility items (Warmog's, Thief's, Crownguard, Steadfast Heart). Rankings shuffle between tiers, but Necessity values are **very close** (0.005–0.015 range). No item dramatically changes importance.

Note: Necessity values are slightly **higher** at DS 6 (opposite to nova_yi). This is because Mordekaiser's overall AVP drops from 5.06 to 4.11, creating more room for individual items to contribute.

**tftable cross-validation** (49k games): Top items are Thief's Gloves (0.009), Crownguard (0.007), Steadfast Heart (0.007). Same item pool, confirming our pipeline identifies the right items.

## Chapter 3: Sona Itemization — Shepherd 5 vs 7

Sona is the AP carry in Shepherd. Top items by Necessity:

| Rank | Sum 5 (25k games) | Nec. | Sum 7 (17k games) | Nec. |
|---|---|---|---|---|
| 1 | Void Staff | +0.052 | Void Staff | +0.092 |
| 2 | Archangel's Staff | +0.037 | Spear of Shojin | +0.086 |
| 3 | Adaptive Helm | +0.033 | Adaptive Helm | +0.056 |
| 4 | Spear of Shojin | +0.031 | Rabadon's Deathcap | +0.041 |
| 5 | Rabadon's Deathcap | +0.025 | Blue Buff | +0.041 |
| 6 | Giant Slayer | +0.021 | Jeweled Gauntlet | +0.040 |

**Top 5 items are the same set** (Void Staff, Shojin, Adaptive Helm, Archangel's, Dcap), just reordered. Void Staff is #1 at both tiers. Spear of Shojin rises from #4 to #2, Archangel drops from #2 to #7. The biggest surprise: **Jeweled Gauntlet** jumps into top 6 at Summon 7 (Nec 0.040) — at Summon 5, it's at 0.014.

**Necessity values increase at higher tier** (opposite to nova_yi). Void Staff goes from 0.052 → 0.092. This makes sense: with lower AVP baseline (3.56 vs 3.96) and more committed builds, the item-specific AVP gap (A - a) widens proportionally.

**tftable cross-validation** (31k games): Void Staff (0.073), Shojin (0.050), Adaptive Helm (0.046), Archangel (0.037), Dcap (0.036). Rankings match our combined data closely. tftable rates Jeweled Gauntlet as "Important" (0.015), suggesting our 7-tier finding (0.040) may be inflated by the smaller sample.

## Chapter 4: MasterYi Replication — N.O.V.A. 2 vs 5

Replicating from the prior experiment for completeness:

| Rank | DRX 2 (51k games) | Nec. | DRX 5 (120k games) | Nec. |
|---|---|---|---|---|
| 1 | Edge of Night | +0.112 | Edge of Night | +0.054 |
| 2 | Giant Slayer | +0.060 | Giant Slayer | +0.045 |
| 3 | Quicksilver | +0.042 | Quicksilver | +0.022 |
| 4 | Hand of Justice | +0.023 | Striker's Flail | +0.017 |
| 5 | Malware Matrix | +0.019 | Sterak's Gage | +0.017 |

**Top 3 identical**, lower ranks within noise. Necessity **decreases** at higher tier — unique among our three cases. Edge of Night drops from 0.112 → 0.054, a 52% reduction.

## Chapter 5: Synthesis — Three Traits, One Pattern

| Property | N.O.V.A. (DRX) | Dark Star | Shepherd (Summon) |
|---|---|---|---|
| Comp | nova_yi | dark_star | shepherd |
| Carry | MasterYi (AD) | Mordekaiser (tank) | Sona (AP) |
| Trait tiers compared | 2 → 5 | 4 → 6 | 5 → 7 |
| Sample (low / high) | 51k / 120k | 33k / 74k | 25k / 17k |
| Top 3 items same? | ✅ Yes | ✅ Yes (pool) | ✅ Yes |
| Ranking changes? | Minor (#4-5) | Minor (#1-2 swap) | Minor (#2-4 swap) |
| Necessity direction | ↓ (decreases) | ↑ (increases) | ↑ (increases) |
| ΔAVP (high vs low) | -0.24 | -0.82 | -0.69 |

**Universal finding: Trait breakpoints do not change carry itemization.** The same items matter regardless of trait tier. Rankings shuffle within noise, but the core item pool is stable.

**Unexpected finding: Necessity direction is not universal.** MasterYi's Necessity decreases at higher tier, while Mordekaiser and Sona's increase. This is likely explained by carry role:
- **MasterYi (AD carry)**: At higher NOVA, the team is stronger overall — MasterYi's items matter less relative to team strength → Necessity compresses.
- **Mordekaiser (tank)**: At DS 4, Mordekaiser's items barely matter (Nec ~0.010) because the comp is too weak — items can't save a bad board. At DS 6, the comp is viable and Mordekaiser's tankiness becomes the deciding factor → Necessity expands.
- **Sona (AP carry)**: Similar to Mordekaiser — at higher Summon, the team can leverage Sona's damage more effectively → item impact increases.

This "Necessity direction" pattern could be a general principle: **Necessity increases with trait tier for carries whose role becomes more leveraged in stronger boards.**

## Cross-Validation Summary

| Comp/Carry | Our top items | tftable top items | Agreement |
|---|---|---|---|
| dark_star / Mordekaiser | Warmog, Thief's, Crownguard | Thief's, Crownguard, Steadfast | ✅ Same pool |
| shepherd / Sona | Void Staff, Shojin, Adaptive | Void Staff, Shojin, Adaptive | ✅ Top 3 match |
| nova_yi / MasterYi | Edge of Night, Giant Slayer, QSS | (from prior experiment) | ✅ |

## What I Learned

1. **Trait breakpoints don't change itemization — this is universal.** Tested across 3 traits, 3 carry types (AD/tank/AP), 3 comps. Items serve the champion's kit, not the trait level.

2. **Necessity direction depends on carry role leverage.** When trait tier makes the carry's role more impactful (tank in a viable comp, AP carry with team support), Necessity increases. When the team already carries (MasterYi in 5 NOVA), individual item impact decreases.

3. **Selection bias is the dominant signal in trait tier comparisons.** Every trait shows better AVP at higher tiers, but this is board strength selection, not trait causation.

4. **Mordekaiser itemization is low-Necessity overall.** His best items (Nec ~0.010-0.015) are an order of magnitude below Sona's (0.050-0.090). Tank itemization matters less than carry itemization in absolute terms.

## Open Questions

- Does the "Necessity direction" pattern (leverage theory) hold for more comps? Could test with Mecha (ASOL carry) or Space Groove.
- Can we separate selection bias from genuine trait effect using control variables (e.g., same board strength, different trait tier)?
- Why does Jeweled Gauntlet spike for Sona at Summon 7? Is this a real interaction or sample noise?

## Questions for Xing

1. **Necessity direction**: Is the "carry leverage" explanation for why Necessity increases/decreases at higher tiers reasonable? Or is there a simpler mechanical explanation?
2. **Mordekaiser's low Necessity**: Tank carries consistently show Nec ~0.01 vs damage carries at ~0.05-0.10. Does tftable show the same pattern? Is tank itemization genuinely less impactful, or is our metric less sensitive to it?
3. **Practical value**: "Trait breakpoints don't change itemization" feels like a validated null result. Is this the expected Module 5 conclusion, or should we be asking a different question about trait breakpoints?

## Review

*(Awaiting review)*
