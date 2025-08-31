import os

TCPA_LITIGATOR_API_BASE_URL = os.getenv("TCPA_LITIGATOR_API_BASE_URL", "https://tcpalitigatorlist.com/api").rstrip("/")
TCPA_LITIGATOR_API_KEY = os.getenv("TCPA_LITIGATOR_API_KEY", "")
TCPA_LITIGATOR_API_TIMEOUT = int(os.getenv("TCPA_LITIGATOR_API_TIMEOUT", "15"))
TCPA_LITIGATOR_AUTH_HEADER = os.getenv("TCPA_LITIGATOR_AUTH_HEADER", "X-API-KEY")

# Endpoint paths kept configurable in case provider changes
TCPA_LITIGATOR_LOOKUP_PATH = os.getenv("TCPA_LITIGATOR_LOOKUP_PATH", "v1/lookup").strip("/")
TCPA_LITIGATOR_SCRUB_PATH = os.getenv("TCPA_LITIGATOR_SCRUB_PATH", "v1/scrub").strip("/")