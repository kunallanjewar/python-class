#Student: Kunal Lanjewar
#File: Ex 13

#!"D:/Documents/Python3.0/pp3/Python32/App/python.exe"  

import os 
uri = os.environ['REQUEST_URI']  
import cgi 
form = cgi.FieldStorage() 

number = form.getvalue('number')

print ("Content-type: text/html\n\n")
print("<!Doctype html><html><body>") 
print("<form action='" + uri + "' method='post'>") 
print("Enter a degree in Farenheit : <input type='text' name='number'>") 
print("<input type='submit' value='Submit'>") 
print("</form>")
	
if(number):
	fahrenheit = float(number)
	celsius = (fahrenheit - 32)*5/9
	print ("It is" ,celsius," degree in Celsius.")