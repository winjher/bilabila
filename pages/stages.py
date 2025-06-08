import pandas as pd

# Create a DataFrame
# data = {
#     'Stage': ['Pupae', 'Larvae', 'Eggs', 'Butterflies'],
#     'Count': [250, 340, 230, 500]
# }

data ='C:/Users/jerwin/Documents/GitHub/butterfly_photos/data/Data_stages.csv'
data = pd.read_csv(data)
df = pd.DataFrame(data)
print(df)

# Descriptive Statistics
print(df.describe())

#### Bar Plot

import matplotlib.pyplot as plt
import seaborn as sns

# Bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x='Stage', y='Count', data=df, palette='viridis')
plt.title('Count by Stage')
plt.xlabel('Stage')
plt.ylabel('Count')
plt.show()

#### Pie Chart


# Pie chart
plt.figure(figsize=(8, 8))
plt.pie(df['Count'], labels=df['Stage'], autopct='%1.1f%%', startangle=140, colors=sns.color_palette('viridis', len(df)))
plt.title('Distribution of Stages')
plt.show()

### Integrate with Streamlit

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
data = {
    'Stage': ['Pupae', 'Larvae', 'Eggs', 'Butterflies'],
    'Count': [250, 340, 230, 500]
}

# Create DataFrame
df = pd.DataFrame(data)

# Streamlit app
st.title("Butterfly Life Stages Data Analysis and Visualization")

# Display data
st.header("Data Overview")
st.write(df)

# Descriptive statistics
st.header("Descriptive Statistics")
st.write(df.describe())

# Bar plot of counts by stage
st.header("Count by Stage")
plt.figure(figsize=(10, 6))
sns.barplot(x='Stage', y='Count', data=df, palette='viridis')
plt.title('Count by Stage')
plt.xlabel('Stage')
plt.ylabel('Count')
st.pyplot(plt)

# Pie chart of stage distribution
st.header("Distribution of Stages")
plt.figure(figsize=(8, 8))
plt.pie(df['Count'], labels=df['Stage'], autopct='%1.1f%%', startangle=140, colors=sns.color_palette('viridis', len(df)))
plt.title('Distribution of Stages')
st.pyplot(plt)
