def digitsPart(string):
	#print("1")
	listDigits=[]
	for i in string:
		listDigits.append(i)
	#print(listDigits)
	i=0
	j=0
	listLength = len(listDigits)
	while i < listLength+j:
		if listDigits[i].isdigit() == True:

			#Bring number to front
			listDigits.insert(0, listDigits[i])
			print("1: ", end='')
			print(listDigits)

			#Remove old copy of number from index
			listDigits.pop(i+1)
			print("2: ", end='')
			print(listDigits)

			#Insert 0 at the place of old number
			listDigits.insert(i+1, "0")
			print("3: ", end='')
			print(listDigits)
			j+=1
			i+=1
		i+=1
	string=''
	for i in listDigits:
		string+=i

	#print(string)
	return string

def lettersPart(string):
	listLetters = []
	for i in string:
		listLetters.append(i)
	j=0
	i=0
	listLength = len(listLetters)
	while i < listLength:
		if listLetters[i].islower() == True:
			#print(listLetters[i])
			try:
				listLetters[i], listLetters[i+1] = listLetters[i+1], listLetters[i]
				listLetters.insert(i+1, "*")
				#print(listLetters)
				i+=2
			except IndexError:
				break
		i+=1
	#print(listLetters)
	string=''
	for i in listLetters:
		string+=i
	return string

def endResult(string):
	numberEncryption = digitsPart(string)
	encryptedString = lettersPart(numberEncryption)
	return encryptedString

string = input()
#lettersPart(string)
#digitsPart(string)
print(endResult(string))
