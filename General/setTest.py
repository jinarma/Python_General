#lex_auth_012693780491968512136

def make_amount(rupees_to_make, no_of_five, no_of_one):
	five_needed = 0
	one_needed = 0

	#Start writing your code here
	#Populate the variables: five_needed and one_needed
	while rupees_to_make > 0:
		if no_of_five >= 1 and rupees_to_make >= 5:
			no_of_five -= 1
			five_needed += 1
			rupees_to_make -= 5
		elif no_of_one >= 1:
			no_of_one -= 1
			one_needed += 1
			rupees_to_make -= 1
		elif rupees_to_make > 0:
			print(-1)
			return
	print("No. of Five needed :", five_needed)
	print("No. of One needed  :", one_needed)
	return

	# Use the below given print statements to display the output
	# Also, do not modify them for verification to work

	#print("No. of Five needed :", five_needed)
	#print("No. of One needed  :", one_needed)
	#print(-1)


#Provide different values for rupees_to_make,no_of_five,no_of_one and test your program
make_amount(28, 8, 5)
