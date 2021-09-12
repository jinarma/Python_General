# You are using Python
n = int(input())


def findType(n):
	divisor_list = []
	sum = 0
	i = 1
	while i < n:
		if n % i == 0:
			divisor_list.append(i)
		i += 1
	for i in divisor_list:
		sum += i
	if sum == n:
		return 0
	elif sum > n:
		return -1
	else:
		return 1


if findType(n) == 1:
	print("Deficient number")
if findType(n) == -1:
	print("Abundant number")
if findType(n) == 0:
	print("Perfect number")
