def dupes(charString):
	charString = charString.upper()
	charList = []
	tempCharList = []
	for ele in charString:
		if ele.isalpha():
			charList.append(ele)
	for i in charList:
		sum1 = 0
		for k, j in enumerate(charList):
			if i == j:
				sum1 += 1
		tempCharList.append(str(i)+'_'+str(sum1))
	charList = []
	# for i in tempCharList:
	# 	if i not in charList:
	# 		charList.append(i)
	[charList.append(x) for x in tempCharList if x not in charList]
	charString = ''
	charString = ','.join(charList)
	return charString

if __name__ == "__main__":
	#string = input()
	string = 'abba $+#cs rw$2*'
	print(dupes(string))