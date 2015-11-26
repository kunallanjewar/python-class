#example 1 - list 
l1 = [3, 6, 9]
print(l1)

l2 = ['A', 'B', 'C', 'D']
print(l2)

l3 = ['Python', 3.4, True]
print(l3)  
#example 2 - tuple
t1 = (3, 6, 9)
print(t1)  
t2 = ('A', 'B', 'C', 'D')
print(t2)  
t3 = ('Python', 3.4, True)
print(t3)  
#example 3 - dictionary
d={'OH':"Ohio", 'TX':"Texas"}
print(d)  
#example 4  
ans = [] #empty list  
fullname = input("What is your full name? ")
major = input("What is your major? ")
f = input('What is the current temperature in Fahrenheit? ')  
ans.append(fullname)
ans.append(major)
#ans.append(weight)  
# C=(F-32)x(5x9)
print('It is', (float(f) - 32) * (5/9), "degrees in Celsius.")