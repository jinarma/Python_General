def spam():
	global eggs
	eggs='spam'
def bacon():
	eggs='bacon local'
def ham():
	print(eggs)

eggs='global'
spam()
print(eggs)