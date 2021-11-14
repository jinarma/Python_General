import math

def number_of_parity_bits(number_of_data_bits):
	for i in range(number_of_data_bits):
		if 2**i >= i + number_of_data_bits + 1:
			print('Number of Data bits:', number_of_data_bits)
			print('Number of Parity bits:', i)
			return i
		else:
			continue

def binary_table(data_bits, parity_bits):
	total_bits = data_bits + parity_bits
	binary_length = math.ceil(math.log(total_bits, 2))
	temp_binary_table_list = []
	for i in range(1, total_bits + 1):
		num_in_binary = bin(i).replace('0b', '')
		# temp_binary_table_list.append(num_in_binary)
		temp_binary_table_list.append('0'*(binary_length-len(num_in_binary)) + num_in_binary)
	return temp_binary_table_list

def make_the_temp_message_list(data_bits, number_parity_bits):
	parity_bits_list = []
	j = 1
	# To set parity bits as '2' and put them in their locationation and '3' for data bits
	for i in range(1, (len(data_bits)+number_parity_bits)+1):
		if i == j:
			parity_bits_list.append(2)
			if j == 1:
				j = j + 1
			else:
				j = j+j
		else:
			parity_bits_list.append(3)

	return parity_bits_list

def final_code_generation(data_bits):
	location = len(data_bits)-1
	data_bits_INT = int(data_bits)
	parity_bits_amount = number_of_parity_bits(len(data_bits))
	binary_list = binary_table(len(data_bits), parity_bits_amount)
	final_message = make_the_temp_message_list(data_bits, parity_bits_amount)
	count = -1
	for i in range(len(final_message)):
		if final_message[i] == 2:
			for j in binary_list:
				if binary_list[location] == 1:
					count += 1
			location -= 1
			if count % 2 == 0:
				final_message[i] = 0
			elif count % 2 != 0:
				final_message[i] = 1
		elif final_message[i] == 3:
			final_message[i] = data_bits_INT%10
			data_bits_INT = data_bits_INT//10
	return final_message[::-1]

def detect_error(message_code, parity_bits_amount):
	index = 3
	n = len(message_code)
	res = 0
	if message_code[-index] == 0:
		message_code[-index] = 1
	else:
		message_code[-index] = 0
	print('New message =', message_code[::])
	
	# Calculate parity bits again
	for i in range(parity_bits_amount):
		val = 0
		for j in range(1, n + 1):
			if(j & (2**i) == (2**i)):
				val = val ^ int(message_code[-j])

		# Create a binary no by appending
		# parity bits together.

		res = res + val*(10**i)

	# Convert binary to decimal
	return int(str(res), 2)

# Driver Code
if __name__ == '__main__':
	data_bits = input('Enter the data bits: ')
	final_code = final_code_generation(data_bits)
	print(final_code)
	print('Position of error is', detect_error(final_code, number_of_parity_bits(len(data_bits))))
