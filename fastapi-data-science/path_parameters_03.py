from enum import Enum
from fastapi import FastAPI

class userType(str, Enum):
    STANDARD = "standard"
    ADMIN = "admin"
app = FastAPI()

@app.get("/users/{type}/{id}")
async def get_user(type: userType, id: int):
    return {"type":userType, "id":id}

#Building from example 3. This script allows for validating the type of string that can be accepted into the api. 
# String enumeration is used to list all the allowed strings that can be used in the API

