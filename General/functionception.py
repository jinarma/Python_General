# how does e.g. string.strip().upper().split() work, meaning, multiple stacking of functions one after the other.

class Big_daddy:
	def __init__(self):
		print('I am big daddy')

	def smol_baby(self):
		print('am smol bby')

	def even_smoller_baby(self):
		print('gugu ga ga')


daddy = Big_daddy()
daddy.smol_baby()
daddy.even_smoller_baby()


string = '  hello there this is a string   '
# print(string)
assert string
print(string.strip())
print(string.strip().upper())
print(string.strip().upper().split())
del string