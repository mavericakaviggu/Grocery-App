import datetime
import mysql.connector

# declaring global variable. This variable will hold the database connection object.
__cnx = None

def get_sql_connection():
  print("Opening mysql connection")
  global __cnx

  #  if the global variable '__cnx' is None, indicating that a connection hasn't been established yet.
  if __cnx is None:
    __cnx = mysql.connector.connect(user='root', password='root4977', database='grocery_store')

  return __cnx

