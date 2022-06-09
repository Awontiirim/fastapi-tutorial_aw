from fastapi import FastAPI, Query
from enum import Enum

class UserFormat(str, Enum):
    SHORT = "short"
    FULL = "full"


app = FastAPI()

@app.get("/users")
async def get_user(page: int = Query(1, gt=0), size: int = Query(10, le=100)):
    return {"page":page, "size":size}
