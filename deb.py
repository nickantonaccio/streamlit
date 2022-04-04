import streamlit as st

d = st.date_input(
    "When's your birthday",
)
st.write('Your birthday is:', d)

picture = st.camera_input("Take a picture")
if picture:
    st.image(picture)
    st.write('this person is awesome!')
