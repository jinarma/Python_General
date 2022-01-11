import re

test_string = '123abc456789abc123ABC'

pattern = re.compile(r'abc')
matches = pattern.finditer(test_string)	# finditer(), findall(), match(), search()
matches_2 = pattern.findall(test_string)

for i, j in matches, matches_2:
	print(i, j, sep='\n')

# print(i, i, i, i, sep=' ')
# print(j, j, j, j, sep=' ')