import streamlit as st
import sqlite3
import ast

st.set_page_config(page_title="Sqlite Images Repeating Forms")  #layout="wide",
st.markdown('<style>#MainMenu{visibility: hidden;} footer{visibility: hidden;}#root>div:nth-child(1)>div>div>div>div>section>div{padding-top: .2rem;</style>', unsafe_allow_html=True)

con=sqlite3.connect('image.db')
cur=con.cursor()
cur.execute(
  '''
    CREATE TABLE IF NOT EXISTS images (title TEXT, img BLOB, notes TEXT)
  '''
)

st.title('Sqlite Images Repeating Rows')
if st.button('Add New Row'):
  cur.execute(  
    '''INSERT INTO images(title, img, notes) VALUES(?,?,?)''', ('', '', '')
  )
  con.commit()

if st.checkbox('Recheck to refresh display', value=True):
  for row in cur.execute(
    '''SELECT rowid, title, img, notes FROM images ORDER BY title'''
  ):
    with st.expander(row[1]):
      with st.form("Edit-"+str(row[0]), clear_on_submit=True):
        title=st.text_input('Title', value=row[1])
        if row[2]:
          img=row[2]
          st.image(row[2])
        file=st.file_uploader('Image', ['png', 'jpg', 'gif', 'bmp'])
        if file:
          img=file.read()
        notes=st.text_area('Notes', placeholder='Some Text', value=row[3])
        if st.form_submit_button('Submit'):
          cur.execute(
            ''' 
              UPDATE images
              SET title=?, img=?, notes=?
              WHERE title=?;
            ''', (title, img, notes, str(row[1]))
          )
          con.commit()
          st.experimental_rerun()
        if st.form_submit_button("Delete"):
          cur.execute(f'''DELETE FROM images WHERE rowid="{row[0]}";''')
          con.commit()
          st.experimental_rerun()



######  FastAPI Access to Data Created With This App:  ######

# import sqlite3

# con=sqlite3.connect('images.db')
# cur=con.cursor()

# from fastapi import FastAPI

# app = FastAPI()
# @app.get("/")
# async def root():
  # myrows=[
    # list(row) for row in cur.execute(
      # '''
        # SELECT namecol, passwordcol, agecol, giftcol, colorcol, lettercol, notescol
        # FROM images
        # ORDER BY namecol;
      # '''
    # )
  # ]
  # return myrows # {"greeting":"Hello world"}

# @app.get("/col/{col}")
# async def get_col(col: str):
  # myrow=[list(row) for row in cur.execute(f"SELECT {col} FROM images;")]
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


##########  handling empty radio buttons  ##########

        # colorval=row[5]
        # if colorval!='' and colorval!=None:
          # chosencolor=colors.index(colorval)
        # else:
          # chosencolor=0