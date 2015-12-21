def getFactorial(x):  
 fac = 1    

 for i in x:   
  fac= fac * i    

 return fac    

def getSum(x):  
 sum = 0    
  
 for i in x:   
   sum = sum + i    
 return sum    

def getAverage(x):  
 avg = getSum(x) / len(x) 
 return avg
  
def main():  
 max = int(input("Enter the maxium: "))  
 n = range(1, max+1)  
 print("You defined:", n)  
 print("\n----Report------")  
 print("Factorial", getFactorial(n))  
 print("Sum", getSum(n))  
 print("Average", getAverage(n))   

if __name__ == "__main__":
     main()