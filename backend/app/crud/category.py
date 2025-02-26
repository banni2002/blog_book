from sqlalchemy.orm import Session
from ..models import Category as CategoryModel
from ..schemas.category import CategoryCreate, Category


# Lấy danh sách category
def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(CategoryModel).offset(skip).limit(limit).all()

# Lấy category theo ID
def get_category_by_id(db: Session, category_id: int):
    return db.query(CategoryModel).filter(CategoryModel.id == category_id).first()

# Tạo mới category
def create_category(db: Session, category: CategoryCreate):
    db_category = CategoryModel(name=category.name, description=category.description)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

# Cập nhật category
def update_category(db: Session, category_id: int, category: CategoryCreate):
    db_category = get_category_by_id(db, category_id)
    if db_category is None:
        return None
    db_category.name = category.name
    db_category.description = category.description
    db.commit()
    db.refresh(db_category)
    return db_category

# Xóa category
def delete_category(db: Session, category_id: int) -> bool:
    db_category = get_category_by_id(db, category_id)
    if db_category is None:
        return False
    db.delete(db_category)
    db.commit()
    return True