catNames=[]
i=0
j=1
while True :
	print("Enter the name of cat "+str(len(catNames))+" Or enter nothing to skip!")
	names=input()
	if names=='':
		break
	else:
		catNames=catNames+[names]
		i=i+1
for names in range(len(catNames)):
	if names==i-1:
		print(catNames[names])
	else:
		print(catNames[names], end=', ')