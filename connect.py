import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)

if db.is_connected():
    print("Database berhasil terhubung")
else:
    print("belum berhasil terhubung ke Database")
