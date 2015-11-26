# Student: Kunal Lanjewar
# FileName: final_2.py
  
try:  
 f = open("h:\\nosuchdirectory\\nosuchfile.txt","w") 
 f.write("This is the grape file")
 f.close() # do not modify this line
except IOError as ex: 
 print(ex)  