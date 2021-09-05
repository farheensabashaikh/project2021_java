import MySQLdb

try:
    query="CREATE DATABASE product "
    mycon=MySQLdb.connect(host="localhost",user="root",passwd="")
    print("mycon excecute")
    cur=mycon.cursor()
    print("cursor excecute")

    cur.execute(query)
    print("execute query")
    mycon.commit()
    print("Database created")
except:
    print("Database not created...")
finally:
    cur.close()
    print("cursor connection close....")
    mycon.close()