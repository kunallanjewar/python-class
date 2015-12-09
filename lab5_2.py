s = ""      # example 1  
for i in range(10):  
 s = s + str(i) + " "   
print(s)  

#example 2 
x = []    # empty list  
for i in range(0, 10) :  
 x.append(i/10)   
print(x)  

s = ""     # example 3  
for i in range(10, 51, 5):  
 s = s + str(i) + " "   
print(s, "\n")  

# example 4  
month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]  
for m in range(len(month)) :  
 print(str(m), "is the index of", month[m])   

s = "\n"      # example 5  
for i in range(5, 0, -1):  
 s = s + str(i) + " "  
print(s)  

s = ""   # example 6  
for i in range(15, -1, -3):  
 s = s + str(i) + " "  
print(s)  

s = "Python Programming"    # example 7 
result = ""  
for i in range(len(s)-1, -1, -1):  
 result = result + s[i]   
print(result)  

sum = 0   # example 8  
for i in range(10, 0, -1):  
 sum = sum + i  
print(sum)  

for i in range(0, 11):  #example 9  
 if i%2 == 0:    
  print(i, "is an even number!");  
 else:     
  print(i, "is an odd number!"); 