import matplotlib.pyplot as plt
from math import sqrt

# plt.plot([1, 2, 3, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7])
x = list(i for i in range(1, 101))
y = list(i for i in range(100, 0, -1))
square = []
for i, j in zip(x, y):
	print(i, j)
	print(sqrt(i**2+j**2))
	percent_temp = round(sqrt(i**2+j**2)*(j/100), 2)
	square.append(percent_temp)
print(x)
print(square)
plt.plot(x, square)

plt.show()

