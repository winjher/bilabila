import streamlit as st
import pandas as pd

st.title('🦋 Bilabila Machine Learning App')

st.info('This is app builds a Machine Learning Model')

with st.Expander('Data'):
  st.write('**Raw Data**')
  df = pd.read_csv('https://github.com/winjher/bilabila/blob/master/Data/butterfly_data.csv')
  df
