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
from tft_stat.filter_params import build_filter_params, load_item_names, parse_unit_spec
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

    data = query(f"unit_items_unique/{holder}", params)
    item_names = load_item_names()

    results = []
    for item in data.get("data", []):
        iid = item.get("unit_items_unique", "")
        if not iid:
            continue
        stats = placement_stats(item.get("placement_count", []))
        if stats["games"] < args.min_count:
            continue

        item_part = iid.split("&")[1] if "&" in iid else iid
        base_item = item_part.rsplit("-", 1)[0] if "-" in item_part else item_part
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


def _params_from_args(args) -> list[str]:
    return build_filter_params(
        comp=getattr(args, "comp", None),
        or_units=getattr(args, "or_units", None),
        units=getattr(args, "units", None),
        traits=getattr(args, "traits", None),
        exclude_units=getattr(args, "exclude_units", None),
        exclude_traits=getattr(args, "exclude_traits", None),
    )


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

    # tftable
    p_tt = sub.add_parser("tftable", help="Query tftable ground-truth data")
    p_tt.add_argument("holder_unit", nargs="?", help="Unit for item data (omit for unit necessity)")
    p_tt.add_argument("--comp", help="Comp key (e.g. nova_95)")

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return

    {"comps": cmd_comps, "total": cmd_total, "units": cmd_units,
     "items": cmd_items, "tftable": cmd_tftable}[args.command](args)


def _add_filter_args(p):
    p.add_argument("--comp", help="Comp key (e.g. nova_95, dark_star)")
    p.add_argument("--or-units", help="OR group: TFT17_Fiora:i3,TFT17_Vex:i3")
    p.add_argument("--units", help="Required units: TFT17_Blitz,TFT17_Morde")
    p.add_argument("--traits", help="Required traits: TFT17_DRX:2")
    p.add_argument("--exclude-units", help="Excluded units")
    p.add_argument("--exclude-traits", help="Excluded traits")


if __name__ == "__main__":
    main()
