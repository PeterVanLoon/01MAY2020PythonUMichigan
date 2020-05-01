
list = []
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    words=line.split()
    for word in words:
            if not word in list:
                list.append(word)
list.sort()#alphalist= list.sort()
print(list)#print(line.rsplit())
#print("Done with first stuff")
