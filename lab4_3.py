print("Method 1") 
 
n1 = input("Enter the first number: ") 
ops = input("Enter the operator: ") 
n2 = input("Enter the second number: ")
  
if (ops == '+') : print(float(n1) + float(n2)) 
if (ops == '-') : print(float(n1) - float(n2)) 
if (ops == '*') : print(float(n1) * float(n2)) 
if (ops == '/') : print(float(n1) / float(n2)) 
if (ops == '%') : print(float(n1) % float(n2)) 
if (ops == '**') : print(float(n1) ** float(n2))  

print("\nMethod 2")  

n1 = input("Enter the first number: ") 
ops = input("Enter the operator: ") 
n2 = input("Enter the second number: ")  

def Add() : return (float(n1) + float(n2)) 
def Sub() : return (float(n1) - float(n2)) 
def Mul() : return (float(n1) * float(n2)) 
def Div() : return (float(n1) / float(n2)) 
def Mod() : return (float(n1) % float(n2)) 
def Exp() : return (float(n1) ** float(n2)) 
 
switch = {  
 "+": Add(),  
 "-": Sub(),  
 "*": Mul(),  
 "/": Div(),  
 "%": Mod(),  
 "**": Exp() 
}
  
try:
  print(switch[ops]);
except KeyError as ex:
  print("No matching case")