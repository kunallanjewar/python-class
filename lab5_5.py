print("FOR LOOP\n") 
s1 = input("Enter your first name: ");  
for i in range(len(s1)) :  
 print((i+1) * s1[i])  
for i in range(len(s1)) :  
 print((len(s1) - i) * s1[i])  
print()  
print("\nWHILE LOOP\n") 
s2 = input("Enter your last name: ");  
i = 0  
while (i < len(s2)):  
 print(s2[i] * (i+1))  
 i = i + 1  
i = 0 
while (i < len(s2)):  
 print(s2[i] * (len(s2) - i))  
 i = i + 1