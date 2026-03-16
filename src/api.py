from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

# 加载模型
model = joblib.load("models/random_forest_model.pkl")

# 加载训练特征
feature_columns = joblib.load("models/feature_columns.pkl")


@app.get("/")
def home():
    return {"message": "House Price Prediction API"}


@app.post("/predict")
def predict(data: dict):

    # 用户输入
    input_df = pd.DataFrame([data])

    # 创建完整特征表
    df = pd.DataFrame(columns=feature_columns)

    # 填充输入
    for col in input_df.columns:
        if col in df.columns:
            df[col] = input_df[col]

    df = df.fillna(0)

    prediction = model.predict(df)[0]

    return {"predicted_price": float(prediction)}