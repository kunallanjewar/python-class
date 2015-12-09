import os  

def searchFile(fileName, keyword):  
 f = open(fileName, 'r')  
 n = 0    

 for line in f:   
  if (line.count(keyword) > 0) :    
   n = n + line.count(keyword)    

 f.close()  
 print("The word \'" + keyword + "\' appears " + str(n) + " time(s) in the web page.")   

def main():  
 import urllib  
 import urllib.request   

 url = input("Enter the URL: ")   

 wp = urllib.request.urlopen(url) 
 webcontent = wp.read()   # read the web content   
 webcontent = str(webcontent)   
 f = open("webpage.html", 'w')        # create a local file    
 f.write(webcontent)              # save web content  
 f.close()   
 keyword = input("Enter a keyword: ")   
 searchFile("webpage.html", keyword)  

if __name__ == "__main__":  
   main()  