#
import sqlite3


def connection():
    cn = sqlite3.connect('Employee.db')
    return cn


connobj = connection()


def create_table(connobj):
    cursorobj = connobj.cursor()
    cursorobj.execute('create table emp (id integer primary key,name text)')
    print('table is created')


# create_table(connobj)

def insert_data(connobj):
    cursorobj = connobj.cursor()
    cursorobj.execute("insert into emp values(3,'Ritik')")
    connobj.commit()
    print('data inserted to table')


# insert_data(connobj)

def update_data(connobj):
    cursorobj = connobj.cursor()
    cursorobj.execute("update emp set name='Vivek'  where id=1")
    connobj.commit()
    print('Record updated')


# update_data(connobj)


#
def retrive_data(connobj):
    cursorobj = connobj.cursor()
    data = cursorobj.execute("select * from emp ")
    for i in data:
        print(i)


# retrive_data(connobj)

# delete record
def delete_data(connobj):
    cursorobj = connobj.cursor()
    cursorobj.execute('delete from emp where name="Vivek" ')
    connobj.commit()
    print('record deleted')


# delete_data(connobj)
retrive_data(connobj)










