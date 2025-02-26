from pydantic import BaseModel
from typing import Optional, List

class ProductBase(BaseModel):
    name: str
    slug: Optional[str] = None 
    short_description: Optional[str] = None
    content: str
    author: str
    feature_image: Optional[str] = None
    gallery_images: Optional[List[str]] = []
    look_inside_images: Optional[List[str]] = []
    price: float
    category_id: int

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    name: Optional[str] = None
    content: Optional[str] = None
    author: Optional[str] = None
    price: Optional[float] = None
    category_id: Optional[int] = None

class ProductResponse(ProductBase):
    id: int
    category_id: int 
    
    class Config:
        from_attribute = True
