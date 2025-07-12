import mysql.connector
from mysql.connector import errorcode

try:
  mydb = mysql.connector.connect(
    host ="localhost",
    user ="root",
    password='12345678' 
  )

  obj_cursor = mydb.cursor()
  sql = "CREATE DATABASE alx_book_store"
  obj_cursor.execute(sql)
  print("Database alx_book_store created successfully!")

except mysql.connector.Error as err:
  if err.errno == errorcode.ER_DB_CREATE_EXISTS:
    print("Database already exists")
  else:
    print("An error occured", err)

obj_cursor.close()
mydb.close()