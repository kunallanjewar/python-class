def acct2Number():  
 s = input("Enter the dollar amount: ")  
 result = ""  
 for i in range(len(s)):   
  if (s[i] == '$') :    
   pass   
  elif (s[i] == ',') :    
   pass    
  else :    
   result = result + s[i]     

 print(result)  

def number2Acct():   

 s = input("Enter a large number: ")  
 print('${:,.2f}'.format(float(s)))  


def number2Acct_asian():  
 s = input("Enter a large number: ")  
 s = '{:.2f}'.format(float(s))    
 result = "$" + s    
 s = s.split('.')    

 if (len(s[0]) > 4):  
  result = ''   
  s1 = s[0]      
  n = len(s[0]) // 4      
  
  for i in range(n):    
   if (i == (n-1)) :
    result = "$" + s1[-5-(i*4):-1-(i*4)] + result    
   else:     
    result = "," + s1[-5-(i*4):-1-(i*4)] + result  
  result = result + "." + s[1]     
 print(result)   

def main():  
 acct2Number()  
 number2Acct()  
 number2Acct_asian()   

if __name__ == "__main__":
     main()