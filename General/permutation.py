# distribute into 3's, at least one of them must be the largest

def check(perm: list):
	if len(perm) == 0:
		return []
	elif len(perm) == 1:
		return [perm]
	num_list = []
	for i in range(len(perm)):
		m = perm[i]
		rem_list = perm[:i]+perm[i+1:]
		for p in check(rem_list):
			num_list.append([m]+p)
	return num_list

num_list = check([1, 2, 3])
lem = [1, 2, 3]
print(lem[:0]+lem[1:])
print(num_list)
