import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="toko_helm"
)

cursor = db.cursor()
sql = "DELETE FROM customers WHERE customer_id=%s"
val = (1, )
cursor.execute(sql, val)

db.commit()
print("{} data diubah".format(cursor.rowcount))