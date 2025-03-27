import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
larval_disease_data = {
    'Disease Name': [
        'Anaphylaxis Infection',
        'Gnats Disease',
        'Tachinid Disease'
    ],
    'Number of Cases': [120, 220, 50]
}

# Create DataFrame
df = pd.DataFrame(larval_disease_data)

# Streamlit app
st.title("Larval Disease Data Analysis and Visualization")

# Display data
st.header("Data Overview")
st.write(df)

# Descriptive statistics
st.header("Descriptive Statistics")
st.write(df.describe())

# Bar plot of number of cases by disease
st.header("Number of Cases by Disease")
plt.figure(figsize=(12, 8))
sns.barplot(x='Disease Name', y='Number of Cases', data=df, palette='viridis')
plt.title('Number of Cases by Disease')
plt.xlabel('Disease Name')
plt.ylabel('Number of Cases')
plt.xticks(rotation=45)
st.pyplot(plt)

# Pie chart of disease distribution
st.header("Disease Distribution")
plt.figure(figsize=(10, 6))
plt.pie(df['Number of Cases'], labels=df['Disease Name'], autopct='%1.1f%%', startangle=140, colors=sns.color_palette('viridis', len(df)))
plt.title('Disease Distribution')
st.pyplot(plt)

# Box plot to understand the distribution of number of cases
st.header("Distribution of Number of Cases")
plt.figure(figsize=(10, 6))
sns.boxplot(y='Number of Cases', data=df, palette='Set2')
plt.title('Distribution of Number of Cases')
plt.ylabel('Number of Cases')
st.pyplot(plt)
