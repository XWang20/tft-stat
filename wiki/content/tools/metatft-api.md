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
| `rank` | By-rank distribution | Rank-specific analysis |
| `server` | By-server distribution | Region-specific meta |
| `recent_matches` | Last 100 game details | Sanity checking, qualitative analysis |

## Other APIs

| API | Returns | Filter? |
|---|---|---|
| `tft-comps-api/unit_items_processed` | Global unit×item summary (66 champs × 183 items) | ❌ |
| `tft-explorer-predictions/popular` | Popular query combinations | ❌ |
| `tft-explorer-predictions/prediction` | Suggested next filter | ✅ |

## Filter Format
- Unit: `unit_tier_numitems_unique=TFT17_Vex-1_.*_3` (occurrence_star_items)
- Trait: `trait=TFT17_DRX_1,TFT17_DRX_2` (tier indices)
- Exclude: prefix with `!`
- OR group: `sf[0][or][0][unit_tier_numitems_unique]=...`

## Sources
- Xing + Mochi API exploration (2026-04-21)
- Playwright network capture from MetaTFT Explorer
