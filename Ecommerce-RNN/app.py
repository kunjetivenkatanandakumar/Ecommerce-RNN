import streamlit as st
import numpy as np


import os
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "sales_rnn_model.keras"
)

model = load_model(MODEL_PATH)


st.title("E-Commerce Sales Forecast")

day1 = st.number_input("Day 1 Sales")
day2 = st.number_input("Day 2 Sales")
day3 = st.number_input("Day 3 Sales")

if st.button("Predict"):

    scaler = MinMaxScaler()

    sample = np.array([[day1],[day2],[day3]])

    scaler.fit(sample)

    scaled = scaler.transform(sample)

    X = scaled.reshape(1,3,1)

    pred = model.predict(X)

    result = scaler.inverse_transform(pred)

    st.success(
        f"Predicted Next Day Sales: {result[0][0]:.2f}"
    )
