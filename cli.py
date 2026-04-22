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
from tft_stat.tftable import get_unit_items, get_comp_summary, get_comp_units, list_comps as tftable_list_comps


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


def cmd_crossval(args):
    if not args.comp:
        print("Error: crossval requires --comp", file=sys.stderr)
        sys.exit(1)
    if not args.holder_unit:
        print("Error: crossval requires a holder unit (e.g. TFT17_Vex)", file=sys.stderr)
        sys.exit(1)

    holder = parse_unit_spec(args.holder_unit)
    item_names = load_item_names()

    # --- tftable data ---
    print(f"Fetching tftable data for {args.comp} / {args.holder_unit}...")
    try:
        tftable_items = get_unit_items(args.comp, args.holder_unit)
    except Exception as e:
        print(f"Error accessing tftable: {e}", file=sys.stderr)
        sys.exit(1)

    if not tftable_items:
        print(f"No tftable data found for {args.holder_unit} in {args.comp}")
        print(f"Available units: {get_comp_units(args.comp)}")
        sys.exit(1)

    tftable_rank = {}
    for i, item in enumerate(sorted(tftable_items, key=lambda x: -x["necessity"])):
        iid = item["item_id"]
        tftable_rank[iid] = {
            "rank": i + 1,
            "necessity": item["necessity"],
            "rate": item["appearance_rate"],
            "rating": item.get("rating", ""),
        }

    # --- our pipeline ---
    print(f"Fetching MetaTFT data for {args.comp} / {args.holder_unit}...")
    params = _params_from_args(args)
    data = query(f"unit_items_unique/{holder}", params)

    results = []
    for item in data.get("data", []):
        iid = item.get("unit_items_unique", "")
        if not iid:
            continue
        stats = placement_stats(item.get("placement_count", []))
        if stats["games"] < 100:
            continue
        item_part = iid.split("&")[1] if "&" in iid else iid
        base_item = item_part.rsplit("-", 1)[0] if "-" in item_part else item_part
        tier = item_part.rsplit("-", 1)[1] if "-" in item_part else "?"
        if tier != "1":
            continue
        results.append((item_names.get(base_item, base_item), base_item, tier, stats))

    overall_avg, total_comp_games = _get_holder_baseline(params, holder)
    add_item_metrics(results, overall_avg, total_comp_games)
    results.sort(key=lambda x: x[3]["weighted_delta"], reverse=True)

    our_rank = {}
    for i, (name, base_item, _, s) in enumerate(results):
        our_rank[base_item] = {
            "rank": i + 1,
            "name": name,
            "necessity": s["weighted_delta"],
            "rate": s["play_rate"],
        }

    # --- comparison (only items present in tftable) ---
    matched = []
    our_items_by_id = {base: (i + 1, name, s) for i, (name, base, _, s) in enumerate(results)}
    for i, item in enumerate(sorted(tftable_items, key=lambda x: -x["necessity"])):
        iid = item["item_id"]
        name = item_names.get(iid, iid)
        t_rank = i + 1
        o = our_items_by_id.get(iid)
        matched.append({
            "name": name,
            "t_rank": t_rank,
            "t_nec": item["necessity"],
            "t_rating": item.get("rating", ""),
            "o_rank": o[0] if o else None,
            "o_nec": o[2]["weighted_delta"] if o else None,
        })

    # re-rank our results within tftable's item set only
    tftable_ids = {item["item_id"] for item in tftable_items}
    our_filtered = [(base, s["weighted_delta"]) for (_, base, _, s) in results if base in tftable_ids]
    our_filtered.sort(key=lambda x: -x[1])
    our_rerank = {iid: rank + 1 for rank, (iid, _) in enumerate(our_filtered)}

    tftable_summary = get_comp_summary(args.comp)

    for m in matched:
        iid_candidates = [item["item_id"] for item in tftable_items
                         if item_names.get(item["item_id"], item["item_id"]) == m["name"]]
        if iid_candidates:
            m["o_rank_matched"] = our_rerank.get(iid_candidates[0])

    print(f"\n{'='*70}")
    print(f"Cross-Validation: {args.holder_unit} items in {args.comp}")
    print(f"tftable: {tftable_summary.get('sample_size', '?'):,} games | "
          f"MetaTFT: {total_comp_games:,} games")
    print(f"{'='*70}")
    print(f"\n{'Item':<28} {'tftable':>10} {'Ours':>10} {'tft#':>5} {'Our#':>5} {'Rating'}")
    print("-" * 70)
    for m in matched:
        t_nec = f"{m['t_nec']:.4f}"
        o_nec = f"{m['o_nec']:.4f}" if m['o_nec'] is not None else "—"
        t_r = str(m["t_rank"])
        o_r = str(m.get("o_rank_matched", "—"))
        print(f"{m['name']:<28} {t_nec:>10} {o_nec:>10} {t_r:>5} {o_r:>5} {m['t_rating']}")

    # rank correlation on matched set
    paired = [(m["t_rank"], m["o_rank_matched"]) for m in matched if m.get("o_rank_matched")]
    if len(paired) >= 3:
        n = len(paired)
        d_sq = sum((t - o) ** 2 for t, o in paired)
        spearman = 1 - 6 * d_sq / (n * (n * n - 1))
        print(f"\nSpearman rank correlation: {spearman:.3f} (n={n})")
        if spearman > 0.8:
            print("Strong agreement between pipelines.")
        elif spearman > 0.5:
            print("Moderate agreement — investigate divergences.")
        else:
            print("Weak agreement — significant methodology differences.")


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

    # crossval
    p_cv = sub.add_parser("crossval", help="Cross-validate item rankings with tftable")
    p_cv.add_argument("holder_unit", help="Unit to check (e.g. TFT17_Vex)")
    _add_filter_args(p_cv)

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return

    {"comps": cmd_comps, "total": cmd_total, "units": cmd_units,
     "items": cmd_items, "crossval": cmd_crossval}[args.command](args)


def _add_filter_args(p):
    p.add_argument("--comp", help="Comp key (e.g. nova_95, dark_star)")
    p.add_argument("--or-units", help="OR group: TFT17_Fiora:i3,TFT17_Vex:i3")
    p.add_argument("--units", help="Required units: TFT17_Blitz,TFT17_Morde")
    p.add_argument("--traits", help="Required traits: TFT17_DRX:2")
    p.add_argument("--exclude-units", help="Excluded units")
    p.add_argument("--exclude-traits", help="Excluded traits")


if __name__ == "__main__":
    main()
