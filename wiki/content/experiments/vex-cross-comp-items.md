# Experiment: Vex Items Across Different Comps
**Status**: ✅ Complete
**Date**: 2026-04-21
**Module**: 1 (Filter Design)

## The Question

Does Vex's BIS change depending on what comp she's in? If the same champion has different optimal items in different compositions, then **filter = foundation** — you can't analyze items without specifying the comp first.

We compare Vex's item metrics in four contexts:
1. **NOVA 95** — the dominant Vex comp (210k games)
2. **Dark Star** — secondary Vex comp (3.7k games)
3. **Shepherd** — another Vex shell (59k games)
4. **Unfiltered** — all Vex games (461k games)

---

## Chapter 1: The Data

### NOVA 95 (210,392 games, AVP 4.11)

| Item | Games | Rate | AVP | Edge | Necessity |
|------|-------|------|-----|------|-----------|
| Guinsoo's Rageblade | 184,304 | 88% | 4.05 | +0.06 | +0.437 |
| Giant Slayer | 77,026 | 37% | 3.99 | +0.13 | +0.074 |
| Hextech Gunblade | 59,825 | 28% | 3.94 | +0.17 | +0.068 |
| Striker's Flail | 33,560 | 16% | 3.79 | +0.32 | +0.062 |
| Rabadon's Deathcap | 20,055 | 10% | 3.75 | +0.37 | +0.039 |
| Red Buff | 15,655 | 7% | 3.68 | +0.43 | +0.035 |
| Archangel's Staff | 20,766 | 10% | 3.95 | +0.17 | +0.018 |

### Dark Star (3,692 games, AVP 3.98)

| Item | Games | Rate | AVP | Edge | Necessity |
|------|-------|------|-----|------|-----------|
| Guinsoo's Rageblade | 2,969 | 80% | 3.93 | +0.05 | +0.199 |
| Dark Star Emblem | 1,707 | 46% | 3.84 | +0.14 | +0.119 |
| Void Staff | 596 | 16% | 3.83 | +0.16 | +0.030 |
| Red Buff | 201 | 5% | 3.76 | +0.23 | +0.013 |
| Rabadon's Deathcap | 304 | 8% | 3.88 | +0.11 | +0.010 |
| Archangel's Staff | 330 | 9% | 3.90 | +0.08 | +0.008 |
| Giant Slayer | 887 | 24% | 3.99 | -0.01 | -0.003 |
| Hextech Gunblade | 528 | 14% | 4.02 | -0.04 | -0.007 |
| Jeweled Gauntlet | 1,144 | 31% | 4.13 | -0.15 | -0.067 |

### Shepherd (58,817 games, AVP 3.53)

| Item | Games | Rate | AVP | Edge | Necessity |
|------|-------|------|-----|------|-----------|
| Giant Slayer | 25,977 | 44% | 3.49 | +0.04 | +0.034 |
| Rabadon's Deathcap | 7,766 | 13% | 3.36 | +0.17 | +0.025 |
| Striker's Flail | 5,422 | 9% | 3.39 | +0.14 | +0.014 |
| Guinsoo's Rageblade | 50,785 | 86% | 3.53 | +0.00 | +0.014 |
| Void Staff | 11,962 | 20% | 3.49 | +0.04 | +0.011 |
| Red Buff | 2,580 | 4% | 3.31 | +0.22 | +0.010 |
| Hextech Gunblade | 13,469 | 23% | 3.50 | +0.03 | +0.010 |

### Unfiltered (460,602 games, AVP 4.10)

| Item | Games | Rate | AVP | Edge | Necessity |
|------|-------|------|-----|------|-----------|
| Guinsoo's Rageblade | 413,838 | 90% | 4.08 | +0.02 | +0.156 |
| Giant Slayer | 191,181 | 42% | 4.04 | +0.06 | +0.046 |
| Rabadon's Deathcap | 45,628 | 10% | 3.85 | +0.25 | +0.028 |
| Striker's Flail | 57,493 | 12% | 3.91 | +0.19 | +0.027 |
| Hextech Gunblade | 125,086 | 27% | 4.03 | +0.07 | +0.025 |
| Red Buff | 26,878 | 6% | 3.76 | +0.34 | +0.021 |

---

## Chapter 2: What Changes

### The Constant — Guinsoo's Rageblade
Guinsoo's is BIS #1 in every context. 80-90% play rate everywhere. This is a **comp-independent truth** about Vex: she needs Guinsoo's.

### The Variables — Slots 2 and 3

| Rank | NOVA 95 | Dark Star | Shepherd |
|------|---------|-----------|----------|
| #2 (Necessity) | Giant Slayer | Dark Star Emblem | Giant Slayer |
| #3 | Hextech Gunblade | Void Staff | Rabadon's Deathcap |
| #4 | Striker's Flail | Red Buff | Striker's Flail |
| #5 | Rabadon's Deathcap | Rabadon's Deathcap | Guinsoo ★2 (tie) |

Key differences:
- **Dark Star Emblem** is #2 in Dark Star (obviously — more trait synergy), doesn't exist in NOVA
- **Giant Slayer** is #2 in NOVA and Shepherd, but **negative Edge** in Dark Star (worse than average!)
- **Hextech Gunblade** is #3 in NOVA but **negative Edge** in Dark Star
- **Void Staff** appears in Dark Star (#3) and Shepherd (#5), barely registers in NOVA
- **Jeweled Gauntlet** is the most popular non-Guinsoo item in Dark Star (31% rate) but has **-0.15 Edge** — a trap item

### Giant Slayer: Good or Bad?

| Context | Rate | Edge | Necessity |
|---------|------|------|-----------|
| NOVA 95 | 37% | +0.13 | +0.074 |
| Dark Star | 24% | -0.01 | -0.003 |
| Shepherd | 44% | +0.04 | +0.034 |
| Unfiltered | 42% | +0.06 | +0.046 |

Giant Slayer is good in NOVA, mediocre in Shepherd, and **borderline bad** in Dark Star. Same item, same champion, completely different value. The comp context changes the item's worth.

Why? Likely because Dark Star already provides massive damage amplification (Doom steals AD/AP from all enemies), so the marginal damage from Giant Slayer is less valuable. NOVA 95 has more synergy with sustained DPS items.

### Jeweled Gauntlet: The Dark Star Trap

In Dark Star, Jeweled Gauntlet has 31% play rate but -0.15 Edge and -0.067 Necessity. It's the **worst common item** on Vex in that comp. Players build it a lot, but it actively hurts performance. This is exactly the kind of finding that comp-filtered analysis reveals — unfiltered, it would be mixed in with NOVA data and look neutral.

---

## Chapter 3: Filter Sensitivity — How Much Does It Matter?

Compare Edge rankings across comps for common items:

| Item | NOVA Edge | Dark Star Edge | Shepherd Edge | Rank Shift |
|------|-----------|---------------|---------------|------------|
| Guinsoo's | +0.06 | +0.05 | +0.00 | Stable (#1) |
| Giant Slayer | +0.13 | **-0.01** | +0.04 | **NOVA #3 → DS negative** |
| Hextech Gunblade | +0.17 | **-0.04** | +0.03 | **NOVA #2 → DS negative** |
| Rabadon's | +0.37 | +0.11 | +0.17 | Stable (top 5) |
| Red Buff | +0.43 | +0.23 | +0.22 | Stable (high Edge, low rate) |
| Void Staff | — | +0.16 | +0.04 | DS-specific value |

**3 out of 6 common items flip sign or change rank dramatically between comps.** Filter matters enormously.

---

## Chapter 4: The Small Sample Problem

Dark Star has only 3,692 games vs NOVA's 210k. Can we trust Dark Star results?

Quick confidence check on Giant Slayer in Dark Star (887 games, AVP 3.99):
- Standard error ≈ σ/√n ≈ 2.0/√887 ≈ 0.067
- 95% CI: [3.86, 4.12]
- Overall AVP is 3.98, which is well within the CI

So the "negative Edge" for Giant Slayer in Dark Star is **not statistically significant** — it could just be noise. But the directional story (Giant Slayer is much less valuable in Dark Star than NOVA) holds: Edge of -0.01 vs +0.13 is a real difference even if the exact sign is uncertain.

Contrast with Jeweled Gauntlet (1,144 games, AVP 4.13):
- SE ≈ 2.0/√1144 ≈ 0.059
- 95% CI: [4.01, 4.25]
- Overall 3.98 is outside the lower bound

Jeweled Gauntlet being bad in Dark Star is more robust — even the optimistic end of the CI (4.01) is worse than average.

---

## Cross-Validation

tftable API not yet available for programmatic access (blocked in prior experiment). Qualitative comparison deferred.

However, we can cross-validate internally: the unfiltered Vex results should be a weighted average of all the per-comp results. NOVA dominates (210k of 461k games = 46%), so the unfiltered ranking should look most like NOVA — and it does. This is consistent.

---

## What I Learned

1. **Filter is the foundation.** Same champion, same item — Giant Slayer is +0.13 Edge in NOVA and -0.01 in Dark Star. Without specifying the comp, "Vex's best items" is a meaningless question. This confirms Dishsoap's core principle: "Add context first."

2. **Some items are comp-independent, some are comp-dependent.** Guinsoo's and Red Buff are always good on Vex. Giant Slayer and Hextech Gunblade depend heavily on the comp. This creates a natural taxonomy:
   - **Universal BIS**: good in every comp (Guinsoo's, Red Buff, Rabadon's)
   - **Comp-conditional**: good in some comps, bad in others (Giant Slayer, Hextech Gunblade, Void Staff)
   - **Trap items**: popular but bad in specific comps (Jeweled Gauntlet in Dark Star)

3. **Necessity catches what Edge misses.** Edge says Red Buff (+0.43) is better than Giant Slayer (+0.13) in NOVA. But Necessity says Giant Slayer (0.074) contributes more than Red Buff (0.035) to the comp's overall performance, because 37% of players build it vs 7%. Both metrics are right — they answer different questions.

4. **Small samples need confidence intervals.** Dark Star's 3.7k games make individual item results noisy. Giant Slayer's negative Edge isn't statistically significant. But the *comparative pattern* (much less valuable than in NOVA) is robust.

5. **Unfiltered data is NOVA-dominated.** Vex appears in 461k games, but 210k are NOVA 95 (46%). Unfiltered analysis mostly tells you about NOVA, with other comps adding noise. This is another argument for filtering.

## Open Questions

- Why exactly does Giant Slayer lose value in Dark Star? Is it the Doom passive (stolen AD/AP makes raw damage items redundant)?
- Are there items that are bad unfiltered but good in a specific comp? (Reverse of the Jeweled Gauntlet trap)
- Can we quantify "how much does filtering matter" as a single number? (e.g., average rank correlation between comp-filtered and unfiltered)
- Module 3 preview: In NOVA 95, do the top *builds* (3-item combos) agree with the top single items?
