def FCFS(process_list: list) -> list:
	process_list = sorted(process_list)		# [at, bt]
	processed_list = []		# [ct, tat, wt]
	buff_point = 0
	for i, ele in enumerate(process_list):
		if buff_point >= ele[0]:
			buff_point += ele[1]
		else:
			buff_point = ele[1]+ele[0]
		processed_list.append([buff_point])
		processed_list[i].append(processed_list[i][0]-ele[0])
		processed_list[i].append(processed_list[i][1]-ele[1])
	return processed_list

# Driver
process_num = int(input('Enter the number of processes: '))
process_list = []
for i in range(process_num):
	process_list.append(list(map(int, input(f'Enter Arrival time and Burst time for process {i+1}: ').split())))
processed_list = FCFS(process_list)

print('Process\tArrival\tBurst\tCompletion\tTAT\tWT')
for i, ele in enumerate(processed_list):
	print(f'P{i}\t{process_list[i][0]}\t{process_list[i][1]}\t{processed_list[i][0]}\t\t{processed_list[i][1]}\t{processed_list[i][2]}')
