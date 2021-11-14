# Make all possible combinatons of players for a selected number of spots
# ****TEST FOR 3 SPOTS****
count = int(input())
player_list = [input() for i in range(count)]
serial = 1
for i in range(count):
	for j in range(count):
		for k in range(count):
			if j > i and k > j:
				print(serial, player_list[i], player_list[j], player_list[k])
				serial += 1
