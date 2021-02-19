import random as rn
names = {0:"Jinu", 1:"Roma", 2:"Tejasvi", 3:"Rudrakshi"}
selected_key = rn.randint(0, 3)
for i in names.keys():
	if selected_key == i:
		print(names[i], "is stupid!", sep=" ")