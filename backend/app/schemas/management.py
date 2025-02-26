from pydantic import BaseModel, EmailStr
from typing import Optional

class ManagementBase(BaseModel):
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    address: Optional[str] = None

class ManagementResponse(ManagementBase):
    id: int

    class Config:
        from_attributes = True

class ManagementUpdate(ManagementBase):
    pass
