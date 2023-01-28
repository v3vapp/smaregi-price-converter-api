from fastapi import FastAPI, File, UploadFile, Request
import os
import shutil
from typing import List

app = FastAPI()

@app.middleware("http")
async def allow_cors(request: Request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "*"
    return response

ALLOWED_EXTENSIONS = set(['csv','jpg'])
UPLOAD_FOLDER = './uploads'


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# FIXME: This api needs to handle 2 csv files. 

@app.post("/upload/")
async def upload_files(files: List[UploadFile] = File(...)):

    # content = await files.read()
    # print(content)

    for file in files:

        if file and allowed_file(file.filename):

            filename = file.filename
            fileobj = file.file
            upload_dir = open(os.path.join(UPLOAD_FOLDER, filename),'wb+')
            shutil.copyfileobj(fileobj, upload_dir)
            upload_dir.close()

    return {"message form v3v": "success!"}
