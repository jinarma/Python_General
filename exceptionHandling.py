def spam(divideBy):
	try:
		return 42/divideBy
	except ZeroDivisionError:
		return "Invalid"

print(spam(2), spam(10), spam(0), spam(3), sep='\n')