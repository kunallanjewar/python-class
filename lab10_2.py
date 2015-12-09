import os 
 
def searchAreaCode(ac):  
 f = open("areacode.txt", 'r'); #open for reading only   
 areaList = f.readlines() # append to the list "areaList" 
 result = 'No matched area code!'    

 for line in areaList:  #  check every element   
  s = line.split('-')    
  if (s[0] == ac):  
   result = s[1]    
   break             # terminate for loop if matched 

 print(result)      # print result after for loop stops   

def main():  
 ans = "y"  

 while (ans.upper() != 'N') :  
  ac = input("Enter a area code: ")   
  searchAreaCode(ac)    

  ans = input("Search again [Y/N]? ")  

if __name__ == "__main__":    
     main()