from pydantic import BaseModel

class SocialMediaBase(BaseModel):
    platform: str
    url: str
    icon: str = ""

class SocialMediaCreate(SocialMediaBase):
    pass

class SocialMediaUpdate(SocialMediaBase):
    pass

# Thêm class Response
class SocialMediaResponse(SocialMediaBase):
    id: int
    
    class Config:
        from_attributes = True  # cho phép chuyển đổi từ ORM model sang Pydantic model