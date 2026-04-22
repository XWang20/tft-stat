"""Access tftable ground-truth data via SSH."""

from __future__ import annotations

import json
import subprocess

TFTABLE_HOST = "wangxing@DESKTOP-QTEB3KH"
TFTABLE_BASE = "/home/wangxing/project/tft_data/analysis/team_comp_sections"

_comp_cache: dict[str, dict] = {}


def _ssh(cmd: str, timeout: int = 15) -> str:
    result = subprocess.run(
        ["ssh", "-o", "ConnectTimeout=10", "-o", "StrictHostKeyChecking=no",
         TFTABLE_HOST, cmd],
        capture_output=True, text=True, timeout=timeout,
    )
    if result.returncode != 0:
        raise RuntimeError(f"SSH failed: {result.stderr.strip()}")
    return result.stdout


def list_comps() -> list[str]:
    out = _ssh(f"ls {TFTABLE_BASE}/compositions/")
    return [f.replace(".json", "") for f in out.strip().split("\n") if f.endswith(".json")]


def load_comp(comp_key: str) -> dict:
    if comp_key not in _comp_cache:
        out = _ssh(f"cat {TFTABLE_BASE}/compositions/{comp_key}.json")
        _comp_cache[comp_key] = json.loads(out)
    return _comp_cache[comp_key]


def get_comp_summary(comp_key: str) -> dict:
    return load_comp(comp_key).get("summary", {})


def get_comp_units(comp_key: str) -> list[str]:
    data = load_comp(comp_key)
    return [s["unit_id"] for s in data.get("priority_sections", []) if "unit_id" in s]


def get_unit_items(comp_key: str, unit_id: str) -> list[dict] | None:
    data = load_comp(comp_key)
    for section in data.get("priority_sections", []):
        if section.get("unit_id") == unit_id:
            matrix = section.get("baseline", {}).get("matrix", {})
            return matrix.get("items", [])
    return None


def get_unit_necessity(comp_key: str) -> list[dict]:
    """Get unit necessity rankings for a comp (from priority_sections meta)."""
    data = load_comp(comp_key)
    result = []
    for s in data.get("priority_sections", []):
        meta = s.get("meta", {})
        result.append({
            "unit_id": s["unit_id"],
            "necessity": meta.get("necessity", 0),
            "ic3_rate": meta.get("ic3_rate", 0),
            "ic3_rank": meta.get("ic3_rank", 0),
        })
    return result


def get_comp_strength() -> list[dict]:
    """Get all comp strength rankings."""
    out = _ssh(f"cat {TFTABLE_BASE}/comp_strength.json")
    data = json.loads(out)
    return data.get("compositions", data if isinstance(data, list) else [])


def get_metatft_link(comp_key: str) -> str | None:
    return load_comp(comp_key).get("metatft_link")
