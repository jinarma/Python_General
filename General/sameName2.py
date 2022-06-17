def spam():
	global eggs
	eggs='spam'
def bacon():
	eggs='bacon local'

eggs='global'
spam()
bacon()
print(eggs)