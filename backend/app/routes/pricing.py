from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.pricing import Pricing, PricingCreate, PricingUpdate
from app.crud.pricing import get_pricings, create_pricing, update_pricing, delete_pricing
from typing import List

router = APIRouter()

@router.get("/pricings", response_model=List[Pricing])
def read_pricings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    pricings = get_pricings(db, skip=skip, limit=limit)
    return pricings

@router.post("/pricings", response_model=Pricing)
def create_new_pricing(pricing: PricingCreate, db: Session = Depends(get_db)):
    return create_pricing(db=db, pricing=pricing)

@router.put("/pricings/{pricing_id}", response_model=Pricing)
def update_existing_pricing(pricing_id: int, pricing: PricingUpdate, db: Session = Depends(get_db)):
    updated_pricing = update_pricing(db=db, pricing_id=pricing_id, pricing=pricing)
    if not updated_pricing:
        raise HTTPException(status_code=404, detail="Bảng giá không tồn tại")
    return updated_pricing

@router.delete("/pricings/{pricing_id}")
def delete_existing_pricing(pricing_id: int, db: Session = Depends(get_db)):
    success = delete_pricing(db=db, pricing_id=pricing_id)
    if not success:
        raise HTTPException(status_code=404, detail="Bảng giá không tồn tại")
    return {"message": "Bảng giá đã được xóa thành công"}
