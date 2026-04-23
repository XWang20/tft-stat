#!/usr/bin/env python3
"""TFT Stat CLI — query MetaTFT Explorer API for composition analysis.

Usage:
    python3 cli.py items TFT17_Vex --comp nova_95
    python3 cli.py units --comp nova_95
    python3 cli.py total --comp dark_star
    python3 cli.py comps
"""

from __future__ import annotations

import argparse
import sys

from tft_stat.api import query
from tft_stat.compositions import COMPOSITIONS
from tft_stat.filter_params import expr_to_params, load_item_names, parse_unit_spec
from tft_stat.metrics import add_item_metrics, placement_stats
from tft_stat import tftable


def cmd_comps(_args):
    print(f"{'Key':<25} {'Name'}")
    print("-" * 55)
    for key, comp in COMPOSITIONS.items():
        print(f"{key:<25} {comp['name']}")


def cmd_total(args):
    params = _params_from_args(args)
    data = query("total", params)
    d = data.get("data", data)
    if isinstance(d, list) and d:
        d = d[0]
    pc = d.get("placement_count")
    if pc:
        stats = placement_stats(pc)
        print(f"Comps Analyzed: {stats['games']:,}")
        print(f"Avg Placement:  {stats['avg']:.2f}")
        print(f"Top 4 Rate:     {stats['top4']:.1f}%")
        print(f"Win Rate:       {stats['win']:.1f}%")
    else:
        print(f"Comps Analyzed: {d.get('total_games', 'N/A')}")
    adj = data.get("filter_adjustment", {})
    if adj.get("override_applied"):
        print(f"Filter adjusted: {adj}")
    elif adj.get("sample_size"):
        print(f"Sample pool:    {adj['sample_size']:,}")


def cmd_units(args):
    params = _params_from_args(args)
    data = query("units_unique", params)

    results = []
    for item in data.get("data", []):
        uid = item.get("units_unique", "")
        if not uid:
            continue
        stats = placement_stats(item.get("placement_count", []))
        if stats["games"] < args.min_count:
            continue
        results.append((uid, stats))

    results.sort(key=lambda x: x[1]["avg"])

    print(f"{'Unit':<30} {'Games':>8} {'AvgPl':>6} {'Top4%':>6} {'Win%':>6}")
    print("-" * 60)
    for uid, s in results[:30]:
        print(f"{uid:<30} {s['games']:>8} {s['avg']:>6.2f} {s['top4']:>5.1f}% {s['win']:>5.1f}%")


def cmd_items(args):
    if not args.holder_unit:
        print("Error: items command requires a holder unit (first positional arg)", file=sys.stderr)
        sys.exit(1)

    holder = parse_unit_spec(args.holder_unit)
    params = _params_from_args(args)

    if getattr(args, "normal_only", False):
        import urllib.parse
        uid = args.holder_unit.split(":")[0]
        for t in ("artifact", "radiant", "trait", "emblem"):
            val = urllib.parse.quote(f"!{uid}-1|{t}_1,2,3", safe="")
            params.append(f"unit_itemtype_counts={val}")
        params.append("item=!TFT17_AnimaSquadItem_.*")

    data = query(f"unit_items_unique/{holder}", params)
    item_names = load_item_names()

    results = []
    exclude_ids = _item_exclude_set(args)
    for item in data.get("data", []):
        iid = item.get("unit_items_unique", "")
        if not iid:
            continue
        stats = placement_stats(item.get("placement_count", []))
        if stats["games"] < args.min_count:
            continue

        item_part = iid.split("&")[1] if "&" in iid else iid
        base_item = item_part.rsplit("-", 1)[0] if "-" in item_part else item_part
        if base_item in exclude_ids:
            continue
        name = item_names.get(base_item, base_item)
        tier = item_part.rsplit("-", 1)[1] if "-" in item_part else "?"
        results.append((name, base_item, tier, stats))

    overall_avg, total_comp_games = _get_holder_baseline(params, holder)
    add_item_metrics(results, overall_avg, total_comp_games)
    results.sort(key=lambda x: x[3]["weighted_delta"], reverse=True)

    print(f"Overall AVP: {overall_avg:.2f} ({total_comp_games:,} games)")
    print()
    print(f"{'Item':<28} {'Games':>7} {'Rate':>5} {'AVP':>5} {'Edge':>6} {'Neces.':>7}")
    print("-" * 65)
    for name, _, tier, s in results[:25]:
        label = f"{name}" if tier == "1" else f"{name} ★{tier}"
        print(f"{label:<28} {s['games']:>7} {s['play_rate']:>4.0%} {s['avg']:>5.2f} {s['edge']:>+6.2f} {s['weighted_delta']:>+7.3f}")

    adj = data.get("filter_adjustment", {})
    print(f"\nTotal sample: {adj.get('sample_size', '?')}")
    print("\nEdge = overall - w/ (positive=good). Necessity = w/o - overall (play-rate weighted).")


def cmd_tftable(args):
    """Query tftable ground-truth data."""
    if not args.comp:
        print("Error: tftable requires --comp", file=sys.stderr)
        sys.exit(1)

    item_names = load_item_names()

    print(f"Fetching tftable: {args.comp}...")
    try:
        summary = tftable.get_comp_summary(args.comp)
    except Exception as e:
        print(f"Error accessing tftable: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"Sample: {summary.get('sample_size', '?'):,} games, "
          f"AVP: {summary.get('avg_placement', 0):.2f}, "
          f"WR: {summary.get('win_rate', 0):.1%}")

    if args.holder_unit:
        items = tftable.get_unit_items(args.comp, args.holder_unit)
        if not items:
            print(f"\nNo item data for {args.holder_unit}.")
            print(f"Available: {tftable.get_comp_units(args.comp)}")
            return
        print(f"\n{args.holder_unit} items (tftable):")
        print(f"{'Item':<40} {'Necessity':>10} {'Rate':>7} {'Rating'}")
        print("-" * 65)
        for item in sorted(items, key=lambda x: -x["necessity"]):
            name = item_names.get(item["item_id"], item["item_id"])
            print(f"{name:<40} {item['necessity']:>10.4f} {item['appearance_rate']:>6.1%} {item.get('rating', '')}")
    else:
        units = tftable.get_unit_necessity(args.comp)
        if not units:
            print("\nNo unit data.")
            return
        print(f"\nUnit necessity (tftable):")
        print(f"{'Unit':<30} {'Necessity':>10} {'IC3 Rate':>9} {'IC3 Rank':>9}")
        print("-" * 62)
        for u in sorted(units, key=lambda x: -x["necessity"]):
            print(f"{u['unit_id']:<30} {u['necessity']:>10.3f} {u['ic3_rate']:>8.1%} {u['ic3_rank']:>9.2f}")


def cmd_scout(args):
    """Scan top player endgame boards — full board view."""
    data = query("recent_matches", [], extra_params={
        "rank": args.rank or "CHALLENGER,GRANDMASTER,MASTER",
    })
    matches = data.get("data", [])
    if not matches:
        print("No matches found.")
        return

    top = [m for m in matches if m.get("placement", 9) <= (args.top or 4)]
    item_names = load_item_names()

    print(f"Meta snapshot: {len(matches)} matches, {len(top)} top-{args.top or 4} boards\n")

    for m in sorted(top, key=lambda x: x.get("placement", 9)):
        placement = m.get("placement", "?")
        rank = m.get("rank", "?")
        server = m.get("server", "?")

        # Parse units
        units = []
        for u in m.get("unit_tier_numitems", []):
            parts = u.rsplit("_", 2)
            if len(parts) >= 3:
                uid = "_".join(parts[:-2])
                star = parts[-2]
                items = parts[-1]
                name = uid.replace("TFT17_", "")
                units.append(f"{name}{'★' + star if star != '1' else ''}{'({})'.format(items) if items != '0' else ''}")

        # Parse builds (3-item only)
        builds = []
        for b in m.get("unit_buildNames", []):
            if "&" in b:
                unit, items_str = b.split("&", 1)
                item_list = items_str.split("|")
                if len(item_list) >= 3:
                    unit_name = unit.replace("TFT17_", "")
                    names = [item_names.get(i, i.replace("TFT_Item_", "").replace("TFT5_Item_", "")) for i in item_list]
                    builds.append(f"{unit_name}: {' / '.join(names)}")

        # Active traits
        traits = [t.replace("TFT17_", "") for t in (m.get("traits") or [])
                  if not t.endswith("_0") and "UniqueTrait" not in t]

        print(f"#{placement} {rank} {server} | {' '.join(units)}")
        for b in builds:
            print(f"  {b}")
        if traits:
            print(f"  traits: {', '.join(traits)}")
        print()


IGNORED_BOARD_UNITS = {"TFT17_Summon"}


def cmd_core(args):
    """Detect primary board composition via MetaTFT comps endpoint."""
    params = _params_from_args(args)
    if not params:
        print("Error: --comp or --filter required for comps query", file=sys.stderr)
        sys.exit(1)

    slots = args.num_unit_slots or "6,7,8,9,10,11"
    params.append(f"num_unit_slots={slots}")

    data = query("exact_units_traits2", params)
    entries = data.get("data", [])
    if not entries:
        print("No board compositions found.")
        return

    entries.sort(key=lambda x: -sum(x.get("placement_count", [])))
    total_games = sum(sum(e.get("placement_count", [])) for e in entries)

    top_n = min(args.show, len(entries))
    print(f"Board compositions: {len(entries)} ({total_games:,} total games)")
    print(f"\n{'#':<4} {'Games':>7} {'Share':>6} {'AVP':>5} {'Lvl':>4}  Units")
    print("-" * 85)
    for i, e in enumerate(entries[:top_n], 1):
        ut = e.get("units_traits", "")
        units = ut.split("|")[0].split("&") if ut else []
        pc = e.get("placement_count", [])
        games = sum(pc)
        avg = sum((j+1)*c for j, c in enumerate(pc)) / games if games else 0
        real_units = [u for u in units if u not in IGNORED_BOARD_UNITS]
        level = len(real_units)
        unit_labels = []
        for idx, uid in enumerate(units):
            name = uid.replace("TFT17_", "")
            if uid in IGNORED_BOARD_UNITS:
                name = f"({name})"
            star = e.get(f"avg_unit_{idx+1}_tier", 0)
            star_str = f"★{star:.1f}" if star >= 1.5 else ""
            unit_labels.append(f"{name}{star_str}")
        tag = " <- primary" if i == 1 else ""
        print(f"{i:<4} {games:>7,} {games/total_games:>5.1%} {avg:>5.2f} {level:>4}  {' '.join(unit_labels)}{tag}")

    primary = entries[0]
    all_primary_units = primary.get("units_traits", "").split("|")[0].split("&")
    primary_units = [u for u in all_primary_units if u not in IGNORED_BOARD_UNITS]
    core_size = len(primary_units)
    primary_games = sum(primary.get("placement_count", []))

    if core_size >= 7:
        filter_parts = [f"Unit('{uid}')" for uid in primary_units]
        filter_str = " & ".join(filter_parts)
        flex_pop = core_size + 1
        comp_flag = f"--comp {args.comp} " if args.comp else ""
        print(f"\nPrimary: {core_size} units (level {core_size}), {primary_games:,} games ({primary_games/total_games:.0%})")
        print(f"+1 command (level {flex_pop}):")
        print(f"  python3 cli.py units {comp_flag}--level {flex_pop} --filter \"{filter_str}\"")

def cmd_games(args):
    """Show sample boards matching a filter — sanity check."""
    params = _params_from_args(args)
    data = query("recent_matches", params)
    matches = data.get("data", [])
    item_names = load_item_names()

    if not matches:
        print("No matches found with this filter.")
        return

    show = min(args.show or 10, len(matches))
    print(f"{show}/{len(matches)} recent boards matching filter\n")

    for m in matches[:show]:
        placement = m.get("placement", "?")
        rank = m.get("rank", "?")
        server = m.get("server", "?")

        units = []
        for u in m.get("unit_tier_numitems", []):
            parts = u.rsplit("_", 2)
            if len(parts) >= 3:
                uid = "_".join(parts[:-2])
                star, items = parts[-2], parts[-1]
                name = uid.replace("TFT17_", "")
                units.append(f"{name}{'★' + star if star != '1' else ''}{'({})'.format(items) if items != '0' else ''}")

        builds = []
        for b in m.get("unit_buildNames", []):
            if "&" in b:
                unit, items_str = b.split("&", 1)
                item_list = items_str.split("|")
                if len(item_list) >= 2:
                    unit_name = unit.replace("TFT17_", "")
                    names = [item_names.get(i, i.replace("TFT_Item_", "")) for i in item_list]
                    builds.append(f"{unit_name}: {' / '.join(names)}")

        print(f"#{placement} {rank} {server} | {' '.join(units)}")
        for b in builds:
            print(f"  {b}")
        print()


def _get_holder_baseline(params: list[str], holder: str) -> tuple[float, int]:
    try:
        units_data = query("units_unique", params)
        for u in units_data.get("data", []):
            if u.get("units_unique", "") == holder:
                stats = placement_stats(u.get("placement_count", []))
                return stats["avg"], stats["games"]
    except Exception:
        pass
    return 4.5, 0


def _item_exclude_set(args) -> set[str]:
    """Build set of item IDs to exclude based on --exclude-tank-items etc."""
    from tft_stat.item_classes import TANK_ITEM_IDS, BRUISER_ITEM_IDS, DMG_ITEM_IDS
    ids: set[str] = set()
    if getattr(args, "exclude_tank_items", False):
        ids |= TANK_ITEM_IDS
    if getattr(args, "exclude_dmg_items", False):
        ids |= DMG_ITEM_IDS
    if getattr(args, "exclude_bruiser_items", False):
        ids |= BRUISER_ITEM_IDS
    return ids


def _params_from_args(args) -> list[str]:
    from tft_stat.filter_expr import Unit, Trait, Item, And, Or, Not
    from tft_stat.filter_params import expr_to_params

    params = []
    if hasattr(args, "comp") and args.comp:
        from tft_stat.compositions import COMPOSITIONS
        comp = COMPOSITIONS.get(args.comp)
        if not comp:
            print(f"Error: unknown comp '{args.comp}'", file=sys.stderr)
            sys.exit(1)
        params = expr_to_params(comp["filter"])

    if hasattr(args, "filter") and args.filter:
        extra_expr = eval(args.filter)
        params.extend(expr_to_params(extra_expr))

    if hasattr(args, "level") and args.level:
        params.append(f"level={args.level}")

    if hasattr(args, "no_emblem") and args.no_emblem:
        params.append("emblem_count=!1-any")

    return params


def main():
    parser = argparse.ArgumentParser(description="TFT Stat — MetaTFT Explorer Query Tool")
    sub = parser.add_subparsers(dest="command")

    # comps
    sub.add_parser("comps", help="List all available compositions")

    # total
    p_total = sub.add_parser("total", help="Overall stats for a comp")
    _add_filter_args(p_total)

    # units
    p_units = sub.add_parser("units", help="Unit stats within a comp")
    _add_filter_args(p_units)
    p_units.add_argument("--min-count", type=int, default=100)

    # items
    p_items = sub.add_parser("items", help="Item stats for a unit within a comp")
    p_items.add_argument("holder_unit", help="Unit to check items for (e.g. TFT17_Vex)")
    _add_filter_args(p_items)
    p_items.add_argument("--min-count", type=int, default=100)
    p_items.add_argument("--normal-only", action="store_true",
                         help="Exclude artifact/radiant/trait/emblem items")
    p_items.add_argument("--exclude-tank-items", action="store_true",
                         help="Exclude tank items (Warmog, Gargoyle, Bramble, etc.)")
    p_items.add_argument("--exclude-dmg-items", action="store_true",
                         help="Exclude damage items (Guinsoo, IE, Dcap, etc.)")
    p_items.add_argument("--exclude-bruiser-items", action="store_true",
                         help="Exclude bruiser items (BT, GA, Gunblade, etc.)")

    # tftable
    p_tt = sub.add_parser("tftable", help="Query tftable ground-truth data")
    p_tt.add_argument("holder_unit", nargs="?", help="Unit for item data (omit for unit necessity)")
    p_tt.add_argument("--comp", help="Comp key (e.g. nova_95)")

    # scout
    p_scout = sub.add_parser("scout", help="Scan top player endgame boards")
    p_scout.add_argument("--rank", help="Rank filter (default: CHALLENGER,GRANDMASTER,MASTER)")
    p_scout.add_argument("--top", type=int, default=4, help="Placement cutoff (default: 4)")

    # core
    p_core = sub.add_parser("core", help="Show board compositions for a comp (primary board detection)")
    _add_filter_args(p_core)
    p_core.add_argument("--num-unit-slots", default=None,
                         help="Board size(s), e.g. 8 or 6,7,8,9,10,11 (default: 6-11)")
    p_core.add_argument("--show", type=int, default=10, help="Compositions to show (default: 10)")

    # games
    p_games = sub.add_parser("games", help="Show sample boards matching a filter (sanity check)")
    _add_filter_args(p_games)
    p_games.add_argument("--show", type=int, default=10, help="Boards to show (default: 10)")

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return

    {"comps": cmd_comps, "total": cmd_total, "units": cmd_units,
     "items": cmd_items, "tftable": cmd_tftable, "scout": cmd_scout,
     "core": cmd_core, "games": cmd_games}[args.command](args)


def _add_filter_args(p):
    p.add_argument("--comp", help="Comp key (e.g. nova_95, dark_star)")
    p.add_argument("--filter", help="Filter expression (e.g. \"Unit('TFT17_Vex', item_min=3) & Trait('TFT17_DRX', min_units=2)\")")
    p.add_argument("--level", type=int, help="Player level filter (e.g. 9, 10)")
    p.add_argument("--no-emblem", action="store_true", help="Exclude games with emblems/spatulas")


if __name__ == "__main__":
    main()
