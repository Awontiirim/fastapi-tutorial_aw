from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{id}")
async def get_user_id(id: int):
    return {"id":id}
