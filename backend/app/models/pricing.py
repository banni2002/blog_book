from sqlalchemy import Column, Integer, String, ARRAY
from app.database import Base

class Pricing(Base):
    __tablename__ = "pricings"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(String)
    description = Column(String)
    features = Column(ARRAY(String))
    popular = Column(Integer)