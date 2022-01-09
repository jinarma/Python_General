import re

test_string = '123abc456789abc123ABC'

pattern = re.compile(r'abc') # r means raw, e.g. \t will be printed instead of tab
pattern2 = re.compile(r'321')
matches = pattern.finditer(test_string)
no_match = pattern2.findall(test_string)

for i in matches:
	print(i)


if not no_match:
	print('False')
	
