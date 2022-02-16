def sorting(array):
	zeros = []
	ones = []
	twos = []
	for ele in array:
		if ele == 0:
			zeros.append(ele)
		elif ele == 1:
			ones.append(ele)
		elif ele == 2:
			twos.append(ele)
	return zeros + ones + twos

size = int(input())
num_list = list(map(int, input().split()))
sorted_list = sorting(num_list)
for ele in sorted_list:
	print(ele, end=' ')