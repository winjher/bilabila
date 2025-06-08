import streamlit as st
import pandas as pd

st.title('🦋 Bilabila Machine Learning App')

st.info('This is app builds a Machine Learning Model')

with st.expander('Data'):
  st.write('**Raw Data**')
  df = pd.read_csv('C:/Users/jerwin/Documents/GitHub/butterfly_photos/data/butterfly_data.csv')
  df

st.write('**X**')
x = df.drop('Species', axis=1)
x

st.write('**y**')
y = df.Species
y

with st.expander('Data visualization'):
  st.scatter_chart(data=df,x='Wingspan_mm', y='Hindwing',color='Place')

#Data preparations
with st.sidebar:
   st.header('Input features')
   Place=st.selectbox('Place','Lepidoptera')