print(3 < 5, "apple" < "Apple", 4 <= 5, "Orange" <= "Oranges") # example 1 
print(7 > 3, "school" > "School", 3 >= 5, "tree" >= "trees") 
print(6 == 7, "home" == "Home", 6 != 7, "home" != "Home") 
 
print('A' < 'B', "apple" < "Apple", "appLe" < "apple") #example 2 
print(ord('a'))   

print(64 == 64.0, 3e5 == 300000)   #example 3  

a = 1    # example 4 
b = 4 
print(a == b)  

a = 5 
print(a < 7)  

s = "apple" 
print(s < "orange")  

a = 4 
b = 1 
print(a < b, 3 > b)
  
print((3 > 2) and (5 < 7), (3 < 2) or (5 < 7), not (3 < 2))   #example 5  

# example 6 
print(True and True, True and False, (5.3 >= 5) and (6.0 <= 6)) 
print(("a" < "b") and ("b" < "c"), ("a" != "") and ("a" != "a")) 
print(('a' in 'apple') and ('b' not in 'apple'))  

#example 7 
print(True or True, True or False, (3 < 4) or (4 < 5)) 
print((5 in range(0, 5)) or (4 in range(0, 5))) 
print(('a' == 'A'.lower()) or ('B' != 'b'.upper()))
  
print(not -2, not "apple", not " ", not 0, not None)   #example 8 