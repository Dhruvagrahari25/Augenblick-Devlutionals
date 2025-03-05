import streamlit as st
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
import tensorflow as tf
import io
from PIL import Image

# Load the trained CNN model
MODEL_PATH = "drill_classifier.h5"
model = tf.keras.models.load_model(MODEL_PATH)

# Function to convert audio to spectrogram
def audio_to_spectrogram(audio_file, target_size=(128, 128)):
    # Load audio
    y, sr = librosa.load(audio_file, sr=None)
    
    # Generate spectrogram
    spectrogram = librosa.feature.melspectrogram(y=y, sr=sr)
    spectrogram_db = librosa.power_to_db(spectrogram, ref=np.max)

    # Convert to image format
    fig, ax = plt.subplots(figsize=(3, 3))  # Keep it square for CNN
    ax.set_axis_off()
    librosa.display.specshow(spectrogram_db, sr=sr, x_axis="time", y_axis="mel", ax=ax)
    
    # Save image to bytes
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format="png", bbox_inches="tight", pad_inches=0)
    plt.close(fig)

    # Load image and resize for CNN input
    img = Image.open(img_buffer).convert("RGB")
    img = img.resize(target_size)
    img_array = np.array(img) / 255.0  # Normalize

    return img_array

# Streamlit UI
st.title("Equipment Health Prediction from Audio")

# File uploader
uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3"])

if uploaded_file:
    # Display audio player
    st.audio(uploaded_file, format="audio/wav")

    # Convert audio to spectrogram
    spectrogram_img = audio_to_spectrogram(uploaded_file)

    # Display spectrogram
    st.image(spectrogram_img, caption="Spectrogram of the Audio", use_column_width=True)

    # Reshape for CNN model
    input_data = np.expand_dims(spectrogram_img, axis=0)  # Add batch dimension

    # Predict using the CNN model
    prediction = model.predict(input_data)
    predicted_class = np.argmax(prediction, axis=1)[0]  # Get class index

    # Display result
    if predicted_class == 1:
        st.success("✅ The machine is working fine.")
    else:
        st.error("⚠️ The machine is not working properly!")