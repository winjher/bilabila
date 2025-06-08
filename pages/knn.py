import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import io

# Load the pre-trained model
model = tf.keras.models.load_model('./model/model_Larval_Diseases.h5') # Replace 'model.h5' with your model file

# Class labels (must match your model's output)
#classes = ["Butterfly", "Pupae", "Larvae", "Eggs","Disease","Defects","Atlas","Batwing","Clippers","Common Jay", "Common Lime","Common Mime","Common Mormon","Emerald Swallow Tail","Giant Silk Moth","Golden Birdwing","Grey Glassy Tiger","Great Eggfly","Great Yellow Mormon","Paper Kite","Pink Rose","Plain Tiger","Red Lacewing","Scarlet Mormon","Tailed Jay","Antbite","Deformed","Old","Overbend","Stetched","Healthy Pupae","Nuclear Polyhedrosis Virus","Baculo Viruses","Ophryocystis  Elektroscirrah","Tachinid Flies","Trichogramma Wasps","Healthy Larvae"]
larval_disease_names =['Anaphylaxis Infection', 'Gnathostomiasis', 'Nucleopolyhedrosis']
# Streamlit app
st.title("Larval Disease Classification")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Image preprocessing (adapt this to your model's requirements)
    image = Image.open(uploaded_file)
    image = image.resize((192, 192)) # Resize to match your model's input shape
    image_array = np.array(image) / 255.0 # Normalize pixel values
    image_array = np.expand_dims(image_array, axis=0) # Add batch dimension

    # Prediction
    predictions = model.predict(image_array)
    predicted_class_index = np.argmax(predictions[0])
    predicted_class = larval_disease_names[predicted_class_index]
    probability = predictions[0][predicted_class_index]

    # Display results
    st.image(image, caption='Uploaded Image')
    st.write(f"Prediction: {predicted_class}")
    st.write(f"Probability: {probability:.2f}")
