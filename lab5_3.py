s = ""    # example 1 
x = 1            # initial value  
while (x<10):    # Boolean expression  
 s = s + str(x) + " "        
 x += 1          # increment   
print(s)  

s = ""    # example 2 
x = 9            # initial value  
while (x>=1):    # Boolean expression  
 s = s + str(x) + " "   
 x -= 1          # increment   
print(s)   

i = 10   # example 3 
f = 1  
while (i >= 1):  
 f = f * i  
 i -= 1  
print(f)    

#example 4 
x = (23, 17, 22, 8, 10, 19, 5, 43, 28)  
min = x[0]  
i = 1                     # initial value  
while(i < len(x)) :  
 if x[i] < min:   
  min = x[i]   
 i += 1                   # increment    
print("The smallest value is", min)  

#example 5 
x = input("Are you nuts? Yes or No? ")  
while(x.upper() != "YES") :  
 x = input("Again, are you nuts? ")  
print("Just kidding!! Thank you.") 
 
# example 6 
print("   1 2 3 4 5 6 7 8 9") 
print("--------------------")  
for i in range(1, 10) : 
 s = str(i) + "|"    
 for j in range(1, 10) :
  s = s + " " + str(i*j)     
 print(s)