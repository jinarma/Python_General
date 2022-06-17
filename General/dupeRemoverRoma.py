import random as rn

# for i in range(3):
# 	print(rn.randint(2, 11))
i = 0
new_list = []
while i < 20:
	rando = rn.randint(2, 10)
	if rando not in new_list:
		new_list.append(int(rando))
		print(rando)
		i += 1
	else:
		if len(new_list) >= 9:
			break
		continue