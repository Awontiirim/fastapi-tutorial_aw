from fastapi import FastAPI, Response
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def custom_header(response:Response):
    response.headers["Custom-Header"] = "Custom-Header-Value"
    return {"hello": "world"}

#Setting custom response headers