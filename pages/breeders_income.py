import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# Sample data
breeders = ['Breeder 1', 'Breeder 2', 'Breeder 3', 'Breeder 4', 'Breeder 5']
monthly_income = [5000, 7000, 3000, 6000, 4000]
monthly_activity = [120, 150, 100, 130, 110]
quality_score = [85, 90, 75, 88, 80]

# Create a DataFrame for saving data
data = pd.DataFrame({
    "Breeder": breeders,
    "Monthly Income": monthly_income,
    "Monthly Activity": monthly_activity,
    "Quality Score": quality_score
})

# Streamlit app
st.title("Bar Graph Example")
st.write("Data visualization of breeders' performance.")

# Create the bar graph
fig = go.Figure()
fig.add_trace(go.Bar(name='Monthly Income', x=breeders, y=monthly_income, marker_color='rgba(54, 162, 235, 0.6)'))
fig.add_trace(go.Bar(name='Monthly Activity (Hours)', x=breeders, y=monthly_activity, marker_color='rgba(75, 192, 192, 0.6)'))
fig.add_trace(go.Bar(name='Quality Score', x=breeders, y=quality_score, marker_color='rgba(255, 99, 132, 0.6)'))

fig.update_layout(
    barmode='group',
    title="Performance Metrics",
    xaxis_title="Breeders",
    yaxis_title="Values",
    yaxis=dict(range=[0, max(monthly_income + monthly_activity + quality_score) + 20])
)

st.plotly_chart(fig)

# Save data to CSV functionality
if st.button("Save Data to CSV"):
    data.to_csv("breeders_data.csv", index=False)
    st.success("Data saved to breeders_data.csv!")
