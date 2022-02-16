


from audioop import reverse
from turtle import pen


def knapSolve(elements_values, elements_weights, capacity):
	elements_profits = []
	elements_profits_ratio = []
	maximum_profit = 0

	for i, j in zip(elements_values, elements_weights):
		elements_profits.append([i, j])

	print(elements_profits[0][1])	# elements_profit[i][j] --- i -> value/weight combination, j -> select either value or weight
	
	elements_profits_sorted = sorted(elements_profits, reverse=True)	# sorts ascending on basis of value
	for i, j in enumerate(elements_profits_sorted):
		if elements_profits_sorted[i][1] == 0:
			temp = elements_profits_sorted.pop(i)
			maximum_profit += temp[0]
		else:
			continue

	print(elements_profits_sorted)
	print(maximum_profit)

	for i in elements_profits_sorted:
		elements_profits_ratio.append(round(i[0]/i[1], 3))

	elements_profits_ratio_sorted = []
	for i, j in enumerate(elements_profits_ratio):
		elements_profits_ratio_sorted.append([j, elements_profits_sorted[i][0], elements_profits_sorted[i][1]])

	elements_profits_sorted = sorted(elements_profits_ratio_sorted, reverse=True)

	print(elements_profits_sorted)

	count = 0
	while capacity >= 0:
		capacity -= elements_profits_sorted[count][2]
		if capacity <= 0:
			break
		maximum_profit += elements_profits_sorted[count][1]
		count += 1
	
	print(maximum_profit)
	print(count)
	
	#  for i, j in zip(elements_values, elements_weights):
	# 	if j != 0:
	# 		elements_profits.append(round((i/j), 2))
	# 	else:
	# 		# elements_profits.append('P'+str(i))
	# 		maximum_profit += i
	# print(sorted(elements_profits, reverse=True))
	pass


# Driver Code
if __name__ == '__main__':

	# 50 elements in each

	# values = [360, 83, 59, 130, 431, 67, 230, 52, 93, 125, 670, 892, 600, 38, 48, 147, 78, 256, 63, 17, 120, 164, 432, 35, 92, 110, 22, 42, 50, 323, 514, 28, 87, 73, 78, 15, 26, 78, 210, 36, 85, 189, 274, 43, 33, 10, 19, 389, 276, 312]
	# weights = [7, 0, 30, 22, 80, 94, 11, 81, 70, 64, 59, 18, 0, 36, 3, 8, 15, 42, 9, 0, 42, 47, 52, 32, 26, 48, 55, 6, 29, 84, 2, 4, 18, 56, 7, 29, 93, 44, 71, 3, 86, 66, 31, 65, 0, 79, 20, 65, 52, 13 ]
	# bag_size = 850

	# values = [25, 24, 15]
	# weights = [18, 14, 10]
	# bag_size = 20
	
	# for custom inputs
	values = []
	weights = []
	count = int(input('How many elements? '))
	for i in range(count):	
		values.insert(i, int(input(f'Value of item {i+1}: ')))
		weights.insert(i, int(input(f'Weight of item {i+1}: ')))
	bag_size = int(input('Enter the size of the sack: '))



	knapSolve(values, weights, bag_size)
