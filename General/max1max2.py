def rotate(array, size):
	for i in range(size):
		num=array[i][1]
		string = array[i][0]
		string = string[-num:] + string[:len(string)-num]
		array[i][0] = string
	return array
def sort_logic_list(rotated_array):
	vowel = ['a', 'e', 'i', 'o', 'u']
	res_array = []
	for i, ele in enumerate(rotated_array):
		tempStr = ''
		string = ele[0]
		for j in range(1, len(string), 2):
			if string[j].casefold() not in vowel:
				tempStr = tempStr+string[j]
			else:
				pass
		if tempStr != '':
			res_array.append(tempStr)
	if res_array == []:
		return ['-1']
	else:
		return sorted(res_array, key=len)
size = int(input())
arr_2D = []
for i in range(size):
	arr_2D.append(input().split(','))
	arr_2D[i][1] = int(arr_2D[i][1])
new_string = ','.join(sort_logic_list(rotate(arr_2D, size)))
print(new_string)