arr = []
for i in range(4):
	for j in range(4):
		arr.append([i, j])
for i in arr:
	if i[1] != 3:
		if (i[0] == 0 and i[1] == 1) or (i[0] == 1 and i[1] == 3) or (i[0] == 2 and i[1] == 0) or (i[0] == 3 and i[1] == 2):
			print(1, end=' ')
		else:
			print(0, end=' ')
	else:
		if (i[0] == 0 and i[1] == 1) or (i[0] == 1 and i[1] == 3) or (i[0] == 2 and i[1] == 0) or (i[0] == 3 and i[1] == 2):
			print(1)
		else:
			print(0)
