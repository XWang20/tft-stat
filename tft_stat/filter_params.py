"""Convert filter expressions and CLI specs to MetaTFT API query parameters."""

from __future__ import annotations

import json
import os
import sys
import urllib.parse

_TRAIT_THRESHOLDS: dict[str, list[int]] = {}
_CONFIG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config", "pbe")


def _load_trait_thresholds():
    global _TRAIT_THRESHOLDS
    if _TRAIT_THRESHOLDS:
        return
    try:
        with open(os.path.join(_CONFIG_DIR, "traits.json")) as f:
            traits = json.load(f)
        for t in traits:
            api = t.get("apiName", "")
            thresholds = [bp["minUnits"] for bp in t.get("breakpoints", [])]
            if thresholds:
                _TRAIT_THRESHOLDS[api] = thresholds
    except Exception as e:
        print(f"Warning: Could not load trait thresholds: {e}", file=sys.stderr)


def load_item_names() -> dict[str, str]:
    try:
        with open(os.path.join(_CONFIG_DIR, "items.json")) as f:
            items = json.load(f)
        return {i["apiName"]: i.get("name_zh", i["name"]) for i in items}
    except Exception:
        return {}


def trait_to_tiers(trait_id: str, min_units: int) -> list[int]:
    _load_trait_thresholds()
    thresholds = _TRAIT_THRESHOLDS.get(trait_id, [])
    if not thresholds:
        return [1]
    tiers = [idx for idx, req in enumerate(thresholds, start=1) if req >= min_units]
    if not tiers:
        tiers = [len(thresholds)]
    return tiers


# --- CLI spec parsers (string → MetaTFT value) ---

def parse_unit_spec(spec: str) -> str:
    """Parse 'TFT17_Vex:s2:i3' → 'TFT17_Vex-1_2_3'."""
    parts = spec.split(":")
    unit_id = parts[0]
    star = items = None
    for p in parts[1:]:
        if p.startswith("s"):
            star = p[1:]
        elif p.startswith("i"):
            items = p[1:]

    suffix = "-1"
    if star and items:
        suffix += f"_{star}_{items}"
    elif items:
        suffix += f"_.*_{items}"
    elif star:
        suffix += f"_{star}"
    return f"{unit_id}{suffix}"


def parse_trait_spec(spec: str) -> str:
    """Parse 'TFT17_DRX:2' → 'TFT17_DRX_1,TFT17_DRX_2'."""
    parts = spec.split(":")
    trait_id = parts[0]
    min_units = int(parts[1]) if len(parts) > 1 else 1
    tiers = trait_to_tiers(trait_id, min_units)
    return ",".join(f"{trait_id}_{t}" for t in tiers)


# --- Expression tree → MetaTFT params ---

def _unit_to_metatft(unit, *, negated: bool = False) -> str:
    suffix = "-1"
    star = items = None
    if unit.star_min is not None or unit.star_max is not None:
        vals = [str(v) for v in (1, 2, 3)
                if (unit.star_min is None or v >= unit.star_min)
                and (unit.star_max is None or v <= unit.star_max)]
        star = ",".join(vals) if vals else None
    if unit.item_min is not None or unit.item_max is not None:
        vals = [str(v) for v in (1, 2, 3)
                if (unit.item_min is None or v >= unit.item_min)
                and (unit.item_max is None or v <= unit.item_max)]
        items = ",".join(vals) if vals else None

    if star and items:
        suffix += f"_{star}_{items}"
    elif items:
        suffix += f"_.*_{items}"
    elif star:
        suffix += f"_{star}"

    val = f"{unit.unit_id}{suffix}"
    return f"!{val}" if negated else val


def _trait_to_metatft(trait, *, negated: bool = False) -> str:
    _load_trait_thresholds()
    thresholds = _TRAIT_THRESHOLDS.get(trait.trait_id, [])

    if thresholds:
        tiers = [idx for idx, req in enumerate(thresholds, start=1)
                 if (trait.min_units is None or req >= trait.min_units)
                 and (trait.max_units is None or req <= trait.max_units)]
        if not tiers and trait.min_units is not None:
            tiers = [len(thresholds)]
        if not tiers and trait.max_units is not None:
            tiers = [1]
        if not tiers:
            tiers = list(range(1, len(thresholds) + 1))
    else:
        tiers = [trait.min_units or 1]

    tokens = [f"{trait.trait_id}_{t}" for t in tiers]
    if negated:
        tokens[0] = f"!{tokens[0]}"
    return ",".join(tokens)


def expr_to_params(expr, *, negated: bool = False, sf_prefix: str | None = None) -> list[str]:
    """Recursively convert a FilterExpr tree into API filter params."""
    from tft_stat.filter_expr import And, Item, Not, Or, Trait, Unit

    if isinstance(expr, Unit):
        val = _unit_to_metatft(expr, negated=negated)
        if sf_prefix:
            key = urllib.parse.quote(f"{sf_prefix}[unit_tier_numitems_unique]")
            return [f"{key}={val}"]
        return [f"unit_tier_numitems_unique={val}"]

    if isinstance(expr, Trait):
        val = _trait_to_metatft(expr, negated=negated)
        if sf_prefix:
            key = urllib.parse.quote(f"{sf_prefix}[trait]")
            return [f"{key}={val}"]
        return [f"trait={val}"]

    if isinstance(expr, Item):
        return []

    if isinstance(expr, Not):
        return expr_to_params(expr.child, negated=not negated, sf_prefix=sf_prefix)

    if isinstance(expr, Or):
        children = expr.children
        if len(children) == 1:
            return expr_to_params(children[0], negated=negated, sf_prefix=sf_prefix)
        params = []
        prefix = sf_prefix or "sf[0]"
        for idx, child in enumerate(children):
            child_prefix = f"{prefix}[or][{idx}]"
            params.extend(expr_to_params(child, negated=negated, sf_prefix=child_prefix))
        return params

    if isinstance(expr, And):
        children = expr.children
        if len(children) == 1:
            return expr_to_params(children[0], negated=negated, sf_prefix=sf_prefix)
        params = []
        sf_idx = 0
        for child in children:
            if isinstance(child, (Unit, Trait)) or \
               (isinstance(child, Not) and isinstance(child.child, (Unit, Trait))):
                params.extend(expr_to_params(child, negated=negated))
            else:
                child_prefix = f"sf[{sf_idx}]"
                params.extend(expr_to_params(child, negated=negated, sf_prefix=child_prefix))
                sf_idx += 1
        return params

    return []


def build_filter_params(*, comp: str | None = None,
                        or_units: str | None = None, units: str | None = None,
                        traits: str | None = None,
                        exclude_units: str | None = None,
                        exclude_traits: str | None = None) -> list[str]:
    """Build API filter params from comp key and/or manual filter specs."""
    params = []

    if comp:
        from tft_stat.compositions import COMPOSITIONS
        comp_def = COMPOSITIONS.get(comp)
        if not comp_def:
            print(f"Error: unknown comp '{comp}'", file=sys.stderr)
            print(f"Available: {', '.join(sorted(COMPOSITIONS.keys()))}", file=sys.stderr)
            sys.exit(1)
        params.extend(expr_to_params(comp_def["filter"]))

    if or_units:
        specs = or_units.split(",")
        if len(specs) == 1:
            params.append(f"unit_tier_numitems_unique={parse_unit_spec(specs[0])}")
        else:
            for i, spec in enumerate(specs):
                key = urllib.parse.quote(f"sf[0][or][{i}][unit_tier_numitems_unique]")
                params.append(f"{key}={parse_unit_spec(spec)}")

    if units:
        for spec in units.split(","):
            params.append(f"unit_tier_numitems_unique={parse_unit_spec(spec)}")

    if traits:
        for spec in traits.split(","):
            params.append(f"trait={parse_trait_spec(spec)}")

    if exclude_units:
        for spec in exclude_units.split(","):
            params.append(f"unit_tier_numitems_unique=!{parse_unit_spec(spec)}")

    if exclude_traits:
        for spec in exclude_traits.split(","):
            params.append(f"trait=!{parse_trait_spec(spec)}")

    return params
