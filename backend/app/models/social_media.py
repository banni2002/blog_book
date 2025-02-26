from sqlalchemy import Column, Integer, String
from app.database import Base

class SocialMedia(Base):
    __tablename__ = "social_media"

    id = Column(Integer, primary_key=True, index=True)
    platform = Column(String, nullable=False)
    icon = Column(String, nullable=False)
    url = Column(String, nullable=True)
