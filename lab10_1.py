import os  

def addContact():  
 firstName = input("Enter first name: ")  
 lastName = input("Enter last name: ")   
 phoneNo = input("Enter phone number: ")   
 emailAddr = input("Enter email address: ")  
 
 f = open("phonebook.dat", 'a') # create a new or open an existing file  
 f.write(firstName + ":")  
 f.write(lastName + ":")  
 f.write(phoneNo + ":")  
 f.write(emailAddr + "\n")  
 f.close()  

def showContact():  
 print("You have the following records:\n");  
 f = open("phonebook.dat", 'r'); #open for reading only    
 print(f.read()) 
 f.close()  

def main():  
 ans = input("Add new contact [Y/N]: ")  
 ans = ans.upper()   
 while (ans != 'N'):   
  addContact()
  ans = input("\nAdd new contact [Y/N]: ")
  ans = ans.upper() 
 showContact()  
if __name__ == "__main__":     main() 