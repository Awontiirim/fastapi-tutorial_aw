from typing import List
from fastapi import APIRouter, HTTPException, status
from models import posts
import db
router = APIRouter()

@router.get("/")
async def get_all_posts() -> List[posts.Post]:
    return list(db.posts.values())

@router.get("/{id}")
async def get_post(id : int ) -> posts.Post:
    try:
        return db.posts[id]
    except KeyError:
        raise HTTPException(status_code=404, detail="post not found")
    
@router.post("/", status_code=201)
async def create_post(post_create: posts.PostCreate):
    try:
        db.users[post_create.user]
    except KeyError:
        raise HTTPException(status_code=400,
        detail=f"User with id {post_create.user} doesn't exist"
        )
    new_id = max(db.posts.keys() or (0,)) + 1
    post = posts.Post(id=new_id, **post_create.dict(), title="Hi There")
    db.posts[new_id] = post
    return post

@router.delete("/{id}", status_code=204)
async def delete_post(id: int)-> posts.Post:
    try:
        db.posts.pop(id)
    except KeyError:
        raise HTTPException(status_code=404, detail="Post not found")
