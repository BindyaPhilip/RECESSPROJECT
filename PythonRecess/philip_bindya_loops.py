#condition
age = 22
if age < 20:
 print("Young")
elif age>=20 and age<=30:
 print("Adult")
else:
 print("Mature")
#loops(for and while)
fruits = ["apple", "banana", "orange", "mango"]
for fruit in fruits:
  print(fruit)
#break and continue in while loop
#break
i = 1
while i < 6:
 if i == 3:
  break
 i+=1
print(i) 
#continue
i=0
while i < 8:
  if i == 4:
   continue
  i+=1
  print(i)