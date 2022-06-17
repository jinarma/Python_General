def fact(num):
	if num==1:
		return 1
	else:
		return fact(num-1)*num
num = int(input())
print('The factorial of {} is {}'.format(num, fact(num)))