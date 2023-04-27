import streamlit as st, dataset
db=dataset.connect('sqlite:///db'); t=db['user']     #t=table
if st.button('Add Row'): t.insert(dict(x='',y=''))   #x,y=name, note
for r in t:                                          #r=row in table
  with st.expander(r['x']):
    with st.form(str(r['id'])):
      x=st.text_input('Name', r['x'])
      y=st.text_area('Note', r['y'])
      if st.form_submit_button('Save'):
        t.update(dict(x=x,y=y,id=r['id']),['id'])
      if st.form_submit_button('Delete'):
        t.delete(id=r['id']); st.experimental_rerun()
