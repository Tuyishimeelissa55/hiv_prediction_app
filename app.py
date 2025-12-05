import streamlit as st
import numpy as np
import joblib

model = joblib.load("hiv_model.pkl")

st.title("HIV Risk Prediction App")

Num_Partners = st.number_input("Number of Sexual Partners", min_value=0)
Condom_Use = st.selectbox("Condom Use (1 = Yes, 0 = No)", [1, 0])
Drug_Use = st.selectbox("Drug Use (1 = Yes, 0 = No)", [1, 0])
STI_History = st.selectbox("History of STIs (1 = Yes, 0 = No)", [1, 0])
Sex_Work_Years = st.number_input("Years in Sex Work", min_value=0)

if st.button("Predict"):
    user_input = np.array([[Num_Partners, Condom_Use, Drug_Use, STI_History, Sex_Work_Years]])
    prediction = model.predict(user_input)

    if prediction[0] == 1:
        st.error("⚠️ High Risk of HIV")
    else:
        st.success("✅ Low Risk of HIV")
