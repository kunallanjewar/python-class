def tuple2String(tuple):  
 s = ''  
 for i in range(len(tuple)): 
  s = s + tuple[i] + " "  
 s = s.replace(' .', '.')
 s = s.replace(' ,', ',')  
 print(s)   

def list2String(list):  
 s = ''  
 for i in range(len(list)):   
  s = s + list[i] + " "    
 s = s.replace(' .', '.')  
 s = s.replace(' ,', ',')  
 print(s)   

def dictKey2String(dict):  
 k = list(dict.keys())   
 s = ''    

 for i in range(len(k)):   
  s = s + str(k[i]) + " "  
 print(s)   

def dictValue2String(dict):   
 v = list(dict.values())    
 s = ''    
 for i in range(len(v)):  
  s = s + str(v[i]) + " "  

 print(s)

def main():  
 # tuple  
 t = ('Life', 'is', 'a', 'journey', '.', 'Time', 'is', 'a', 'river', '.')     

 # list   
 l = ["Look", "in", "the", "mirror", "to", "meet", "your", "true", "enermy", ",", "lover", ",", "and", "friend", "."]
 
 # dictionary  
 wd = {   "Mon": 'getsu-yoobi',   "Tue": 'ka-yoobi',   "Wed": 'sui-yoobi',   "Thu": 'moku-yoobi',   "Fri": 'kin-yoobi',   "Sat": 'do-yoobi',   "Sun": 'nichi-yoobi'   }    

 tuple2String(t)  
 list2String(l)  
 dictKey2String(wd)  
 dictValue2String(wd)  

if __name__ == "__main__":     
     main()