# REQUIRES API KEY TO OPERATE

import json
import urllib.request, urllib.error, urllib.parse
import os
from dotenv import load_dotenv

# print(urllib.parse.urlencode({'address':'jammu, jammu and kashmir'}))	# converts to URL lingo
load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env'))
API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')
url = 'https://maps.googleapis.com/maps/api/geocode/json?key=' + API_KEY

# This PATH is the current directory
PATH = os.path.dirname(os.path.abspath(__file__))
while True:
	address = input('Enter address - ')
	address_encoded = urllib.parse.urlencode({'address':address})
	url = '&'.join([url, address_encoded])
	data = urllib.request.urlopen(url).read().decode()

	# stores the recieved data from URL request as 'currentAddress.json'
	fhand = open(os.path.join(PATH, 'currentAddress.json'), 'w')
	fhand.write(data)
	fhand.close()

	# checks if the recieved JSON is valid or not
	try:
		js = json.loads(data)
	except:
		print('Not a valid address, try again')
		break

	# checks if data retrieval was successful of not
	if not 'status' or js['status'] != 'OK':
		print('====== DATA RETRIVAL FAILED ======')
		print(url.decode().strip())
		continue

	print(f'For {address}:\n\tLatitude: {js["results"][0]["geometry"]["location"]["lat"]}\n\tLongitude: {js["results"][0]["geometry"]["location"]["lng"]}\n\tAddress: {js["results"][0]["formatted_address"]}')
	break
	# print(js)
