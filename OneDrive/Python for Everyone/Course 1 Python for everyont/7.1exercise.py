# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname,"r")
print("BS")



count = 0
for line in fh:
    #print(line.strip())
    xxx=line.strip()
    print(xxx.upper())
    #count = count + 1

#print(count,"Lines")
