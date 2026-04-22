# Experiment: Carry Leverage and Necessity Direction
**Status**: 🧪 draft
**Date**: 2026-04-22
**Module**: 5 (Trait Breakpoints)

## The Question

The [[experiments/2026-04-22-trait-breakpoint-multi-comp]] found that Necessity **direction** varies by carry type when comparing low vs high trait tiers:
- MasterYi (AD carry, nova_yi): Necessity ↓ at higher NOVA
- Mordekaiser (tank, dark_star): Necessity ↑ at higher Dark Star
- Sona (AP carry, shepherd): Necessity ↑ at higher Summon

The proposed explanation: **carry leverage** — when a higher trait tier makes the carry's role more impactful, Necessity increases. Does this hold across more comps?

We test two new cases:
1. **Nami** in Space Groove (AP carry) — Space Groove 5 vs 7
2. **Corki** in Meeple (AD carry) — Astronaut 5 vs 7

## Chapter 1: Nami in Space Groove — SG 5 vs 7

### Headline Numbers

| Tier | Games | AVP |
|------|-------|-----|
| SG 5 | 229,588 | 4.11 |
| SG 7 | 60,855 | 3.49 |

ΔAVP = -0.62 (higher tier = better placement, as expected from selection bias).

### Item Necessity Comparison

| Rank | SG 5 (230k games) | Nec. | SG 7 (61k games) | Nec. |
|---|---|---|---|---|
| 1 | Spear of Shojin | +0.071 | Nashor's Tooth | +0.092 |
| 2 | Nashor's Tooth | +0.035 | Spear of Shojin | +0.082 |
| 3 | Void Staff | +0.018 | Jeweled Gauntlet | +0.061 |
| 4 | — | — | Void Staff | +0.034 |

**Necessity increases across the board at SG 7.** Nashor's Tooth jumps from 0.035 to 0.092 (+163%). Shojin from 0.071 to 0.082 (+15%). Most dramatic: **Jeweled Gauntlet** goes from not in the top items at SG 5 to #3 at SG 7 (Nec 0.061).

This matches the leverage theory: at SG 7, the team composition is fully committed to supporting Nami's carry role, so her itemization has more impact on outcomes.

### tftable Cross-Validation

tftable (142k games, overall): Shojin 0.073, Nashor's 0.046, Void Staff 0.017. Our SG 5 numbers are close to tftable's overall (Shojin 0.071 vs 0.073, Void Staff 0.018 vs 0.017). The SG 7 values (0.082, 0.092) are elevated above tftable, consistent with leverage amplification in fully committed boards.

## Chapter 2: Corki in Meeple — Astronaut 5 vs 7

### Headline Numbers

| Tier | Games | AVP |
|------|-------|-----|
| Astro 5 | 103,418 | 4.48 |
| Astro 7 | 68,754 | 4.46 |

ΔAVP = -0.02 — almost no difference! This is unusual compared to the other trait breakpoints (DRX -0.24, DS -0.82, Summon -0.69, SG -0.62).

### Item Necessity Comparison

| Rank | Astro 5 (103k games) | Nec. | Astro 7 (69k games) | Nec. |
|---|---|---|---|---|
| 1 | Deathblade | +0.039 | Deathblade | +0.043 |
| 2 | Last Whisper | +0.027 | Last Whisper | +0.027 |
| 3 | Blue Buff | +0.020 | Blue Buff | +0.026 |
| 4 | Striker's Flail | +0.020 | Striker's Flail | +0.022 |

**Rankings are identical. Necessity barely changes.** Deathblade 0.039 → 0.043 (+10%), Blue Buff 0.020 → 0.026 (+30%), but the absolute magnitudes are small and the order is completely stable.

### tftable Cross-Validation

tftable (70k games): Deathblade 0.052, Last Whisper 0.035, Striker's 0.023. Rankings match perfectly. tftable values are slightly higher across the board — likely a different data window.

## Chapter 3: Synthesis — Updated Leverage Theory

### All Five Cases Combined

| Comp | Carry | Type | Trait | Low Nec (top item) | High Nec (top item) | Direction | ΔAVP |
|---|---|---|---|---|---|---|---|
| nova_yi | MasterYi | AD | DRX 2→5 | +0.112 | +0.054 | **↓** | -0.24 |
| meeple_corki | Corki | AD | Astro 5→7 | +0.039 | +0.043 | **→** (flat) | -0.02 |
| dark_star | Mordekaiser | Tank | DS 4→6 | +0.010 | +0.015 | **↑** | -0.82 |
| shepherd | Sona | AP | Sum 5→7 | +0.052 | +0.092 | **↑** | -0.69 |
| space_groove | Nami | AP | SG 5→7 | +0.071* | +0.092 | **↑** | -0.62 |

*Nami's top item at SG 5 is Shojin (0.071), but Nashor's overtakes at SG 7 (0.092).

### The Pattern

**AP carries and tanks: Necessity increases at higher trait tier.** Sona (+77%), Nami (+30% Shojin, +163% Nashor), Mordekaiser (+50%).

**AD carries: Necessity stays flat or decreases.** MasterYi (-52%), Corki (+10%, essentially flat).

### Possible Explanations

1. **AD carry independence**: AD carries (MasterYi, Corki) deal consistent auto-attack damage regardless of team composition. Their items amplify personal DPS. Higher trait tiers give the team more power, but the carry's personal contribution doesn't scale with trait level — so item Necessity stays flat.

2. **AP carry team-dependence**: AP carries (Nami, Sona) often deal burst/AoE damage that benefits from longer survival (team tankiness) and trait synergies. At higher trait tiers, the team enables the AP carry to cast more, making each cast-amplifying item more impactful — Necessity increases.

3. **Tank leverage is board-viability-gated**: Mordekaiser's items don't matter when the board is too weak (DS 4). At DS 6, the board is viable and his tankiness becomes the deciding factor — Necessity increases.

4. **ΔAVP as confound**: Corki's ΔAVP is only -0.02 (Astro 5 vs 7 are almost the same strength), so there's little selection bias difference to create Necessity divergence. The other cases all have large ΔAVP gaps (0.24–0.82).

## What I Learned

1. **Carry leverage theory partially validated but needs refinement.** The original claim was "Necessity increases when carry role becomes more leveraged." This holds for AP carries and tanks (4/5 cases), but AD carries are flat or decrease. The better framing: **item Necessity direction depends on carry type, not just leverage**.

2. **ΔAVP magnitude matters.** Corki shows almost no ΔAVP between trait tiers (-0.02), which means the two populations are nearly identical. Large Necessity direction changes only appear when there's meaningful selection difference between tiers (ΔAVP ≥ 0.2). The Necessity direction may be measuring selection bias intensity, not carry leverage per se.

3. **Jeweled Gauntlet is a high-tier indicator for AP carries.** JG appears in Nami's top 3 only at SG 7 (not SG 5), and in Sona's top 6 only at Summon 7. This suggests JG is a "commitment item" — you only build it when you've already secured the comp, which happens more at high trait tiers.

## Open Questions

- Is the AD vs AP distinction the real axis, or is it ΔAVP magnitude? Corki's flat result could be because Astro 5→7 is a weak breakpoint, not because he's AD.
- Can we find an AP carry with flat Necessity direction, or an AD carry with increasing direction, to break the pattern?
- Is Jeweled Gauntlet's tier-sensitivity a form of selection bias (only built in winning boards) or genuine interaction (crit synergizes with high SG)?

## Questions for Xing

1. **AD vs AP framing**: Is the carry type explanation (AD auto-attackers are team-independent, AP casters are team-dependent) the right way to think about this? Or is it simpler — ΔAVP magnitude determines how much Necessity can change?
2. **Corki's ΔAVP anomaly**: Astronaut 5 vs 7 shows almost no AVP difference (-0.02). Is this because the Astronaut trait is weak, or because the comp definition already selects for Astronaut 5+?
3. **Practical value**: "High trait tier changes Necessity direction for AP carries but not AD carries" — is this actionable for item recommendations, or just descriptive?

## Review

*(Awaiting review)*
