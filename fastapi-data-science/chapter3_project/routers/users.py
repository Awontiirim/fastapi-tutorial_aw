from typing import List
from django.db import router
from fastapi import APIRouter, HTTPException, status
from chapter3_project.models.users import User, UserCreate
from typing import List
from chapter3_project import db
router = APIRouter()

@router.get("/")
async def get_users() -> List[User]:
    return list(db.users.values())

