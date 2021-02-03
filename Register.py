#!C:\Users\HP\AppData\Local\Programs\Python\Python38\Python

import cgi
import mysql.connector as mycon

print("Content-type: text/html")
print()

form=cgi.FieldStorage()
id=form.getvalue("uid")
ps=form.getvalue("psw")
nm=form.getvalue("unm")

con=mycon.connect(host='localhost',user='root',password='12345',database='python')
curs=con.cursor()

try:
    curs.execute("insert into users values('%s','%s','%s');" %(id,ps,nm))
    con.commit()
    print('<h2>User registration successful</h2>')
except Exception as err:
    print(err)
    
con.close()