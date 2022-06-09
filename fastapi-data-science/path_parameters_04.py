from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/users/{id}")
async def get_user(id: int = Path(..., ge=1)):
    return {"id":id}


#Path function provided by fastapi allows for advanced validation of int or str
