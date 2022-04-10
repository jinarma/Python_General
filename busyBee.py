def performQueries(s:str, a:list[list[int]], n:int, q:int) -> str:
	for i in range(q):
		left = a[i][0]-1
		right = a[i][1]
		string1 = s[left:right]
		for _ in range(len(s[left:right])):
			if list(string1) == list(reversed(string1)):
				s = s[:left] + string1 + s[right:]
				break
			else:
				string1 = string1[-1] + string1[0:len(string1)-1:]
				continue
	return s

size, queries = list(map(int, input().split()))
string = input()
query_list = []
for i in range(queries):
	query_list.append(list(map(int, input().split())))

print(performQueries(string, query_list, size, queries))
