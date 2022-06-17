from random import randint as rn
num_list = list(rn(100, 200)/10 for _ in range(20))
for i, ele in enumerate(sorted(num_list)):
	print(f'At {i} hash({ele}) = {hash(ele)}')