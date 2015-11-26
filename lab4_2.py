print("Method 1")  

score = float(input("Enter the score: "))
  
if (score < 60) : grade = "F"  
if (score >= 60) : grade = "D"  
if (score >= 70) : grade = "C" 
if (score >= 80) : grade = "B"  
if (score >= 90) : grade = "A"  

print("It is a", grade, ".\n")  

print("\nMethod 2") 
 
score = float(input("Enter the score: ")) 
 
if (score >= 60):  
 if (score >= 70):   
  if (score >= 80):    
   if (score >= 90):     
    grade = "A"    
   else:     
    grade = "B"   
  else:    
   grade = "C"  
 else:   
  grade = "D" 
else:   
 grade ="F"  

print("It is a", grade, ".\n")  

print("\nMethod 3")  

score = round(float(input("Enter the score: ")) * 100)  

if (score in range(0, 6000)):  
 print("It is an F.") 
if (score in range(6000, 7000)):  
 print("It is a D.")  
if (score in range(7000, 8000)):  
 print("It is a C.")   
if (score in range(8000, 9000)):  
 print("It is a B.")   
if (score in range(9000, 10000)):  
 print("It is an A.")  

print("\nMethod 4") 
  
score = float(input("Enter the score: ")) 
 
if (score >=90):   
 print("It is an A."); 
elif (score >=80):   
 print("It is a B."); 
elif (score >=70):   
 print("It is a C."); 
elif (score >=60):   
 print("It is a D."); 
else:   
 print("It is an F.");