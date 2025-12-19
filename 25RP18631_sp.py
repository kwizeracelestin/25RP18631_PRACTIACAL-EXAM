import streamlit as st
import pickle
import numpy as np
import os

# Check if model exists to avoid errors
model_path = '25RP18631_best_model.pkl'

st.title("🌱Crop Yield Predictor(Designed by 25RP18631)")

if os.path.exists(model_path):
    # Load the saved model [cite: 67, 81]
    model = pickle.load(open(model_path, 'rb'))

    # User input for temperature [cite: 20]
    temp = st.number_input("Average Temperature (°C)", min_value=0.0, max_value=100000.0, value=25.0)

    if st.button("Predict Yield"):
        # Reshape input for the model
        prediction = model.predict(np.array([[temp]]))
        st.success(f"The predicted Crop Yield is: {prediction[0]:.2f} tons/hectare")
        
        # Displaying the logic from your case study [cite: 23]
      
else:
    st.error(f"Model file '{model_path}' not found. Please run your Jupyter Notebook first to save the model[cite: 65].")