import streamlit as st

st.title('🗓️ Day 17')
st.write('#30DaysOfStreamlit')

st.header('st.secrets()')
st.write("Database username:" ,st.secrets['db_username'])
st.write("Database password:" ,st.secrets['db_password'])
st.write("My cool secrets:", st.secrets["message"]["keyword"])