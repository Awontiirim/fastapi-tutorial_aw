from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.post('/files')
async def upload_files(file: UploadFile = File(...)):
    return {"file_size": file.filename, "content_type":file.content_type }

## This endpoint extends Files by allowing to upload larger files 
# The content_type is to determine the type of file uploaded and then possibly 
    # validate it with a given list of accepted files