# checks if a right triangle pattern can be printed

n = 7


def find(n):
	sum = 0
	i = 1
	while i <= n:
		sum += i
		if sum == n:
			return 1
		elif sum > n:
			return 0
		else:
			i += 1
	return 0


if find(n):
	print("Yes")
else:
	print("No")
