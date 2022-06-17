from fastapi import APIRouter, HTTPException, status
from chapter3_project.models import posts
from chapter3_project import db
router = APIRouter()

@router.post("/")
async def get_posts():
    return {}