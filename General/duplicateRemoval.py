def dupeRemove(array):
	tempArray = []
	for i in array:
		if i in tempArray:
			continue
		else:
			tempArray.append(i)
	return tempArray

size = int(input())
ls1 = []
for i in range(size):
	ls1.append(input())
updated_array = dupeRemove(ls1)
for i in updated_array:
	print(i)