import streamlit as st
import time

st.title('🗓️ Day 21 st.progress()')
st.write('#30DaysOfStreamlit')

with st.expander('About this app'):
    st.write('this is an application used to wish happy birthday to a precious person')
    global button
    button = st.button('Greetings')

my_bar = st.progress(0)
if button:
    for percent_complete in range(100):
        time.sleep(0.05)
        my_bar.progress(percent_complete + 1)
    
    st.image('https://img.freepik.com/free-vector/happy-birthday-flags-confetti-card_1017-32699.jpg?t=st=1650561599~exp=1650562199~hmac=7d99456f86b925be8fe4420e133a594a9666a1cff1a846ef96434f428e2898e7&w=740')
    st.balloons()


