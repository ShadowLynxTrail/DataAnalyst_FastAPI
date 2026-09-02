
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models import Sale

def get_summary(db: Session):
    total_sales = db.query(func.count(Sale.id)).scalar()
    total_revenue = db.query(func.sum(Sale.quantity * Sale.price)).scalar()
    avg_check = total_revenue / total_sales if total_sales else 0
    return {
        "total_sales": total_sales,
        "total_revenue": total_revenue,
        "avg_check": avg_check
    }

def get_category_revenue(db: Session):
    rows = db.query(
        Sale.category,
        func.sum(Sale.quantity * Sale.price).label("revenue")
    ).group_by(Sale.category).order_by(func.sum(Sale.quantity * Sale.price).desc()).all()
    return [{"category": row.category, "revenue": row.revenue} for row in rows]

def get_top_products(db: Session, limit: int = 5):
    rows = db.query(
        Sale.product_name,
        func.sum(Sale.quantity * Sale.price).label("revenue")
    ).group_by(Sale.product_name).order_by(func.sum(Sale.quantity * Sale.price).desc()).limit(limit).all()
    return [{"product_name": row.product_name, "revenue": row.revenue} for row in rows]