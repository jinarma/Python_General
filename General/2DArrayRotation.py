
def arrayRotation(ls2):
	choice = int(input('Enter the angle of rotation (Clockwise)\n0 for no rotation\n1 for 90 degrees\n2 for 180 degrees\n3 for 270 degress\n'))
	# 2D array printed
	print('2D array')
	for row, sub_list in enumerate(ls2):
		for column, sub_list_ele in enumerate(sub_list):
			print(sub_list_ele, end=' ')
		print()
	print()
	if choice == 0:
		# 2D array printed
		print('2D array')
		for row, sub_list in enumerate(ls2):
			for column, sub_list_ele in enumerate(sub_list):
				print(sub_list_ele, end=' ')
			print()
		print()
	elif choice == 1:
		# 2D array rotation clockwise 90 degrees
		print('2D array rotated clockwise 90 degrees')
		for row, sub_list in enumerate(ls2):
			for column, sub_list_ele in enumerate(sub_list):
				print(sub_list[row], end=' ')
			print()
		print()
	elif choice == 2:
		# 2D array rotated clockwise 180 degrees
		print('2D array rotated clockwise 180 degrees')
		for row, sub_list in enumerate(ls2):
			for column, sub_list_ele in enumerate(sub_list[::-1]):
				print(sub_list_ele, end=' ')
			print()
		print()
	elif choice == 3:
		# 2D array rotated clockwise 270 degrees
		print('2D array rotated clockwise 270 degrees')
		for row, sub_list in enumerate(ls2):
			for column, sub_list_ele in enumerate(sub_list):
				print(sub_list[-(row+1)], end=' ')
			print()
		print()

if __name__ == '__main__':
	size = int(input('Size of array: '))
	arr2D = []

	for i in range(size):
		print('Enter elements for row', i)
		arr2D.append(input().split())
	arrayRotation(arr2D)
	
