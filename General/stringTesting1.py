someString = "Hello who dis"
print(someString)
newList = someString.split()
print(newList)
newString = newList[0]
print(newString)
someString = someString[len(newString)+1:]
print(someString)