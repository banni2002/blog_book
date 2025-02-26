from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from ..crud.cat_product import create_cat_product as crud_create_cat_product, get_cat_products, get_cat_product_by_id, update_cat_product as crud_update_cat_product, delete_cat_product as crud_delete_cat_product
from ..schemas.cat_product import CatProductCreate, CatProductResponse
from ..database import get_db

router = APIRouter(prefix="/cat_products", tags=["Category-Product Relations"])

@router.get("/", response_model=List[CatProductResponse])
def read_cat_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    cat_products = get_cat_products(db, skip=skip, limit=limit)
    return cat_products

@router.get("/{category_id}", response_model=CatProductResponse)
def read_cat_product(category_id: int, db: Session = Depends(get_db)):
    db_cat_product = get_cat_product_by_id(db, category_id=category_id)
    if db_cat_product is None:
        raise HTTPException(status_code=404, detail="CatProduct not found")
    return db_cat_product

@router.post("/", response_model=CatProductResponse)
def create_cat_product(cat_product: CatProductCreate, db: Session = Depends(get_db)):
    return crud_create_cat_product(db=db, category=cat_product)

@router.put("/{category_id}", response_model=CatProductResponse)
def update_cat_product(category_id: int, cat_product: CatProductCreate, db: Session = Depends(get_db)):
    db_cat_product = get_cat_product_by_id(db, category_id=category_id)
    if db_cat_product is None:
        raise HTTPException(status_code=404, detail="CatProduct not found")
    return crud_update_cat_product(db=db, category_id=category_id, cat_product=cat_product)

@router.delete("/{category_id}", response_model=CatProductResponse)
def delete_cat_product(category_id: int, db: Session = Depends(get_db)):
    success = crud_delete_cat_product(db=db, category_id=category_id)
    if not success:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"message": "Category deleted successfully"}