def findAverage(n, m, arr):		# n = size, m = num of phases
	for i in range(m):
		inputs = []
		try:
			inputs = list(map(int, input().split()))
		except EOFError:
			pass
		if inputs != []:
			for i in range(inputs[0]-1,inputs[1]):
				arr[i] += inputs[2]
			inputs = []
	return sum(arr)//5

print(findAverage(5, 3, [0,0,0,0,0]))