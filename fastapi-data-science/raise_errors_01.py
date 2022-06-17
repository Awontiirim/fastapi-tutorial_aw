#from http.client import HTTPException
from fastapi import Body, FastAPI, status, HTTPException


app = FastAPI()

@app.post('/password')
async def check_password(password: str = Body(...), confirm_password: str = Body(...)):
    if password != confirm_password:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            detail="Passwords do not match",
        )
    return {"message": "Passwords match"}
