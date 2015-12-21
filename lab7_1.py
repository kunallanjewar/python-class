def showCPU():  
 import platform  
 print(platform.processor())  

def showOS():   
 import os;   
 print(os.name)  

def getSysInfo():      # function declaration  
 import platform       # function body  

 print("System Info: \n",   
  "system: ", platform.system(), "\n",   
  "machine: ", platform.machine(), "\n",   
  "platform: ", platform.platform(), "\n",  
  "uname: ", platform.uname(), "\n",   
  "version: ", platform.version(), "\n")   # end of function 
 
def getEV():  
 import os  
 print(os.environ['USERNAME'])
  
def main():  
 s  = "--------------------------\n" 
 s += "| A. Show CPU info       |\n"  
 s += "| B. Show OS info        |\n" 
 s += "| C. Show System info    |\n" 
 s += "| D. Show User name      |\n" 
 s += "--------------------------\n"  

 print(s)  

 s = input("Enter your choice [A/B/C/D]:")  
 s = s.upper()
    
 if (s == 'A'): showCPU()  
 elif (s == 'B'): showOS() 
 elif (s == 'C'): getSysInfo()  
 elif (s == 'D'): getEV()  
 else: print("Invalid option!") 
 
if __name__ == "__main__":     
    main()
