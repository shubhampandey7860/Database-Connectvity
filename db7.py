import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root', password ='root', database = 'test')
mycursor = mydb.cursor()
cmd = 'select *from person where name="Yash Sharma" '
mycursor.execute(cmd)
myresult = mycursor.fetchall()
for row in myresult:
    print(row)
