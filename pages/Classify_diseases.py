import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os

# Streamlit Title
st.title("Larval Disease Prediction with CNN")

# GPU Options Configuration
st.sidebar.header("GPU Options")
gpu_growth = st.sidebar.checkbox("Allow GPU growth?", value=True)

if gpu_growth:
    config = tf.compat.v1.ConfigProto()
    config.gpu_options.allow_growth = True
    session = tf.compat.v1.InteractiveSession(config=config)
    tf.compat.v1.disable_eager_execution()

# CNN Model Initialization
st.header("Initialize and Compile the CNN Model")

classifier = Sequential()
classifier.add(Conv2D(32, (3, 3), input_shape=(128, 128, 3), activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2)))
classifier.add(Conv2D(32, (3, 3), activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2)))
classifier.add(Flatten())
classifier.add(Dense(units=128, activation='relu'))
classifier.add(Dense(units=3, activation='sigmoid'))

classifier.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
st.success("CNN Model Compiled Successfully!")

# Data Augmentation and Directory Inputs
st.header("Prepare Training and Validation Data")

train_dir = st.text_input("C:/Users/jerwin/Documents/GitHub/butterfly_photos/larval diseases/train")
val_dir = st.text_input("C:/Users/jerwin/Documents/GitHub/butterfly_photos/larval diseases/val")

if train_dir and val_dir:
    train_datagen = ImageDataGenerator(rescale=1./255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
    test_datagen = ImageDataGenerator(rescale=1./255)

    try:
        training_set = train_datagen.flow_from_directory(
            train_dir,
            target_size=(128, 128),
            batch_size=6,
            class_mode='categorical'
        )
        valid_set = test_datagen.flow_from_directory(
            val_dir,
            target_size=(128, 128),
            batch_size=3,
            class_mode='categorical'
        )
        st.success("Data Loaded Successfully!")
        st.write("Class Labels:", training_set.class_indices)
    except Exception as e:
        st.error(f"Error loading data: {e}")

# Training the CNN Model
if st.button("Train CNN"):
    if train_dir and val_dir:
        classifier.fit_generator(
            training_set,
            steps_per_epoch=20,
            epochs=50,
            validation_data=valid_set
        )
        st.success("Model Training Completed!")

# Save the Model
if st.button("Save Model"):
    model_path = st.text_input(
        "Enter the path to save the model (e.g., ./disease_model.h5):",
        key="save_model_path"
    )
    if model_path:
        classifier.save(model_path)
        st.success(f"Model saved to {model_path}")

