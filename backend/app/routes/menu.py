from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..schemas.menu import Menu, MenuCreate, MenuUpdate
from ..crud.menu import get_menu_items, get_menu_item_by_id, create_menu_item, update_menu_item, delete_menu_item

router = APIRouter()

# Lấy danh sách menu (có phân trang)
@router.get("/menu/", response_model=List[Menu])
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_menu_items(db, skip=skip, limit=limit)

# Thêm menu mới
@router.post("/menu/", response_model=Menu)
def create_menu_route(menu_item: MenuCreate, db: Session = Depends(get_db)):
    return create_menu_item(db, menu_item)

# Sửa menu
@router.put("/menu/{menu_id}", response_model=Menu)
def update_menu_route(menu_id: int, menu_item: MenuUpdate, db: Session = Depends(get_db)):
    db_menu = get_menu_item_by_id(db, menu_id)
    if db_menu is None:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return update_menu_item(db, menu_id, menu_item)

# Xóa menu
@router.delete("/menu/{menu_id}", response_model=bool)
def delete_menu_route(menu_id: int, db: Session = Depends(get_db)):
    success = delete_menu_item(db, menu_id)
    if not success:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return success
