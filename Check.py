#!C:\Users\HP\AppData\Local\Programs\Python\Python38\Python

import cgi
import mysql.connector as mycon

print("Content-type: text/html")
print()

form=cgi.FieldStorage()
id=form.getvalue("uid")
ps=form.getvalue("psw")

con=mycon.connect(host='localhost',user='root',password='12345',database='python')
curs=con.cursor()

curs.execute("select count(*) from users where userid='%s' and pswd='%s';" %(id,ps))
cnt=curs.fetchone()

print(cnt)

if cnt[0]==1:
    #print("<h2>Welcome to python web development</h2>")
    print("<html>")
    print("<head>")
    print("<meta http-equiv='refresh' content='0;url=Admin.html'/>")
    print("</head>")
    print("</html>")
else:
    print("<h2>Sorry password failed</h2>")
