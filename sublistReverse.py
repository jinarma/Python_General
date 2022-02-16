
ls1 = []
lsTemp = []
size = int(input())
s1 = input().split()
for i in s1:
	ls1.append(int(i))
k = int(input())
i = 0
while i <= size:			
	for j in ls1[i:i+k]:
		lsTemp.insert(i, j)
	i+=k
