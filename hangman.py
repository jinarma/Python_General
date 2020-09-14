import os

def gameLogic(name):
	pseudoString=''
	test=0
	length=len(name)
	oneCharacter=input()
	numberOfChoices=3
	for i in range(0, length):
		if oneCharacter==name[i]:
			print(oneCharacter, end='')
			pseudoString=pseudoString[ : i]+oneCharacter
		else:
			print("*", end='')
			test=test+1
		if test==length:
			print('Wrong guess!\nYou have '+str(numberOfChoices)+' choices left.')
			numberOfChoices=numberOfChoices-1
	print('\n'+pseudoString)
movieName=input("Enter the name of a movie: ")
os.system('cls')
print("Guess the letters of the movie!")
gameLogic(movieName)