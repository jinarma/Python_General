def binary_search(num_list, occur):
	head = 0
	tail = len(num_list)-1
	while head <= tail:
		mid = (head+tail)//2
		if occur < num_list[mid]:
			tail = mid - 1
		elif occur > num_list[mid]:
			head = mid + 1
		else:
			while num_list[mid] == num_list[mid-1] and mid > 0 and mid < len(num_list):
				mid = mid - 1
			return mid


def add_first_occurance(array, occurance):
	add_list = []
	for occur in occurance:
		if occur in array:
			add_list.append(binary_search(array, occur))
			# for i, ele in enumerate(array):
			# 	if ele == occur:
			# 		add_list.append(i)
			# 		break
			# 	else:
			# 		continue
		else:
			add_list.append(-1)
	
	return sum(add_list)

if __name__ == '__main__':
	num_list_size = int(input())
	num_list = list(map(int, input().split()))
	check_list_size = int(input())
	check_list = list(map(int, input().split()))
	print(add_first_occurance(num_list, check_list))