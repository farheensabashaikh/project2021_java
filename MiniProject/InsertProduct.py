import MySQLdb

try:
    mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="product")
    print("mycon excecute")
    cur=mycon.cursor()
    print("cursor excecute")
    query1="insert into list(name,price) values('Laptop',1000) "
    query2="insert into list(name,price) values('Phone',2000)"
    query3="insert into list(name,price) values('SSD',200)"
    query4="insert into list(name,price) values('Headphone',800)"
    query5="insert into list(name,price) values('Printer',3500)"
    query6="insert into list(name,price) values('Keyboard',500)"
    cur.execute(query1)
    cur.execute(query2)
    cur.execute(query3)
    cur.execute(query4)
    cur.execute(query5)
    cur.execute(query6)
    mycon.commit()
    print("value inserted sucessfully .....")
except:
    print("value not inserted...")
finally:
    cur.close()
    print("cursor connection close...")
    mycon.close()
    print("DB connection close...")