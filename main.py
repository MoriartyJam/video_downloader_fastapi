import shutil
from typing import Union

from fastapi import FastAPI, UploadFile, File

app = FastAPI()


@app.post("/")
async def root(file: UploadFile = File(...)):
    with open(f'{file.filename}', "wb") as butter:
        shutil.copyfileobj(file.file, butter)
    return {"file_name": file.filename}
