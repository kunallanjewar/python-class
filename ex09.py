#Student: Kunal Lanjewar
#Programming Ex: 09

import re  

# Student ID 
str = input("Enter your Student ID: ")  
if ( not re.match(r"^D[0-9]", str) ) :
 print("Not a valid Student ID.")  

# CMD ID
str = input("Enter your CMS ID: ")  
if ( not re.match(r"^@[0-9]+s$", str) ) :
 print("Not a valid Student ID.")  

