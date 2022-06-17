import email
from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    name : str 
    age: int

class User(BaseModel):
    id : int 
    email : str