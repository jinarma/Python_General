import copy


def sort_positive(num_list):
	if num_list[2] >= 0:
		return num_list[2]
	else:
		return []

def SRTF(process_list):
	remaining_time_total = 0
	for _, _, rt in process_list:
		remaining_time_total += rt
	process_list.sort(key=lambda x: x[1])	# sorts based on AT
	remaining_time_total += process_list[0][1]
	
	ready_queue = []
	current_process = []
	i = 0
	# for i in range(remaining_time_total):
	while remaining_time_total > 1:
		remaining_time_total = 0
		for ele in process_list:
			if ele[1] <= i:
				ready_queue.append(ele)
				process_list.remove(ele)

		ready_queue.sort(key=sort_positive)		# sorts the ready queue based on RT
		remaining_time_total += ele[2]

		try:
			current_process.append(ready_queue.pop(0))
			print(i, f'P{current_process[0][0]}')
			current_process[0][2] -= 1
			if current_process[0][2] <= 0:
				current_process.pop()
			else:
				ready_queue.append(current_process.pop(0))
		except:
			print(i, '[empty]')

		i += 1




	# process_list.sort(key= lambda x: x[1])		# sorts by RT
	# # for i in range(remaining_time_total, -1, -1):
	# i = 0
	# while i < process_list[-1][0]:
	# 	if process_list[i][2] > 0:
	# 		process_list[i][2] -= 1
	# 		print(f'-> P{i}', end=' ')
	# 	else:
	# 		i += 1
	# 	# print(i)

# driver code
if __name__ == '__main__':
	process_list = [[1, 26, 8], [2, 2, 3], [3, 6, 9], [4, 1, 4], [5, 5, 2]]		# [pID, at, bt]
	process_list_copy = copy.copy(process_list)
	SRTF(process_list_copy)
	pass
