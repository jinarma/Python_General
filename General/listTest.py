x = [1, 2, 3, 4]
x2 = [3, 4, 2, 3]
x3 = [5, 1, 2, 9]

y = [5, 1, 2, 9]
y2 = [1, 2, 3, 4]
y3 = [3, 4, 2, 3]

bigX = []
bigX.append(x)
bigX.append(x2)
bigX.append(x3)

bigY = []
bigY.append(y)
bigY.append(y2)
bigY.append(y3)

print(bigX)
print(bigY)

for i, j in zip(bigX, bigY):
	for m, n in zip(i, j):
		print(m, n)
