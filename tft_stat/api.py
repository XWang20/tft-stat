"""MetaTFT Explorer API client."""

from __future__ import annotations

import json
import urllib.request

API_BASE = "https://api-hc.metatft.com/tft-explorer-api"

DEFAULT_PARAMS = {
    "formatnoarray": "true",
    "compact": "true",
    "queue": "1100",
    "patch": "current",
    "days": "3",
    "rank": "CHALLENGER,DIAMOND,EMERALD,GRANDMASTER,MASTER,PLATINUM",
    "permit_filter_adjustment": "true",
}


def query(endpoint: str, filter_params: list[str], extra_params: dict | None = None) -> dict:
    base_params = dict(DEFAULT_PARAMS)
    if extra_params:
        base_params.update(extra_params)

    qs = "&".join(f"{k}={v}" for k, v in base_params.items())
    if filter_params:
        qs += "&" + "&".join(filter_params)

    url = f"{API_BASE}/{endpoint}?{qs}"

    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0",
        "Origin": "https://www.metatft.com",
        "Referer": "https://www.metatft.com/",
    })

    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read())
