string="Most of the time we spend a lot of time trying to to convince people about what we are capable of doing"
#length of the string
length = len(string)
print(length)
#looping through the string
for i in range(length):
    print(string[i])
#this can also be used
for characters in string:
    print(characters)
#slicing a string
slice1 = string[5:]
slice2 = string[:8]
slice3 = string[9:20]
print(slice1)
print(slice2)
print(slice3)