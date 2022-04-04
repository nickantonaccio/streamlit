import streamlit as st

st.set_page_config(
    page_title="A/B Testing App", page_icon="📊", initial_sidebar_state="expanded"
)


number = st.slider("Pick a number", 0, 100)

d = st.date_input(
     "When's your birthday",
    # datetime.date(2019, 7, 6))
)
st.write('Your birthday is:', d)

picture = st.camera_input("Take a picture")
if picture:
     st.image(picture)
