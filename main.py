import shutil
from typing import Union
from typing import List

from fastapi import FastAPI, UploadFile, File

app = FastAPI()


@app.post("/")
async def root(file: UploadFile = File(...)):
    with open(f'{file.filename}', "wb") as butter:
        shutil.copyfileobj(file.file, butter)
    return {"file_name": file.filename}


@app.post("/img")
async def upload_image(files: List[UploadFile] = File(...)):
    for img in files:
        with open(f'{img.filename}', "wb") as butter:
            shutil.copyfileobj(img.file, butter)
    return {"file_name": "Good"}

