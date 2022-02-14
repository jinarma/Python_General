def rotation_query(num_of_rotations, num_list, queries):
	num_list = num_list[-(num_of_rotations+1):] + num_list[:num_of_rotations] # rotation complete
	for i in queries:
		print(num_list[i], end=' ')

n = list(map(int, input().split()))
array_size = n[0]
rotation_size = n[1]
array = list(map(int, input().split()))
query_size = int(input())
query_array = list(map(int, input().split()))
rotation_query(rotation_size, array, query_array)