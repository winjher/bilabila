import os
import keras
from keras.models import load_model
import streamlit as st
import tensorflow as tf
import numpy as np
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

# Set up Streamlit interface
st.sidebar.header('Pupae Defects Classification CNN Model')
pupae_defects_names = [
    'Ant bites',
    'Deformed body',
    'Healthy Pupae',
    'Old Pupa',
    'Overbend',
    'Stretch abdomen'
]

# Host plants for butterflies
host_plants = {
    'Ant bites': "Host plant: Acacia",
    'Deformed body': "Host plant: Citrus",
    'Healthy Pupae': "Host plant: Multiple species",
    'Old Pupa': "Host plant: Varied depending on species",
    'Overbend': "Host plant: Different depending on species",
    'Stretch abdomen': "Host plant: Various host plants"
}

# Load model
model = load_model('model/Pupae_Defects_Model.h5')
st.sidebar.success("Model loaded successfully.")

# Function to classify images
def classify_images(image_path):
    input_image = tf.keras.utils.load_img(image_path, target_size=(180, 180))
    input_image_array = tf.keras.utils.img_to_array(input_image)
    input_image_exp_dim = tf.expand_dims(input_image_array, 0)
    predictions = model.predict(input_image_exp_dim)
    result = tf.nn.softmax(predictions[0])
    outcome = 'The Image belongs to ' + pupae_defects_names[np.argmax(result)] + ' with a score of ' + str(np.max(result) * 100)
    return outcome, np.argmax(result)

# Sidebar file uploader
uploaded_file = st.sidebar.file_uploader('Upload an Image')
if uploaded_file is not None:
    with open(os.path.join('upload', uploaded_file.name), 'wb') as f:
        f.write(uploaded_file.getbuffer())

    st.image(uploaded_file, width=200)
    outcome, label = classify_images(uploaded_file)
    st.markdown(outcome)

    if st.sidebar.button('Show Treatment'):
        treatment_info = {
            0: "Treatment for Ant bites...",
            1: "Treatment for Deformed body...",
            2: "Treatment for Golden Birdwing defects pupae...",
            3: "No treatment needed, Golden Birdwing healthy pupae.",
            4: "No treatment needed, Healthy Pupae.",
            5: "Treatment for Old Pupa...",
            6: "Treatment for Overbend...",
            7: "Treatment for Stretch abdomen..."
        }
        st.markdown(treatment_info[label])
    
    # Host plants button
    if st.sidebar.button('Show Host Plants'):
        st.markdown(host_plants[pupae_defects_names[label]])

# Function to evaluate model on validation data
def evaluate_model():
    # Path to validation dataset
    base_dir = 'C:/Users/jerwin/Documents/butterfly_photos/pupae defects'
    batch_size = 32
    img_size = 180

    # Load validation data
    val_ds = tf.keras.utils.image_dataset_from_directory(
        base_dir,
        seed=123,
        validation_split=0.2,
        subset='validation',
        batch_size=batch_size,
        image_size=(img_size, img_size)
    )

    # Get true labels from the validation generator
    val_labels = np.concatenate([y for x, y in val_ds], axis=0)

    # Predict on validation data
    val_predictions = model.predict(val_ds)
    val_predictions_labels = np.argmax(val_predictions, axis=1)

    # Compute confusion matrix
    cm = confusion_matrix(val_labels, val_predictions_labels)

    # Compute metrics
    report = classification_report(val_labels, val_predictions_labels, target_names=pupae_defects_names, output_dict=True)
    precision = report['macro avg']['precision']
    recall = report['macro avg']['recall']

    # Display confusion matrix
    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=pupae_defects_names, yticklabels=pupae_defects_names, ax=ax)
    ax.set_xlabel('Predicted')
    ax.set_ylabel('Actual')
    st.pyplot(fig)

    # Display precision and recall
    st.write(f'Precision: {precision:.2f}')
    st.write(f'Recall: {recall:.2f}')

# Button to evaluate model
if st.sidebar.button('Evaluate Model'):
    evaluate_model()
