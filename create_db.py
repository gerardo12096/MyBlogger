import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)
#This creates the initial database to store user credentials
my_cursor = mydb.cursor()
my_cursor.execute("CREATE DATABASE project_db");

for db in my_cursor:
    print(db)
