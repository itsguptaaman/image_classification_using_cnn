import os
import re
import unicodedata

from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
import aiofiles
import uvicorn

from prediction import predict_image  


UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app = FastAPI(
    title="Image Classification API",
    description="An API for classifying images using a model",
    version="1.0.0"
)

class PredictionResult(BaseModel):
    filename: str
    prediction: str

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def secure_filename(filename):
    filename = unicodedata.normalize('NFKD', filename).encode('ascii', 'ignore').decode('utf-8')
    filename = re.sub(r'[^a-zA-Z0-9.-]', '_', filename)
    return filename

@app.get("/", summary="Check API status")
async def home():
    return {"status": "online"}

@app.post("/predict", response_model=PredictionResult, summary="Upload an image and get a prediction")
async def upload_file(file: UploadFile = File(...)):
    if file.filename == '':
        raise HTTPException(status_code=400, detail="No file part")
    if allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        async with aiofiles.open(filepath, 'wb') as out_file:
            content = await file.read()
            await out_file.write(content)

        predicted_label, _ = predict_image(filepath)
        print(f"Predicted label: {predicted_label}")

        return {"filename": filename, "prediction": predicted_label}
    raise HTTPException(status_code=400, detail="Invalid file format")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
