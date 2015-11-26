income = float(input("Enter your annual income: "))
  
if (income >= 0 and income <= 25000) :  tax_rate = 0 
elif (income >= 25000 and income <= 55000) :  tax_rate = 25 
elif (income >= 55000 and income <= 105000) :  tax_rate = 28 
elif (income >= 105000 and income <= 250000) :  tax_rate = 33 
else:  tax_rate = 40  

depd = int(input("Enter the number of dependents: "))  

if (depd < 3) :  deductible = 1000 
if (depd < 5) :  deductible = 6500 
if (depd > 5) :  deductible = 10000   

switch = {
  0: "financially disadvantaged",
  25: "low-income",
  28: "middle-class",
  33: "high-income",
  40: "rich" 
}  
  
taxable = income * (1-tax_rate/100) - deductible  
 
if (taxable <= 0) :  taxable = 0  

print("Your year 20nn taxable income is", "%.2f" % taxable) # 2 digits next to decimal point  

print("You are rated as:", switch[tax_rate]) 