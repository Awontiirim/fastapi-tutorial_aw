from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()
@app.get("/file", response_class=FileResponse)

async def file():
    return 