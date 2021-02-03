#!C:\Users\HP\AppData\Local\Programs\Python\Python38\Python

import cgi
import mysql.connector as mycon

print("Content-type: text/html")
print()

form=cgi.FieldStorage()
no=int(form.getvalue("ano"))

con=mycon.connect(host='localhost',user='root',password='12345',database='python')
curs=con.cursor()

curs.execute("select * from accounts where accno=%d" %no)
data=curs.fetchone()

print("<h3>Search Result</h3>")

try:
    print("<b>Name : %s" %data[1])
    print("<br><b>Type : %s" %data[2])
    print("<br><b>Balance : %.2f" %data[3])
except:
    print("<b>Account does not exist")

con.close()