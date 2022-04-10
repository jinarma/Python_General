size = int(input())
list_of_coords = []
for i in range(size):
	list_of_coords.append(list(map(int, input().split())))

flag = ''
x, y = list_of_coords[0]
count = 0
for i, ele in enumerate(list_of_coords):
	if i < len(list_of_coords) - 1:
		if ele[0] != list_of_coords[i+1][0] and ele[1] == list_of_coords[i+1][1] and flag != 'x':
			count += 1
			flag = 'x'
		elif ele[1] != list_of_coords[i+1][1] and ele[0] == list_of_coords[i+1][0] and flag != 'y':
			count += 1
			flag = 'y'
	else:
		if ele[0] != list_of_coords[0][0] and ele[1] == list_of_coords[0][1] and flag != 'x':
			count += 1
			flag = 'x'
		elif ele[1] != list_of_coords[0][1] and ele[0] == list_of_coords[0][0] and flag != 'y':
			count += 1
			flag = 'y'
print(count)