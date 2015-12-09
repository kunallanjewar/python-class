import os 
import os.path 
import time  

files = []       # emply python list  

def filterDir(dir):  
 for item in os.listdir(dir) :   
  if( os.path.isfile(dir + "\\" + item) ) :  
   files.append(item)      # append to files  

def showDateTime(dt):     # convert Epoch time to wall clock time  
 return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(dt))  

def showFileInfo(p):    
 tc = showDateTime(os.path.getctime(p))  
 la = showDateTime(os.path.getatime(p))  
 lm = showDateTime(os.path.getmtime(p))    

 result = os.path.basename(p) + "\t" + str(tc) + "\t"  
 result = result + str(la) + "\t" 
 result = result + str(lm) + "\t"  
 result = result + str(os.path.getsize(p)) + "\n"   
 return result  

def getReport(dir):   
 f = open('fileinfo.dat', 'w+')   
 f.write("File Name\tTime Created\tLast Access\tLast Modified\tFile Size\n")   

 for item in files:  
  s = showFileInfo(dir + "\\" + item)  
  f.write(s)  
  print(s)   
 f.close()  

def main():  
 dir = input("Enter a path to a directory: ")  
 filterDir(dir)   
 getReport(dir)  

if __name__ == "__main__":
     main() 