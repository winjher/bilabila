import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
pupae_defects_data = {
    'Defect Type': [
        'Ant bites', 'Deformed body', 
        'Healthy Pupae', 'Old Pupa', 'Overbend', 'Stretch abdomen'
    ],
    'Number of Defects': [50, 30, 200, 25, 15, 40]
}

# Create DataFrame
df = pd.DataFrame(pupae_defects_data)

# Streamlit app
st.title("Pupae Defects Data Analysis and Visualization")

# Display data
st.header("Data Overview")
st.write(df)

# Descriptive statistics
st.header("Descriptive Statistics")
st.write(df.describe())

# Bar plot of number of defects by defect type
st.header("Number of Defects by Defect Type")
plt.figure(figsize=(12, 8))
sns.barplot(x='Defect Type', y='Number of Defects', data=df, palette='viridis')
plt.title('Number of Defects by Defect Type')
plt.xlabel('Defect Type')
plt.ylabel('Number of Defects')
plt.xticks(rotation=45)
st.pyplot(plt)

# Pie chart of defect distribution
st.header("Defect Distribution")
plt.figure(figsize=(10, 6))
plt.pie(df['Number of Defects'], labels=df['Defect Type'], autopct='%1.1f%%', startangle=140, colors=sns.color_palette('viridis', len(df)))
plt.title('Defect Distribution')
st.pyplot(plt)

# Box plot to understand the distribution of number of defects
st.header("Distribution of Number of Defects")
plt.figure(figsize=(10, 6))
sns.boxplot(y='Number of Defects', data=df, palette='Set2')
plt.title('Distribution of Number of Defects')
plt.ylabel('Number of Defects')
st.pyplot(plt)
