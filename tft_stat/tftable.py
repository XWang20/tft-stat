"""Access tftable ground-truth data via SSH."""

from __future__ import annotations

import json
import subprocess

TFTABLE_HOST = "wangxing@DESKTOP-QTEB3KH"
TFTABLE_BASE = "/home/wangxing/project/tft_data/analysis/team_comp_sections"


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
    out = _ssh(f"cat {TFTABLE_BASE}/compositions/{comp_key}.json")
    return json.loads(out)


def get_unit_items(comp_key: str, unit_id: str) -> list[dict] | None:
    """Get tftable item necessity ranking for a unit in a comp."""
    data = load_comp(comp_key)
    for section in data.get("priority_sections", []):
        if section.get("unit_id") == unit_id:
            matrix = section.get("baseline", {}).get("matrix", {})
            return matrix.get("items", [])
    return None


def get_comp_summary(comp_key: str) -> dict:
    data = load_comp(comp_key)
    return data.get("summary", {})


def get_comp_units(comp_key: str) -> list[str]:
    """List all units with priority sections in a comp."""
    data = load_comp(comp_key)
    return [s["unit_id"] for s in data.get("priority_sections", []) if "unit_id" in s]
