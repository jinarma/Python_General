def check_words(word_list, word_string):
	result_list = []
	for ele in word_list:
		temp_char = list(ele)
		temp = list(word_string)
		while temp_char != [] and temp != []:
			if temp_char[0] in temp:
				temp.remove(temp_char[0])
				temp_char.pop(0)
			else:
				break
		if temp_char == []:
			result_list.append(ele)
	if result_list == []:
		return ['-1']				
	else:
		return result_list
word_list = input().split(',')
word_string = input()
result = ','.join(check_words(word_list, word_string))
print(result)