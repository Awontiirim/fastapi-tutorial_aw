from fastapi import FastAPI,Form

app = FastAPI()

@app.post('/users')
async def create_user(name: str = Form(...), age: int = Form(...)):
    return {"name": name, "age":age}

#Start the Server using the command:    
    # uvicorn form_data_01:app

# send the request via terminal using the command:
    #  http -v --form POST http://localhost:8000/users name=John age=30

# Visit the OpenAPI docs with the url : 
    #  http://localhost:8000/docs

#FastAPI does not allow you to define pydantic models to validate form data. 
# Only allows it for json data