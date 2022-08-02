import urllib.request
import urllib.parse
import urllib.error
from twurl import augment
import ssl

print("* Calling Twitter...")
url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json', {'screen_name': 'Shubhankar_afp', 'count': '2'})
print(url)

# Ignoring SSL certs errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

connection = urllib.request.urlopen(url, context=ctx)
data = connection.read()
print(data)

headers = dict(connection.getheaders())
print(headers)