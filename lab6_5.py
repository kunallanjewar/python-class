print("Content-Type: text/html\n\n"); 
print("<html><body>");  

# The random module contains a number of random number generators 
import random    
# tuple - array of numbers 
n = (1, 3, 5, 7);  

print(n[0] , " is n[0]!<br />"); 
print(n[1] , " is n[1]!<br />"); 
print(n[2] , " is n[2]!<br />"); 
print(n[3] , " is n[3]!<br />");  
print("<hr width=100%>");  

# list - array of strings 
tip= ["Right click the mouse!","Double click the mouse!","Double right click the mouse!","Press F8 and F12!","Find the ANY key!","Press Shift+Ctrl+Alt+Del!","Hold the Esc key for 2 seconds!"];  

# generate random number from 0 to 6 
i=random.randint(0,6);  
print("Tip of the day is: <b>" , tip[i] , "</b>");  
print("<hr width=100%>");  

# dictionary - associative Array 
school = { "UCI": "University of California, Irvine",     
           "UCSD": "University of California, San Diego",
           "UCLA": "University of California, Los Angeles", 
           "UCD": "University of California, Davis" };  
                
print(school["UCI"] , "<br>"); 
print(school["UCLA"] , "<br>");   
print(school["UCD"] , "<br>");   
print(school["UCSD"] , "<br>");  
  
print("</body></html>");