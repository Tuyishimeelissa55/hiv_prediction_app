# app.py

import streamlit as st
import pandas as pd
import numpy as np
import pickle
import requests

# --- Load the trained model ---
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# --- Streamlit App Interface ---
st.title("HIV Prediction App")
st.write("Enter the following details:")

# Input fields (based on your dataset)
age = st.number_input("Age", min_value=0, max_value=120, value=25)
bmi = st.number_input("BMI", min_value=0.0, max_value=50.0, value=22.5)
risk_level = st.selectbox("Risk Level", ["Low", "Medium", "High"])

# Collect input data into a DataFrame
input_data = pd.DataFrame({
    "Age": [age],
    "BMI": [bmi],
    "Risk_Level": [risk_level]
})

# --- Prediction ---
if st.button("Predict"):
    prediction = model.predict(input_data)
    st.success(f"The predicted result is: {prediction[0]}")

    # --- Send result to ThingSpeak ---
    THINGSPEAK_API_KEY = "KGVZ4UJJZ9KZQ36G"
    CHANNEL_FIELD = "field1"  # adjust field if needed

    data = {CHANNEL_FIELD: prediction[0]}
    response = requests.post(
        f"https://api.thingspeak.com/update?api_key={THINGSPEAK_API_KEY}",
        data=data
    )

    if response.status_code == 200:
        st.info("Prediction successfully sent to ThingSpeak!")
    else:
        st.error("Failed to send prediction to ThingSpeak.")
