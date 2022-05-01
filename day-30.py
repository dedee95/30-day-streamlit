import requests
import streamlit as st
from streamlit_lottie import st_lottie

# ---- LOAD ASSETS ----
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

load_lottie= load_lottieurl("https://assets8.lottiefiles.com/private_files/lf30_cwyafad8.json")
st_lottie(load_lottie, height=200, key='imageyt')

st.header('🖼️ YouTube Thumbnail Image Extractor App')

# Image settings
st.sidebar.header('Settings')
img_dict = {'Max': 'maxresdefault', 'High': 'hqdefault', 'Medium': 'mqdefault', 'Standard': 'sddefault'}
selected_img_quality = st.sidebar.selectbox('Select image quality', ['Max', 'High', 'Medium', 'Standard'])
img_quality = img_dict[selected_img_quality]

yt_url = st.text_input('Paste YouTube URL')
def get_ytid(input_url):
    if 'youtu.be' in input_url:
        ytid = input_url.split('/')[-1]
    if 'youtube.com' in input_url:
        ytid = input_url.split('=')[-1]
    return ytid

# Display YouTube thumbnail image
if yt_url != '':
    ytid = get_ytid(yt_url) # yt or yt_url
    yt_img = f'http://img.youtube.com/vi/{ytid}/{img_quality}.jpg'
    st.image(yt_img)
    st.write('YouTube video thumbnail image URL: ', yt_img)
else:
    st.write('☝️ Enter URL to continue ...')