import pandas as pd 
import streamlit as st 
from st_aggrid import AgGrid

st.set_page_config(page_title="Netflix Shows", layout="wide") 
st.title("Netlix shows analysis")

shows = pd.read_csv("./netflix_titles.csv")  

AgGrid(shows)