import copy
import random
# Consider using the modules imported above.


class Hat:
	
	def __init__(self, *args, **kwargs):
		self.contents = []
		for key, value in kwargs.items():
			while kwargs[key] != 0:
				self.contents.append(key)
				kwargs[key] -= 1
		# print(self.contents)

	def draw(self, removed):
		if removed > len(self.contents):
			return self.contents
		else:
			removals = []
			while removed:
				temp = random.randint(0, len(self.contents)-1)
				if temp not in removals:
					removals.append(temp)
					removed -= 1
				else:
					continue
		# print(removals)
		# temp = copy.copy(self.contents)
		res = []
		temp_contents = []
		for i, ele in enumerate(self.contents):
			if i in removals:
				res.insert(0, ele)
			else:
				temp_contents.append(ele)


		# print(self.contents)
		# print(res)

		# res_dict = dict()
		# for ele in res:
		# 	if ele not in res_dict:
		# 		res_dict[ele] = 1
		# 	else:
		# 		res_dict[ele] += 1

		self.contents = temp_contents
		return res



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
	m, n = 0, num_experiments
	for _ in range(num_experiments):
		hat_copy = copy.copy(hat)
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
# print(hat.draw(3))
print(experiment(hat, {'blue':2, 'green':1}, 4, 1000))
