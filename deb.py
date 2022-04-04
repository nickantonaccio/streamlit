import streamlit as st

howmuch = st.slider('How much do you dig Nick?', 0, 100)
if howmuch:
    st.write('You dig nick: ', howmuch)

d = st.date_input(
    "Please pick tomorrow's date",
)
if d:
    st.write('Deb will still be totally awesome on: ', d)

picture = st.camera_input("Take a picture")
if picture:
    st.image(picture)
