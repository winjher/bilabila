# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import os

# # Define a CSV file name to store the tasks data
# csv_file = "tasks.csv"

# # Initialize session state to store tasks
# if 'tasks' not in st.session_state:
#     # If the CSV exists, load the tasks. Otherwise, start with an empty list.
#     if os.path.exists(csv_file):
#         st.session_state.tasks = pd.read_csv(csv_file).to_dict('records')
#     else:
#         st.session_state.tasks = []

# # Task Registration Form
# st.title("Task Registration and CSV Persistence")

# # Input fields for task registration
# day = st.date_input("Select the Day")
# hour = st.time_input("Select the Hour")
# activity = st.selectbox("Choose Activity Type", 
#                          ["Harvesting Pupae and Eggs", 
#                           "Feeding Larvae", 
#                           "Butterfly Foraging"])
# details = st.text_input("Additional Details")

# # Button for adding a task
# if st.button("Add Task"):
#     new_task = {
#         "Day": str(day),
#         "Hour": str(hour),
#         "Activity": activity,
#         "Details": details
#     }
#     # Append the new task to our session state
#     st.session_state.tasks.append(new_task)
#     # Save the updated tasks list to CSV
#     df = pd.DataFrame(st.session_state.tasks)
#     df.to_csv(csv_file, index=False)
#     st.success(f"Task added: {new_task}")

# # Display the registered tasks as a new data table
# if st.session_state.tasks:
#     st.subheader("Registered Tasks for Proper Care Management")
#     df = pd.DataFrame(st.session_state.tasks)
#     st.dataframe(df)

#     # Plotting the distribution of tasks by activity as a bar chart
#     st.subheader("Task Activity Distribution")
#     fig, ax = plt.subplots()
#     df["Activity"].value_counts().plot(kind='bar', ax=ax)
#     ax.set_title("Tasks Distribution by Activity")
#     ax.set_xlabel("Activity")
#     ax.set_ylabel("Count")
#     st.pyplot(fig)

import streamlit as st
import pandas as pd
import os  # Import the os module
import matplotlib.pyplot as plt  # Import matplotlib

# Define a CSV file name to store the tasks data
csv_file = "./data/tasks.csv"
care_csv_file = "./data/care_data.csv" #Define CSV for care data

# Initialize session state to store tasks and care data
if 'tasks' not in st.session_state:
    st.session_state.tasks = []  # Initialize as an empty list
if 'care_data' not in st.session_state:
    st.session_state.care_data = []

# Define the list of butterfly species
species_list = ['Butterfly-Clippers',
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
                'Moth-Giant Silk']

# --- Sidebar Menu ---
st.sidebar.title("Task Management")
menu_selection = st.sidebar.radio("Choose an action",
                                 ["Register Task", "View Tasks", "View Task Distribution", "Record Care Activity", "View Care Activities"])

# --- Main Content Area ---
if menu_selection == "Register Task":
    # Task Registration Form
    st.title("Task Registration")

    # Input fields for task registration
    day = st.date_input("Select the Day")
    hour = st.time_input("Select the Hour")
    activity = st.selectbox("Choose Activity Type",
                                    ["Harvesting Pupae and Eggs",
                                     "Feeding Larvae",
                                     "Butterfly Foraging"])
    details = st.text_input("Additional Details")
    species = st.selectbox("Select Species", species_list)

    # Button for adding a task
    if st.button("Add Task"):
        new_task = {
            "Day": str(day),
            "Hour": str(hour),
            "Activity": activity,
            "Details": details,
            "Species": species,
        }
        # Append the new task to our session state
        st.session_state.tasks.append(new_task)
        # Save the updated tasks list to CSV
        try:
            df = pd.DataFrame(st.session_state.tasks)
            df.to_csv(csv_file, index=False)
            st.success(f"Task added and saved to {csv_file}: {new_task}")
        except Exception as e:
            st.error(f"Error saving task to CSV: {e}. Task added to session, but not saved.")
            st.session_state.tasks.append(new_task)  # Ensure task is added to session state even if CSV save fails.

elif menu_selection == "View Tasks":
    # Display Tasks
    st.title("View Tasks")
    if st.session_state.tasks:
        df_tasks = pd.DataFrame(st.session_state.tasks)
        st.dataframe(df_tasks)  # Display as a DataFrame
    else:
        st.info("No tasks registered yet.") #Change to info

elif menu_selection == "View Task Distribution":
    # Display the registered tasks as a table and plot
    st.title("Task Distribution")
    if st.session_state.tasks:
        df = pd.DataFrame(st.session_state.tasks)
        st.dataframe(df)

        # Plotting the distribution of tasks by activity as a bar chart
        st.subheader("Task Activity Distribution")
        try:
            fig, ax = plt.subplots()
            df["Activity"].value_counts().plot(kind='bar', ax=ax)
            ax.set_title("Tasks Distribution by Activity")
            ax.set_xlabel("Activity")
            ax.set_ylabel("Count")
            st.pyplot(fig)

            # Plotting the distribution of tasks by species as a bar chart
            st.subheader("Task Species Distribution")
            fig_species, ax_species = plt.subplots()
            df["Species"].value_counts().plot(kind='bar', ax=ax_species)
            ax_species.set_title("Tasks Distribution by Species")
            ax_species.set_xlabel("Species")
            ax_species.set_ylabel("Count")
            st.pyplot(fig_species)

        except Exception as e:
            st.error(f"Error creating plot: {e}.")
    else:
        st.info("No tasks registered yet.") #Change to info

elif menu_selection == "Record Care Activity":
    # Record Care Activity
    st.title("Record Care Activity")

    care_day = st.date_input("Select Care Day")
    care_hour = st.time_input("Select Care Hour")
    care_species = st.selectbox("Select Species", species_list)
    care_activity = st.text_input("Care Activity Description")

    if st.button("Record Care"):
        new_care_data = {
            "Day": str(care_day),
            "Hour": str(care_hour),
            "Species": care_species,
            "Activity": care_activity,
        }
        st.session_state.care_data.append(new_care_data)
        st.success(f"Care activity recorded: {new_care_data}")
        #save care data
        try:
            df_care = pd.DataFrame(st.session_state.care_data)
            df_care.to_csv(care_csv_file, index=False)
            st.success(f"Care activity saved to {care_csv_file}") # Add success message for saving
        except Exception as e:
            st.error(f"Error saving care data to CSV: {e}")

elif menu_selection == "View Care Activities":
    # View Care Activities
    st.title("View Care Activities")
    if st.session_state.care_data:
        df_care = pd.DataFrame(st.session_state.care_data)
        st.dataframe(df_care)
    else:
        st.info("No care activities recorded yet.") #Change to info
