# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

target =''
count = 0
sum = 0
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL- ')
if len(url) < 1 : url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
stringposition = input('Enter position -')
repetition = input('Enter repeats -')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

position = int(stringposition)
tags = soup.find_all('a')# Retrieve all of the anchor tags
target = tags[position-1]
print(target)
html = urllib.request.urlopen(target, context=ctx).read()#print(soup.prettify())#Figure out what I have
#print(tags)#Figure out what I have
for tag in tags:
    #pr#print(tag.get('href', None))
    #print(type(position))
    #print(type(target))#target=tag[position-1]
    #print("TAG: ",tag) #Figure out what I have
    #print(target)#print(type(tag))  #Figure out what I have
    #print("URL: ", tag.get("comments", None))  #Figure out what I have
    #print('Attrs:',tag.attrs)  #Figure out what I have
    xxxx = str(tag) # turn the tag into a string
    #print(xxxx) #Figure out what I have
    #print(type(xxxx)) #Figure out what I have
    xxx= re.split('([0-9]+)',xxxx) #get the xxxx string broken on the numbers
    #print(xxx)  #Figure out what I have
    xx=xxx[2] #here I get the part of the string that is the number
    #print(xx) #Figure out what I have
    #print(type(xx))  #Figure out what I have
    try:
        found = re.search('>(.+?)</a>', xx).group(1)
    except AttributeError:
    # AAA, ZZZ not found in the original string
        found = '' # apply your error handling
    #print(found)
    #x=int(xx) #Change the string number into an integer
    #print(x) #Figure out what I have
    #print(type(x)) #Figure out what I have
    #print(sum) #Figure out what I have
    #count = count +1
    #print(count) #Figure out what I have
print("Count ", count)



#tags = soup('a')
#for tag in tags:
    #print(tag.get('href', None))
