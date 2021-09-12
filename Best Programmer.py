# You are using Python
def findType(num):
	num_list = []
	sum_of_num = 0
	for i in range(1, num):
		if num % i == 0:
			num_list.append(i)
	for i in num_list:
		sum_of_num += i
	if sum_of_num < num:
		print('Deficient number')
		return 1
	elif sum_of_num == num:
		print('Perfect number')
		return 0
	elif sum_of_num > num:
		print('Abundant number')
		return -1


findType(int(input()))
