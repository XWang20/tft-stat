# MetaTFT Explorer API
**Status**: ✅ verified

## Base URL
`https://api-hc.metatft.com/tft-explorer-api/`

## Common Parameters
```
formatnoarray=true
compact=true
queue=1100          # ranked
patch=current
days=3
rank=CHALLENGER,DIAMOND,EMERALD,GRANDMASTER,MASTER,PLATINUM
permit_filter_adjustment=true
level=10            # player level filter (optional, 1-10)
```

## Endpoints

| Endpoint | Returns | Use For |
|---|---|---|
| `total` | Total games, overall AVP | Sample size check |
| `units_unique` | Per-unit AVP, games | Unit performance, overall AVP baseline |
| `items_unique` | Global item frequency | Item meta overview |
| `unit_items_unique/{unit}` | Items on specific unit | **Item analysis (our main tool)** |
| `unit_builds` | 3-item build combos per unit | [[methods/build-analysis]] |
| `traits` | Trait activation frequency/AVP | Trait breakpoint analysis |
| `exact_units_traits2` | Board compositions + avg star levels | **Board detection, primary board, `core` subcommand** |
| `exact_units_traits` | Board compositions (no star levels) | Same as above, without star data |
| `extra_traits` | +1 trait activation data | +1 trait analysis |
| `rank` | By-rank distribution | Rank-specific analysis |
| `server` | By-server distribution | Region-specific meta |
| `recent_matches` | Last 100 game details | Sanity checking, qualitative analysis |

### Endpoint Aliases

Some endpoint names have aliases — the actual API name has a `_unique` suffix:

| CLI / Short Name | Actual API Endpoint |
|---|---|
| `unit_tier_numitems` | `unit_tier_numitems_unique` |
| `unit_items` | `unit_items_unique` |
| `items` | `items_unique` |
| `units` | `units_unique` |

### Explorer Tab to Endpoint Mapping

MetaTFT Explorer UI tabs map to these endpoints:

| Explorer Tab | Endpoint | Notes |
|---|---|---|
| Units | `units_unique` | |
| Items | `items_unique` / `unit_items_unique` | |
| Builds | `unit_builds` | |
| Traits | `traits` | |
| Comps | `exact_units_traits2` | Requires `num_unit_slots` param |
| +1 Traits | `extra_traits` | |
| Games | `recent_matches` | |
| Servers | `server` | |
| Rank | `rank` | |

## Other APIs

| API | Returns | Filter? |
|---|---|---|
| `tft-comps-api/unit_items_processed` | Global unit x item summary (66 champs x 183 items) | No |
| `tft-comps-api/comps_data` | Global comp clustering data (auto-detected comps) | No |
| `tft-explorer-predictions/popular` | Popular query combinations | No |
| `tft-explorer-predictions/prediction` | Suggested next filter | Yes |

## Filter Format
- Unit: `unit_tier_numitems_unique=TFT17_Vex-1_.*_3` (occurrence_star_items)
- Trait: `trait=TFT17_DRX_1,TFT17_DRX_2` (tier indices)
- Exclude: prefix with `!`
- OR group: `sf[0][or][0][unit_tier_numitems_unique]=...`

## Sources
- Xing + Mochi API exploration (2026-04-21)
- Playwright network capture from MetaTFT Explorer
- CLI `core` subcommand development (2026-04-23) — discovered `exact_units_traits2`, `extra_traits`, alias map
