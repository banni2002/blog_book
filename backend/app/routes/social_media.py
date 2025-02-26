from fastapi import APIRouter, Depends, File, UploadFile, HTTPException, Form
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.social_media import SocialMediaResponse, SocialMediaCreate, SocialMediaUpdate
from app.crud.social_media import get_social_media, get_social_media_by_id, create_social_media, update_social_media, delete_social_media
import shutil
import os
from datetime import datetime

router = APIRouter(prefix="/social_media", tags=["Social Media"])


@router.get("/", response_model=list[SocialMediaResponse])
def read_social_media(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_social_media(db, skip, limit)

UPLOAD_DIR = "app/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/")
async def create_social(
    platform: str = Form(...),
    url: str = Form(...),
    file: UploadFile = File(None),
    db: Session = Depends(get_db)
):
    # Xử lý upload file
    image_url = ""
    if file:
        # Tạo tên file duy nhất
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_extension = os.path.splitext(file.filename)[1]
        new_filename = f"{timestamp}{file_extension}"
        
        # Lưu file
        file_path = os.path.join(UPLOAD_DIR, new_filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            
        # Tạo đường dẫn tương đối để lưu vào DB
        image_url = f"/uploads/{new_filename}"
    
    # Tạo object social media
    social_media_data = SocialMediaCreate(
        platform=platform,
        url=url,
        icon=image_url
    )
    
    # Lưu vào database
    return create_social_media(db, social_media_data)

@router.put("/{social_media_id}", response_model=SocialMediaResponse)
async def update_social(
    social_media_id: int,
    platform: str = Form(...),
    url: str = Form(None),
    file: UploadFile = File(None),
    db: Session = Depends(get_db)
):
    # Kiểm tra social media có tồn tại không
    existing_social = get_social_media_by_id(db, social_media_id)
    if not existing_social:
        raise HTTPException(status_code=404, detail="Social Media not found")

    image_url = existing_social.icon  # Giữ nguyên icon cũ nếu không có file mới

    if file:
        # Xóa file cũ nếu có
        if existing_social.icon:
            old_file_path = os.path.join(UPLOAD_DIR, os.path.basename(existing_social.icon))
            if os.path.exists(old_file_path):
                os.remove(old_file_path)

        # Lưu file mới
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_extension = os.path.splitext(file.filename)[1]
        new_filename = f"{timestamp}{file_extension}"
        file_path = os.path.join(UPLOAD_DIR, new_filename)
        
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        image_url = f"/uploads/{new_filename}"

    # Cập nhật thông tin mới
    social_media_data = SocialMediaUpdate(
        platform=platform,
        url=url,
        icon=image_url
    )
    updated_social = update_social_media(db, social_media_id, social_media_data)
    return updated_social

@router.delete("/{social_media_id}")
def delete_social(social_media_id: int, db: Session = Depends(get_db)):
    deleted_social = delete_social_media(db, social_media_id)
    if not deleted_social:
        raise HTTPException(status_code=404, detail="Social Media not found")
    return {"message": "Deleted successfully"}
