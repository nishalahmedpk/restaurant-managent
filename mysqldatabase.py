from mysql.connector import*

host,user,password = 'localhost','root','1234567890'

def connectioncheck(x):
    if x.is_connected():
        print('Connected...')

def new_user():
    con = connect(host=host, user=user,password=password)
    connectioncheck(con)
    cur = con.cursor()
    cur.execute('create database if not exists Restaurant_Management')
    cur.execute('use Restaurant_Management')
    cur.execute('create table if not exists fooditems(Name varchar(20) NOT NULL primary key,Price int NOT NULL,Category varchar(20))')
    con.close()
new_user()

def newdatabase(x):
    con = connect(host=host, user=user,password=password,database='restaurant_management')
    cur = con.cursor()
    cur.execute(f'create table if not exists {x}(SNO int primary key,Mobile int(10) not null,No_Of_Items int not null,Items varchar(300) not null,OrderType varchar(20) not null,Status varchar(20) not null,Price int not null)')
    con.close()

def getordernop(x):
    con = connect(host=host, user=user,password=password,database='restaurant_management')
    cur = con.cursor()
    cur.execute(f"Select * from {x}")
    x=cur.rowcount
    con.close()
    return x+1

def getfooditems():  #Not Working
    con = connect(host=host, user=user,password=password,database='restaurant_management')
    cur = con.cursor()
    cur.execute("Select distinct Name from fooditems")
    x=list(cur.fetchall())
    con.close()
    return x
print(getfooditems)
