import streamlit as st
import pandas as pd
from streamlit_pandas_profiling import st_profile_report


st.title('Day 14 Streamlit Components')
st.write('#30DaysOfStreamlit')

st.header('Streamlit Pandas Profiling')
df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')

pr = df.profile_report()
st_profile_report(pr)