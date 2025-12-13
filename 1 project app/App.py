import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

# Page config
st.set_page_config(page_title="Salary Prediction", layout="centered")

st.title("💼 Salary Prediction App")
st.write("Predict salary based on years of experience")

# Sample dataset (simple)
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
y = np.array([30000, 35000, 40000, 45000, 50000,
              55000, 60000, 65000, 70000, 75000])

# Train model
model = LinearRegression()
model.fit(X, y)

# User input
experience = st.number_input(
    "Enter Years of Experience",
    min_value=0.0,
    max_value=50.0,
    step=0.5
)

# Prediction
if st.button("Predict Salary"):
    salary = model.predict([[experience]])
    st.success(f"💰 Predicted Salary: ₹ {salary[0]:,.2f}")

