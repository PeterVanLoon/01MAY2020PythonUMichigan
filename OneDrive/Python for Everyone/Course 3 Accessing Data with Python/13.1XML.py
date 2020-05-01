import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#BELOW  Here I enter the URL, and open it.
address = input('Enter location: ')
if len(address) < 1 : address = "http://py4e-data.dr-chuck.net/comments_42.xml"
else: address ="http://py4e-data.dr-chuck.net/comments_445412.xml"
print(address)
print(type(address))
print('Retrieving', address)
uh = urllib.request.urlopen(address, context=ctx)

data = uh.read()  # Opening it is not enough, one must read it also
print('Retrieved', len(data), 'characters') # This is the length of the string
#print(data.decode())  #I printed this out just to see what I was getting

tree = ET.fromstring(data) #Data is XML, so now I have to transform it
print(tree)
counts = tree.findall('comments/comment/count')
#print(counts)
total = 0
for count in counts:
    #print(type(count.text))
    total += int(count.text) #I need to add the .text, because count is an XML
    #                           data type
print(total)
