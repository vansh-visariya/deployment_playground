import streamlit as st
import requests

API_URL = "http://localhost:8000/predict"

st.title("Insurance Premium Prediction")
st.write("Enter the details below to predict the insurance premium.")

age = st.number_input("Age", min_value=1, max_value=100, value=25)
weight = st.number_input("Weight (in kgs)", min_value=1.0, max_value=300.0, value=70.0)
height = st.number_input("Height (in meters)", min_value=1.0, max_value=2.5, value=1.75)
income_lpa = st.number_input("Income (in lakhs per annum)", min_value=0.0, value=5.0)
smoker = st.selectbox("Is the person a smoker?", options=[True, False])
city = st.text_input("City of residence", value="Mumbai")
occupation = st.selectbox("Occupation", options=['private_job', 'unemployed', 'business_owner', 'retired', 'student','government_job', 'freelancer'])

if st.button("Predict"):
    data = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation
    }
    response = requests.post(API_URL, json=data)
    if response.status_code == 200:
        prediction = response.json()['predicted_insurance_premium']
        st.write(f"Predicted Insurance Premium: {prediction}")
    else:
        st.write("Error occurred while making the prediction.")