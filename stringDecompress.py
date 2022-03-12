def decompress(string):
	char_list = []
	for i, ele in enumerate(string):
		if ele.isdigit():
			for _ in range(int(ele)-1):
				char_list.append(string[i-1])
		else:
			char_list.append(ele)
	return ''.join(char_list)

string_1 = 'ab2c4df2b2'
print(decompress(string_1))