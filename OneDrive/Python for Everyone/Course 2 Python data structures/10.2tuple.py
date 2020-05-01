fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
counts = dict()
for line in fh:
    if not line.startswith("From "): continue
    else:
        ipos = line.find(':')
#        print(ipos)
        first = line[(ipos-2):ipos]
#        print(first)
        counts[first]=counts.get(first,0)+1
#print (counts)    #print (total)
hourhistogram = list()
for key, val in counts.items():
    newtup = (key,val)
    hourhistogram.append(newtup)#bigcount = None
#bigword = None
hourhistogram = sorted(hourhistogram)

for key,val in hourhistogram:
    print (key,val)#for emailaddress,count in counts.items():#
    #if bigcount is None or count >bigcount:
    #    bigword = emailaddress
    #    bigcount = count



#print (bigword, bigcount)#p
