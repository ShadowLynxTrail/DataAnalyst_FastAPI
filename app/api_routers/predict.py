from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database import get_db
from app.ml import predict_sales
from app.api.deps import get_current_user
from app.models import User

router = APIRouter(prefix="/predict", tags=["predict"])

class SalesPredictionRequest(BaseModel):
    date: str
    category: str
    region: str
    product_name: str
    price: float

@router.post("/sales")
def predict_sales_endpoint(
    request: SalesPredictionRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        result = predict_sales(request.model_dump())
        return {"predicted_quantity": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))