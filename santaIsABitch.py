def nibba(m, num_of_boxes):
	num_of_boxes = sorted(num_of_boxes)
	minimum = num_of_boxes[m-1] - num_of_boxes[0]
	for i in range(len(num_of_boxes)-m):
		if num_of_boxes[i+m-1] - num_of_boxes[i] <= minimum:
			minimum = num_of_boxes[i+m-1] - num_of_boxes[i]
		else:
			continue
	return minimum


num_children = int(input())
size_of_array = int(input())
children_array = []
for i in range(size_of_array):
	children_array.append(int(input()))
print(nibba(num_children, children_array))