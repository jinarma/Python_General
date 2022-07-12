import re

string = 'This is an example of a rEAAAAllly long string2123 sa which elementy is the largest, find out!'
words = re.findall(r'[a-z]+\w', string)
# print(max(word))
print(max(string.split()))
maximum = ''
for ele in words:
	if len(ele) >= len(maximum):
		maximum = ele

print(maximum)