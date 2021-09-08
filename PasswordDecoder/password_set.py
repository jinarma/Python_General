""" Only for digit pin for now """

def set_password(string):
	file = open('D:\Programming\Python\Github\Python_General\PasswordDecoder\password.txt', 'w')
	file.write(string)
	file.close()
	return file

set_password(input("Enter your pin: "))

