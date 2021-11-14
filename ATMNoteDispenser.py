total_money_entered = int(input('Enter the amount you want to withdraw (multiples of 100 or 500) '))
five_hundred_notes = 0
two_hundred_notes = 0
one_hundred_notes = 0

if total_money_entered%100 == 0:
	while total_money_entered > 500:
		total_money_entered -= 500
		five_hundred_notes += 1
	while total_money_entered >= 200:
		total_money_entered -= 200
		two_hundred_notes += 1
	while total_money_entered >= 100:
		total_money_entered -= 100
		one_hundred_notes += 1
elif total_money_entered%100 != 0:
	print('Please enter the correct amount and try again.')

print('500 x', five_hundred_notes, '\n200 x', two_hundred_notes, '\n100 x', one_hundred_notes, sep=' ')
