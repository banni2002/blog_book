from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..schemas.category import Category, CategoryCreate
from ..crud.category import get_categories, get_category_by_id, create_category, update_category, delete_category

router = APIRouter()

# Lấy danh sách category
@router.get("/categories/", response_model=List[Category])
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_categories(db, skip=skip, limit=limit)

# Tạo mới category
@router.post("/categories/", response_model=Category)
def create_category_route(category: CategoryCreate, db: Session = Depends(get_db)):
    return create_category(db=db, category=category)

# Cập nhật category
@router.put("/categories/{category_id}", response_model=Category)
def update_category_route(category_id: int, category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = get_category_by_id(db, category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return update_category(db=db, category_id=category_id, category=category)

# Xóa category
@router.delete("/categories/{category_id}", response_model=bool)
def delete_category_route(category_id: int, db: Session = Depends(get_db)):
    success = delete_category(db=db, category_id=category_id)
    if not success:
        raise HTTPException(status_code=404, detail="Category not found")
    return success