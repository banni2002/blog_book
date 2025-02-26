from sqlalchemy.orm import Session
from ..models import Menu
from ..schemas.menu import MenuCreate, MenuUpdate

# Lấy tất cả menu
def get_menu_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Menu).offset(skip).limit(limit).all()

# Lấy menu theo ID
def get_menu_item_by_id(db: Session, menu_id: int):
    return db.query(Menu).filter(Menu.id == menu_id).first()

# Thêm menu
def create_menu_item(db: Session, menu_item: MenuCreate):
    db_menu = Menu(label=menu_item.label, href=menu_item.href)
    db.add(db_menu)
    db.commit()
    db.refresh(db_menu)
    return db_menu

# Cập nhật menu
def update_menu_item(db: Session, menu_id: int, menu_data: MenuUpdate):
    menu_item = db.query(Menu).filter(Menu.id == menu_id).first()
    if menu_item:
        menu_item.label = menu_data.label
        menu_item.href = menu_data.href
        db.commit()
        db.refresh(menu_item)
        return menu_item
    return None

# Xóa menu
def delete_menu_item(db: Session, menu_id: int):
    menu_item = db.query(Menu).filter(Menu.id == menu_id).first()
    if menu_item:
        db.delete(menu_item)
        db.commit()
        return True
    return False
