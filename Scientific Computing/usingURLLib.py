import urllib.request, urllib.error, urllib.parse
import webbrowser

def sort_by_value(key_value_pair: set, *args, **kwargs):
	return key_value_pair[1]

# file handle for the text returned by http://data.pr4e.org/romeo.txt
def romeo_text():
	return urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

# file handle for the text returned by http://www.dr-chuck.com/page1.htm
def dr_chuck():
	return urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')

# creating a dictionary for every word (case insensitive) in the text
def dict_of_words(file_handle):
	count = dict()
	for line in file_handle:
		print(line.decode().strip())
		for word in line.decode().strip().split():
			count[word] = count.get(word, 0) + 1
	# creating a new sorted dictionary based on the value of count dict elements
	count = dict(sorted(count.items(), key= lambda x: x[1], reverse=True))
	return count

fhand = dr_chuck()
for i, line in enumerate(fhand):
	print(line.decode().strip())
	if i == 3:
		webbrowser.open(f'{line[9:-3].decode()}')
# print(dict_of_words(fhand))


