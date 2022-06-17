import re

string = 'Two of my most favourite numbers are 0 and 12'
# string = 'Two of my most favourite numbers are zero and one'

x = re.findall('[0-9]+', string)	# returns connected numbers as one. i.e. ['0', '12']
# x = re.findall('[0-9]', string)	# returns every number as seperate. i.e. ['0', '1', '2']
print(x)

y = re.findall('[aeiou]', string)	# returns all the individual lowercase matching characters, in this case vowels
y_connected = re.findall('[aeiou]+', string)	# returns all the individual AND connected lowercase matching characters, in this case vowels
print(y)

z = re.findall('[A-z]+', string)	# returns all english words

print(z)

vowel_occurance = {}
for char in y:
	vowel_occurance[char] = vowel_occurance.get(char, 0) + 1
for key, value in sorted(vowel_occurance.items()):
	print(key, '* '*value, sep=' ')