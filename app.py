import streamlit as st
import requests

st.title("🏠 House Price Prediction System")

st.write("Enter property details:")

# 用户输入
carpet_area = st.number_input("Carpet Area", value=1000)
bathroom = st.number_input("Bathroom", value=2)
balcony = st.number_input("Balcony", value=1)
parking = st.number_input("Car Parking", value=1)

# 按钮
if st.button("Predict Price"):

    data = {
        "Carpet Area": carpet_area,
        "Bathroom": bathroom,
        "Balcony": balcony,
        "Car Parking": parking
    }

    try:
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=data
        )

        result = response.json()

        st.success(f"Predicted Price: {result['predicted_price']:.2f}")

    except:
        st.error("API connection failed. Make sure FastAPI is running.")