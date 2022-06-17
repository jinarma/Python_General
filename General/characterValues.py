# This program illustrates that apart from int 0, float 0.0 and string ''; every other value evaluates to True.
name = ''
while not name:
	name = input('Enter your name: ')
print('How many guests will you have over?')
numOfGuests = int(input())
if numOfGuests:
	print("Make sure you have enuff room for "+str(numOfGuests)+" people!")
print("Done!")