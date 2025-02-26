from sqlalchemy import Column, Integer, String
from app.database import Base

class Management(Base):
    __tablename__ = "management"

    id = Column(Integer, primary_key=True, index=True)
    phone = Column(String, nullable=True)
    email = Column(String, nullable=True)
    address = Column(String, nullable=True)