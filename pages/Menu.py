import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define the navigation menu items
MENU_ITEMS = [
    "Home",
    "About",
    "Contact",
    "Larval Diseases",
    "Pupae Defects",
    "Butterfly Life Cycle",
    "Breeders",
    "Breeders Income",
    "Butterfly",
    "Butterfly Data",
    "Care Management",
    "Classification",
    "Classifier",
    "Classify Diseases",
    "CNN Classifier",
    "Countdown",
    "Defects",
    "Diseases",
    "Example",
    "Hostplants",
    "Larval Disease",
    "Life Stages",
    "Menu",
    "OpenCV",
    "Purchasers",
    "Stages",
    "Tasks",
    "Transfer Learning",
]

# Define functions to display content for each section
def display_home():
    st.title("🦋 Welcome to the Butterfly App")
    st.write("This app provides information about butterflies and their care.")

def display_about():
    st.title("About Butterflies")
    st.write("Butterflies are fascinating insects with a complex life cycle.")
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/6/68/Butterfly_beauty_01.jpg",
        caption="Beautiful Butterfly",
    )

def display_contact():
    st.title("Contact Us")
    st.write("If you have any questions, please contact us at contact@butterflyapp.com")

def display_larval_diseases():
    st.title("Larval Diseases")
    st.write("Learn about common diseases that affect butterfly larvae.")
    larval_disease_names = ["Anaphylaxis Infection", "Gnathostomiasis", "Nucleopolyhedrosis"]
    number_of_cases = [120, 220, 50]

    st.subheader("Disease Cases")
    df_diseases = pd.DataFrame({"Disease Name": larval_disease_names, "Number of Cases": number_of_cases})
    st.write(df_diseases)

    # Plotting
    st.subheader("Disease Distribution")
    fig, ax = plt.subplots()
    sns.barplot(x="Disease Name", y="Number of Cases", data=df_diseases, palette="viridis", ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

def display_pupae_defects():
    st.title("Pupae Defects")
    st.write("Discover the different types of defects that can occur in pupae.")
    pupae_defects_names = ["Ant bites", "Deformed body", "Healthy Pupae", "Old Pupa", "Overbend", "Stretch abdomen"]
    number_of_defects = [50, 30, 200, 25, 15, 40]

    st.subheader("Defect Cases")
    df_defects = pd.DataFrame(
        {"Defect Type": pupae_defects_names, "Number of Defects/Healthy": number_of_defects}
    )
    st.write(df_defects)

    # Plotting
    st.subheader("Defect Distribution")
    fig, ax = plt.subplots()
    sns.barplot(x="Defect Type", y="Number of Defects/Healthy", data=df_defects, palette="magma", ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

def display_butterfly():
    st.title("Butterfly Data")
    st.write("Explore data related to various butterfly and moth species.")

    # Corrected data structure for the DataFrame.  It was not correctly formed.
    species_of_butterfly = [
        "Butterfly-Clippers",
        "Butterfly-Common Jay",
        "Butterfly-Common Lime",
        "Butterfly-Common Mime",
        "Butterfly-Common Mormon",
        "Butterfly-Emerald Swallowtail",
        "Butterfly-Golden Birdwing",
        "Butterfly-Gray Glassy Tiger",
        "Butterfly-Great Eggfly",
        "Butterfly-Great Yellow Mormon",
        "Butterfly-Paper Kite",
        "Butterfly-Pink Rose",
        "Butterfly-Plain Tiger",
        "Butterfly-Red Lacewing",
        "Butterfly-Scarlet Mormon",
        "Butterfly-Tailed Jay",
        "Moth-Atlas",
        "Moth-Giant Silk",
    ]
    total_number_of_images = [250, 340, 230, 500, 200, 100, 50, 75, 120, 90, 110, 80, 130, 60, 100, 40, 30, 20]  # Added data to match

    st.subheader("Species Information")
    df_butterfly = pd.DataFrame({"Species": species_of_butterfly, "Number of Images": total_number_of_images})

    with st.expander("Data"):
        st.write("**Raw Data**")
        try:
            df = pd.read_csv("./data/butterfly_data.csv")
            st.write(df)
        except FileNotFoundError:
            st.error("butterfly_data.csv not found at the specified path.")
            df = None  # Set df to None to prevent errors later

    # Plotting
    st.subheader("Species Distribution")
    if df is not None:  # only plot if the dataframe was loaded
        fig, ax = plt.subplots()
        sns.barplot(x="Species", y="Number of Images", data=df_butterfly, palette="viridis", ax=ax)
        plt.xticks(rotation=45, ha="right")  # Rotate x-axis labels for readability
        plt.tight_layout()  # Prevent labels from getting cut off
        st.pyplot(fig)

    st.write(df_butterfly)


def display_butterfly_life_cycle():
    st.title("Butterfly Life Cycle")
    st.write("Explore the stages of a butterfly's life cycle.")
    life_cycle = ["Pupae", "Larvae", "Eggs", "Butterflies"]
    number_of_stages = [250, 340, 230, 500]
    st.subheader("Life Stages")
    df_stages = pd.DataFrame({"Stages Type": life_cycle, "Number of Stages": number_of_stages})
    with st.expander("Data"):
        st.write("**Raw Data**")
        try:
            df = pd.read_csv("./data/Stages.csv")
            st.write(df)
        except FileNotFoundError:
            st.error("Stages.csv not found at the specified path.")

    # Plotting
    st.subheader("Butterfly Life Cycle Distribution")
    fig, ax = plt.subplots()
    sns.barplot(x="Stages Type", y="Number of Stages", data=df_stages, palette="viridis", ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

    st.write(df_stages)


# Define a CSV file name to store the tasks data
csv_file = "./data/tasks.csv"
care_csv_file = "./data/care_data.csv"  # Define CSV for care data


def display_task():
    # Initialize session state for tasks and care data if not already initialized
    if "tasks" not in st.session_state:
        st.session_state.tasks = []
    if "care_data" not in st.session_state:
        st.session_state.care_data = []

    # Define the list of butterfly species
    species_list = [
        "Butterfly-Clippers",
        "Butterfly-Common Jay",
        "Butterfly-Common Lime",
        "Butterfly-Common Mime",
        "Butterfly-Common Mormon",
        "Butterfly-Emerald Swallowtail",
        "Butterfly-Golden Birdwing",
        "Butterfly-Gray Glassy Tiger",
        "Butterfly-Great Eggfly",
        "Butterfly-Great Yellow Mormon",
        "Butterfly-Paper Kite",
        "Butterfly-Pink Rose",
        "Butterfly-Plain Tiger",
        "Butterfly-Red Lacewing",
        "Butterfly-Scarlet Mormon",
        "Butterfly-Tailed Jay",
        "Moth-Atlas",
        "Moth-Giant Silk",
    ]
    # --- Sidebar Menu ---
    st.sidebar.title("Task Management")
    menu_selection = st.sidebar.radio(
        "Choose an action",
        [
            "Register Task",
            "View Tasks",
            "View Task Distribution",
            "Record Care Activity",
            "View Care Activities",
        ],
    )

    # --- Main Content Area ---
    if menu_selection == "Register Task":
        # Task Registration Form
        st.title("Task Registration")

        # Input fields for task registration
        day = st.date_input("Select the Day")
        hour = st.time_input("Select the Hour")
        activity = st.selectbox(
            "Choose Activity Type",
            [
                "Harvesting Pupae and Eggs",
                "Feeding Larvae",
                "Butterfly Foraging",
            ],
        )
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
                st.session_state.tasks.append(new_task)  # Ensure task is added even if CSV save fails

    elif menu_selection == "View Tasks":
        # Display Tasks
        st.title("View Tasks")
        if st.session_state.tasks:
            df_tasks = pd.DataFrame(st.session_state.tasks)
            st.dataframe(df_tasks)  # Display as a DataFrame
        else:
            st.info("No tasks registered yet.")

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
            st.info("No tasks registered yet.")

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
            # save care data
            try:
                df_care = pd.DataFrame(st.session_state.care_data)
                df_care.to_csv(care_csv_file, index=False)
                st.success(f"Care activity saved to {care_csv_file}")  # Add success message for saving
            except Exception as e:
                st.error(f"Error saving care data to CSV: {e}")

    elif menu_selection == "View Care Activities":
        # View Care Activities
        st.title("View Care Activities")
        if st.session_state.care_data:
            df_care = pd.DataFrame(st.session_state.care_data)
            st.dataframe(df_care)
        else:
            st.info("No care activities recorded yet.")


# Create a dictionary to map menu items to their corresponding functions
MENU_FUNCTIONS = {
    "Home": display_home,
    "About": display_about,
    "Contact": display_contact,
    "Larval Diseases": display_larval_diseases,
    "Pupae Defects": display_pupae_defects,
    "Butterfly": display_butterfly,
    "Butterfly Life Cycle": display_butterfly_life_cycle,
    "Task Management": display_task,
    # Add other menu items and their corresponding functions here
}

# Create the sidebar menu
st.sidebar.title("Navigation")
selected_item = st.sidebar.selectbox("Choose an option", MENU_ITEMS)

# Display the content based on the selected item
if selected_item in MENU_FUNCTIONS:
    MENU_FUNCTIONS[selected_item]()
else:
    st.write(f"Content for '{selected_item}' is not yet implemented.")
