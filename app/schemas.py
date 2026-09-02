
from pydantic import BaseModel, EmailStr,  ConfigDict
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
    model_config = ConfigDict(from_attributes=True)

# --- Item schemas ---
class ItemBase(BaseModel):
    name: str
    price: float

class ItemCreate(ItemBase):
    pass

class ItemOut(ItemBase):
    id: int
    owner_id: int
    model_config = ConfigDict(from_attributes=True)

class Token(BaseModel):
        access_token: str
        token_type: str = "bearer"