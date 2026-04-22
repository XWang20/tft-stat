# Experiment: Cross-Validation — Our Necessity vs tftable
**Status**: 🧪 In Progress (tftable data extraction blocked)
**Date**: 2026-04-21
**Module**: 9 (Cross-Validation) — preview

## The Question

Do our calculated Necessity scores match tftable's necessity scores for the same comp?

## Our Results (MetaTFT Explorer API)

Vex in Nova 95, overall AVP 4.109, 213,183 games:

```
Item                  Rate   Necessity
Guinsoo's Rageblade    87%   +0.418
Giant Slayer           36%   +0.070
Hextech Gunblade       28%   +0.065
Striker's Flail        16%   +0.061
Rabadon's Deathcap     10%   +0.039
Red Buff                7%   +0.035
Archangel's Staff      10%   +0.018
Morellonomicon          4%   +0.010
```

## tftable Cross-Validation

**Blocked**: tftable.cc uses fully client-side rendering — `__NEXT_DATA__` is empty, comp data is embedded in JS bundles, not accessible via simple API or SSR extraction. Need a different approach:

- [ ] Option 1: Xing provides tftable data directly (he has access)
- [ ] Option 2: Parse tftable's JS bundles to find data endpoints
- [ ] Option 3: Screenshot comparison (manual)

## What I Learned

tftable's architecture is different from MetaTFT:
- MetaTFT: data from API endpoints (easy to query programmatically)
- tftable: data compiled into static JS bundles (harder to extract)

This is a useful lesson — not all "public" data is equally accessible.

## Open Questions
- [ ] Get tftable necessity scores for comparison
- [ ] If they differ, which is more accurate and why?
- [ ] Does tftable use the same Necessity formula?
