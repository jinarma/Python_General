def customLen(testString):
	spam = 0
	for i in testString:
		spam=spam+1
	return spam
length = customLen('some String')
print(length)