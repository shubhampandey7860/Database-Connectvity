import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="test")
mycursor = mydb.cursor()
cmd = 'create table if not exists person(id int,name varchar(20))'
mycursor.execute(cmd)
print('Table created successfully')
