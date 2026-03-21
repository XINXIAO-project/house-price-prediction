from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

# 加载模型
pipeline = joblib.load("models/house_price_pipeline.pkl")

# 加载训练特征
feature_columns = joblib.load("models/feature_columns.pkl")


@app.get("/")
def home():
    return {"message": "House Price Prediction API"}


@app.post("/predict")
def predict(data: dict):

    df = pd.DataFrame([data])

    prediction = pipeline.predict(df)[0]

    return {
        "predicted_price": float(prediction)
    }