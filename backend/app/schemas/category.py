from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Category schemas
class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

__all__ = ['CategoryBase', 'CategoryCreate', 'Category']
