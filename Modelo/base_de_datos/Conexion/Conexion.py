import mysql.connector

def conexion():
    
  con = mysql.connector.connect(

    host = "localhost",
    user = "root",
    password = "",
    database = "Banco_multitodo" 

  )
  con.autocommit = True
  return con
