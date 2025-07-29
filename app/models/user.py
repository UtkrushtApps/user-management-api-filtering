from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr
    role: str
    status: str

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    role: Optional[str]
    status: Optional[str]

class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True
