import os

def gameLogic(name):
	movieNameList = []
	hiddenMovieNameList = []
	for i in name:
		movieNameList.append(i)
		hiddenMovieNameList.append('*')
	#print(hiddenMovieNameList)
	#basic test for signing
	i=0
	while i < 3:
		checkChar = input("\nEnter a letter")
		for j in range(len(movieNameList)):
			if checkChar == movieNameList[j]:
				print('x'*(j)+checkChar+(len(movieNameList)-(j-1))*'x', end='')
				
			else:
				i+=1


movieName=input("Enter the name of a movie: ")
os.system('cls')
print("Guess the letters of the movie!")
gameLogic(movieName)