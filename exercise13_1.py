from urllib.request import urlopen
import xml.etree.ElementTree as ET
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
tree = ET.fromstring(data)
# find all the count tags in the tree
results = tree.findall('comments/comment')
total = 0
# get the value of count and start adding
for result in results:
    # Look at the parts of a tag
    total = total + int(result.find('count').text)

print('Count ', len(results))
print('Sum ', total)
