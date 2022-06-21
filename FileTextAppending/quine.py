# A quine is a computer program, that takes no input and prints out its own source code as output.
import os
fhand1 = open(os.path.abspath(__file__), 'r')
file = fhand1.read()
fhand1.close()
print(file)