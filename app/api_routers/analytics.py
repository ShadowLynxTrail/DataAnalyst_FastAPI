
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.analytics import get_summary, get_category_revenue, get_top_products

router = APIRouter(prefix="/analytics", tags=["analytics"])

@router.get("/summary")
def read_summary(db: Session = Depends(get_db)):
    return get_summary(db)

@router.get("/category_revenue")
def read_category_revenue(db: Session = Depends(get_db)):
    return get_category_revenue(db)

@router.get("/top_products")
def read_top_products(limit: int = 5, db: Session = Depends(get_db)):
    return get_top_products(db, limit)