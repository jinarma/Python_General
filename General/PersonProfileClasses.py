class Person:
	def __init__(self):
		self.name = input('Name: ')
		self.age = int(input('Age: '))
		self.height = int(input('Height(cm): '))
		self.religon = input('Religon: ')
		print('Nationality: ', end='')
		self.nationality = country_selection()
	def display(self):
		print(self.name, self.age, self.height, self.religon, self.nationality, sep='\n')

def country_selection():
	country_dict = {1:'IN', 2:'JP', 3:'US', 4:'UK', 5:'AU', 6:'Other'}
	print('Choose the number corrosponding to your country.')
	for s, i in country_dict.items():
		print(s, i)
	temp = int(input())
	return country_dict[temp]
	
person1 = Person()
person1.display()
""" country_selection() """
