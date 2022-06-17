def mergeSort(arr):
	if len(arr) > 1:
		leftArr = arr[:len(arr)//2]
		rightArr = arr[len(arr)//2:]
		
		mergeSort(leftArr)
		mergeSort(rightArr)

		i, j, k = 0, 0, 0

		while i < len(leftArr) and j < len(rightArr):
			if leftArr[i] < rightArr[j]:
				arr[k] = leftArr[i]
				i += 1
			else:
				arr[k] = rightArr[j]
				j += 1
			k += 1

		while i < len(leftArr):
			arr[k] = leftArr[i]
			i += 1
			k += 1
		
		while j < len(rightArr):
			arr[k] = rightArr[j]
			j += 1
			k += 1

arr = [8, 9, 4, 0, 3, 2, 1]
mergeSort(arr)
print(arr)
