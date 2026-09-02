
from pydantic import BaseModel, EmailStr
from datetime import datetime

# --- User schemas ---
class UserBase(BaseModel):
    email: EmailStr
    name: str

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

# --- Item schemas ---
class ItemBase(BaseModel):
    name: str
    price: float

class ItemCreate(ItemBase):
    pass

class ItemOut(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True