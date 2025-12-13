import pickle
import streamlit as st
import os

@st.cache_resource
def load_model(filepath):
    if not os.path.exists(filepath):
        st.error(f"Model file not found: {filepath}")
        return None
    with open(filepath, "rb") as f:
        model = pickle.load(f)
    return model

model = load_model("salary_prediction/Salary_pre_linear_reg_model.pkl")
