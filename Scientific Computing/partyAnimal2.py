class PartyAnimal:
	x = 0
	name = ''

	def __init__(self, name):
		self.name = name
		print(f'{self.name} created')

	def party(self):
		self.x += 1
		print(f'{self.name} party count {self.x}')

sam = PartyAnimal('Sam')
sam.party()

dapz = PartyAnimal('Dapz')
dapz.party()
sam.party()
