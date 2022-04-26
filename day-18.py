import streamlit as st
import pandas as pd

st.title('🗓️ Day 18 st.file_uploader()')
st.write('#30DaysOfStreamlit')

st.subheader('Input CSV')
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df = df.drop('Id', axis=1)
    st.subheader('DataFrame')
    st.write(df.head())
    st.subheader('Descriptive Statistics')
    st.write(df.describe())
else:
    st.info('☝️ Upload a CSV file')