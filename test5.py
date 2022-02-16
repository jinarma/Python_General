
def dupes(ls1):
	ls2 = []
	for i in ls1:
		temp = 0
		for j in ls1:
			if i == j:
				temp += 1
		ls2.append(str(i)+'_'+str(temp))
	string = ','.join(ls2)
	return string
		


a = input()
a = a.upper()
ls = []
for i in a:
	if i.isalnum():
		ls.append(i)
print(ls)
print(dupes(ls))