while True:
	print('Who are you?')
	name = input()
	if name != 'Jinu':
		print('Wrong user!')
		continue
	print('Hello '+name+'! What is the password? (Hint: Its a fish')
	password = input()
	if password != 'swordfish':
		print('Wrong password! Try again')
		continue
	break
print('Access granted!')