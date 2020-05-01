# Use the file name mbox-short.txt as the file name
count = 0
total = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    ipos = line.find(':')
    num = line[ipos+1:]
    value=float(num)
    #print(value)
    count = count + 1
    total = value +total
    #print (count)
    #print (total)
print ("Average spam confindence:",total/count)#print(line.rsplit())
#print("Done with first stuff")
