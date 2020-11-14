import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="toko_helm"
)

cursor = db.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
values = [
  ("Doni", "Jakarta"),
  ("Ella", "Surabaya"),
  ("Fani", "Bandung"),
  ("Galih", "Depok")
]
for val in values:
  cursor.execute(sql, val)
  db.commit() #u/ menyimpan data

print("{} data ditambahkan".format(len(values)))