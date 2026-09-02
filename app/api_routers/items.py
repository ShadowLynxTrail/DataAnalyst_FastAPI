

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app import schemas, crud

router = APIRouter()

@router.post('/',response_model= schemas.ItemOut, status_code=201)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):

    return crud.create_item(db, item, owner_id=1)

@router.get("/", response_model=List[schemas.ItemOut])
def read_items(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)):
    return crud.get_items(db, skip=skip, limit=limit)


@router.get("/{item_id}", response_model=schemas.ItemOut)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_item(db, item_id= item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item
    
