import streamlit as st, ast

if 'total' not in st.session_state:
  st.session_state.total=''
if st.button('Clear'): st.session_state.total=''
col1, col2, col3, col4, col5=st.columns([1,1,1,1,4])
if col1.button('1'): st.session_state.total+='1'
if col2.button('2'): st.session_state.total+='2'
if col3.button('3'): st.session_state.total+='3'
if col4.button('+'): st.session_state.total+='+'
if col1.button('4'): st.session_state.total+='4'
if col2.button('5'): st.session_state.total+='5'
if col3.button('6'): st.session_state.total+='6'
if col4.button('-'): st.session_state.total+='-'
if col1.button('7'): st.session_state.total+='7'
if col2.button('8'): st.session_state.total+='8'
if col3.button('9'): st.session_state.total+='9'
if col4.button('.'): st.session_state.total+='.'
if col1.button('0'): st.session_state.total+='0'
if col2.button('*'): st.session_state.total+='*'
if col3.button('/'): st.session_state.total+='/'
if col4.button('='): 
  st.session_state.total=str(eval(st.session_state.total))
st.text_input('Result', st.session_state.total)
