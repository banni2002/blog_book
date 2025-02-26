from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class CatProductBase(BaseModel):
    name: str
    description: Optional[str] = None

class CatProductCreate(CatProductBase):
    pass

class CatProductResponse(CatProductBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attribute = True
