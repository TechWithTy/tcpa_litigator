from typing import Any, Dict, List, TypedDict


class LookupResult(TypedDict, total=False):
    phone: str
    listed: bool
    categories: List[str]
    matched_entities: List[str]
    notes: str


class LookupResponse(TypedDict):
    success: bool
    result: LookupResult


class ScrubItem(TypedDict, total=False):
    phone: str
    listed: bool
    reason: str


class ScrubResponse(TypedDict):
    success: bool
    results: List[ScrubItem]