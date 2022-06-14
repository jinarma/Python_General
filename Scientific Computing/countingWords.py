counts = {}
text = input().lower()
words = text.strip(', . ; ?')
words = words.split()
for word in words:
	counts[word] = counts.get(word, 0) + 1
print(counts)