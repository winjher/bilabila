import streamlit as st

st.title('🦋 Bilabila Machine Learning App')

st.info('This is app builds a Machine Learning Model')

df=pd.read_csv("https://github.com/winjher/bilabila/blob/master/Data/butterfly_data.csv")
df
