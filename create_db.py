import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="America!1324"
)
#This creates the initial database to store user credentials
my_cursor = mydb.cursor()
my_cursor.execute("CREATE DATABASE user");

for db in my_cursor:
    print(db)