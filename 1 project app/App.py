import streamlit as st

st.title("🚀 My Streamlit App")

name = st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value=1, max_value=100)

if st.button("Submit"):
    st.success(f"Hello {name}, you are {age} years old!")

