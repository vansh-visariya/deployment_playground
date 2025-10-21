from fastapi import FastAPI, Path, HTTPException, Query
import json
from fastapi.responses import JSONResponse
from scheme.user_input import Input
from scheme.prediction_res import PredictionResponse
from model.predict import predict_insurance_premium, model

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the Insurance Premium Prediction API"}

# for the machine health check (mostly for the AWS deployment)
@app.get("/health")
async def health():
    return {"status": "ok",
            "model_status": "loaded" if model else "not loaded",
            "model_version": "1.0.0"}

@app.post("/predict", response_model=PredictionResponse)
async def predict(input: Input):
    input_data = {
        'bmi': input.bmi,
        'age_group': input.age_group,
        'lifestyle_risk': input.lifestyle_risk,
        'city_tier': input.city_tier,
        'income_lpa': input.income_lpa,
        'occupation': input.occupation
    }
    try:
        prediction = predict_insurance_premium(input_data)
        return JSONResponse(status_code=200, content={"predicted_insurance_premium": prediction})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))