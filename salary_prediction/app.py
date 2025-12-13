import streamlit as st
import pickle
import numpy as np
import os

st.set_page_config(page_title="Salary Prediction", layout="centered")

st.title("💼 Salary Prediction using Linear Regression")
st.write("Enter years of experience to predict salary")

# Get the absolute path to the current directory
current_dir = os.path.dirname(__file__)

# Join the directory with the model filename (assuming it's in the same folder)
model_path = os.path.join(current_dir, "salary_model.pkl")

# Use st.cache_resource for performance
@st.cache_resource
def load_model(path):
    """Loads the pickled model from the specified path."""
    try:
        with open(path, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        st.error(f"Error: Model file not found at expected location: {path}")
        st.stop()
    except Exception as e:
        st.error(f"An error occurred while loading the model: {e}")
        st.stop()

model = load_model(model_path)

# --- User Input and Prediction ---
experience = st.number_input(
    "Years of Experience",
    min_value=0.0,
    max_value=50.0,
    step=0.1
)

if st.button("Predict Salary"):
    # Reshape the input for the model: [[experience]]
    input_data = np.array([[experience]]) 
    prediction = model.predict(input_data)
    
    st.success(f"💰 Predicted Salary: ₹ {prediction[0]:,.2f}")
