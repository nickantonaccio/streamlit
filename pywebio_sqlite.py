from pywebio.input import *
from pywebio.output import *
import sqlite3
import ast

con=sqlite3.connect('crud-pywebio.db')
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

def startup():
  selection=select('PyWebIO Sqlite', options=['Create', 'Read', 'Update', 'Delete', 'Quit'])
  if selection=='Create':
    create_data()
  elif selection=='Read':
    read_data()
  elif selection=='Update':
    update_data()
  elif selection=='Delete':
    delete_data()
  elif selection=='Quit':
    quit_program()
  else:
    startup()

def create_data():
  data = input_group("Values",[
    input('Name', name='name'),
    input("Password", name='password', type=PASSWORD),
    input('Age', name='age'),
    select('Gift', name='gift', options=['roses', 'jewelry', 'dinner', 'trip', 'money']),
    radio("Color", name="color", options=['red', 'green', 'blue', 'black']),
    checkbox("Letters", name="letter", options=['A', 'B', 'C', 'D']),
    textarea('Notes', name='notes', rows=3, placeholder='Some text')
  ])
  cur.execute(  
    '''
      INSERT INTO crud(namecol, passwordcol, agecol, giftcol, colorcol, lettercol, notescol) 
      VALUES(?,?,?,?,?,?,?)
    ''', (     
      data['name'], 
      data['password'], 
      data['age'], 
      data['gift'], 
      data['color'], 
      str(data['letter']),
      data['notes']        
    )
  )
  con.commit()
  read_data()

def read_data():
  myrows=[
    list(row) for row in cur.execute(
      '''
        SELECT namecol, passwordcol, agecol, giftcol, colorcol, lettercol, notescol
        FROM crud
        ORDER BY rowid
      '''
    ) # ORDER BY namecol
  ]
  myrows.insert(0,['Name', 'Password', 'Age', 'Gift', 'Color', 'Letter', 'Notes'])
  with use_scope('scope1', clear=True):
     put_table(myrows)
  startup()

def update_data():
  names=[str(row[0]) for row in cur.execute(f"SELECT namecol FROM crud;")]
  name_to_update=select('Name to Update:', options=names),
  row_to_update=cur.execute(f'''SELECT * FROM crud WHERE namecol="{name_to_update[0]}";''').fetchall()[0]
  data = input_group("Values",[
    input('Name', name='name', value=row_to_update[0]),
    input("Password", name='password', type=PASSWORD, value=row_to_update[1]),
    input('Age', name='age', value=row_to_update[2]),
    select('Gift', name='gift', options=['roses', 'jewelry', 'dinner', 'trip', 'money'], value=row_to_update[3]),
    radio("Color", name="color", options=['red', 'green', 'blue', 'black'], value=row_to_update[4]),
    checkbox("Letters", name="letter", options=['A', 'B', 'C', 'D'], value=ast.literal_eval(row_to_update[5])),
    textarea('Notes', name='notes', rows=3, placeholder='Some text', value=row_to_update[6])
  ])
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
    ''', (     
      data['name'], 
      data['password'], 
      data['age'], 
      data['gift'], 
      data['color'], 
      str(data['letter']),
      data['notes'],
      str(name_to_update[0])     
    )
  )
  con.commit()
  read_data()
  startup()
  
def delete_data():
  names=[str(row[0]) for row in cur.execute(f"SELECT namecol FROM crud;")]
  name_to_delete=select('Name to Delete:', options=names),
  cur.execute(f'''DELETE FROM crud WHERE namecol="{name_to_delete[0]}";''')
  con.commit()
  put_text(f"{name_to_delete[0]} has been deleted")
  startup()

def quit_program():
  con.close()
  popup('', [
    put_markdown('# Database closed')
  ])
  quit()

read_data()
startup()

# from pywebio import *
# def main():
  # read_data()
  # startup()
# start_server(main, port=8080, remote_access=True, debug=True)