"""Placement statistics and item metric calculations."""

from __future__ import annotations


def placement_stats(placement_count: list[int]) -> dict:
    total = sum(placement_count)
    if total == 0:
        return {"games": 0, "avg": 0, "top4": 0, "win": 0}
    avg = sum((i + 1) * c for i, c in enumerate(placement_count)) / total
    top4 = sum(placement_count[:4]) / total * 100
    win = placement_count[0] / total * 100
    return {"games": total, "avg": avg, "top4": top4, "win": win}


def add_item_metrics(results: list, overall_avg: float, total_comp_games: int) -> None:
    """Add edge, play_rate, necessity (weighted_delta), marginal to each result's stats dict."""
    for _name, _base, _tier, s in results:
        p = s["games"] / total_comp_games if total_comp_games > 0 else 0
        edge = overall_avg - s["avg"]
        if p < 1.0:
            no_item_avg = (overall_avg - p * s["avg"]) / (1 - p)
            weighted_delta = no_item_avg - overall_avg
            marginal = no_item_avg - s["avg"]
        else:
            no_item_avg = overall_avg
            weighted_delta = 0
            marginal = 0
        s["edge"] = edge
        s["play_rate"] = p
        s["weighted_delta"] = weighted_delta
        s["marginal"] = marginal
        s["no_item_avg"] = no_item_avg
