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


# --- Value token generation (ported from metatft_links.py) ---

def _value_tokens(minimum, maximum, *, allowed=(1, 2, 3)) -> list[str]:
    """Generate value tokens for a (min, max) range within allowed values.

    Returns e.g. ['2', '3'] for min=2, max=3 with allowed=(1,2,3).
    Returns [] when both min and max are None (unconstrained).
    """
    norm_min = int(minimum) if minimum is not None else None
    norm_max = int(maximum) if maximum is not None else None
    if norm_min is None and norm_max is None:
        return []
    if not allowed:
        return []
    if norm_min is not None and norm_max is not None and norm_min > norm_max:
        norm_min, norm_max = norm_max, norm_min

    candidates = [
        v for v in allowed
        if (norm_min is None or v >= norm_min)
        and (norm_max is None or v <= norm_max)
    ]

    if not candidates and norm_min is not None and norm_min > max(allowed):
        candidates = [max(allowed)]
    if not candidates and norm_max is not None and norm_max < min(allowed):
        candidates = [min(allowed)]
    if not candidates:
        return []
    return [str(v) for v in candidates]


# --- Expression tree → MetaTFT params ---

def _unit_to_metatft(unit, *, negated: bool = False) -> str:
    """Build unit value string for API params.

    Handles star_min/max and item_min/max via _value_tokens.
    Unconstrained units get '-1_.*' suffix (star wildcard) since the API's
    unit_tier_numitems_unique param requires explicit star wildcard.
    """
    star_tokens = _value_tokens(unit.star_min, unit.star_max)
    item_tokens = _value_tokens(unit.item_min, unit.item_max)

    parts = ["-1"]
    if star_tokens:
        parts.append(",".join(star_tokens))
    elif item_tokens:
        parts.append(".*")
    if item_tokens:
        parts.append(",".join(item_tokens))

    # When unconstrained (no star/item filters), add star wildcard
    # so the API matches all star levels, not just 1-star
    if not star_tokens and not item_tokens:
        parts.append(".*")

    val = f"{unit.unit_id}{'_'.join(parts)}"
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


# --- Item exclusion collection (ported from metatft_links.py) ---

def _collect_item_exclusions(expr, negated: bool = False):
    """Yield (carrier_id, item_id) pairs from ~Item(..., carrier_unit_id=...) nodes.

    Descends through And and Not; skips Or branches (ambiguous negation scope)
    and plain Item nodes without a carrier.
    """
    from tft_stat.filter_expr import And, Item, Not

    if expr is None:
        return
    if isinstance(expr, Not):
        yield from _collect_item_exclusions(expr.child, not negated)
        return
    if isinstance(expr, Item):
        if negated and expr.carrier_unit_id:
            yield (expr.carrier_unit_id, expr.item_id)
        return
    if isinstance(expr, And):
        for child in expr.children:
            yield from _collect_item_exclusions(child, negated)


def _item_exclusion_params(expr) -> list[str]:
    """Build unit_item exclusion params from ~Item(...) nodes in the expression tree.

    Generates item_holder=true, item_holder_unit=, and unit_item= params.
    """
    exclusions = list(_collect_item_exclusions(expr))
    if not exclusions:
        return []

    params: list[str] = []
    carriers: dict[str, str] = {}
    unit_item_params: list[str] = []

    for carrier_id, item_id in exclusions:
        base_suffix = "-1"
        carriers.setdefault(carrier_id, base_suffix)
        param = f"unit_item=!{carrier_id}{base_suffix}%26{item_id}-1"
        if param not in unit_item_params:
            unit_item_params.append(param)

    params.append("item_holder=true")
    for carrier, suffix in carriers.items():
        params.append(f"item_holder_unit={carrier}{suffix}")
    params.extend(unit_item_params)

    return params


# --- Recursive expression converter (core) ---

def _is_flat_eligible(child) -> bool:
    """Check if a child node can be rendered as a flat unit=/trait= parameter.

    Eligible: Unit, Trait, Not(Unit), Not(Trait).
    """
    from tft_stat.filter_expr import Not, Trait, Unit

    if isinstance(child, (Unit, Trait)):
        return True
    if isinstance(child, Not) and isinstance(child.child, (Unit, Trait)):
        return True
    return False


def _expr_to_params_core(expr, *, negated: bool = False, sf_prefix: str | None = None) -> list[str]:
    """Recursively convert a FilterExpr tree into API filter params (units/traits).

    Item nodes are skipped here; they are handled separately by _item_exclusion_params.
    """
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
        return _expr_to_params_core(expr.child, negated=not negated, sf_prefix=sf_prefix)

    if isinstance(expr, Or):
        children = expr.children
        if len(children) == 1:
            return _expr_to_params_core(children[0], negated=negated, sf_prefix=sf_prefix)
        params = []
        prefix = sf_prefix or "sf[0]"
        for idx, child in enumerate(children):
            child_prefix = f"{prefix}[or][{idx}]"
            params.extend(_expr_to_params_core(child, negated=negated, sf_prefix=child_prefix))
        return params

    if isinstance(expr, And):
        children = expr.children
        if len(children) == 1:
            return _expr_to_params_core(children[0], negated=negated, sf_prefix=sf_prefix)

        # When inside an sf[] context, all children use sf[] sub-indices
        if sf_prefix is not None:
            params = []
            for idx, child in enumerate(children):
                child_prefix = f"{sf_prefix}[and][{idx}]"
                params.extend(_expr_to_params_core(child, negated=negated, sf_prefix=child_prefix))
            return params

        # Top-level And: flat-eligible leaves go as flat params,
        # complex children use sf[] structured params
        params = []
        sf_idx = 0
        for child in children:
            if _is_flat_eligible(child):
                params.extend(_expr_to_params_core(child, negated=negated))
            else:
                child_prefix = f"sf[{sf_idx}]"
                params.extend(_expr_to_params_core(child, negated=negated, sf_prefix=child_prefix))
                sf_idx += 1
        return params

    return []


def expr_to_params(expr, *, negated: bool = False, sf_prefix: str | None = None) -> list[str]:
    """Convert a FilterExpr tree into API filter params.

    Handles Unit, Trait, And, Or, Not via recursive conversion, plus
    Item exclusions (~Item with carrier_unit_id) via separate collection.
    """
    params = _expr_to_params_core(expr, negated=negated, sf_prefix=sf_prefix)
    # Collect Item exclusions only at the top level (no sf_prefix)
    if sf_prefix is None:
        params.extend(_item_exclusion_params(expr))
    return params


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
