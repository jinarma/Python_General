def is_or_not():
	print('0 == 0.0', 0 == 0.0)
	print('0 != 0.0', 0 != 0.0)
	print('0 is 0.0', 0 is 0.0)
	print('0 is not 0.0', 0 is not 0.0)

def a_or_b():
	a = 10
	b = 10
	c = 11
	print(f'a = {a}, b = {b}, id(a) = {id(a)}, id(b) = {id(b)}, id(c) = {id(c)}')

if __name__ == '__main__':
	a_or_b()
