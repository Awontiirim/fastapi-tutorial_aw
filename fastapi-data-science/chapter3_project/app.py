from fastapi import FastAPI
from routers.posts import router as posts_router
#import chapter3_project.routers.posts 
from routers.users import router as users_router
app = FastAPI()

app.include_router(posts_router, prefix="/posts")
app.include_router(users_router, prefix="/users")