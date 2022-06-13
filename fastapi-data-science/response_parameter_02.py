from fastapi import FastAPI, Response

app = FastAPI()

@app.get('/')
async def custom_cookies(response:Response):
    response.set_cookie("cookie-name", "cookie-value", max_age=86400)
    return {"hello":"world"}
