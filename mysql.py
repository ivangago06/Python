import pymysql

db = pymysql.connect(
    user="root",
    password="!B4rc3l0n4$",
    host="0.0.0.0",
    port="3306",
    database="curso"
)

cursor=db.cursor()
cursor.execute("SHOW DATABASES")
print(cursor.fetchone())