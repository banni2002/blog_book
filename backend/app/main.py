from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from .routes.category import router as category_router
from .routes.blog import router as blog_router
from .routes.menu import router as menu_router
from .routes.admin import router as admin_router
from .routes.pricing import router as pricing_router
from .routes.slide import router as slide_router
from .routes.cat_product import router as cat_product_router
from .routes.product import router as product_router
from .routes.social_media import router as social_router
from .routes.management import router as management_router
from .database import engine, Base
from .models import category, blog, menu, admin, pricing, slide, cat_product, product, social_media, management

# Tạo bảng nếu chưa có
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(category_router)
app.include_router(blog_router)
app.include_router(menu_router)
app.include_router(admin_router)
app.include_router(pricing_router)
app.include_router(slide_router)
app.include_router(cat_product_router)
app.include_router(product_router)
app.include_router(social_router)
app.include_router(management_router)
app.mount("/uploads", StaticFiles(directory="app/uploads"), name="uploads")
