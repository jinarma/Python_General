import copy


def SRTF(process_list):
	remaining_time_total = 0
	for _, _ , rt in process_list:
		remaining_time_total += rt
	print(remaining_time_total)

	ready_queue = []
	process_list.sort(key= lambda x: x[1])
	# for i in range(remaining_time_total, -1, -1):
	i = 0
	while i < process_list[-1][0]:
		if process_list[i][2] > 0:
			process_list[i][2] -= 1
			print(f'-> P{i}', end=' ')
		else:
			i += 1
		# print(i)

# driver code
if __name__ == '__main__':
	process_list = [[0, 3, 8], [1, 2, 3], [2, 0, 9], [3, 1, 4], [4, 5, 2]]		# [pID, at, bt]
	process_list_copy = copy.copy(process_list)
	SRTF(process_list_copy)
	pass