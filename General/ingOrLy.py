# accept space strings, if word less than 4 chars, then as is, if above 3 add ing, if above 3 and has ing at the end, then add ly at the end

from turtle import end_fill


string = input().split()
for i, ele in enumerate(string):
	if len(ele) < 4:
		continue
	elif ele[-3::].upper() == 'ING':
		string[i] = ele + 'ly'
	else:
		string[i] = ele + 'ing'

for ele in string:
	print(ele, end=' ')