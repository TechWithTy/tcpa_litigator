
# TCPA Litigator
Target: [backend/app/core/third_party_integrations/tcpa_litigator/README.md](cci:7://file:///c:/Users/tyriq.DESKTOP-U7P592K/OneDrive/Documents/Github-New/deal-scale-backend-autoscaling/backend/app/core/third_party_integrations/tcpa_litigator/README.md:0:0-0:0)

```markdown
# TCPA Litigator

Lookup and batch scrub phone numbers against TCPA litigator lists.

## Environment
- TCPA_LITIGATOR_API_BASE_URL=[https://tcpalitigatorlist.com/api](https://tcpalitigatorlist.com/api)
- TCPA_LITIGATOR_API_KEY=<your_key>
- TCPA_LITIGATOR_API_TIMEOUT=15
- TCPA_LITIGATOR_AUTH_HEADER=X-API-KEY
- TCPA_LITIGATOR_LOOKUP_PATH=v1/lookup
- TCPA_LITIGATOR_SCRUB_PATH=v1/scrub

## Endpoints (served by this app)
Base prefix: `/tcpa-litigator`
- GET `/health`
- POST `/lookup`
  - body: `{"phone": "+15551234567"}`
- POST `/scrub`
  - body: `{"phones": ["+15551234567", "+15557654321"]}`

## Quickstart (via this app)
Health:
```bash
curl -sS "http://localhost:8000/tcpa-litigator/health"