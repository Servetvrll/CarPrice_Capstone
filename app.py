from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import pickle
import pandas as pd
from pydantic import BaseModel
import uvicorn

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load Model
with open("car_price_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("label_encoders.pkl", "rb") as f:
    label_encoders = pickle.load(f)

with open("binary_encoders.pkl", "rb") as f:
    binary_encoders = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("model_columns.pkl", "rb") as f:
    model_columns = pickle.load(f)


# Car İnput Features
class CarFeatures(BaseModel):
    brand: str
    model: str
    year: int
    transmission: str
    km: float
    fuelType: str
    engineSize: float

#İ
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict")
async def predict(features: CarFeatures):

    input_df = pd.DataFrame([features.model_dump()])
    input_df['brand'] = input_df['brand'].str.strip()
    # --- PREPROCESSING ---

    # A. Unseen Label Protection
    if input_df['model'].iloc[0] not in label_encoders['model'].classes_:
        input_df.loc[0, 'model'] = label_encoders['model'].classes_[0]

    if input_df['brand'].iloc[0] not in label_encoders['brand'].classes_:
        input_df.loc[0, 'brand'] = label_encoders['brand'].classes_[0]

        # B. Label Encoding
    for col in ["brand", "model"]:
        input_df[col] = label_encoders[col].transform(input_df[col])

    # C. Binary Encoding (Transmission & FuelType)
    for col in ["transmission", "fuelType"]:
        input_df = binary_encoders[col].transform(input_df)

    # D. Feature Scaling (KM, EngineSize, Year)
    scale_cols = ['km', 'engineSize', 'year']
    input_df[scale_cols] = scaler.transform(input_df[scale_cols])

    # E. Reindex
    input_df = input_df.reindex(columns=model_columns, fill_value=0)

    # 3. TAHMİN
    prediction = model.predict(input_df)

    return {"predicted_price": float(prediction[0])}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)