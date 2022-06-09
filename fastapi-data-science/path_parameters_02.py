from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{type}/{id}")
async def path_parameters(type: str, id: int):
    return {"type": type, "id":id}

# Accepts any string as the type parameter