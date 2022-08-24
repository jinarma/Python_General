import copy
import random
# Consider using the modules imported above.


class Hat:
	
	def __init__(self, **kwargs):
		self.contents = []
		for key, value in kwargs.items():
			self.contents += ([key]*value)

	def draw(self, removed):
		if removed > len(self.contents):
			return self.contents
		res = []
		for i in range(removed):
			res.append(self.contents.pop(random.randint(0, len(self.contents))))
		# print(self.contents)
		# print(res)
		return res



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
	m, n = 0, num_experiments
	for _ in range(num_experiments):
		hat_copy = copy.deepcopy(hat)
		# print(id(hat), id(hat_copy))
		# print(hat_copy.draw(3))
		all_balls = 0
		hat_removed_dict = {}
		for ele in hat_copy.draw(num_balls_drawn):
			if ele not in hat_removed_dict:
				hat_removed_dict[ele] = 1
			else:
				hat_removed_dict[ele] += 1

		for key, value in hat_removed_dict.items():
			try:
				if expected_balls[key] == value:
					all_balls += 1
			except:
				continue
		if all_balls == len(expected_balls):
			m += 1
	# print(m)
	return m/n

random.seed(95)
hat = Hat(blue=3, red=2, green=6)
hat.draw(3)
# print(experiment(hat, {'blue':2, 'green':1}, 4, 1000))
print(hat)
