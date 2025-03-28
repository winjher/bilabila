import streamlit as st
import cv2
import numpy as np
import winsound

# Streamlit app setup
st.title("Motion Detection with OpenCV")
st.text("Press 'Start Detection' to activate your camera.")

# Initialize the webcam
start_detection = st.button("Start Detection")

if start_detection:
    st.text("Press 'Q' in the camera window to quit.")

    # Open the webcam (adjust the index if necessary)
    cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        st.error("Error: Camera not accessible!")
    else:
        while cam.isOpened():
            ret, frame1 = cam.read()
            ret, frame2 = cam.read()

            if not ret:
                st.error("Error: Unable to read frames from the camera!")
                break

            diff = cv2.absdiff(frame1, frame2)
            gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
            blur = cv2.GaussianBlur(gray, (5, 5), 0)
            _, thresh = cv2.threshold(blur, 20, 250, cv2.THRESH_BINARY)
            dilated = cv2.dilate(thresh, None, iterations=3)

            contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            for contour in contours:
                if cv2.contourArea(contour) < 500:
                    continue
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)

                # Play sound on motion detection
                winsound.Beep(500, 200)
                winsound.PlaySound("alert.wav", winsound.SND_ASYNC)

            cv2.imshow("Motion Detection", frame1)

            if cv2.waitKey(10) == ord("q"):
                break

        cam.release()
        cv2.destroyAllWindows()
