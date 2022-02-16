string = input()
count = 0
for i in range(len(string)):
	for j in range(len(string)):
		count += 1
print(count)