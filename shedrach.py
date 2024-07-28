import numpy as np
import pandas as pd
import streamlit as st
import joblib
import pickle

# Streamlit app
st.title("House Price Prediction")

# User input for prediction
st.header("Enter House Details for Prediction")

house_age = st.number_input("House Age", step=1)
num_bedrooms = st.number_input("Number of Bedrooms", step=1)
num_bathrooms = st.number_input("Number of Bathrooms", step=1)
area = st.number_input("Area", step=1)
location = st.selectbox("Location", ['Urban', 'SubUrban', 'Rural'])

params = {'HouseAge': [house_age], 'Bedroom':[num_bedrooms], 'FullBath':[num_bathrooms], 'LotArea':[area], 'Location': [location]}
params = pd.DataFrame(params)

# encode the categorical variable
location = {'Rural':0, 'SubUrban':1, 'Urban':2}
params['Location'] = location[params['Location'][0]]

# loading the saved model
loaded_model = pickle.load(open("HousePredict.pkl", 'rb'))

# Make prediction
if st.button("Predict"):
    prediction = loaded_model.predict(params)
    st.write(f"Predicted House Price: ${prediction[0]:,.2f}")