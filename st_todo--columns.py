import streamlit as st
from datetime import datetime
from datetime import date
import sqlite3
con=sqlite3.connect('todo.db')
cur=con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS todo(item TEXT, note TEXT, date TEXT)')

st.set_page_config(page_title="To Do", layout="wide")
st.markdown('<style>#MainMenu{visibility: hidden;} footer{visibility: hidden;}#root>div:nth-child(1)>div>div>div>div>section>div{padding-top: 1.3rem;</style>', unsafe_allow_html=True)

st.title('To Do Columns')
if st.button('Add New Item'):
  today = date.today()
  cur.execute('INSERT INTO todo(item, note, date) VALUES(?,?,?)', ('','',today))
  con.commit()

for row in cur.execute('SELECT rowid, item, note, date FROM todo ORDER BY rowid'):
    with st.form(f'ID-{row[0]}'):
      itemcol, notecol, datecol, btncol = st.columns([3, 4, 2, 1])
      item=itemcol.text_input('Item', row[1])
      note=notecol.text_area('Note', row[2], height=50)
      date=datecol.date_input('Date', datetime.strptime(row[3], '%Y-%m-%d'))
      btncol.markdown('#')
      if btncol.form_submit_button('Save'):
        cur.execute(
          'UPDATE todo SET item=?, note=?, date=? WHERE rowid=?;', 
          (item, note, str(date), str(row[0]))
        )
        con.commit()
        st.experimental_rerun()
      if btncol.form_submit_button("Delete"):
        cur.execute(f'DELETE FROM todo WHERE rowid="{row[0]}";')
        con.commit()
        st.experimental_rerun()
