def string2Array(s):  
 s = s.split(" ")  
 for i in range(len(s)):     # remove punctuation   
  s[i] = s[i].strip(',')   
  s[i] = s[i].strip('.')   
  s[i] = s[i].strip(':')   
  s[i] = s[i].strip('!')   
  s[i] = s[i].strip('-')  
  s[i] = s[i].strip('\'')  
  s[i] = s[i].strip('\"')    
 s = set(s)        # get distinct     
 s = list(s)       # convert to Python list   
 subStringCount(s)   

def subStringCount(s):  
 print("\nSubstring\t", "Frequency")  
 print("---------\t", "---------")    

 for i in range(len(s)):  
  c = original.count(s[i])     # count how many times s[i] appears      
  
  print(s[i], '\t', '{:10d}'.format(c))  # right aligned    

def main():  
 global original    
 original = input("Enter a paragraph: ")    
 s = original.lower()    # convert to lower-case    
 string2Array(s)   

if __name__ == "__main__":   
     main() 