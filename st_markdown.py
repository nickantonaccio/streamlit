import streamlit as st, sqlite3
con=sqlite3.connect('markdown.db')
cur=con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS db(name TEXT, code TEXT)')

if st.button('Add New Row'):
  cur.execute('INSERT INTO db(name, code) VALUES(?,?)', ('',''))
  con.commit()

for row in cur.execute('SELECT rowid, name, code FROM db ORDER BY name'):
  with st.form(f'ID-{row[0]}'):
    name=st.text_input('Name', row[1])
    code=st.text_area('Code', row[2])
    if st.form_submit_button('Save and View'):
      cur.execute(
        'UPDATE db SET name=?, code=? WHERE rowid=?;', 
        (name, code, str(row[0]))
      )
      con.commit() ; st.experimental_rerun()
    if st.form_submit_button("Delete"):
      cur.execute(f'DELETE FROM db WHERE rowid="{row[0]}";')
      con.commit() ; st.experimental_rerun()
    st.markdown(code)
