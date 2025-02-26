from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.management import ManagementResponse, ManagementUpdate
from app.crud.management import get_management, update_management

router = APIRouter(prefix="/management", tags=["Management"])

@router.get("/", response_model=ManagementResponse)
def read_management(db: Session = Depends(get_db)):
    management = get_management(db)
    if not management:
        raise HTTPException(status_code=404, detail="Management data not found")
    return management

@router.put("/", response_model=ManagementResponse)
def update_management_data(data: ManagementUpdate, db: Session = Depends(get_db)):
    return update_management(db, data)
