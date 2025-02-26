from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Blog schemas
class BlogBase(BaseModel):
    title: str
    slug: str
    meta_description: Optional[str] = None
    content: str
    image_feature: Optional[str] = None
    category_id: int
    author_name: Optional[str] = None

class BlogCreate(BlogBase):
    pass

class Blog(BlogBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

__all__ = ['BlogBase', 'BlogCreate', 'Blog']
