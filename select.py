import sqlite3

db=sqlite3.connect("test.db")

cursor = db.cursor() 
datos = cursor.execute("SELECT * FROM personas")

print(datos.fetchone()) #fetchall

cursor.close()