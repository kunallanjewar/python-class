# Student: Kunal Lanjewar
# Programming Ex. : 07

def PV(FV, r, n):  
 import math  
 r = (r/100)  
 return (FV/(1+r)**n)
 
def main():  

 
 FV = float(input("Enter the future value: ")) 
 r = float(input("Enter the interest rate: ")) 
 n = float(input("Enter the number of years: "))  
 pv = PV(FV, r, n)
 
 print("$%.2f" % pv)
  
if __name__ == "__main__":   
     main()