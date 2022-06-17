def hidden_name(name_function):
	def wrapper(*args, **kwargs):
		print('Wrapper Started')
		val = name_function(*args, **kwargs)
		print('Wrapper Ended')
		return val
	return wrapper

@hidden_name			# means, actual_name = hidden_name(actual_name)
def actual_name(name):
	print(f'Hi! My name is {name}')

@hidden_name
def add(x, y):
	return x + y

@hidden_name
def multiply(x, y):
	return x * y

actual_name('John Cena')
print(add(10, 12))
print(multiply(2, 5))