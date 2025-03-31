import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Define a CSV file name to store the tasks data
csv_file = "tasks.csv"

# Initialize session state to store tasks
if 'tasks' not in st.session_state:
    # If the CSV exists, load the tasks. Otherwise, start with an empty list.
    if os.path.exists(csv_file):
        st.session_state.tasks = pd.read_csv(csv_file).to_dict('records')
    else:
        st.session_state.tasks = []

# Task Registration Form
st.title("Task Registration and CSV Persistence")

# Input fields for task registration
day = st.date_input("Select the Day")
hour = st.time_input("Select the Hour")
activity = st.selectbox("Choose Activity Type", 
                         ["Harvesting Pupae and Eggs", 
                          "Feeding Larvae", 
                          "Butterfly Foraging"])
details = st.text_input("Additional Details")

# Button for adding a task
if st.button("Add Task"):
    new_task = {
        "Day": str(day),
        "Hour": str(hour),
        "Activity": activity,
        "Details": details
    }
    # Append the new task to our session state
    st.session_state.tasks.append(new_task)
    # Save the updated tasks list to CSV
    df = pd.DataFrame(st.session_state.tasks)
    df.to_csv(csv_file, index=False)
    st.success(f"Task added: {new_task}")

# Display the registered tasks as a new data table
if st.session_state.tasks:
    st.subheader("Registered Tasks for Proper Care Management")
    df = pd.DataFrame(st.session_state.tasks)
    st.dataframe(df)

    # Plotting the distribution of tasks by activity as a bar chart
    st.subheader("Task Activity Distribution")
    fig, ax = plt.subplots()
    df["Activity"].value_counts().plot(kind='bar', ax=ax)
    ax.set_title("Tasks Distribution by Activity")
    ax.set_xlabel("Activity")
    ax.set_ylabel("Count")
    st.pyplot(fig)
