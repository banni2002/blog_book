from pydantic import BaseModel
from typing import List

class PricingBase(BaseModel):
    name: str
    price: str
    description: str
    features: List[str]  # Đảm bảo đây là danh sách
    popular: int

class PricingCreate(PricingBase):
    pass

class PricingUpdate(BaseModel):
    name: str | None = None
    price: str | None = None
    description: str | None = None
    features: List[str] | None = None
    popular: int | None = None

class Pricing(PricingBase):
    id: int

    class Config:
        from_attribute = True
