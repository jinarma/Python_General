def count(n):
	table = [0 for i in range(n+1)]
	table[0] = 1
	for i in range(2, n+1):
		table[i] += table[i-2]
	for i in range(4, n+1):
		table[i] += table[i-4]
	for i in range(6, n+1):
		table[i] += table[i-6]
	return table[n]
n = 10
print('Count for', n, 'is', count(n))
n = 13
print('Count for', n, 'is', count(n))