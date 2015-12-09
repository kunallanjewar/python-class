s = ""  #example 1  
for i in range(1, 10):   
 if (i == 6):   
  break  
 else:   
  s = s + str(i) + " "    
print(s)  

s = ""  # example 2 
i = 0  
while (i <= 9):   
 if (i ==7):    
  break;    
 s = s + str(i) + " "     
 i += 1   
print(s)  

#example 3 
for n in range(2, 11):  
 for x in range(2, n):   
  if n % x == 0:    
   print(n, 'equals', x, '*', n/x)   
   break  
  else: # loop fell through without finding a factor    
   print(n, 'is a prime number')  

s = "\n"  #example 4 
i = -1  
while (i <= 20):  
 i = i + 1                      
 if i % 2 != 0:    
  continue      
 s = s + str(i) + " "   
print(s)  

s = ""       #example 5 
m = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")  
for i in m:  
 if i == "May":   
  pass  
 else:   
  s = s + str(i) + " "    
print(s)