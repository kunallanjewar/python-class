lsta =[ 1, 2, 3, 4, 5 ] 
print(len(lsta), lsta.count(3))  

lstb = lsta        # copy list 
print(lsta, lstb) 
print(lsta == lstb)  

lsta[2] = 7 
print(lsta, lstb)     # synchronization  

lstb.insert(4, 9) 
print(lsta, lstb)   

lsta.remove(7) 
print(lsta, lstb)   

lstb.pop(3)   # delete the element of index 3 
print(lsta, lstb)   

del lsta[:]         # delete all elements  
del lstb[:]  
print()  

tupa = ("dog", "cat", "horse", "pig", "rat", "cow") 
tupb = tupa         # copy tuple 
print(tupa, tupb) 
print(tupa == tupb)  

# tuple elements can't be removed, redefine them 
tupa = None 
tupb = None  

dica = { "cis245": "Perl Programming","cis246": "PHP Programming","cis247": "Python Programming" }  
print(dica.keys())     # print all keys 
print(dica.values())   # print all values 
print(dica.items()) # prnt all display key-value pairs  
print('cis247' in dica)  
dicb = dica.copy()      # copy dictionary 
print(dica == dicb)  
dica.clear()  # use delete all elements 
dicb.clear()  

print("lsta is", lsta, "lstb is", lstb) 
print("tupa is", tupa, "tupb is", tupb) 
print("dica is", dica, "dicb is", dicb)  
print("\n\nObject deleted...\n") 
del lsta 
del lstb 
del tupa 
del tupb 
del dica 
del dicb 