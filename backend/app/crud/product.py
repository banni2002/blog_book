import json
from sqlalchemy.orm import Session
from ..models.product import Product
from ..schemas.product import ProductCreate, ProductUpdate
from typing import List
from slugify import slugify

def get_products(db: Session):
    products = db.query(Product).all()
    
    # Chuyển đổi nếu cần thiết
    for product in products:
        if isinstance(product.gallery_images, str):
            product.gallery_images = json.loads(product.gallery_images)
        if isinstance(product.look_inside_images, str):
            product.look_inside_images = json.loads(product.look_inside_images)
        if product.category_id is None:
            product.category_id = 0  # Đặt giá trị mặc định cho category_id

    return products


def get_product_by_id(db: Session, product_id: int) -> Product:
    return db.query(Product).filter(Product.id == product_id).first()

def count_products(db: Session) -> int:
    return db.query(Product).count()

def create_product(db: Session, product: ProductCreate) -> Product:
    db_product = Product(
        name=product.name,
        slug=slugify(product.name),
        short_description=product.short_description,
        content=product.content,
        author=product.author,
        feature_image=product.feature_image,
        gallery_images=product.gallery_images,
        look_inside_images=product.look_inside_images,
        price=product.price,
        category_id=product.category_id
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db: Session, product_id: int, product_update: ProductUpdate) -> Product:
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product:
        for key, value in product_update.dict(exclude_unset=True).items():
            setattr(db_product, key, value)
        db.commit()
        db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int) -> bool:
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return True
    return False
