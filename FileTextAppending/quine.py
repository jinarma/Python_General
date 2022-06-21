import os
fhand1 = open(os.path.abspath(__file__), 'r')
file = fhand1.read()
fhand1.close()
print(file)