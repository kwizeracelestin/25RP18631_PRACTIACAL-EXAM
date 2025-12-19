import streamlit as st
import joblib
import pandas as pd
import os

# -------------------------------
# Crop Yield Prediction App
# -------------------------------

st.set_page_config(page_title="Crop Yield PredictorDESIGNED BY 25RP18631)", page_icon="🌱")

st.title("🌱 Crop Yield Predictor")
st.write("Predict crop yield based on average temperature using a trained ML model.")

# Model path (must match the saved model name)
model_path = "25RP18631_model.pkl"

# Check if model exists
if os.path.exists(model_path):

    # Load trained model
    model = joblib.load(model_path)

    # User input
    temp = st.number_input(
        "Average Temperature (°C)",
        min_value=0.0,
        max_value=100.0,
        value=25.0
    )

    # Prediction
    if st.button("Predict Yield"):
        # Keep feature name exactly as in training
        input_data = pd.DataFrame([[temp]], columns=["Temperature"])

        prediction = model.predict(input_data)

        st.success(
            f"The predicted Crop Yield is: {prediction[0]:.2f} tons/hectare"
        )

else:
    st.error(
        "Model file not found. Please run the training code first "
        "to generate '25RP18631_model.pkl'."
    )
