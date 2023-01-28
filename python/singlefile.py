from fastapi import FastAPI, File, UploadFile, Request
import os
import shutil

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


@app.post("/upload/")
async def upload(file: UploadFile = File(...)):

    if file and allowed_file(file.filename):

        content = await file.read()
        print(content)

        filename = file.filename
        fileobj = file.file
        upload_dir = open(os.path.join(UPLOAD_FOLDER, filename),'wb+')
        shutil.copyfileobj(fileobj, upload_dir)
        upload_dir.close()

        return {"アップロードされたファイル": filename}
    if file and not allowed_file(file.filename):
        return {"warning": "許可されたファイルタイプではありません"}