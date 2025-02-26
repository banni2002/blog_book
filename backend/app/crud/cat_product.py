from sqlalchemy.orm import Session
from ..models import CatProduct 
from ..schemas.cat_product import CatProductCreate

# Lấy danh sách category
def get_cat_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(CatProduct).offset(skip).limit(limit).all()

# Lấy category theo ID
def get_cat_product_by_id(db: Session, category_id: int):
    return db.query(CatProduct).filter(CatProduct.id == category_id).first()

# Tạo mới category
def create_cat_product(db: Session, category: CatProductCreate):
    db_category = CatProduct(name=category.name, description=category.description)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

# Cập nhật category
def update_cat_product(db: Session, category_id: int, cat_product: CatProductCreate):
    db_cat_product = get_cat_product_by_id(db, category_id)
    if db_cat_product is None:
        return None
    db_cat_product.name = cat_product.name
    db_cat_product.description = cat_product.description
    db.commit()
    db.refresh(db_cat_product)
    return db_cat_product

# Xóa category
def delete_cat_product(db: Session, category_id: int):
    db_cat_product = get_cat_product_by_id(db, category_id)
    if db_cat_product is None:
        return False
    db.delete(db_cat_product)
    db.commit()
    return True