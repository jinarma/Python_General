#Program to capitalize the specific word

def highlight_word(sentence, word):
	count=0
	special_char_list = [',', "'", '"', ':', ';', '/', '?', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|']
	list_1 = sentence.split()
	for i in range(len(list_1)):
		if list_1[i] == word:
			list_1[i] = word.upper()
			count=1
	if list_1[-1] != word and count == 0:
		for i in range(len(list_1)):
			list_2 = list(list_1[i])
			temp_word = ""
			for character in special_char_list:
				try:
					list_2.remove(character)
					print("inside try")
				except ValueError:
					continue
			for j in range(len(list_2)): #this creates a temp word from the elements in list_2
				temp_word+=list_2[j]
			new_word_list = []
			if temp_word == word:
				word = word.upper()
				new_word_list = list(word)
				list_2 = new_word_list
			print(list(list_2), i, sep=" ")
		print(list_2)
		print(list_1)
				# for checker_character in special_char_list:
				# 	try:
				# 		list_1[i][j].remove(checker_character)
				# 	except ValueError:
				# 		continue
			#convert list to string and check if it is = "word"
		# print(list_1[j])
#	return list_1

#print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
#print(highlight_word("Automating with Python is fun", "fun"))