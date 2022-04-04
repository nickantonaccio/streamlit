import streamlit as st

howmuch = st.slider('How much do you dig Nick?', 0, 100)

d = st.date_input(
    "Please pick tomorrow's date",
)

picture = st.camera_input("Take a picture")
if picture:
    st.image(picture)
    st.write('Deb will still be totally awesome on: ', d)
    st.write('You dig nick: ', howmuch)
