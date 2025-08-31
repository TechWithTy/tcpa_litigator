import logging
from typing import Dict

from fastapi import APIRouter

from app.core.third_party_integrations.tcpa_litigator.client import TCPALitigatorClient
from app.core.third_party_integrations.tcpa_litigator.api._requests import LookupRequest, ScrubRequest

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/tcpa-litigator", tags=["tcpa_litigator"])


@router.get("/health")
async def health() -> Dict:
    client = TCPALitigatorClient()
    return {
        "healthy": bool(client.base_url),
        "base_url": client.base_url,
        "has_api_key": bool(client.api_key),
    }


@router.post("/lookup")
async def lookup(req: LookupRequest):
    client = TCPALitigatorClient()
    return client.lookup(req.phone)


@router.post("/scrub")
async def scrub(req: ScrubRequest):
    client = TCPALitigatorClient()
    return client.scrub(req.phones)
