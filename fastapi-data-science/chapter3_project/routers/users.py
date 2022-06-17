from typing import List
from fastapi import APIRouter, HTTPException, status
from models.users import User, UserCreate
from typing import List
import db
router = APIRouter()

@router.get("/")
async def get_users() -> List[User]:
    return list(db.users.values())

