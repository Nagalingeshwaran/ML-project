import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title="Salary Prediction", layout="centered")

st.title("💼 Salary Prediction App")

@st.cache_resource
def load_model():
    return joblib.load("Salary_pre_linear_reg_model.pkl")

model = load_model()

experience = st.number_input(
    "Enter Years of Experience",
    min_value=0.0,
    max_value=50.0,
    step=0.5
)

if st.button("Predict Salary"):
    prediction = model.predict([[experience]])
    st.success(f"💰 Predicted Salary: ₹ {prediction[0]:,.2f}")

