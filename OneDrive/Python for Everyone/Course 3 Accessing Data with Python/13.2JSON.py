import urllib.request, urllib.parse, urllib.error
import json
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

total = 0
count = 0#BELOW  Here I enter the URL, and open it.
address = input('Enter location: ')
if len(address) < 1 : address = "http://py4e-data.dr-chuck.net/comments_42.json"
else: address ="http://py4e-data.dr-chuck.net/comments_445413.json"
print(address)
#print(type(address))
#print(len(address))
print('Retrieving', address)
uh = urllib.request.urlopen(address, context=ctx)

data = uh.read().decode()  # Opening it is not enough, one must read it also
print('Retrieved', len(data), 'characters') # This is the length of the string
#print(data)  #I printed this out just to see what I was getting

info = json.loads(data) #Data is JSON
#print(json.dumps(data, indent=4))
#print(info)
print("Length", len(info))
#for item in info["comments"]:
    #print('Name', item['name'])
    #print('Count', item['count'])

for item in info["comments"]:
    total += int(item['count'])
    count += 1


print('Count:', count)
print('Sum=', total)
