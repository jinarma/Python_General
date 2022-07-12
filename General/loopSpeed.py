# Concludes that in certain small repetitive tasks, clubbed loops are quicker


import time


def for_individual(itr):
	for i in range(itr):
		a	= 1 + 1

def for_in_fives(itr):
	for i in range(0, itr, 2):
		a	= 1 + 1
		a	= 1 + 2
		a	= 1 + 3
		a	= 1 + 4
		a	= 1 + 5
	


if __name__ == '__main__':

	itr	= int(input('How many iterations: '))
	flag = -1
	while flag != 0 or flag != 1:
		flag = int(input('0 for - for_individual\n1 for - for_in_fives\n'))
		if flag == 0 or flag == 1:
			break
		else:
			print('Not a valid choice')
	flag = bool(flag)

	start = time.time()
	
	if flag == True:
		for_in_fives(itr)
	elif flag == False:
		for_individual(itr)

	end	= time.time()
	print(end-start)
