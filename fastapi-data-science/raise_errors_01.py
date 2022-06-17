#from http.client import HTTPException
from fastapi import Body, FastAPI, status, HTTPException


app = FastAPI()

@app.post('/password')
async def check_password(password: str = Body(...), confirm_password: str = Body(...)):
    if password != confirm_password:
        raise HTTPException(
            status_code=400,
            detail="Passwords do not match",
        )
    return {"message": "Passwords match"}

#HttpException method allows you to build raise exceptions when an endpoint is not hit correctly. 
# The detail keyword allows you to customize the error message returned when the api is not hit correctly.

