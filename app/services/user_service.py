from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.models.user import UserCreate, UserUpdate
from typing import List, Optional

class UserService:
    def __init__(self, db: AsyncSession = Depends(get_db)):
        self.db = db

    async def create_user(self, user_data: UserCreate):
        pass

    async def list_users(self, role: Optional[str], status: Optional[str]):
        pass

    async def get_user(self, user_id: int):
        pass

    async def update_user(self, user_id: int, user_data: UserUpdate):
        pass

    async def delete_user(self, user_id: int):
        pass
