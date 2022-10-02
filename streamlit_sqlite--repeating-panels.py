import streamlit as st
import sqlite3
import ast

st.set_page_config(page_title="Sqlite CRUD Repeating Forms")  #layout="wide",
st.markdown('<style>#MainMenu{visibility: hidden;} footer{visibility: hidden;}#root>div:nth-child(1)>div>div>div>div>section>div{padding-top: 1rem;</style>', unsafe_allow_html=True)

con=sqlite3.connect('crud.db')
cur=con.cursor()
cur.execute(
  '''
    CREATE TABLE IF NOT EXISTS crud (
      namecol TEXT, 
      passwordcol TEXT, 
      agecol TEXT, 
      giftcol TEXT, 
      colorcol TEXT, 
      lettercol TEXT, 
      notescol TEXT
    )
  '''  # key_col INTEGER NOT NULL PRIMARY KEY,
)

st.title('Sqlite CRUD Repeating Forms')
if st.button('Add New Row'):
  cur.execute(  
    '''
      INSERT INTO crud(namecol, passwordcol, agecol, giftcol, colorcol, lettercol, notescol) 
      VALUES(?,?,?,?,?,?,?)
    ''', ('', '', '1', '', '', '[]', '')
  )
  con.commit()

if st.checkbox('Recheck to refresh display', value=True):
  for row in [
    list(rows) for rows in cur.execute(
      '''
        SELECT rowid, namecol, passwordcol, agecol, giftcol, colorcol, lettercol, notescol
        FROM crud
        ORDER BY namecol
      '''
    )
  ]:
    with st.expander(row[1]):
      with st.form("Edit-"+str(row[0]), clear_on_submit=True):
        name=st.text_input('Name', value=row[1])
        password=st.text_input('Password', type='password', value=row[2])
        age=st.number_input('Age', min_value=1, max_value=120, value=int(row[3]), step=1)
        gifts=['roses', 'jewelry', 'dinner', 'trip', 'money', '']
        gift=st.selectbox('Gift', gifts, index=gifts.index(row[4]))
        colors=['red', 'green', 'blue', 'black']
        colorval=row[5]
        if colorval!='' and colorval!=None:
          chosencolor=colors.index(colorval)
        else:
          chosencolor=0
        color=st.radio('Color', colors, index=chosencolor)
        letters=st.multiselect('Letters', ['A', 'B', 'C', 'D'], default=ast.literal_eval(row[6]))
        notes=st.text_area('Notes', placeholder='Some Text', value=row[7])
        if st.form_submit_button('Submit'):
          cur.execute(
            ''' 
              UPDATE crud
              SET namecol=?,
                  passwordcol=?,
                  agecol=?,
                  giftcol=?,
                  colorcol=?,
                  lettercol=?,
                  notescol=?
              WHERE namecol=?;
            ''', (name, password, age, gift, color, str(letters), notes, str(row[1]))
          )
          con.commit()  # con.close()
          st.experimental_rerun()
        if st.form_submit_button("Delete"):
          cur.execute(f'''DELETE FROM crud WHERE namecol="{row[1]}";''')
          con.commit()
          st.experimental_rerun()



######  FastAPI Access to Data Created With This App:  ######

# import sqlite3

# con=sqlite3.connect('crud.db')
# cur=con.cursor()

# from fastapi import FastAPI

# app = FastAPI()
# @app.get("/")
# async def root():
  # myrows=[
    # list(row) for row in cur.execute(
      # '''
        # SELECT namecol, passwordcol, agecol, giftcol, colorcol, lettercol, notescol
        # FROM crud
        # ORDER BY namecol;
      # '''
    # )
  # ]
  # return myrows # {"greeting":"Hello world"}

# @app.get("/col/{col}")
# async def get_col(col: str):
  # myrow=[list(row) for row in cur.execute(f"SELECT {col} FROM crud;")]
  # return myrow

# at command line:  uvicorn fastapi-sqlite:app
# http://127.0.0.1:8000
# http://127.0.0.1:8000/col/namecol


# at command line:  uvicorn fastapi-sqlite:app
# http://127.0.0.1:8000
# http://127.0.0.1:8000/col/namecol



#######  More Style  #######

# st.markdown(
  # """
    # <style>
      # .css-18e3th9 {
          # padding-top: 0rem;
          # padding-bottom: 10rem;
          # padding-left: 5rem;
          # padding-right: 5rem;
      # }
      # .css-1d391kg {
          # padding-top: 3.5rem;
          # padding-right: 1rem;
          # padding-bottom: 3.5rem;
          # padding-left: 1rem;
      # }
    # </style>
  # """, unsafe_allow_html=True
# )