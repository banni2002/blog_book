from sqlalchemy.orm import Session
from ..models import Blog as BlogModel
from ..schemas.blog import BlogCreate, Blog

# Lấy danh sách blog
def get_blogs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(BlogModel).offset(skip).limit(limit).all()

# Lấy blog theo ID
def get_blog_by_id(db: Session, blog_id: int):
    return db.query(BlogModel).filter(BlogModel.id == blog_id).first()

def count_blogs(db: Session):
    return db.query(BlogModel).count()

# Tạo mới blog
def create_blog(db: Session, blog: BlogCreate):
    db_blog = BlogModel(
        title=blog.title,
        slug=blog.slug,
        meta_description=blog.meta_description,
        content=blog.content,
        image_feature=blog.image_feature,
        category_id=blog.category_id,
        author_name=blog.author_name
    )
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog

# Cập nhật blog
def update_blog(db: Session, blog_id: int, blog: BlogCreate):
    db_blog = get_blog_by_id(db, blog_id)
    if db_blog:
        db_blog.title = blog.title
        db_blog.slug = blog.slug
        db_blog.meta_description = blog.meta_description
        db_blog.content = blog.content
        db_blog.image_feature = blog.image_feature
        db_blog.category_id = blog.category_id
        db_blog.author_name = blog.author_name
        db.commit()
        db.refresh(db_blog)
        return db_blog
    return None

# Xóa blog
def delete_blog(db: Session, blog_id: int):
    db_blog = get_blog_by_id(db, blog_id)
    if db_blog:
        db.delete(db_blog)
        db.commit()
        return True
    return False
