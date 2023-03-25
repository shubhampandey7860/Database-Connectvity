# Select all records from the table

# If you are only interested in one row, you can use the fetchone() method.
# We use the fetchall() method, which fetches all rows from the last executed statement.
import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', password='root', database='test')
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM person")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
