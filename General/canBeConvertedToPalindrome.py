def checkPalindrome(string):
	count = 0
	index = 0
	print(string[0], string[-(0+1)])
	print(string[1], string[-(1+1)])
	if string[::] == string[::-1]:
		print('palindrome')
	else:
		for i in range(len(string)):
			if string[i] != string[-(i+1)]:
				index = i
				count += 1
		if count == 0:
			print('Palindrome')
		elif count == 1:
			print(f'Replace {string[-(index+1)]} at index {index} with {string[index]}')
		else:
			print('not a possible palindrome')

checkPalindrome('soup')
checkPalindrome('soupuos')
checkPalindrome('soupuop')