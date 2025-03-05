import streamlit as st
import pickle
import numpy as np

# Load the trained model
MODEL_PATH = "logistic_regression_model.pkl"

def load_model():
    with open(MODEL_PATH, "rb") as file:
        model = pickle.load(file)
    return model

model = load_model()

# Define Min-Max Scaling Function
def min_max_scale(value, min_val, max_val):
    return (value - min_val) / (max_val - min_val)

# Streamlit UI
st.title("Equipment Health Prediction")

# Input sliders with original value ranges
temperature = st.slider("Temperature (°C)", min_value=0.0, max_value=150.0, value=25.0, step=0.1)
vibration = st.slider("Vibration Level", min_value=0.0, max_value=100.0, value=10.0, step=0.1)
power_usage = st.slider("Power Usage (kW)", min_value=0.0, max_value=1000.0, value=100.0, step=0.1)
humidity = st.slider("Humidity (%)", min_value=0.0, max_value=100.0, value=50.0, step=0.1)

# Scale the inputs between 0 and 1
scaled_temperature = min_max_scale(temperature, 0, 150)
scaled_vibration = min_max_scale(vibration, 0, 100)
scaled_power_usage = min_max_scale(power_usage, 0, 1000)
scaled_humidity = min_max_scale(humidity, 0, 100)

# Predict button
if st.button("Check Equipment Status"):
    input_data = np.array([[scaled_temperature, scaled_vibration, scaled_power_usage, scaled_humidity]])
    prediction = model.predict(input_data)
    
    if prediction[0] == 1:
        st.success("✅ The machine is working fine.")
    else:
        st.error("⚠️ The machine is not working properly!")
