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
for names in catNames:
	if j==i:
		print(names)
	else:
		print(names, end=', ')
	j=j+1