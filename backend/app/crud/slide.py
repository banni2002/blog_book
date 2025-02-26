from sqlalchemy.orm import Session
from fastapi import UploadFile
import os
from datetime import datetime
from ..models.slide import Slide
from ..schemas.slide import SlideUpdate

async def create(db: Session, title: str, file: UploadFile, order: int = 0):
    # Lưu file
    UPLOAD_DIR = "uploads/slides"
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)
        
    file_extension = os.path.splitext(file.filename)[1]
    file_name = f"{datetime.now().timestamp()}{file_extension}"
    file_path = os.path.join(UPLOAD_DIR, file_name)
    
    with open(file_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)
    
    # Tạo slide trong database
    db_slide = Slide(
        title=title,
        image_url=f"/uploads/slides/{file_name}",
        order=order
    )
    db.add(db_slide)
    db.commit()
    db.refresh(db_slide)
    return db_slide

def get_slides(db: Session, active_only: bool = False):
    query = db.query(Slide)
    if active_only:
        query = query.filter(Slide.active == True)
    return query.order_by(Slide.order).all()

def update(db: Session, slide_id: int, slide_update: SlideUpdate):
    db_slide = db.query(Slide).filter(Slide.id == slide_id).first()
    if db_slide:
        update_data = slide_update.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_slide, key, value)
        db.commit()
        db.refresh(db_slide)
    return db_slide

def delete(db: Session, slide_id: int):
    db_slide = db.query(Slide).filter(Slide.id == slide_id).first()
    if db_slide:
        # Xóa file ảnh
        image_path = os.path.join(os.getcwd(), db_slide.image_url.lstrip("/"))
        if os.path.exists(image_path):
            os.remove(image_path)
        # Xóa record trong database
        db.delete(db_slide)
        db.commit()
        return True
    return False