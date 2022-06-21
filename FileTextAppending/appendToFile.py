from ctypes import sizeof
from io import SEEK_END
import os

def add_to_file(string):
	file = open('D:/Programming/Python/Github/Python_General/FileTextAppending/testString.txt', 'a')
	file.seek(2)
	file.write(string)
	file.write('\n')
	print(file.tell(), 'bytes')
	file.close()
	# os.remove(file.name)	# deletes the file

add_to_file('Sup brah')

