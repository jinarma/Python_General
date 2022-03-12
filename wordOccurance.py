def occurances(word_list, check):
	count = 0
	while check in word_list:
		count += 1
		word_list.remove(check)
	return count
ls1 = ['abc', 'abcd', 'AVde', 'abc', 'Abc']
word = 'Abc'
print(occurances(ls1, word))