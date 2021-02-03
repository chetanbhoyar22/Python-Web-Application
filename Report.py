#!C:\Users\HP\AppData\Local\Programs\Python\Python38\Python


import mysql.connector as mycon

print("Content-type: text/html")
print()

con=mycon.connect(host='localhost',user='root',password='12345',database='python')
curs=con.cursor()

curs.execute("select * from accounts;")
all=curs.fetchall()

print("<center>")
print("<h2 style='color:green'>Accounts Report</h2><hr>")
print("<table border='1' bordercolor='pink' cellspacing='0' width='70%'>")
print("<tr style='background-color:azure'><th>Number<th>Name<th>Type<th>Balance</tr>")

for one in all:
    print("<tr style='font-family:consolas'>")
    print("<td>"+str(one[0]))
    print("<td>"+one[1])
    print("<td>"+one[2])
    print("<td>"+str(one[3]))
    print("</tr>")

print("</table>")
print("<a href='index.html'>Home</a>")
print("</center>")