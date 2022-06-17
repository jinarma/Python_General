def dupe_remover(string):
	new_list = []
	for ele in string:
		if ele not in new_list:
			new_list.append(ele)
		else:
			continue
	return ''.join(new_list)

char_string = input()
print(dupe_remover(char_string))