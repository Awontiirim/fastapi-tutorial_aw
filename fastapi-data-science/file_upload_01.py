from fastapi import FastAPI, File

app = FastAPI()

@app.post('/files')
async def upload_file(file: bytes = File(...)):
    return {"file_size": len(file)}

#to endpoint to allow determine the number of bytes in an uploaded file 

# issue is that, bytes are stored in memory and so this might work for small files 
# but it will have issues with large files 

