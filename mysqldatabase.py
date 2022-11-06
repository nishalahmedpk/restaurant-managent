from mysql.connector import *

host,user,password = 'localhost','root','1234567890'

def connectioncheck(x):
    if x.is_connected():
        print('Connected...')

def new_userquickfix():
    con = connect(host=host, user=user,password=password)
    connectioncheck(con)
    cur = con.cursor()
    cur.execute('create database if not exists Restaurant_Management')
    cur.execute('use Restaurant_Management')
    cur.execute('create table if not exists fooditems(Name varchar(20) NOT NULL primary key,Price int NOT NULL,Category varchar(20))')
    con.close()

new_userquickfix()

def new_user(x):
    con = connect(host=host, user=user,password=password)
    cur = con.cursor()
    cur.execute('create database if not exists Restaurant_Management')
    cur.execute('use Restaurant_Management')
    cur.execute('create table if not exists fooditems(Name varchar(20) NOT NULL primary key,Price int NOT NULL,Category varchar(20))')
    cur.execute(f'create table if not exists {x}(SNO int primary key,Mobile varchar(20) not null,No_Of_Items int not null,Items varchar(300) not null,OrderType varchar(20) not null,Status varchar(20) not null,Price int not null)')
    con.close()

def newdatabase(x):
    con = connect(host=host, user=user,password=password,database='restaurant_management')
    cur = con.cursor()
    cur.execute(f'drop table if exists {x}')
    cur.execute(f'create table if not exists {x}(SNO int primary key,Mobile varchar(20) not null,No_Of_Items int not null,Items varchar(300) not null,OrderType varchar(20) not null,Status varchar(20) not null,Price int not null)')
    con.close()

def getordernop(x):
    con = connect(host=host, user=user,password=password,database='restaurant_management')
    cur = con.cursor()
    cur.execute(f"Select * from {x}")
    cur.fetchall()
    x=cur.rowcount
    con.close()
    return x+1

def getfooditems():
    con = connect(host=host, user=user,password=password,database='restaurant_management')
    cur = con.cursor()
    cur.execute("Select distinct Name from fooditems")
    x=list(cur.fetchall())
    l=[]
    for i in x:
        for j in i:
            l.append(j)
    con.close()
    return l

#Returns Full List For additems():
def getallfoooditems():
    con = connect(host=host, user=user,password=password,database='restaurant_management')
    cur = con.cursor()
    cur.execute("Select * from fooditems")
    x=list(cur.fetchall())
    con.close()
    return x

def getfoodcategory():
    con = connect(host=host, user=user,password=password,database='restaurant_management')
    cur = con.cursor()
    cur.execute("Select distinct Category from fooditems")
    x=list(cur.fetchall())
    con.close()
    return x

def addtodata1(name,price,category):
    con = connect(host=host, user=user,password=password,database='restaurant_management')
    cur = con.cursor()
    cur.execute(f"Insert into fooditems values('{name}',{price},'{category}')")
    con.commit()
    con.close()

def addtodatabase1(serialnumber,moobilenumber,noofitemsoredered,o,type123,status123,initialtotal,path):
    con = connect(host=host, user=user,password=password,database='restaurant_management')
    cur = con.cursor()
    cur.execute(f"""Insert into {path} values({int(serialnumber)},'{moobilenumber}',{noofitemsoredered},"{o}",'{type123}','{status123}',{int(initialtotal)})""")
    con.commit()
    con.close()

def deleteorder1(orderno,path):
    con = connect(host=host, user=user,password=password,database='restaurant_management')
    cur = con.cursor()
    cur.execute(f"delete from {path} where sno={orderno}")
    con.commit()
    con.close()

fooditems = getfooditems()

listofallfooditems = getallfoooditems()

currencies = ['AED','INR', 'USD']

foodcategory = getfoodcategory()

ordertypecombovalues = ['Dine-in','Take-Away','Delivery']

paystatuesvalues = ('Paid','Not Paid','Credit')

restaurantname='BIG RESTAURANT'

foreground123 = 'black'

background = 'black'

textcolour = 'gold'

numbers = list(range(1,14))