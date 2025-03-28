import streamlit as st
from PIL import Image
import tensorflow as tf
from tensorflow.keras.applications.mobilenet import MobileNet, preprocess_input, decode_predictions
import numpy as np

# Set up the app
st.set_page_config(page_title="Butterfly Prediction", layout="centered")
st.title("🐛 Butterfly Prediction App")
st.write("Scan and classify butterfly images using MobileNet.")

# File uploader
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Load and preprocess image
    image = Image.open(uploaded_file).resize((224, 224))
    st.image(image, caption="Uploaded Image", use_container_width=True)
    
    # Load MobileNet model
    model = MobileNet(weights="imagenet")
    img_array = preprocess_input(np.expand_dims(np.array(image), axis=0))

    # Predict
    predictions = model.predict(img_array)
    decoded_predictions = decode_predictions(predictions, top=3)[0]
    st.subheader("Predictions:")
    for i, (imagenet_id, label, score) in enumerate(decoded_predictions):
        st.write(f"{i + 1}. **{label}**: {score * 100:.2f}%")

# Add Webcam functionality (future extension)
st.write("Webcam functionality can be added using Streamlit's MediaPipe or OpenCV integrations.")
