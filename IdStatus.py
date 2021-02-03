#!C:\Users\HP\AppData\Local\Programs\Python\Python38\Python


import cgi
import mysql.connector as mycon

print("Content-type: text/html")
print()

form=cgi.FieldStorage()
id=form.getvalue("uid")

con=mycon.connect(host='localhost',user='root',password='12345',database='python')
curs=con.cursor()

curs.execute("select count(*) from users where userid='%s';" %id)
cnt=curs.fetchone()

if cnt[0]==0:
    print("<span style='color:green'>Congrats! ID available</span>")
else:
    print("<span style='color:red'>Sorry! ID already taken</span>")

con.close()