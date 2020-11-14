#import modul
import mysql.connector

#connect ke database yg sudah dibuat
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="toko_helm"
)
# buat skema
cursor = db.cursor()
sql = """CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    address Varchar(255)
)
"""
#execute sql
cursor.execute(sql)

print("Tabel customers berhasil dibuat")