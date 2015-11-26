x = 5    #example 1 
print(x is 5)  

x = 5 
print(x is not 4)
  
x = (4, 7, 2, 1) 
print(2 in x, 3 not in x) 
 
x = 2     #example 2 
y = x 
print(id(x), id(y)) 
print(x is y, x is not y)  

x = 3 
y = 3 
print(id(x), id(y)) 
print(x is y, x is not y)  

x = (1, 2, 3) 
y = (1, 2, 3) 
print(id(x), id(y)) 
print(x is y, x is not y)
  
x = "apple"    # example 3 
print('a' in x, 'a' not in x)  

x = [0, 1, 2, 3, 4, 5] 
print(3 in x, 7 in x, 9 not in x, 2 not in x)  

y = (4.3, 2.1, 7.5, 3.4) 
print(7.5 in y, 7.4 in y, 3.5 not in y, 2.1 not in y) 
 
z = ["apple", "banana", "cherry"] 
print("banana" in z, "Banana" in z, "Apple" not in z, "cherry" not in z)  

print(5 in range(2, 10))  

print(5 & 6, 5 | 6, ~5)      #example 4 
print((5|6) == (5|3)) 
print(3 << 2, 11 >> 1, 67 >> 3, 127 >> 2) 