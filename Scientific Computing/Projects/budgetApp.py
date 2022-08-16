class Category:

	categories = []
	names = []

	def __init__(self, category):
		self.ledger = []
		self.category = category.capitalize()
		Category.names.append(self.category)
		Category.categories.append(self)

	def __str__(self):
		self.string = ''
		self.string += ''.join(self.category.center(30,'*'))
		self.string += '\n'
		total = 0
		for ele in self.ledger:
			self.string += ''.join(str(ele['description'][:23]).ljust(23, ' '))
			self.string += ''.join('{:.2f}'.format(ele['amount']).rjust(7, ' '))
			self.string += '\n'
			total += ele['amount']
		self.string += f'Total: {total}'
		return self.string

	def deposit(self, amount, description=''):
		self.ledger.append({'amount':amount, 'description':description})

	def withdraw(self, amount, description=''):
		if Category.check_funds(self, amount):
			self.ledger.append({'amount':-amount, 'description':description})
			return True
		else:
			return False

	def get_balance(self):
		self.balance = 0
		for transaction in self.ledger:
			self.balance += transaction['amount']
		return self.balance

	def transfer(self, amount, diff_category):
		if self.check_funds(amount):
			Category.withdraw(self, amount, f'Transfer to {diff_category.category}')
			Category.deposit(diff_category, amount, f'Transfer from {self.category}')
			return True
		else:
			return False
	
	def check_funds(self, amount):
		if amount > Category.get_balance(self):
			return False
		else:
			return True

def create_spend_chart(categories):
	num_list = []
	maximum = 0
	for ele in categories:
		if len(ele.category) > maximum:
			maximum = len(ele.category)
	
	temp_names = []
	result = 'Percentage spent by category\n'

	for ele in categories:
		temp_names.append(list(ele.category.ljust(maximum, ' ')))

	for category in categories:
		temp_sum = 0
		for transaction in category.ledger:
			if float(transaction['amount']) < 0:
				temp_sum += abs(float(transaction['amount']))
		num_list.append(temp_sum)
	
	num_list.append(sum(num_list))

	for i in range(len(num_list)-1):
		num_list[i] = int((num_list[i]/num_list[-1])*10)
	num_list.pop()

	dot_list = []
	for ele in num_list:
		temp_str = 'o'*(ele+1)
		dot_list.append(list(temp_str.ljust(11, ' ')))

	if len(num_list) == 0:
		for i in range(10, -1, -1):
			result += (f'{str(i*10).rjust(3)}| ')
	if len(num_list) == 1:
		for i in range(10, -1, -1):
			result += (f'{str(i*10).rjust(3)}| {dot_list[0][i]}  \n')
	if len(num_list) == 2:
		for i in range(10, -1, -1):
			result += (f'{str(i*10).rjust(3)}| {dot_list[0][i]}  {dot_list[1][i]}  \n')
	if len(num_list) == 3:
		for i in range(10, -1, -1):
			result += (f'{str(i*10).rjust(3)}| {dot_list[0][i]}  {dot_list[1][i]}  {dot_list[2][i]}  \n')
	if len(num_list) == 4:
		for i in range(10, -1, -1):
			result += (f'{str(i*10).rjust(3)}| {dot_list[0][i]}  {dot_list[1][i]}  {dot_list[2][i]}  {dot_list[3][i]}  \n')
	result += ((' '*4).ljust((5+len(num_list)*3), '-'))+'\n'
	for i in range(maximum):
		result += ' '*5
		if len(num_list) >= 1:
			result += temp_names[0][i]+'  '
		if len(num_list) >= 2:
			result += temp_names[1][i]+'  '
		if len(num_list) >= 3:
			result += temp_names[2][i]+'  '
		if len(num_list) >= 4:
			result += temp_names[3][i]+'  '
		if i != maximum-1:
			result += '\n'
	
	return result


food = Category('Food')
entertainment = Category('entertainment')
business = Category('business')
food.deposit(900, 'deposit')
entertainment.deposit(900, 'deposit')
business.deposit(900, 'deposit')
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
# print([business, food, entertainment])
print(create_spend_chart([business, food, entertainment]))

