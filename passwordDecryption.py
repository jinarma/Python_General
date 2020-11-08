'''Encryption works like this, if a lowercase letter is encountered, then it swaps it with the next letter and adds an * right after the first letter in line, e.g. HeLO will become HL*eO. If a digit is encountered, then it is moved to the first positon and a zero is also placed in its place. e.g. H3L0 becomes 03H0L0. So in gist, a word like H3Llo Th3RE becomes, 33H0Lo*l T0*hRE. Your job is to decript a password, knowing these key factors.'''

# def digitsPart(string):
# 	count=0
# 	listOfNum = []
# 	listOfChar = []
# 	for i in range(len(string)):
# 		if string[i].isdigit() != True:
# 			break
# 		else:
# 			listOfNum.append(string[i])

# 	print(listOfNum)
# 	listLength = len(listOfNum)
# 	stringLength = len(string)
# 	print("listLength = {}\nstringLength = {}".format(listLength, stringLength))

# 	string = string[listLength:]
# 	print("new string: "+string)

# 	for i in range(len(string)):
# 		listOfChar.append(string[i])
# 	print(listOfChar)

# 	for i in range(len(string)):
# 		if listOfChar[i] == "0":
# 			listOfChar[i] = listOfNum[count]
# 			count+=1
# 	print(listOfChar)
# 	string=''
# 	for i in listOfChar:
# 		string+=i

# 	print(string)
	
# 	# return string
	
def lettersPart(string):
	print("")

def endResult(string):
	print("")

encryptedString = input()
digitsPart(encryptedString)
#print(endResult(encryptedString))