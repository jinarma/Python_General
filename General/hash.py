num = [1, 2, 3, 4, 3, 2, 4, 2]
num2 = [1, 2, 3, 4, 3, 2, 4, 3]
num3 = [1, 2, 3, 4, 3, 2, 4, 2]
class hashMaker():
	def __init__(self, ls1):
		self.ls1 = ls1


a = hashMaker(num)
b = hashMaker(num2)
c = hashMaker(num3)
hash_of_a = hash(a)
print(hash(a))
print(hash(b))
print(hash(c))