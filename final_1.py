#Student: Kunal Lanjewar
#FileName: final_1.py


import time
import datetime
global dt


dt = datetime.datetime.now()
hr = dt.strftime("%H")

h = int(hr)

if (h >= 12):
 h = h-12
 print(h)
 
 if (h == 0):
  print("Zero")

 elif(h==1):
  print("One")

 elif(h==2):
  print("Two")

 elif(h==3):
  print("Three")

 elif(h==4):
  print("Four")

 elif(h==5):
  print("Five")

 elif (h == 6):
  print("Six")

 elif(h==7):
  print("Seven")

 elif(h==8):
  print("Eight")

 elif(h==9):
  print("Nine")

 elif(h==10):
  print("Ten")

 else:
  print("Eleven")

if (int(hr)<12):
 if (h == 0):
  print("Zero")

 elif(h==1):
  print("One")

 elif(h==2):
  print("Two")

 elif(h==3):
  print("Three")

 elif(h==4):
  print("Four")

 elif(h==5):
  print("Five")

 elif (h == 6):
  print("Six")

 elif(h==7):
  print("Seven")

 elif(h==8):
  print("Eight")

 elif(h==9):
  print("Nine")

 elif(h==10):
  print("Ten")

 else:
  print("Eleven")









 


