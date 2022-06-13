from fastapi import FastAPI, File, UploadFile
from typing import List
app = FastAPI()

@app.post('/files')
async def upload_multiple_files(files: List[UploadFile] = File(...)):
    documents = []
    for file in files:
        #await file.seek(0)
        document_class = {"file_name": file.filename, "content_type":file.content_type }
        documents.append(document_class)
    return documents
    # return [
    #      {"file_name": file.filename, "content_type": file.content_type}
    #      for file in files
    #  ]
   