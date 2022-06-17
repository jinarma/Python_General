def reduceArray(array):
	steps_array = []
	while array != []:
		count = 0
		while 0 in array:
			array.remove(0)
			if array == []:
				return steps_array
	minimum = min(array)
	for i, ele in enumerate(array):
		array[i] = ele - minimum
		count += 1
	steps_array.append(count)
	return steps_array

size = int(input())
num_list = []
for i in range(size):
	num_list.append(int(input()))
print(reduceArray(num_list))