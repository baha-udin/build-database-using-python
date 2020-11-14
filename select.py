import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="toko_helm"
)
#Cursor u/ mengeksekusi Sql
cursor = db.cursor()
sql = "SELECT * FROM customers"
cursor.execute(sql) #excute query

hasil = cursor.fetchone()

print(hasil)