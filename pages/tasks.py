import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Create a list to store tasks
tasks = []

# Input fields
st.title("Task Registration and Visualization")
day = st.date_input("Select the Day")
hour = st.time_input("Select the Hour")
activity = st.selectbox("Choose Activity Type", 
                        ["Harvesting Pupae and Eggs", 
                         "Feeding Larvae", 
                         "Butterfly Foraging"])
details = st.text_input("Butterfly Details")

# Add Task Button
if st.button("Add Task"):
    task = {
        "Day": str(day),
        "Hour": str(hour),
        "Activity": activity,
        "Details": details
    }
    tasks.append(task)
    st.success(f"Task added: {task}")

# Display Registered Tasks
if tasks:
    st.subheader("Registered Tasks:")
    for idx, task in enumerate(tasks, start=1):
        st.write(f"{idx}. {task}")
    
    # Convert to DataFrame for Plotting
    task_df = pd.DataFrame(tasks)

    # Plot the data
    st.subheader("Task Visualization")
    fig, ax = plt.subplots()
    task_df["Activity"].value_counts().plot(kind='bar', ax=ax)
    ax.set_title("Task Distribution")
    ax.set_xlabel("Activity Type")
    ax.set_ylabel("Count")
    st.pyplot(fig)
