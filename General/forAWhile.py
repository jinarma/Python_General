print("Enter 'for' to print using for loop\nEnter 'while' to print using while loop")
choice=input()
if choice == 'for':
	for i in range(1, 11):
		print(str(i)+" ")
elif choice == 'while':
	i = 1
	while i < 11:
		print(str(i)+" ")
		i=i+1
else:
	print("Not a valid choice!")