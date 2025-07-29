from fastapi import APIRouter, Depends, Query, HTTPException, status
from typing import List, Optional
from app.models.user import UserCreate, UserResponse, UserUpdate
from app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, service: UserService = Depends()):
    pass

@router.get("/", response_model=List[UserResponse])
async def list_users(
    role: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
    service: UserService = Depends()
):
    pass

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, service: UserService = Depends()):
    pass

@router.put("/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user: UserUpdate, service: UserService = Depends()):
    pass

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int, service: UserService = Depends()):
    pass
