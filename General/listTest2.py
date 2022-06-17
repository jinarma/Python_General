elements_profits_sorted = [[892, 18], [670, 59], [600, 0], [514, 2], [432, 52], [431, 80], [389, 65], [360, 7], [323, 84], [312, 13], [134, 0]]

print(elements_profits_sorted)
temp = []
temp = elements_profits_sorted.pop(2)
maximum_profit = 0
maximum_profit = temp[0]
print(elements_profits_sorted[2][0])
print(type(temp))
print(maximum_profit)

for i in range(len(elements_profits_sorted)):
		if elements_profits_sorted[i][1] == 0:
			temp = elements_profits_sorted.pop(i)
			maximum_profit += temp[0]
		else:
			continue
print(elements_profits_sorted)
print(maximum_profit)
