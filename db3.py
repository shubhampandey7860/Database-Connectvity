# check database exists

import mysql.connector
mydb = mysql.connector.connect(host='localhost',user='root',password='root')
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for row in mycursor:
    print(row)
