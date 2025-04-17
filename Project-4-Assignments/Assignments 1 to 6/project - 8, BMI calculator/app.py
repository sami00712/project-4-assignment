import streamlit as st
import time


st.set_page_config(page_title="BMI CALCULATOR", layout="centered")


st.title("🚦 BMI Calculator")
st.markdown("## Enter your weight and height for BMI calculation")


col1, col2 = st.columns(2)
with col1:
    weight = st.number_input("Weight (kg):", min_value=1.0, format="%.2f")
with col2:
    height = st.number_input("Height (m):", min_value=0.5, format="%.2f")  # Fixed min value


if height > 0 and weight > 0:
    # BMI Calculation
    bmi = weight / (height ** 2)
    
    
    st.subheader("Your BMI is:")
    st.markdown(f"### {bmi:.2f}", unsafe_allow_html=True)

   
    if bmi < 18.5:
        st.warning("⚠️ Underweight")
    elif 18.5 <= bmi < 24.9:
        st.success("✅ Normal weight")
    elif 25 <= bmi < 29.9:
        st.warning("⚠️ Overweight")
    else:
        st.error("❗ Obesity – Consider consulting a doctor.")
else:
    st.info("ℹ️ Please enter a valid weight and height.")
