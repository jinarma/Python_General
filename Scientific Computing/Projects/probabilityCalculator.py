import copy
import random
# Consider using the modules imported above.


class Hat:
	
	def __init__(self, **kwargs):
		self.contents = []
		for key, value in kwargs.items():
			self.contents += ([key]*value)
		# print(self.contents)

	def draw(self, removed):
		if removed > len(self.contents):
			return self.contents
		res = []
		for i in range(removed):
			# res.append(self.contents.pop(random.randint(0, len(self.contents)-i-1)))
			temp = self.contents.pop(int(random.random() * len(self.contents)))
			res.append(temp)
		# print(self.contents)
		# print(res)
		return res



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
	m, n = 0, num_experiments
	# compared = []
	# for key, values in expected_balls.items():
	# 	compared += [key]*values
	# # print(compared)
	for _ in range(num_experiments):
		expected_balls_copy = copy.deepcopy(expected_balls)
		hat_copy = copy.deepcopy(hat)
		balls_drawn = hat_copy.draw(num_balls_drawn)
		for ele in balls_drawn:
			if ele in expected_balls_copy:
				expected_balls_copy[ele] -= 1
		count = 0
		for ele in expected_balls_copy.values():
			if ele <= 0:
				count += 1
		if count == len(expected_balls.keys()):
			m += 1
	# print(m)
	return m/n

random.seed(95)
hat = Hat(blue=3, red=2, green=6)
# hat.draw(3)
print(experiment(hat, {'blue':2, 'green':1}, 4, 1000))
print(hat)
