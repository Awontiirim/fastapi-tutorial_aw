from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()
@app.get("/redirect", response_class=RedirectResponse)
async def get_new_url():
    return RedirectResponse('/new-url', status_code=301)

#Notes
# The RedirectResponse response class is used when you want to redirect a current url to a new url 
