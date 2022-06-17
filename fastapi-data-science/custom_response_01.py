from fastapi import FastAPI
from fastapi.responses import HTMLResponse, PlainTextResponse

app = FastAPI()

@app.get("/html", response_class=HTMLResponse)
async def get_html():
    return """
        <html>
            <head>
                <title> Hello world! </title>
            </head>
            <body>
                <h1>Hello world! </h1>
            </body>
        </html>
    """
@app.get("/plain-text", response_class=PlainTextResponse)
async def get_plain():
    return "Hello world!"


#Notes
# response_class allows you to specify the type of response your endpoint should give. 
# The default class in fastapi returns a JSON response
#As shown in this example, it is possible to define the response_classes in the get method as a parameter
# The response_class controls some of the response headers automatically

