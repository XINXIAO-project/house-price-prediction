from fastapi import FastAPI
import joblib
import pandas as pd

# 创建API
app = FastAPI()

# 加载模型
model = joblib.load("../models/random_forest_model.pkl")


@app.get("/")
def home():
    return {"message": "House Price Prediction API"}


@app.post("/predict")
def predict(data: dict):

    # 将输入转换为DataFrame
    df = pd.DataFrame([data])

    # 模型预测
    prediction = model.predict(df)[0]

    return {
        "predicted_price": float(prediction)
    }