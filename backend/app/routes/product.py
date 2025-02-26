from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..crud import product as crud_product
from ..schemas.product import ProductCreate, ProductUpdate, ProductResponse
from ..database import get_db
from typing import List

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/", response_model=List[ProductResponse])
def read_products(db: Session = Depends(get_db)):
    return crud_product.get_products(db)

@router.get("/count", response_model=dict)
def count_products(db: Session = Depends(get_db)):
    total = crud_product.count_products(db)
    return {"total": total}

@router.get("/{product_id}", response_model=ProductResponse)
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = crud_product.get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return crud_product.create_product(db, product)

@router.put("/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, product_update: ProductUpdate, db: Session = Depends(get_db)):
    product = crud_product.update_product(db, product_id, product_update)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    if not crud_product.delete_product(db, product_id):
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}
