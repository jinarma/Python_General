import random as rn
number = rn.randint(1, 20)
for i in range(number):
	if i < number-1:
		print(rn.randint(0, 1), end=' ')
	else:
		print(rn.randint(0, 1))
print("There were "+str(number)+" iterations")