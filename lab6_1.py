# list 
lst =[ 1, 2, 3, 4, 5 ]; 
number = input("Enter an integer (0-4): ");  
# user entries are string, use int() for type casting 
print("You selected", lst[int(number)],"!");  

# tuple  
tup = ("dog", "cat", "horse", "pig", "rat", "cow"); 
animal = input("Enter another integer (0-5): "); 
print("You picked", tup[int(animal)],"!");  

# dictionary  
dic = { "cis245": "Perl Programming", "cis246": "PHP Programming","cis247": "Python Programming" };  
course = input("Enter a course (e.g., cis245): ");  
print("You selected", dic[course],"!");