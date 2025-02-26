from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class SlideBase(BaseModel):
    title: str
    order: Optional[int] = 0
    active: Optional[bool] = True

class SlideCreate(SlideBase):
    pass

class SlideUpdate(BaseModel):
    title: Optional[str] = None
    order: Optional[int] = None
    active: Optional[bool] = None

class SlideResponse(SlideBase):
    id: int
    image_url: str
    created_at: datetime

    class Config:
        from_attribute = True