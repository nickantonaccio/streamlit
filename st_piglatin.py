import streamlit as st

text = st.text_area('Type or paste some  text')
if text:
  word_list = text.split(' ')
  pig_latin = ' '
  for word in word_list:
    if word.isalpha():
      pigword = word[1:] + word[0] + 'ay'
      pig_latin = pig_latin + pigword + ' '
    else:
      pig_latin += word
  st.write(pig_latin.strip(' '))
