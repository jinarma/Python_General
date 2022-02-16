f1 = open('hamming/hammingCodeGeeks.py', 'r')
f2 = open('hamming/hammingCleaned.py', 'w')
f3 = open('hamming/test.py', 'r')


for line in f1:
	if '#' not in line and line[:2] != '\n':
		# for char in line:
		f2.write(line)
f2.close()
f2 = open('hamming/hammingCleaned.py', 'r')
print(f1.read())

