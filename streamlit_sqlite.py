import streamlit as st
import sqlite3
import pandas as pd
import ast

st.set_page_config(layout="wide", page_title="Sqlite CRUD")
st.markdown('<style>#MainMenu{visibility: hidden;} footer{visibility: hidden;}#root>div:nth-child(1)>div>div>div>div>section>div{padding-top: 0rem;</style>', unsafe_allow_html=True)

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

st.title('CRUD Example')
col1, col2=st.columns([2,3])
with col1:
  st.header("Create/Update/Delete")
  names=[str(row[0]) for row in cur.execute(f"SELECT namecol FROM crud;")]
  names.insert(0, '')
  name_to_update=st.selectbox('', names)
  if name_to_update!='':
    createorupdate='update'
    row_to_update=cur.execute(f'''SELECT * FROM crud WHERE namecol="{name_to_update}";''').fetchall()[0]
    nameval=row_to_update[0]
    passval=row_to_update[1]
    ageval=int(row_to_update[2])
    giftval=row_to_update[3]
    colorval=row_to_update[4]
    lettersval=ast.literal_eval(row_to_update[5])
    notesval=row_to_update[6]
  else:
    createorupdate='create'
    nameval=''
    passval=''
    ageval=30
    giftval=''
    colorval=None
    lettersval=[]
    notesval=''
  with st.form("Create or Update a Row of Data", clear_on_submit=True):
    name=st.text_input('Name', value=nameval)
    password=st.text_input('Password', type='password', value=passval)
    age=st.number_input('Age', min_value=1, max_value=120, value=ageval, step=1)
    gifts=['roses', 'jewelry', 'dinner', 'trip', 'money']
    if giftval!='':
      chosengift=gifts.index(giftval)
    else:
      chosengift=0
    gift=st.selectbox('Gift', gifts, index=chosengift)
    colors=['red', 'green', 'blue', 'black']
    if colorval!=None:
      chosencolor=colors.index(colorval)
    else:
      chosencolor=0
    color=st.radio('Color', colors, index=chosencolor)
    letters=st.multiselect('Letters', ['A', 'B', 'C', 'D'], default=lettersval)
    notes=st.text_area('Notes', placeholder='Some Text', value=notesval)
    if st.form_submit_button("Submit"):
      if createorupdate=='create':
        cur.execute(  
          '''
            INSERT INTO crud(namecol, passwordcol, agecol, giftcol, colorcol, lettercol, notescol) 
            VALUES(?,?,?,?,?,?,?)
          ''', (name, password, age, gift, color, str(letters), notes)
        )
        con.commit()  # con.close()
      else:
        cur.execute(
          ''' 
            UPDATE crud
            SET namecol = ? ,
                passwordcol = ? ,
                agecol = ? ,
                giftcol = ? ,
                colorcol = ? ,
                lettercol = ? ,
                notescol = ?
            WHERE namecol = ?;
          ''', (name, password, age, gift, color, str(letters), notes, str(nameval))
        )
        con.commit()  # con.close()
        st.experimental_rerun()
    if st.form_submit_button("Delete"):
      cur.execute(f'''DELETE FROM crud WHERE namecol="{name_to_update}";''')
      con.commit()
      st.write(f"{name_to_update} has been deleted")

with col2:
  st.header("Read")
  if st.checkbox('Recheck to refresh display', value=True):
    myrows=[
      list(row) for row in cur.execute(
        '''
          SELECT rowid, namecol, passwordcol, agecol, giftcol, colorcol, lettercol, notescol
          FROM crud
          ORDER BY namecol
        '''
      )
    ]
    st.dataframe(
      pd.DataFrame(
        myrows, 
        columns=['rowid', 'name', 'password', 'age', 'gift', 'color', 'letters', 'notes']), 
        height=800
    )



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