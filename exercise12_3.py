from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter the url - ')
count = int(input('Enter count: '))
position = int(input('Enter position:'))
for x in range(count+1):
    print('Retrieving ', url)
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    # Retrieve all of the anchor tags
    tags = soup('a')
    url =  tags[position-1].get('href', None)
