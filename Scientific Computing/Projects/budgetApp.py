class Category:

	categories = []

	def __init__(self, category: str):
		self.ledger = []
		self.category = category
		Category.categories.append(self)

	def __str__(self):
		self.string = ''
		self.string += ''.join(self.category.capitalize().center(30,'*'))
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
	for category in categories:
		temp_sum = 0
		for transaction in category.ledger:
			if float(transaction['amount']) < 0:
				temp_sum += abs(float(transaction['amount']))
		num_list.append(temp_sum)
	
	num_list.append(sum(num_list))

	for i in range(len(num_list)-1):
		num_list[i] = num_list[i]/num_list[-1]
		

food = Category('food')
print(food.category)
food.deposit(20, 'something')
food.deposit(10, 'some')
food.deposit(30)
print(food.ledger)
print(food.withdraw(69))
print(food.ledger)
print(food.category)
clothing = Category('clothing')
print(clothing.category)
clothing.deposit(150, 'dui')
print(food.get_balance())
print(clothing.get_balance())
food.transfer(40, clothing)
print(food.get_balance())
print(clothing.get_balance())
# print(food.__dir__())
print(food)
for ele in Category.categories:
	print(ele.category)

create_spend_chart(Category.categories)