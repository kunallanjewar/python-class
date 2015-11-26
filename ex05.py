#Student: Kunal Lanjewar
#Programming: Exercise 05



#---------------------For Loop-------------------------------#

print("\nFOR LOOP\n") 

s = input("Enter your First name: ");  

for i in range(len(s)-1, -1, -1):    
 print((i+1) * s[i]) 
