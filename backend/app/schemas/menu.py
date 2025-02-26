from pydantic import BaseModel

class Menu(BaseModel):
    id: int
    label: str
    href: str

class MenuCreate(BaseModel):
    label: str
    href: str

class MenuUpdate(BaseModel):
    label: str
    href: str

class MenuOut(MenuCreate):
    id: int

    class Config:
        from_attributes = True

__all__ = ['Menu', 'MenuCreate', 'MenuUpdate', 'MenuOut']