import datetime 
dt = datetime.datetime.now() # get the current date/time 
h = int(dt.strftime("%H")) # get hour value  
h = h % 12  # turn 24 hour format to 12 hour format 
 
print("Python if structure")  
if (h == 0) : print("It is twelve o\'clock") 
if (h == 1) : print("It is one o\'clock") 
if (h == 2) : print("It is two o\'clock") 
if (h == 3) : print("It is three o\'clock") 
if (h == 4) : print("It is four o\'clock") 
if (h == 5) : print("It is five o\'clock") 
if (h == 6) : print("It is six o\'clock") 
if (h == 7) : print("It is seven o\'clock") 
if (h == 8) : print("It is eight o\'clock") 
if (h == 9) : print("It is night o\'clock") 
if (h == 10) : print("It is ten o\'clock") 
if (h == 11) : print("It is eleven o\'clock")
  
print("\nswitch simulation")  

switch = {  
 0: "It is twelve o\'clock",  
 1: "It is one o\'clock",  
 2: "It is two o\'clock",  
 3: "It is three o\'clock",  
 4: "It is four o\'clock",  
 5: "It is five o\'clock",  
 6: "It is six o\'clock",  
 7: "It is seven o\'clock",  
 8: "It is eight o\'clock",  
 9: "It is eight o\'clock",  
 10: "It is ten o\'clock",  
 11: "It is eleven o\'clock", 
}  
print(switch[h])