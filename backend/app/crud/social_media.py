from sqlalchemy.orm import Session
from app.models.social_media import SocialMedia
from app.schemas.social_media import SocialMediaCreate, SocialMediaUpdate

def get_social_media(db: Session, skip: int = 0, limit: int = 10):
    return db.query(SocialMedia).offset(skip).limit(limit).all()

def get_social_media_by_id(db: Session, social_media_id: int):
    return db.query(SocialMedia).filter(SocialMedia.id == social_media_id).first()

def create_social_media(db: Session, social_media: SocialMediaCreate):
    db_social_media = SocialMedia(**social_media.dict())
    db.add(db_social_media)
    db.commit()
    db.refresh(db_social_media)
    return db_social_media

def update_social_media(db: Session, social_media_id: int, social_media: SocialMediaUpdate):
    db_social = db.query(SocialMedia).filter(SocialMedia.id == social_media_id).first()
    if db_social:
        for key, value in social_media.dict(exclude_unset=True).items():
            setattr(db_social, key, value)
        db.commit()
        db.refresh(db_social)
    return db_social

def delete_social_media(db: Session, social_media_id: int):
    db_social = db.query(SocialMedia).filter(SocialMedia.id == social_media_id).first()
    if db_social:
        db.delete(db_social)
        db.commit()
    return db_social
