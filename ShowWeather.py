#!C:\Users\HP\AppData\Local\Programs\Python\Python38\Python

import cgi
from urllib import request as req
import json

print("Content-type: text/html")
print()

form=cgi.FieldStorage()
ct=form.getvalue("city")

print("<center><h3>Weather information for : %s</h3>" %ct)
print("<hr>")

try:
    response=req.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+ct+'&appid=5ea9269ece0f0c287803a5b69fca4d80')
    data=response.read()
    info=json.loads(data)
    #print(info)
    print("<center>")
    print('<b>Description : '+info['weather'][0]['description'])
    print("<br><span style='color:green;font-size:17px;font-family:tahoma'>")
    kel=info['main']['temp']
    cels=kel-272.15
    print('<b>Temperature : %.2f celsius' %cels)
    print('</span>')
    print('<br><b>Pressure : '+str(info['main']['pressure']))
    print('<br><b>Humidity : '+str(info['main']['humidity']))
    
except:
    print('<b>Error communicating with REST API')
     

