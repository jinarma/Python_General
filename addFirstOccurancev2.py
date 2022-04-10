def add_first_occurance(array, occurance):
	add_list = []
	for occur in occurance:
		if occur in array:
			add_list.append(array.index(occur))
		else:
			add_list.append(-1)
	
	return sum(add_list)

if __name__ == '__main__':
	num_list_size = int(input())
	num_list = list(map(int, input().split()))
	check_list_size = int(input())
	check_list = list(map(int, input().split()))
	print(add_first_occurance(num_list, check_list))