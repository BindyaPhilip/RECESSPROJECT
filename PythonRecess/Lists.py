#1
playernames=["Messi","Ronaldo","Neymar","Suarez","Xavi"]
print(playernames[1])
#2
playernames[0]="Mbappe"
print(playernames)
#3
playernames.append("Kane")
print(playernames)
#4
index=3
playername="Iniesta"
playernames.insert(index,playername)
print(playernames)
#5
del playernames[3]
print(playernames)
#6
print(playernames[-1])
#7
positions=1,2,3,4,5,6,7
print(positions[2:5])
#8
countries = ['USA', 'Canada', 'Germany', 'France', 'Japan']

# Making a copy using the slice operator
countries_copy = countries[:]

# Modifying the original list
countries.append('Australia')

# Displaying both lists
print("Original List:", countries)
print("Copied List:", countries_copy)
#9
for country in countries:
    print(country)
#10
animals = ['lion', 'tiger', 'elephant', 'zebra', 'giraffe']
# Display the sorted lists
print("Ascending Order:",sorted(animals) )
print("Descending Order:", sorted(animals, reverse=True))
#11
for animal in animals:
    index = animal.find("a")
    if(index!=-1):
        print(animal)
#12
first_names = ['John', 'Emma', 'Michael', 'Sophia']
last_names = ['Mukasa', 'Muwanguzi', 'Semaganda', 'Mutesi']

# Join the first names and last names
full_names = [first + ' ' + last for first, last in zip(first_names, last_names)]

# displaying
for name in full_names:
    print(name)

