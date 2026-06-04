"""Boolean expression tree for composition filters.

Leaf nodes: Unit, Trait, Item
Branch nodes: And, Or, Not
Compose with &, |, ~ operators.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Union


class _ExprOps:
    def __and__(self, other: FilterExpr) -> And:
        left = self.children if isinstance(self, And) else (self,)
        right = other.children if isinstance(other, And) else (other,)
        return And(children=left + right)

    def __or__(self, other: FilterExpr) -> Or:
        left = self.children if isinstance(self, Or) else (self,)
        right = other.children if isinstance(other, Or) else (other,)
        return Or(children=left + right)

    def __invert__(self) -> Not:
        return Not(child=self)


@dataclass(frozen=True)
class Unit(_ExprOps):
    unit_id: str
    star_min: int | None = None
    star_max: int | None = None
    item_min: float | None = None
    item_max: float | None = None
    count: int = 1


@dataclass(frozen=True)
class Trait(_ExprOps):
    trait_id: str
    min_units: int | None = None
    max_units: int | None = None


@dataclass(frozen=True)
class Item(_ExprOps):
    item_id: str
    carrier_unit_id: str | None = None


@dataclass(frozen=True)
class And(_ExprOps):
    children: tuple[FilterExpr, ...] = ()


@dataclass(frozen=True)
class Or(_ExprOps):
    children: tuple[FilterExpr, ...] = ()


@dataclass(frozen=True)
class Not(_ExprOps):
    child: FilterExpr = None


FilterExpr = Union[Unit, Trait, Item, And, Or, Not]


def collect_unit_ids(expr: FilterExpr) -> list[str]:
    """Collect ``unit_id`` values from positive ``Unit`` leaves.

    Nodes inside ``Not(...)`` are skipped — they represent exclusions and
    should not contribute to *core_units*.
    """
    result: list[str] = []
    _collect_unit_ids_inner(expr, result, negated=False)
    return result


def _collect_unit_ids_inner(expr: FilterExpr, out: list[str], *, negated: bool) -> None:
    if isinstance(expr, Unit):
        if not negated and expr.unit_id not in out:
            out.append(expr.unit_id)
    elif isinstance(expr, (Trait, Item)):
        pass
    elif isinstance(expr, And):
        for child in expr.children:
            _collect_unit_ids_inner(child, out, negated=negated)
    elif isinstance(expr, Or):
        for child in expr.children:
            _collect_unit_ids_inner(child, out, negated=negated)
    elif isinstance(expr, Not):
        _collect_unit_ids_inner(expr.child, out, negated=True)
