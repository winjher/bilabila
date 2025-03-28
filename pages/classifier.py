

import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array, ImageDataGenerator
from PIL import Image #For image display in Streamlit

# Load pre-trained model (assuming you've already trained and saved it)
try:
    cnn = tf.keras.models.load_model('butterfly_classifier.h5') #Change to your model's filename
    st.success("Model loaded successfully!")
except OSError:
    st.error("Model file not found. Please train and save the model first.")
    st.stop() #Stop execution if model loading fails


# Class labels (This should match your training data)
class_labels = {
    0: 'Butterfly-Clippers',
    1: 'Butterfly-Common Jay',
    2: 'Butterfly-Common Lime',
    3: 'Butterfly-Common Mime',
    4: 'Butterfly-Common Mormon',
    5: 'Butterfly-Emerald Swallowtail',
    6: 'Butterfly-Golden Birdwing',
    7: 'Butterfly-Gray Glassy Tiger',
    8: 'Butterfly-Great Eggfly',
    9: 'Butterfly-Great Yellow Mormon',
    10: 'Butterfly-Paper Kite',
    11: 'Butterfly-Pink Rose',
    12: 'Butterfly-Plain Tiger',
    13: 'Butterfly-Red Lacewing',
    14: 'Butterfly-Tailed Jay',
    15: 'Moth-Atlas',
    16: 'Moth-Giant Silk',
    17: 'None try again!!'
}


def predict_image(image_path):
    try:
        img = load_img(image_path, target_size=(64, 64))
        img_array = img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0  # Normalize the image

        predictions = cnn.predict(img_array)
        predicted_class_index = np.argmax(predictions[0])
        predicted_class = class_labels[predicted_class_index]
        confidence = predictions[0][predicted_class_index]

        return predicted_class, confidence
    except Exception as e:
        return "Error: " + str(e), 0


# Streamlit app
st.title("Butterfly Classifier")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image_data = uploaded_file.read()
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image.", use_column_width=True)

    with st.spinner('Classifying...'):
        temp_file = "temp_image.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_data)

        prediction, confidence = predict_image(temp_file)
        st.write(f"Prediction: {prediction}")
        st.write(f"Confidence: {confidence:.2f}")



