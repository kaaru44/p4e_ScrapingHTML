# Created by Carl Jones III on 1/31/19
# p4e Following Links in HTML Using BeautifulSoup

import urllib.request, urllib.parse, urllib.error, ssl
from bs4 import BeautifulSoup

start_url = input('Enter a URL: ')
url_position = input('Enter next URL position in tag list: ')
loop_count = input('Enter scraping loop count: ')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

cntr = 0

#print('Specified URL position:', url_position)
#print('First URL at Position:', start_url)

while cntr < int(loop_count):

    html = urllib.request.urlopen(start_url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    new_url = tags[int(url_position) - 1]
    start_url = new_url.get('href', None)

    #print('New URL: ', start_url)

    cntr = cntr + 1

final_url = start_url
print('Final URL:', final_url)
