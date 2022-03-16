from ctypes import sizeof
from io import SEEK_END
import os

def write(string):
	file = open('D:/Programming/Python/Github/Python_General/FileTextAppending/testString.txt', 'a')
	file.write(string)
	file.write('\n')
	file.seek(0, SEEK_END)
	print(file.tell(), 'bytes')
	file.close()
	# os.remove(file.name)	# deletes the file

write('Sup brah')

