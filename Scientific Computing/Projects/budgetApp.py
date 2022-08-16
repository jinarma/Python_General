class Category:

	categories = []
	names = []

	def __init__(self, category: str):
		self.ledger = []
		self.category = category.capitalize()
		Category.names.append(self.category)
		Category.categories.append(self)

	def __str__(self):
		self.string = ''
		self.string += ''.join(self.category.center(30,'*'))
		self.string += '\n'
		for ele in self.ledger:
			self.string += ''.join(str(ele['description']).ljust(23, ' '))
			self.string += ''.join('{:.2f}'.format(ele['amount']).rjust(7, ' '))
			self.string += '\n'
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

def create_spend_chart(categories: list[Category]):
	num_list = []
	res = max(list(map(len, Category.names)))
	temp_names = []

	for ele in Category.names:
		temp_names.append(list(ele.ljust(res, ' ')))

	for category in categories:
		temp_sum = 0
		for transaction in category.ledger:
			if float(transaction['amount']) < 0:
				temp_sum += abs(float(transaction['amount']))
		num_list.append(temp_sum)
	
	num_list.append(sum(num_list))

	for i in range(len(num_list)-1):
		num_list[i] = round((num_list[i]/num_list[-1])*10)
	num_list.pop()

	dot_list = []
	for ele in num_list:
		temp_str = 'o'*(ele+1)
		# dot_list.append(list(temp_str))
		dot_list.append(list(temp_str.ljust(11, ' ')))

	if len(num_list) == 0:
		for i in range(10, -1, -1):
			print(f'{str(i*10).rjust(3)}| ')
	if len(num_list) == 1:
		for i in range(10, -1, -1):
			print(f'{str(i*10).rjust(3)}| {dot_list[0][i]}  ')
	if len(num_list) == 2:
		for i in range(10, -1, -1):
			print(f'{str(i*10).rjust(3)}| {dot_list[0][i]}  {dot_list[1][i]}')
	if len(num_list) == 3:
		for i in range(10, -1, -1):
			print(f'{str(i*10).rjust(3)}| {dot_list[0][i]}  {dot_list[1][i]}  {dot_list[2][i]}')
	if len(num_list) == 4:
		for i in range(10, -1, -1):
			print(f'{str(i*10).rjust(3)}| {dot_list[0][i]}  {dot_list[1][i]}  {dot_list[2][i]}  {dot_list[3][i]}')
	print((' '*4).ljust((5+len(num_list)*3), '-'))
	for i in range(res):
		print(' '*5, end='')
		if len(num_list) >= 1:
			print(temp_names[0][i], end='  ')
		if len(num_list) >= 2:
			print(temp_names[1][i], end='  ')
		if len(num_list) >= 3:
			print(temp_names[2][i], end='  ')
		if len(num_list) >= 4:
			print(temp_names[3][i], end='  ')
		print()


food = Category('food')
food.category
food.deposit(20, 'something')
food.deposit(10, 'some')
food.deposit(30)
food.ledger
food.withdraw(69)
food.ledger
food.category
clothing = Category('clothing')
clothing.category
clothing.deposit(150, 'dui')
clothing.withdraw(20)
food.get_balance()
clothing.get_balance()
food.transfer(40, clothing)
food.get_balance()
clothing.get_balance()
# food.__dir__()
print(food)
print(clothing)
for ele in Category.categories:
	print(ele.category)

create_spend_chart(Category.categories)
print('yo', Category.names)
