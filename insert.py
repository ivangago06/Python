import sqlite3
conn=sqlite3.connect("test.db")
sql = " INSERT INTO personas(curp,nombre,apellido)VALUES('hdhdhdddhd','hola','mundo') "
cur = conn.cursor()
cur.execute(sql)
conn.commit()
conn.close()

