# file = open('E:\Programming\Python\Github\Python_General\zipBomb\someFile.txt', 'w')
# file.close()
file = open('E:\Programming\Python\Github\Python_General\zipBomb\someFile.txt', 'a')
for i in range(20):
	file.write(str(i))
	file.write(' ')
file.close()