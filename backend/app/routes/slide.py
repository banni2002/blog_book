from fastapi import APIRouter, Depends, File, UploadFile, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.crud.slide import create, get_slides, update, delete
from app.schemas.slide import SlideResponse, SlideUpdate
from app.database import get_db

router = APIRouter(prefix="/slides", tags=["slides"])

@router.post("", response_model=SlideResponse)
async def create_slide(
    title: str,
    order: int = 0,
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    return await create(db, title, file, order)

@router.get("", response_model=List[SlideResponse])
def get_all_slides(active_only: bool = False, db: Session = Depends(get_db)):
    return get_slides(db, active_only)

@router.put("/{slide_id}", response_model=SlideResponse)
def update_slide(slide_id: int, slide_update: SlideUpdate, db: Session = Depends(get_db)):
    slide = update(db, slide_id, slide_update)
    if not slide:
        raise HTTPException(status_code=404, detail="Slide not found")
    return slide

@router.delete("/{slide_id}")
def delete_slide(slide_id: int, db: Session = Depends(get_db)):
    success = delete(db, slide_id)
    if not success:
        raise HTTPException(status_code=404, detail="Slide not found")
    return {"message": "Slide deleted successfully"}