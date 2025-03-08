import streamlit as st

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight", " You need to gain some weight!"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight", "Great! You have a healthy weight."
    elif 25 <= bmi < 29.9:
        return "Overweight", "You should consider losing some weight."
    else:
        return "Obese", "❌ It's important to focus on a healthier lifestyle."

# Streamlit UI
st.title("BMI Calculator")
st.write("Enter your weight and height to calculate your BMI.")

weight = st.number_input("Enter your weight (kg):", min_value=1.0, step=0.1)
height = st.number_input("Enter your height (m):", min_value=0.5, step=0.01)

if st.button("Calculate BMI"):
    if weight > 0 and height > 0:
        bmi = calculate_bmi(weight, height)
        category, advice = bmi_category(bmi)
        st.success(f"Your BMI is: **{bmi:.2f}**")
        st.info(f"Category: **{category}**")
        st.warning(advice)
    else:
        st.error("Please enter valid weight and height values.")

