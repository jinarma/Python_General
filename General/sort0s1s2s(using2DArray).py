def sorting(array):
	sorting_array = [[], [], []]
	for ele in array:
		if ele == 0:
			sorting_array[0].append(ele)
		elif ele == 1:
			sorting_array[1].append(ele)
		elif ele == 2:
			sorting_array[2].append(ele)
	return sorting_array[0] + sorting_array[1] + sorting_array[2]

size = int(input())
num_list = list(map(int, input().split()))
sorted_list = sorting(num_list)
for ele in sorted_list:
	print(ele, end=' ')
