import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="toko_helm"
)

cursor = db.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Kate", "Malang")
cursor.execute(sql, val)

db.commit()

print("{} data ditambahkan".format(cursor.rowcount))