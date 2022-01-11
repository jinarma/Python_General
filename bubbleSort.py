from random import randint as rd

def bubbleSort(uList):
	oList = []
	if len(uList) == 0:
		print('List empty')
		return uList
	else:
		while uList:
			oList.append(min(uList))
			uList.remove(min(uList))
		return oList

if __name__ == '__main__':
	unsortedList = list(rd(1, 50) for i in range(10))
	# unsortedList = []
	# Soooooo yeah! Python has a stupid way of passing an argument called "Passing by object reference" thats why the value of the unorderedList is being updated in the main function when not explicitly specifying. FML!!!!!
	print(unsortedList)
	bubbleSort(unsortedList)
	print(unsortedList)
	# print(bubbleSort(unsortedList))
