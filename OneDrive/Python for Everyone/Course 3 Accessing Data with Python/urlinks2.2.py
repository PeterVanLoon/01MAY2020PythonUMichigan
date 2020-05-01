# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

target =''
count = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL- ')
if len(url) < 1 : url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
else: url = "http://py4e-data.dr-chuck.net/known_by_Layah.html"
stringposition = input('Enter position -')
repetition = input('Enter repeats -')

html = urllib.request.urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, 'html.parser')
position = int(stringposition)
tags = soup.find_all('a')# Retrieve all of the anchor tags
target = tags[position-1]
count = count +1
print("000000",count)
print("000000",target)
print
print

while count <= int(repetition)-1:
    count = count +1
    print("CCCCC", count)
    yyyy= re.split('"(.+?)"',str(target))
    html = urllib.request.urlopen(str(yyyy[1]), context=ctx).read()#print(soup.prettify())#Figure out what I have
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup.find_all('a')# Retrieve all of the anchor tags
    target = tags[position-1]
    print("AAAAA", target)
    print("here it is:",target)

    print("AAAAA", count, "repetition",repetition)

else:
    print("done")
    print(target)
    try:
        found = re.search('>(.+?)</a>', str(target)).group(1)
    except AttributeError:
    # AAA, ZZZ not found in the original string
        found = ''
    print(found)
print("Count ", count)
