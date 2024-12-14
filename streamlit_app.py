import streamlit as st
import cv2
import numpy as np

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

img = np.full((800,800,3), 255)

st.image(img)