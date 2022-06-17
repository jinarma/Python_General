#lex_auth_012693782475948032141

def calculate_bill_amount(food_type, quantity_ordered, distance_in_kms):
	bill_amount = 0
	#write your logic here
	delivery_charges = 0
	if quantity_ordered > 0 and distance_in_kms > -1:
			if distance_in_kms >= 0 and distance_in_kms < 3:
				delivery_charges = 0
			elif distance_in_kms >= 3 and distance_in_kms < 6:
				delivery_charges = 3*(distance_in_kms-3)
			else:
				delivery_charges = 9
				distance_in_kms = distance_in_kms - 6
				delivery_charges = delivery_charges + 6*distance_in_kms
	else:
		return -1
	if food_type == 'V':
		bill_amount = 120 * quantity_ordered + delivery_charges
	elif food_type == 'N':
		bill_amount = 150 * quantity_ordered + delivery_charges
	else:
		return -1
	return bill_amount

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount = calculate_bill_amount("N",1,7)
print(bill_amount)
