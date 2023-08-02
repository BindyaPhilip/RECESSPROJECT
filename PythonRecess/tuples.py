#1
x = ("samsung", "iphone", "tecno", "redmi")
favorite_brand = "iphone"  

if favorite_brand in x:
    print("My favorite phone brand is:", favorite_brand)
else:
    print("My favorite phone brand is not in the tuple.")
#2
print(x[-2])
#3
x_list = list(x)
index = x_list.index("iphone")
x_list[index] = "itel"

# Convert the list back to a tuple
x_updated = tuple(x_list)

# Print the updated tuple
print(x_updated)
#4
x = ("samsung", "iphone", "tecno", "redmi")

# Convert the tuple to a list
x_list = list(x)
x_list.append("Huawei")
x_updated = tuple(x_list)
print(x_updated)
#5
x = ("samsung", "iphone", "tecno", "redmi")
for i in  x:
    print (i)
#6
x = ("samsung", "iphone", "tecno", "redmi")
x_updated = tuple(item for item in x if item != "samsung")
print(x_updated)
#7
cities = tuple(["Kampala", "Entebbe", "Jinja", "Mbarara", "Gulu"])
print(cities)
#8
cities = ('Kampala', 'Entebbe', 'Jinja', 'Mbarara', 'Gulu')
city1, city2, city3, city4, city5 = cities
print(city1)
print(city2)
print(city3)
print(city4)
print(city5)
#9
print(cities[1:4])
#10
first_names = ("John", "Jane", "Michael", "Sarah")
last_names = ("Muwanga", "Kiiza", "Mugerwa", "Natukunda")

# Join the two tuples
full_names = first_names + last_names
print(full_names)
#11
colors = ("red", "blue", "green")
print(colors*3)
#12
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print(thistuple.count(8))






