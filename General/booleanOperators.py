import sys

while True:
	choice=input("Enter 'And' to check the table of and operator\nEnter 'Or' to check the table of or operator\nEnter 'not' to check the table of not operator\nEnter 'exit' to exit the program\n")
	if choice == 'and':
		print("i | j | and")
		for i in range(2):
			for j in range(2):
				a = i and j
				print(str(i)+" | "+str(j)+" | "+str(a))

	if choice == 'or':
		print("i | j | or")
		for i in range(2):
			for j in range(2):
				a = i or j
				print(str(i)+" | "+str(j)+" | "+str(a))

	if choice == 'not':
		print("i | not")
		for i in range(2):
			a = not i
			print(str(i)+" | "+str(a))
	if choice == 'exit':
		sys.exit()