def ipv4_binary(ipaddr):  
 s = ipaddr  
 s = s.split('.')      # use . as delimiter  
 
 for i in range(len(s)):  
  s[i] = bin(int(s[i]))   # convert the value to binary
  s[i] = s[i].replace('0b', '')    # remove the leading '0b' 

 for i in range(len(s)):    
  if (len(s[i]) == 8) :    
   pass   
  else:   
   n = 8 - len(s[i])       

   for j in range(n):     
    s[i] = '0' + s[i]      

 x = '.'  
 s = x.join(s)     # recombine the string  
 print(s)  


def ipv6(ip):  
 s = ip.split('.')      # use . as delimiter    
 ipv6 = ""  
 for i in s:   
  if (i == s[1]):
    ipv6 = ipv6 + toHex(i) + ":"    
  else:     
    ipv6 = ipv6 + toHex(i)     

 ipv6 = "0:0:0:0:0:ffff:" + ipv6     # append the ipv6 heading
 print(ipv6)   

def toHex(s):  
 s = hex(int(s))  
 s1 = s[2:]    

 if (len(s1) == 1): s1 = "0" + s1    
 return s1  

def main():  
 ipaddr = input("Enter a valid IPv4 address: ")    
 ipv6(ipaddr)  
 ipv4_binary(ipaddr)  

if __name__ == "__main__":
     main() 