import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Function to display content for each menu item
def display_content(item):
    if item == "Home":
        st.title("Welcome to the Butterfly App")
        st.write("This app provides information about butterflies and their care.")
    elif item == "About":
        st.title("About Butterflies")
        st.write("Butterflies are fascinating insects with a complex life cycle.")
        st.image("https://upload.wikimedia.org/wikipedia/commons/6/68/Butterfly_beauty_01.jpg", caption="Beautiful Butterfly")
    elif item == "Contact":
        st.title("Contact Us")
        st.write("If you have any questions, please contact us at contact@butterflyapp.com")
    elif item == "Larval Diseases":
        st.title("Larval Diseases")
        st.write("Learn about common diseases that affect butterfly larvae.")
        larval_disease_names = ['Anaphylaxis Infection', 'Gnathostomiasis', 'Nucleopolyhedrosis']
        number_of_cases = [120,220, 50]

        st.subheader("Disease Cases")
        df_diseases = pd.DataFrame({
            'Disease Name': larval_disease_names,
            'Number of Cases': number_of_cases
        })
        st.write(df_diseases)

        # Plotting
        st.subheader("Disease Distribution")
        fig, ax = plt.subplots()
        sns.barplot(x='Disease Name', y='Number of Cases', data=df_diseases, palette='viridis', ax=ax)
        plt.xticks(rotation=45)
        st.pyplot(fig)

    elif item == "Pupae Defects":
        st.title("Pupae Defects")
        st.write("Discover the different types of defects that can occur in pupae.")
        pupae_defects_names = ['Ant bites', 'Deformed body', 'Healthy Pupae', 'Old Pupa', 'Overbend', 'Stretch abdomen']
        number_of_defects = [50, 30, 200, 25, 15, 40]

        st.subheader("Defect Cases")
        df_defects = pd.DataFrame({
            'Defect Type': pupae_defects_names,
            'Number of Defects/Healthy': number_of_defects
        })
        st.write(df_defects)

        # Plotting
        st.subheader("Defect Distribution")
        fig, ax = plt.subplots()
        sns.barplot(x='Defect Type', y='Number of Defects/Healthy', data=df_defects, palette='magma', ax=ax)
        plt.xticks(rotation=45)
        st.pyplot(fig)

    elif item == "Butterfly Life Cycle":
        st.title("Butterfly Life Cycle")
        st.write("Explore the stages of a butterfly's life cycle.")
        # st.image("https://upload.wikimedia.org/wikipedia/commons/1/19/Life_cycle_of_butterflies.jpg", caption="Butterfly Life Cycle")
        life_cycle=['Pupae','Larvae','Eggs','Butterflies']
        number_of_stages=[250,340,230,500]
        st.subheader("Life Stages")
        df_stages = pd.DataFrame({
            'Stages Type': life_cycle,
            'Number of Stages': number_of_stages,
        })
       
        # Plotting
        st.subheader("Butterfly Life Cycle")
        fig, ax = plt.subplots()
        sns.barplot(x='Stages Type', y='Number of Stages', data=df_stages, palette='viridis', ax=ax)
        plt.xticks(rotation=45)
        st.pyplot(fig)

        st.write(df_stages)
        # Create the sidebar menu
        st.sidebar.title("Navigation")
            # Define the navigation menu items


selected_item = st.sidebar.selectbox("Choose an option", menu_items)

# Display the content based on the selected item
display_content(selected_item)
