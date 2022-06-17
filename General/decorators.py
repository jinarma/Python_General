def universe(country):
	def earth(someone):
		print('This is earth')
		country(someone)
		print('Leaving earth')
	return earth

@universe
def person(someone):
	print(f'This is {someone}')

person('Jinarma')