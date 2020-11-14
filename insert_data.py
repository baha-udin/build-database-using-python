import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="toko_helm"
)
#add data
cursor = db.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)" #%s sebagai placeholder data yg ditambahkan
val = ("Kate", "Malang")
cursor.execute(sql, val)

db.commit()

print("{} data ditambahkan".format(cursor.rowcount))