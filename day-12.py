import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(layout='wide')
st.title('Day 12 st.checkbox()')
st.write('#30DaysOfStreamlit')


st.header('List of Chart')
st.write('Choose a chart that you think is interesting')
line = st.checkbox('Line Chart')
simple = st.checkbox('Area Chart')
bar = st.checkbox('Bar Chart')

data = pd.DataFrame(np.random.randn(50, 2), columns=['A', 'B'])
chart = [line, simple, bar]
col = len(list(filter(lambda x: x, chart))) 
if col == 3:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.line_chart(data)
    with col2:
        st.area_chart(data)
    with col3:
        st.bar_chart(data)

if col != 3:
    if line:
        st.line_chart(data)

    if simple:
        st.area_chart(data)

    if bar:
        st.bar_chart(data)