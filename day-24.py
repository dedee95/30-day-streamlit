import streamlit as st
import numpy as np
import pandas as pd
from time import time

st.title('🗓️ Day 24 st.cache()')
st.write('#30DaysOfStreamlit')

col1, col2 = st.columns(2)
    
# Using cache
a0 = time()
@st.cache()
def load_data_a():
    df = pd.DataFrame(
        np.random.rand(2000000, 3),
        columns=['a', 'b', 'c']
    )
    return df

# Not using cache
b0 = time()
def load_data_b():
    df = pd.DataFrame(
        np.random.rand(2000000, 3),
        columns=['a', 'b', 'c']
    )
    return df

with col1:
    st.subheader('Using st.cache')
    st.write(load_data_a())
    a1 = time()
    st.info(a1-a0)
with col2:
    st.subheader('Not using st.cache')
    st.write(load_data_b())
    b1 = time()
    st.info(b1-b0)

