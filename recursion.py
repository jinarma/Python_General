def factorial(num):
	if num == 1:
		return 1
	else:
		return factorial(num-1)*num

def addition(num):
	if num == 1:
		return 1
	else:
		return addition(num-1)+num

print(factorial(5))
print(addition(5))
