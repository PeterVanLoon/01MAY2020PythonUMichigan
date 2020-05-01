count = 0

fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("From"): continue
    else:
        #print("LOOK HERE")
        wordlist = line.split()
        if len(wordlist)<3:continue
        #print(wordlist)
        emailaddress = wordlist[1]
        print(emailaddress)
        #print(count)
    count = count + 1
#print ("STOP")    #print (total)
print ("There were", count,"lines in the file with From as the first word")#p
