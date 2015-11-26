n1 = float(input("Enter the first number: ")) 
n2 = float(input("Enter the second number: "))  

print("sum:", str(n1 + n2)) 
print("difference:", str(n1 - n2)) 
print("product:", str(n1 * n2)) 
print("quotient:", str(n1 / n2)) 
print("remainder:", str(n1 % n2)) 
print("integer division:", str(n1 // n2)) 
print("exponent:", str(n1 ** n2)) 
 
x1 = n1 
y1 = n2 
x1 += 1 
y1 -= 1 
 
print("increment by 1:", str(x1)) 
print("decrement by 1:", str(y1))  
print("(n1 >= n2):", n1 >= n2) 
print("(n1 == n2):", n1 == n2)  
print("bitwise and:", str(int(n1) & int(n2))) 
print("bitwise or:", str(int(n1) | int(n2))) 