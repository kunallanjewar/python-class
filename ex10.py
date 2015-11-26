# Student Name: Kunal Lanjewar
# Programming Ex: 10

import os  

def addContent():
 dir = os.getcwd() + "\\elite01"  
 if not os.path.exists(dir):   
  os.mkdir(dir);


 f=open("elite01\\message.txt", 'a')
 f.write("This is Programming Exercise 10.")
 f.close()
  
def showContent():
 dir = os.getcwd() + "\\elite01" 
 f = open("elite01\\message.txt", 'r');
 print(f.read())
 f.close()
 
 for item in os.listdir(dir):
  print ("['",item,"']")

def main():

 addContent()
 showContent()  

if __name__ == "__main__":
    main() 