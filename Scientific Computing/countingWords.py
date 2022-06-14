def index_to_sort(ls):
	return ls[1]


counts = {}
text = input().lower()
words = text.strip(', . ; ?')
words = words.split()
for word in words:
	counts[word] = counts.get(word, 0) + 1
# print(sorted(counts.items(), reverse=True))
print(sorted(counts.items(), key=index_to_sort, reverse=True))