import os

def outputHTML():  
 html = "<!Doctype html><html>"    
 if os.name == "nt" :  
  html += "<body bgcolor = 'pink'>"  
  html += "Windows OS<br />"     
  sysDrive = os.getenv("SystemDrive")  
  dirList = os.listdir(sysDrive + "\\")  
 
 elif os.name == "posix" :  
  html += "<body bgcolor = 'yellow'>" 
  html += "Unix/Linux OS<br />"      
  dirList = os.listdir("~")      
 
 elif os.name == "mac" :  
  html += "<body bgcolor = 'menu'>"  
  html += "Mac/Apple OS<br />"      
  dirList = os.listdir("::")     

 else:   
  html += "<body bgcolor = 'orange'>"  
  html += "Unknown OS<br />"      
  dirList = os.listdir("")  
  html += "Found the following files and directories:<ul>"  
  
 for i in dirList:  
  html += "<li><a href=\'"+ i + "\'>" + i + "</a><br>"  
 html += "</ul>"  
 html += "</body></html>"  
 return html  

def main():    
 f = open('myos.html', 'w')   
 f.write(outputHTML())  
 f.close()  
if __name__ == "__main__":
     main()