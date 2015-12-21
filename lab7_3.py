def month_payment(P, r, n):  
 import math  
 r = (r/12)/100  
 return (r + (r / (((1+r)**n) - 1))) * P  

def total_payment(mp, n):
 return mp * n  

def total_paid_interest(tp, P):  
 return tp - P  

def FV(P, r, n):  
 n = n/12  
 r = r/100  
 return (P * ((1+r)**n))  

def main():  
 P = float(input("Enter the principal: ")) 
 r = float(input("Enter the annual interest rate: ")) 
 n = int(input("Enter the total number of payments: "))  
 mp = month_payment(P, r, n)   
 tp = total_payment(mp, n)  
 ti = total_paid_interest(tp, P)  
 fv = FV(P, r, n)  
 print("\n--------REPORT---------")  
 print("Total payment:", "$%.2f" % tp)  
 print("Monthly payment:", "$%.2f" % mp)  
 print("Total paid interest:", "$%.2f" % ti)  
 print("Future value:", "$%.2f" % fv)  
if __name__ == "__main__":   
     main()