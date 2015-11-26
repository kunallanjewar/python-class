zodiac = ""  

y = int(input("What year were you born? "))
  
print("\nMethod 1: if structure") 
 
y = y % 12  

if (y==0): zodiac = "Monkey" 
elif (y==1): zodiac = "Rooster"
elif (y==2): zodiac = "Dog"
elif (y==3): zodiac = "Pig"
elif (y==4): zodiac = "Rat"
elif (y==5): zodiac = "Ox"
elif (y==6): zodiac = "Horse"
elif (y==7): zodiac = "Rabbit"
elif (y==8): zodiac = "Dragon"
elif (y==9): zodiac = "Snake"
elif (y==10): zodiac = "Horse"
else: zodiac = "Goat"  

print("You were born in", zodiac, "year.") 
 
print("\nMethod 2: swtich simulation") 
 
switch = {
  0: "Monkey",
  1: "Rooster",
  2: "Dog",  
  3: "Pig",
  4: "Rat",
  5: "Ox",
  6: "Horse",
  7: "Rabbit",
  8: "Dragon",
  9: "Snake",
  10: "Horse",
  11: "Goat"
}  

print("You were born in", switch[y], "year.")