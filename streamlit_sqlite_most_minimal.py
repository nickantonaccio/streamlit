    import streamlit as st, ast, sqlite3
    con=sqlite3.connect('db.db')
    cur=con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS db(name TEXT, letters TEXT, note TEXT)')

    if st.button('Add New Row'):
      cur.execute('INSERT INTO db(name, letters, note) VALUES(?,?,?)', ('','[]',''))
      con.commit()

    for row in cur.execute('SELECT rowid, name, letters, note FROM db ORDER BY name'):
      with st.expander(row[1]):
        with st.form(f'ID-{row[0]}'):
          name=st.text_input('Name', row[1])
          letters=st.multiselect('Letters', ['A', 'B', 'C'], ast.literal_eval(row[2]))
          note=st.text_area('Note', row[3])
          if st.form_submit_button('Save'):
            cur.execute(
              'UPDATE db SET name=?, letters=?, note=? WHERE name=?;', 
              (name, str(letters), note, str(row[1]))
            )
            con.commit() ; st.experimental_rerun()
          if st.form_submit_button("Delete"):
            cur.execute(f'DELETE FROM db WHERE rowid="{row[0]}";')
            con.commit() ; st.experimental_rerun()
