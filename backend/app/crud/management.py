from sqlalchemy.orm import Session
from app.models.management import Management
from app.schemas.management import ManagementBase

def get_management(db: Session):
    return db.query(Management).first()

def update_management(db: Session, data: ManagementBase):
    management = get_management(db)
    if not management:
        management = Management(**data.dict())
        db.add(management)
    else:
        for key, value in data.dict(exclude_unset=True).items():
            setattr(management, key, value)
    db.commit()
    db.refresh(management)
    return management