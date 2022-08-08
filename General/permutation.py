# distribute into 3's, at least one of them must be the largest

def check(num):
	temp = 0
	for i in range(110+(num-2), (num-2)*100+12):
		ele = str(i)
		if '0' in ele:
			continue
		if sum(map(int, ele)) == num:
			if ele[0] == ele[1] and ele[2] <= ele[0]:
				continue
			if ele[0] == ele[2] and ele[1] <= ele[0]:
				continue
			if ele[1] == ele[2] and ele[0] <= ele[1]:
				continue
			print(ele)
			temp += 1
	return temp

num = check(int(input()))
print(num)
