# import random

# cards_to_check = list(random.randint(1000000000000000, 9999999999999999) for _ in range(10))
# print(cards_to_check)

""" [6600718925190860, 7138377791110174, 2401537370423315, 7795268087742703, 1409724007627225, 2230969971150222, 3446561381789640, 5523658704650816, 3187537039981985, 6176251366369169] """

def validate_credit_car_number(card_number: int) -> bool:
	try:
		if len(card_number) == 16:
			card_number = int(card_number)
		else:
			print('Invalid card number')
			exit()
	except ValueError:
		print('Invalid card number')
		exit()
	card_digits = list(str(card_number))
	double_of_seconds = list(ele*2 for ele in list(map(int, card_digits[::2])))
	for i, ele in enumerate(double_of_seconds):
		if ele > 9:
			double_of_seconds.insert(i, sum([ele//10, ele%10]))
			double_of_seconds.pop(i+1)
	double_of_seconds = sum(double_of_seconds)
	sum_of_seconds = sum(map(int, card_digits[1::2]))
	if (sum_of_seconds+double_of_seconds)%10 == 0:
		return True
	return False

if __name__ == '__main__':
	card_number = input('Enter the number: ')
	if validate_credit_car_number(card_number):
		print('Valid card number')
	else:
		print('Invalid card number')
		
	
