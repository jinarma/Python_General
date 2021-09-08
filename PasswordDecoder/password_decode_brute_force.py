""" Only for digit pin for now """
from time import time

start = time()

def import_password_for_verification():
	file = open('D:\Programming\Python\Github\Python_General\PasswordDecoder\password.txt', 'r')
	data = file.read()
	file.close()
	return data

def decode_password():
	actual_password = int(import_password_for_verification())
	decoded_password = 0
	while decoded_password != actual_password:
		decoded_password += 1
		#print(decoded_password)
	print('Actual password {}, Decoded password {}'.format(actual_password, decoded_password))

decode_password()

end = time()
print('Total time:', (end-start))