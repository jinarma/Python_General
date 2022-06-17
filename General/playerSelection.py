# Make all possible combinatons of players for a selected number of spots

count = int(input())
player_list = [input() for i in range(count)]
serial = 1
for i in range(count):
	for j in range(count):
		if j != i:
			print(serial, player_list[i], player_list[j], sep='\t')
			serial += 1