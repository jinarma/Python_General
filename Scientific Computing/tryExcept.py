for i in range(3):
	try:
		usr_input = abs(int(input('Enter your age (years): ')))
		print(f'You\'re {usr_input} years old!')
		break
	except:
		if i < 2:
			print('Incorrect value, try again!\n')
		else:
			print('You\'ve exceeded the maximum number of tries.')