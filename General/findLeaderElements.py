def leaderElements(array):
	leaderArray = []
	for i, ele in enumerate(array):
		for j in range(i, len(array)):
			if ele < array[j]:
				break
			else:
				if j == len(array)-1:
					leaderArray.append(ele)
	return leaderArray

size = int(input())
numberList = list(map(int, input().split()))
leaders = leaderElements(numberList)
for ele in leaders:
	print(ele, end=' ')