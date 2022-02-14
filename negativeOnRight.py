def arrange_negatives(num_list):
	new_list = []
	for i, ele in enumerate(num_list):
		if ele < 0:
			new_list.append(ele)
		else:
			new_list.insert(0, ele)
	return new_list

array = list(map(int, input().split()))
print(arrange_negatives(array))