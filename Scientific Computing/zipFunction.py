num_list = [2, 4, 3, 1, 3]
name_list = ['sharma', 'gupta', 'mahajan', 'jagtap', 'rana']
zipped = list(zip(num_list, name_list))
print(zipped)
for ele1, ele2 in zipped:
	print(ele1)
	print(ele2)

max(num_list)