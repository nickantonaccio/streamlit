import streamlit as st
import pandas as pd
import numpy as np
st.title('SF Trees')
st.write('This app maps trees in San Francisco from'
	 ' the following dataset (trees.csv):')
trees_df = pd.read_csv('trees.csv')
trees_df = trees_df.dropna(subset=['longitude', 'latitude'])
trees_df = trees_df.sample(n = 1000)
st.write(trees_df)
st.map(trees_df)
