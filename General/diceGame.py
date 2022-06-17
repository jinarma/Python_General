import random

#Dice roll function
def roll():
	sideUp=random.randint(1,6)
	return sideUp

#Repeat turn logic
def repeatTurn():
	print("You get another turn "+names+"\nThrow the die")
	input()
	diceSideUp=random.randint(1,5)
	print("The dice rolled up "+str(diceSideUp))
	return diceSideUp

#Add logic to add players
playerNames=[]
scoreSum=[]
while True:
	print("Enter the name of the player: ")
	names=input()
	if names=='':
		break
	else:
		playerNames=playerNames+[names]


#Dice throw prompt
while True:
	for names, i in zip(playerNames, range(len(playerNames))):
		print("Play your turn "+str(names))
		print("Throw the die")
		input()
		diceSideUp=roll()
		print("The dice rolled up "+str(diceSideUp))
		scoreSum[i]=[diceSideUp]
		while diceSideUp==6:
			scoreSum[i]=scoreSum[i]+repeatTurn()
