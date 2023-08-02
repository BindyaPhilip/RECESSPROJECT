#1
beverages = set(["coffee", "tea", "juice"])
print(beverages)
#2
beverages = {"coffee", "tea", "juice"}
beverages.update(["soda", "smoothie"])
print(beverages)
#3
mySet = {"oven", "kettle", "microwave", "refrigerator"}
if "microwave" in mySet:
    print("Microwave is present in the set")
else:
    print("Microwave is not present in the set")
#4
mySet = {"oven", "kettle", "microwave", "refrigerator"}
mySet.remove("kettle")
print(mySet)
#5
mySet = {"oven", "kettle", "microwave", "refrigerator"}
for item in mySet:
    print(item)
#6
mySet = {"apple", "banana", "orange", "grape"}
myList = ["pineapple", "kiwi"]
mySet.update(myList)
print(mySet)
#7
ages = {25, 30, 35, 40}
first_names = {"John", "Jane", "Isaac", "Phiona"}
print(ages.union(first_names))




