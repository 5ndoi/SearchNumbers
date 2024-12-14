import streamlit as st
import cv2
import numpy as np

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# マウス座標
mouse_x, mouse_y = -1, -1

# マウスのコールバック関数
def mouse_callback(event, x, y, flags, param):
    global mouse_x, mouse_y
    if event == cv2.EVENT_MOUSEMOVE:
        cv2.circle(img, (x, y), 1, (0, 255, 255), -1)

img = np.full((800,800,3), 0)
window = st.empty()

while True:
    cv2.setMouseCallback("FaceMesh", mouse_callback)
    window.image(img)

