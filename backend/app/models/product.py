from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Numeric, ARRAY
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    slug = Column(String(255), nullable=False)
    short_description = Column(String, nullable=True)
    content = Column(String, nullable=False)
    author = Column(String(255), nullable=False)
    feature_image = Column(String, nullable=True)
    gallery_images = Column(ARRAY(String), nullable=True) 
    look_inside_images = Column(ARRAY(String), nullable=True)
    price = Column(Numeric(10, 2), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    category_id = Column(Integer, ForeignKey("cat_products.id"), nullable=False)
    category = relationship("CatProduct", back_populates="products")