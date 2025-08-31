import requests
from requests import Session
from typing import Any, Dict, Optional

from app.core.third_party_integrations.tcpa_litigator import config


class TCPALitigatorBase:
    """Reusable HTTP base for TCPA Litigator API."""

    def __init__(self, api_key: Optional[str] = None):
        self.session: Session = requests.Session()
        self.base_url: str = config.TCPA_LITIGATOR_API_BASE_URL
        self.timeout: int = config.TCPA_LITIGATOR_API_TIMEOUT
        self.api_key: str = api_key or config.TCPA_LITIGATOR_API_KEY
        self.auth_header_name: str = config.TCPA_LITIGATOR_AUTH_HEADER

    def _headers(self, extra: Optional[Dict[str, str]] = None) -> Dict[str, str]:
        headers: Dict[str, str] = {"Accept": "application/json", "Content-Type": "application/json"}
        if self.api_key:
            headers[self.auth_header_name] = self.api_key
        if extra:
            headers.update(extra)
        return headers

    def _url(self, path: str) -> str:
        return f"{self.base_url}/{path.lstrip('/')}"

    def get(self, path: str, *, params: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None):
        resp = self.session.get(self._url(path), params=params or {}, headers=self._headers(headers), timeout=self.timeout)
        resp.raise_for_status()
        return resp.json()

    def post(self, path: str, *, json: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None):
        resp = self.session.post(self._url(path), json=json or {}, headers=self._headers(headers), timeout=self.timeout)
        resp.raise_for_status()
        return resp.json()