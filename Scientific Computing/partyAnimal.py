class PartyAnimal:
	x = 0
	def __init__(self):
		print('I am constructed')

	def party(self):
		self.x = self.x + 1
		print('So far', self.x)

	def __del__(self):
		print('I am destructed at', self.x)

animal = PartyAnimal()
animal.party()
animal.party()
animal.party()
animal = 43
print('animal contains', animal)
# animal.party()	# error cuz animal object destroyed when it was initialized as INT 43