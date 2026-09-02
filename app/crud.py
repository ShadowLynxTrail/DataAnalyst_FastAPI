
from sqlalchemy.orm import Session
from app import models, schemas
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# --- Пользователи ---
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    hashed = pwd_context.hash(user.password)
    db_user = models.User(
        email=user.email,
        name=user.name,
        hashed_password=hashed
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# --- Товары ---
def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()

def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()

def create_item(db: Session, item: schemas.ItemCreate, owner_id: int):
    db_item = models.Item(**item.dict(), owner_id=owner_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item