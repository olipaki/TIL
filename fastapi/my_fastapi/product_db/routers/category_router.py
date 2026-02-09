from fastapi import APIRouter, Depends, status
from product_db.schemas.category import CategoryCreateRequest, CategoryResponse
from product_db.services.category_service import category_service
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter(prefix="/category-db", tags=["category-db"])


@router.post("", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
def create_category(data: CategoryCreateRequest, db: Session = Depends(get_db)):
    return category_service.create_category(db, data)


@router.get("", response_model=list[CategoryResponse])
def get_categories(db: Session = Depends(get_db)):
    return category_service.get_categories(db)
