fname = input("Enter file name: ")
fh = open(fname)
counts = dict()
for line in fh:
    if not line.startswith("From"): continue
    else:
        wordlist = line.split()
        if len(wordlist)<3:continue
        emailaddress = wordlist[1]
        #print(emailaddress)
        #print (counts)
        counts[emailaddress]=counts.get(emailaddress,0)+1

#print ("STOP")    #print (total)
bigcount = None
bigword = None
for emailaddress,count in counts.items():
    if bigcount is None or count >bigcount:
        bigword = emailaddress
        bigcount = count



print (bigword, bigcount)#p
