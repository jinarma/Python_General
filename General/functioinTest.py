def caps(text):
	return text.upper()

print(caps('Hello'))
dupe = caps	# function as an object. Turns dupe into the same function

print(dupe('suh'))