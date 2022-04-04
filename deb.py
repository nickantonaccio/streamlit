import streamlit as st

howmuch = st.slider('How much do you dig Nick?', 0, 100)
if howmuch:
    st.write('You dig Nick: ', howmuch, '%')

d = st.date_input(
    "Please pick tomorrow's date",
)
if d:
    st.write('Deb will be totally awesome on: ', d)

picture = st.camera_input("Take a picture")
if picture:
    st.write('I dig the following person 100%!')
    st.image(picture)
