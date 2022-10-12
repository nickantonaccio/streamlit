import streamlit as st
import sqlite3

con=sqlite3.connect('picscols.db')
cur=con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS pics(id TEXT, img BLOB, note TEXT)')

st.set_page_config(page_title="Sqlite Images", layout="wide")
st.markdown('<style>#MainMenu{visibility: hidden;} footer{visibility: hidden;}#root>div:nth-child(1)>div>div>div>div>section>div{padding-top: 1.4rem;</style>', unsafe_allow_html=True)

st.title('Sqlite Images')
if st.button('Add New Image'):
  cur.execute('INSERT INTO pics(id, img, note) VALUES(?,?,?)', ('', '', ''))
  con.commit()

if st.checkbox('Recheck to refresh display', value=True):
  for row in cur.execute('SELECT rowid, id, img, note FROM pics ORDER BY id'):
    with st.form(f'ID-{row[0]}', clear_on_submit=True):
      imgcol, notecol = st.columns([3, 2])
      id=notecol.text_input('id', row[1])
      note=notecol.text_area('note', row[3])
      if row[2]:
        img=row[2]
        imgcol.image(row[2])
      file=imgcol.file_uploader('Image', ['png', 'jpg', 'gif', 'bmp'])
      if file: 
        img=file.read()
      if notecol.form_submit_button('Save'):
        cur.execute(
          'UPDATE pics SET id=?, img=?, note=? WHERE id=?;', 
          (id, img, note, str(row[1]))
        )
        con.commit()
        st.experimental_rerun()
      if notecol.form_submit_button("Delete"):
        cur.execute(f'''DELETE FROM pics WHERE rowid="{row[0]}";''')
        con.commit()
        st.experimental_rerun()
