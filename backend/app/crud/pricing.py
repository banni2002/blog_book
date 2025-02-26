from sqlalchemy.orm import Session
from app.models.pricing import Pricing
from app.schemas.pricing import PricingCreate, PricingUpdate
from typing import List, Optional

def get_pricings(db: Session, skip: int = 0, limit: int = 100) -> List[Pricing]:
    return db.query(Pricing).offset(skip).limit(limit).all()

def create_pricing(db: Session, pricing: PricingCreate) -> Pricing:
    db_pricing = Pricing(**pricing.dict())
    db.add(db_pricing)
    db.commit()
    db.refresh(db_pricing)
    return db_pricing

def update_pricing(db: Session, pricing_id: int, pricing: PricingUpdate) -> Optional[Pricing]:
    db_pricing = db.query(Pricing).filter(Pricing.id == pricing_id).first()
    if not db_pricing:
        return None

    for key, value in pricing.dict(exclude_unset=True).items():
        setattr(db_pricing, key, value)

    db.commit()
    db.refresh(db_pricing)
    return db_pricing

def delete_pricing(db: Session, pricing_id: int) -> bool:
    db_pricing = db.query(Pricing).filter(Pricing.id == pricing_id).first()
    if not db_pricing:
        return False

    db.delete(db_pricing)
    db.commit()
    return True
