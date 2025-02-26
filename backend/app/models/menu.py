from sqlalchemy import Column, Integer, String
from ..database import Base

class Menu(Base):
    __tablename__ = "menu"

    id = Column(Integer, primary_key=True, index=True)
    label = Column(String, nullable=False)
    href = Column(String, unique=True, nullable=False)
