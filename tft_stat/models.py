"""Dataclasses that describe compositions and filter configurations."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Sequence

if TYPE_CHECKING:
    from tft_stat.filter_expr import FilterExpr


@dataclass(slots=True)
class UnitFilterConfig:
    unit_id: str
    star_min: int | None = None
    star_max: int | None = None
    item_min: float | None = None
    item_max: float | None = None
    count: int = 1


@dataclass(slots=True)
class TraitFilterConfig:
    trait_id: str
    min_units: int | None = None
    max_units: int | None = None


@dataclass(slots=True)
class ItemFilterConfig:
    item_id: str
    carrier_unit_id: str | None = None


@dataclass(slots=True)
class CompositionDefinition:
    key: str
    display_name_cn: str
    display_name_en: str
    carry_unit_id: str | None = None
    carry_unit_cost: float | None = None
    exclude_tank_items_for_carriers: list[str] = field(default_factory=list)
    exclude_dmg_items_for_carriers: list[str] = field(default_factory=list)
    exclude_bruiser_items_for_carriers: list[str] = field(default_factory=list)
    filter: FilterExpr | None = None
    core_comp_rank: int = 1  # Which rank of core_comp to use (1 = most common, 2 = second most common, etc.)

    @property
    def core_units(self) -> list[str]:
        if self.filter is not None:
            from tft_stat.filter_expr import collect_unit_ids
            return collect_unit_ids(self.filter)
        return []

    @property
    def display_name(self) -> str:
        """Backwards compatible accessor for code that still expects a single display name."""
        return self.display_name_cn

    def title_for_locale(self, locale: str) -> str:
        if locale == "zh_cn":
            return self.display_name_cn
        if locale == "en_us":
            return self.display_name_en
        return self.display_name_en or self.display_name_cn or self.key


CompositionDefinitions = Sequence[CompositionDefinition]

__all__ = [
    "CompositionDefinition",
    "CompositionDefinitions",
    "ItemFilterConfig",
    "TraitFilterConfig",
    "UnitFilterConfig",
]
