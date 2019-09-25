from urllib.request import urlopen
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter the url - ')
# Read URL
data = urlopen(url, context=ctx).read()
print('Retrieving ', url)
#parse retrieved document
jsonData = json.loads(data)
# find all the count tags in the tree
print('User Count', len(jsonData['comments']))
total = 0
# get the value of count and start adding
for result in jsonData['comments']:
    # Look at the parts of a tag
    total = total + int(result['count'])


print('Sum ', total)