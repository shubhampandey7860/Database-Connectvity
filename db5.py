import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root', password='root', database='test')
mycursor = mydb.cursor()
cmd = 'insert into person values (102,"Yash Sharma") '
mycursor.execute(cmd)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
