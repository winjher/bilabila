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
st.header('Butterfly and its host plants')

butterfly_names = ['Butterfly-Clippers',
 'Butterfly-Common Jay',
 'Butterfly-Common Lime',
 'Butterfly-Common Mime',
 'Butterfly-Common Mormon',
 'Butterfly-Emerald Swallowtail',
 'Butterfly-Golden Birdwing',
 'Butterfly-Gray Glassy Tiger',
 'Butterfly-Great Eggfly',
 'Butterfly-Great Yellow Mormon',
 'Butterfly-Paper Kite',
 'Butterfly-Pink Rose',
 'Butterfly-Plain Tiger',
 'Butterfly-Red Lacewing',
 'Butterfly-Scarlet Mormon',
 'Butterfly-Tailed Jay',
 'Moth-Atlas',
 'Moth-Giant Silk ']


model = load_model('./model/Butterfly_Model.h5')
st.success("Model loaded successfully.")

# Function to classify images
def classify_images(image_path):
    input_image = tf.keras.utils.load_img(image_path, target_size=(180, 180))
    input_image_array = tf.keras.utils.img_to_array(input_image)
    input_image_exp_dim = tf.expand_dims(input_image_array, 0)
    predictions = model.predict(input_image_exp_dim)
    result = tf.nn.softmax(predictions[0])
    outcome = 'The Image belongs to ' + butterfly_names[np.argmax(result)] + ' with a score of ' + str(np.max(result) * 100)
    return outcome, np.argmax(result)

# Sidebar file uploader
uploaded_file = st.sidebar.file_uploader('Upload an Image')
if uploaded_file is not None:
    with open(os.path.join('upload', uploaded_file.name), 'wb') as f:
        f.write(uploaded_file.getbuffer())

    st.image(uploaded_file, width=200)
    outcome, label = classify_images(uploaded_file)
    st.markdown(outcome)

    if st.sidebar.button('Show Hostplants'):
        hostplants_info = {
            0: "Wild Cucumber.",
            1: "'Avocado Tree', 'Soursop', 'Sugar Apple', 'Amuyon', 'Indian Tree'.",
            2: "'Limeberry', 'Calamondin', 'Pomelo', 'Sweet Orange', 'Calamansi'.",
            3: "'Clover Cinnamon', 'Wild Cinnamon",
            4: "'Limeberry', 'Calamondin', 'Pomelo', 'Sweet Orange', 'Calamansi', 'Lemoncito'.",
            5: "'Curry Leafs', 'Pink Lime-Berry Tree'.",
            6: "'Dutchman Pipe', 'Indian Birthwort'",
            7: "'Limeberry', 'Calamondin', 'Pomelo', 'Sweet Orange', 'Calamansi'.",
            8: "Dutchman Pipe', 'Indian Birthwort'",
            9: "'Sweet Potato', 'Water Spinach'",
            10:"'Common Skillpod'",
            11:"'Dutchman Pipe', 'Indian Birthwort'",
            12:"'Crown flower', 'Giant Milkweed'",
            13:"'Wild Bush Passion Fruits'",
            14:"'Calamondin', 'Pomelo', 'Sweet Orange', 'Calamansi'",
            15:"'Avocado Tree', 'Soursop', 'Sugar Apple', 'Amuyon', 'Indian Tree'",
            16:"'Gmelina Tree', 'Soursop'",
            17:"'Curry Leafs'"
        }
        st.markdown(hostplants_info[label])

# Function to evaluate model on validation data
def evaluate_model():
    # Path to validation dataset
    base_dir = 'C:/Users/jerwin/Documents/butterfly_photos/butterfly'
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
    report = classification_report(val_labels, val_predictions_labels, target_names=butterfly_names[:len(np.unique(val_labels))], output_dict=True)
    precision = report['macro avg']['precision']
    recall = report['macro avg']['recall']

    # Display confusion matrix
    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=butterfly_names[:len(np.unique(val_labels))], yticklabels=butterfly_names[:len(np.unique(val_labels))], ax=ax)
    ax.set_xlabel('Predicted')
    ax.set_ylabel('Actual')
    st.pyplot(fig)

    # Display precision and recall
    st.write(f'Precision: {precision:.2f}')
    st.write(f'Recall: {recall:.2f}')

# Button to evaluate model
if st.sidebar.button('Evaluate Model'):
    evaluate_model()
