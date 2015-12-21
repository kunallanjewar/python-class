def main():
 x = [] 
  
 def populate(): 
  for i in range(0, 47):  # 0 ~ 46    
   x.insert(i, i + 1)    # 1 ~ 47  
 
 def shuffle():   
  import random  
  for i in range(0, 47):   
   n = random.randint(0, 46)   
   temp = x[n]   # swap x[n] and x[i]   
   x[n] = x[i]    
   x[i] = temp  
 
 def showIt():  
  import random  
  s = ""  
  for i in range(0, 5):     # display first 5 number 
   s = s + str(x[i]) + " "   
  
  s = s + "mega: " + str(random.randint(1, 27))   # add mega number  
  print(s)  
 
 def showDialog():   
  n = int(input("How many drawings?: "))  
  i = 0   
  while (i < n):    
   shuffle()   # call shuffle
   showIt()    # call showIt   
   i = i + 1  

 populate()   # call populate  
 showDialog() # call showDialog 
main()        # call main 