from typing import Any, Dict, List

from app.core.third_party_integrations.tcpa_litigator import config
from app.core.third_party_integrations.tcpa_litigator.api._base import TCPALitigatorBase


class TCPALitigatorClient(TCPALitigatorBase):
    """Client for TCPA Litigator List API: lookup and scrub endpoints."""

    def lookup(self, phone: str) -> Dict[str, Any]:
        path = config.TCPA_LITIGATOR_LOOKUP_PATH
        payload = {"phone": phone}
        return self.post(path, json=payload)

    def scrub(self, phones: List[str]) -> Dict[str, Any]:
        path = config.TCPA_LITIGATOR_SCRUB_PATH
        payload = {"phones": phones}
        return self.post(path, json=payload)