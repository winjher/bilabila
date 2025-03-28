import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
butterfly_data = {
    'Butterfly Species': [
        "BATWING", "ATLAS MOTH", "RED LACEWING", "COMMON MIME", "PLAIN TIGER", "TAILED JAY",
        "COMMON JAY", "GREAT EGGFLY", "PAPER KITE", "PINK ROSE", "COMMON LIME", "EMERALD SWALLOWTAIL",
        "GREAT YELLOW MORMON", "COMMON MORMON", "SCARLET MORMON", "GIANT SILK MOTH", "CLIPPER", "GOLDEN BIRDWING"
    ],
    'Total Inspected': [
        150, 200, 120, 170, 130, 160, 180, 140, 190, 155, 165, 175, 185, 195, 135, 145, 125, 210
    ],
    'Defects Detected': [
        5, 10, 4, 7, 3, 6, 9, 5, 8, 7, 6, 4, 5, 8, 3, 6, 2, 9
    ]
}

# Create DataFrame
df = pd.DataFrame(butterfly_data)

# Calculate defect rate
df['Defect Rate (%)'] = (df['Defects Detected'] / df['Total Inspected']) * 100

# Streamlit app
st.title("Butterfly Species Quality Check Analysis")

# Display data
st.header("Data Overview")
st.write(df)

# Descriptive statistics
st.header("Descriptive Statistics")
st.write(df.describe())

# Bar plot of defects detected by butterfly species
st.header("Defects Detected by Butterfly Species")
plt.figure(figsize=(12, 8))
sns.barplot(x='Butterfly Species', y='Defects Detected', data=df, palette='viridis')
plt.title('Defects Detected by Butterfly Species')
plt.xlabel('Butterfly Species')
plt.ylabel('Defects Detected')
plt.xticks(rotation=90)
st.pyplot(plt)

# Bar plot of defect rates by butterfly species
st.header("Defect Rate (%) by Butterfly Species")
plt.figure(figsize=(12, 8))
sns.barplot(x='Butterfly Species', y='Defect Rate (%)', data=df, palette='magma')
plt.title('Defect Rate (%) by Butterfly Species')
plt.xlabel('Butterfly Species')
plt.ylabel('Defect Rate (%)')
plt.xticks(rotation=90)
st.pyplot(plt)

# Box plot to understand the distribution of defect rates
st.header("Distribution of Defect Rates (%)")
plt.figure(figsize=(10, 6))
sns.boxplot(y='Defect Rate (%)', data=df, palette='Set2')
plt.title('Distribution of Defect Rates (%)')
plt.ylabel('Defect Rate (%)')
st.pyplot(plt)
