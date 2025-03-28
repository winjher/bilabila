
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
data = {
    'Breeder': ['Breeder 1', 'Breeder 2', 'Breeder 3', 'Breeder 4', 'Breeder 5'],
    'Monthly Income': [5000, 7000, 3000, 6000, 4000],
    'Monthly Activity (Hours)': [120, 150, 100, 130, 110],
    'Quality Score': [85, 90, 75, 88, 80]
}

# Create DataFrame
df = pd.DataFrame(data)

# Streamlit app
st.title("Breeder Data Analysis and Visualization")

# Display basic information about the data
st.header("Data Overview")
st.write(df)
st.write("Basic information about the dataset:")
st.write(df.info())
st.write("Descriptive statistics:")
st.write(df.describe())

# Bar plot of monthly income
st.header("Monthly Income by Breeder")
plt.figure(figsize=(10, 6))
sns.barplot(x='Breeder', y='Monthly Income', data=df, palette='Blues_d')
plt.title('Monthly Income by Breeder')
plt.xlabel('Breeder')
plt.ylabel('Monthly Income')
st.pyplot(plt)

# Bar plot of monthly activity
st.header("Monthly Activity (Hours) by Breeder")
plt.figure(figsize=(10, 6))
sns.barplot(x='Breeder', y='Monthly Activity (Hours)', data=df, palette='Greens_d')
plt.title('Monthly Activity (Hours) by Breeder')
plt.xlabel('Breeder')
plt.ylabel('Monthly Activity (Hours)')
st.pyplot(plt)

# Bar plot of quality score
st.header("Quality Score by Breeder")
plt.figure(figsize=(10, 6))
sns.barplot(x='Breeder', y='Quality Score', data=df, palette='Reds_d')
plt.title('Quality Score by Breeder')
plt.xlabel('Breeder')
plt.ylabel('Quality Score')
st.pyplot(plt)

# Pair plot to explore relationships between variables
st.header("Pair Plot of Breeder Data")
sns.pairplot(df, diag_kind='kde', markers='+')
plt.suptitle('Pair Plot of Breeder Data', y=1.02)
st.pyplot(plt)