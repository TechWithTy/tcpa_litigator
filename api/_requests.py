from typing import List
from pydantic import BaseModel, Field


class LookupRequest(BaseModel):
    phone: str = Field(..., description="E.164 or national format phone number")


class ScrubRequest(BaseModel):
    phones: List[str] = Field(..., description="List of phone numbers to scrub")