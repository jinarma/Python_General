'''Encryption works like this, if a lowercase letter is encountered, then it swaps it with the next letter and adds an * right after the first letter in line, e.g. HeLO will become HL*eO. If a digit is encountered, then it is moved to the first positon and a zero is also placed in its place. e.g. H3L0 becomes 03H0L0. So in gist, a word like H3Llo Th3RE becomes, 33H0Lo*l T0*hRE. Your job is to decript a password, knowing these key factors.

H3LO->3H0LO; h3LO->3h0LO; H3lO->3H0O*l; H31O->13H00O; heL0->0e*hL0; He1O.'''

def digitsPart(string):
	count=0
	listOfNum = []
	listOfChar = []
	for i in range(len(string)):
		if string[i].isdigit() != True:
			break
		else:
			listOfNum.append(string[i])

	listLength = len(listOfNum)
	stringLength = len(string)

	string = string[listLength:]

	for i in range(len(string)):
		listOfChar.append(string[i])

	for i in reversed(range(len(string))):
		if listOfChar[i] == "0":
			listOfChar[i] = listOfNum[count]
			count+=1
	string=''
	for i in listOfChar:
		string+=i
	
	return string
	
def lettersPart(string):
	letterList = []
	for i in range(len(string)):
		letterList.append(string[i])

	for i in range(len(string)):
		if letterList[i] == "*":
			temp = letterList[i-1]
			letterList[i-1] = letterList[i+1]
			letterList[i+1] = temp
	i=0
	while i < len(letterList):
		if letterList[i] == "*":
			letterList.pop(i)
		i+=1
	string=''
	for i in letterList:
		string+=i
	return string

def endResult(encryptedString):
	digitsDoneString=digitsPart(encryptedString)
	decryptedString=lettersPart(digitsDoneString)
	return decryptedString

encryptedString = input()
print(endResult(encryptedString))