import streamlit as st
import joblib
import numpy as  np 
import pandas as pd
# Load your trained models
model = joblib.load("model.pkl")
#App title when the page was loading to the user of the data
st.title("🏠 House Price Prediction App") 
st.divider()
st.write("This app uses a trained Machine Learning model to predict house prices based on input features the make the prediction . Enter the details below and click **Predict** to get an estimated price."
st.divider() 
# Input fields

bedrooms = st.number_input("Number of Bedrooms", min_value=0, value=3)
bathrooms = st.number_input("Number of Bathrooms", min_value=0, value=2)
condition = st.number_input("Condition (1–5)", min_value=1, max_value=5, value=3)
number_of_schools = st.number_input("Number of Schools Nearby", min_value=0, value=2)

st.divider() #this was used to add the break line to the pages 

# Prepare input from the user 

x = np.array([[bedrooms, bathrooms, condition, number_of_schools]])

# Predict button
predict_button = st.button("🔮 Predict")

if predict_button:
    prediction = model.predict(x)[0]
    st.success(f"💰 Estimated House Price: {prediction:,.2f}")
    st.balloons()
else:
    st.info("Please enter values and click **Predict** to see the result.")



