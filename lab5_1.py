s = ""          # example 1  
for i in (1, 2, 3, 4):    
 s = s + str(i) + " " 
print(s)  

s = ""        # example 2  
for i in (1, '2', 3.09, True, None):   
 s = s + str(i) + " " 
print(s)  

x = (1, 2, 3, 4)    # example 3 
s = ""  
for i in x :   
 s = s + str(i) + " " 
print(s);  

x = "Python"   # example 4 
s = ""  
for i in x :  
 s = s + str(i) * 2 + " "    # display twice 
print(s, "\n")  

x = "Python"  # example 5 
s = "" 
j = 1  
for i in x :  
 s = s + str(i * j) + "\n"  
 j = j + 1  
print(s)  

s = "" # example 6  
for i in ['P', 'y', 't', 'h', 'o', 'n'] :    
 s = s + str(ord(i)) + " " 
print(s, "\n")  

x = ['Apple', 15, True, 3.15]  # example 7 
s = ""  
for i in x: 
 s = s + str(i) + " " 
print(s)  

x = []    # example 8   
for i in (4, 5, 6, 7):  
 x.append(i)   
print(x, "\n")  
s = ""    # example 9  
for i in (66, 67, 68, 69, 70, 71):  
 s = s + chr(i)   
print(s) 