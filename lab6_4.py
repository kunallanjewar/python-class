# tuple of different types of elements 
x = ( [14, 16], ("apple", "banana"), [3.2, 5.6], {0:True, 1:False} )  

for r in range(len(x)):
 print(type(x[r]))     # display the data type  
 
for c in range(len(x[r])):  
 s = "x[" + str(r) + "][" + str(c) + "] = " + str(x[r][c])   
 print(s)  

print()    

#tuple of differnt elements with inequal sizes 
y = [ {0:"dog", 1:"cat", 2:"cow"}, [245, 246, 247, 248], (4.5, 4.6, 4.7, 4.8, 4.9), (True) ]    
r = 0 
while (r < len(x)): 
 print(type(x[r]))     # display the data type  
 c = 0  
 while (c < len(x[r])):   
  s = "y[" + str(r) + "][" + str(c) + "] = " + str(x[r][c]) 
  print(s)   
  c += 1  
 r += 1   
print()   

#dictionary of differnt elements with inequal sizes 
z = { "lst": [1, 2, 3, 4],"tup": (5, 6, 7),"dic": {0: "tuna", 1: "salmon"}  }  
zk = sorted(z.keys())   # a list of keys  

for r in range(len(z)):    
 for c in range(len(z[zk[r]])):   
  s = "z['" + str(zk[r]) + "'][" + str(c) + "] = " + str(z[zk[r]][c])   
  print(s)