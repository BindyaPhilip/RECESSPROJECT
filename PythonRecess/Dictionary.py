#1
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
print(Shoes["size"])
#2
Shoes["brand"] = "Adidas"
print(Shoes)
#3
Shoes["type"] = "sneakers"
print(Shoes)
#4
print(list(Shoes.keys()))
#5
print(list(Shoes.values()))
#6
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40,
    "type": "sneakers"
}
if "size" in Shoes:
    print("Key 'size' exists in the dictionary")
else:
    print("Key 'size' does not exist in the dictionary")
#7
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40,
    "type": "sneakers"
}
# Loop through the keys and values of the dictionary using keys()
for key in Shoes.keys():
    value = Shoes[key]
    print(f"Key: {key}, Value: {value}")
#8
del Shoes["color"]
print(Shoes)
#9
Shoes.clear()

print(Shoes)
#10
# Original dictionary
original_dict = {
    "name": "Philip",
    "age": 23,
    "city": "Kampala"
}

# Copy the dictionary
copied_dict = dict(original_dict)

# Modify the copied dictionary
copied_dict["age"] = 25
copied_dict["city"] = "Entebebe"

# Print the original and copied dictionaries
print("Original Dictionary:", original_dict)
print("Copied Dictionary:", copied_dict)
#11
# Nested dictionary example
student = {
    "name": "Philip",
    "age": 20,
    "grades": {
        "math": 85,
        "physics": 90,
        "economics": 75
    }
}
print("Student Name:", student["name"])
print("Student Age:", student["age"])
print("Math Grade:", student["grades"]["math"])
print("Physics Grade:", student["grades"]["physics"])
print("Economics Grade:", student["grades"]["economics"])










