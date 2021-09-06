from matplotlib import pyplot as plt

plotX = []
plotY = []

for num in range(1, 10):
	x = []
	y = []
	count = 0
	print("Starting number:", num, sep=' ')
	y.append(num)
	count += 1
	while num != 1:
			if num % 2 == 0:
				num = num/2
				print(num)
				y.append(num)
				count += 1
			elif num % 2 != 0:
				num = 3*num+1
				print(num)
				y.append(num)
				count += 1
	for n in range(count):
		x.append(n+1)
	
	plotX.append(x)
	plotY.append(y)

for i_x, i_y in zip(plotX, plotY):
	plt.plot(i_x, i_y, alpha=0.7)

plt.show()
