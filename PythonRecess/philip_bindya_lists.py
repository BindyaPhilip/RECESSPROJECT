#lists are used to store many items and they can be duplicated
names = ["Rashid","Devote","Trevour"]
print(names)
#duplication
names=["Rashid","Devote","Trevour","Rashid","Rashid"]
print(names)
#list length
print(len(names))
#type
print(type(names))
#accessing the items of the list
print(names[2])
print(names[-1])
#appending
names.append("Philo")
print(names)
#accessing items in a range
print(names[2:4])
FootballTeams = ["Mancity","Arsenal","Man U","Newcastle","Liverpool"]
#changing list items
FootballTeams[1] = "Brighton"
print(FootballTeams)
#removing an item
FootballTeams.remove("Man U")
print(FootballTeams)
#removing an item using the pop(),include an index inside the pop
FootballTeams.pop(2)
print(FootballTeams)
#without an index inside the pop
FootballTeams.pop()
print(FootballTeams)