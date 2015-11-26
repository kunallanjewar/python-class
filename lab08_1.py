def reverseIt(s):
 s1 = s
 s2 = ""  

 for i in range(len(s1)-1, -1, -1):   
  s2 = s2 + s1[i]    
 print(s2 * 2)       # display twice   

def backwardIndex(s):    
 s1 = ''    

 # backward  
 for i in range(1, len(s)+1):   # 1 ~ len(s)   
  s1 = s1 + s[-i] + " "     
 print(s1)   

def multipleFormat(s): 
 print(s.upper())  
 print(s.lower())  
 print(s.capitalize())  
 print(s.title())    

def replaceIt(s):  
 s = s.split();    
 
 for i in range(len(s)) :   
  s[i] = "<i>" + s[i] + "</i>"    
 print(s)   

def main():  
 s = input("Enter a sentence: ")  
 reverseIt(s)  
 backwardIndex(s)  
 multipleFormat(s)  
 replaceIt(s)   

if __name__ == "__main__":     
     main()