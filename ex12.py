#Student Name: Kunal Lanjewar
#Programming Ex: 12

import math  
def getSqrt(n):   
 return math.sqrt(float(n))  

s = input("Enter a numerical value: ")  

try:
 for i in s:
  if (i.isdigit() or i == "."):       
   sType = "nonstr"  
  if (sType =="nonstr"):    
   print(getSqrt(s)) 
except ValueError:
  print("Not a numerical value..")