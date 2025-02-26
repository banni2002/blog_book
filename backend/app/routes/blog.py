from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..schemas.blog import Blog, BlogCreate
from ..crud.blog import (
    get_blogs, get_blog_by_id, create_blog, update_blog, delete_blog, count_blogs as count_blogs_crud
)

router = APIRouter()

@router.get("/blogs/", response_model=List[Blog])
def read_blogs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_blogs(db, skip=skip, limit=limit)

@router.get("/blogs/count", response_model=dict)
def count_blogs(db: Session = Depends(get_db)):
    total = count_blogs_crud(db)
    return {"total": total}

@router.post("/blogs/", response_model=Blog)
def create_blog_route(blog: BlogCreate, db: Session = Depends(get_db)):
    return create_blog(db=db, blog=blog)

@router.put("/blogs/{blog_id}", response_model=Blog)
def update_blog_route(blog_id: int, blog: BlogCreate, db: Session = Depends(get_db)):
    db_blog = get_blog_by_id(db, blog_id)
    if db_blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")  

    return update_blog(db=db, blog_id=blog_id, blog=blog)

@router.patch("/blogs/{blog_id}", response_model=Blog)
def partial_update_blog(blog_id: int, blog: BlogCreate, db: Session = Depends(get_db)):
    db_blog = get_blog_by_id(db, blog_id)
    if db_blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")  

    return update_blog(db=db, blog_id=blog_id, blog=blog)

@router.delete("/blogs/{blog_id}")
def delete_blog_route(blog_id: int, db: Session = Depends(get_db)):
    db_blog = get_blog_by_id(db, blog_id)
    if db_blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")  

    if delete_blog(db=db, blog_id=blog_id):
        return {"message": "Blog deleted successfully"}

    raise HTTPException(status_code=400, detail="Failed to delete blog")
