from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error

url = input('Enter - ')
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
# print(tags)
for tag in tags:
	if str(tag.get('href'))[:4] == 'http':
		print(tag.get('href', None))