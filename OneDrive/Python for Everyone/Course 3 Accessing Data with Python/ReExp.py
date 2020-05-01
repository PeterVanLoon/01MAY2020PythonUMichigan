import re
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "regex_sum_42.txt"
fh = open(fname)
strnumlist = []
numlist =[]
count = 0
sum = 0
num = 0
for line in fh:
    line = line.rstrip() # I wonder if I really need this
    stuff = re.findall('[0-9]+',line) # this goes through each line and gives
                                     # list of numbers, or nothing, from that
                                     #line.
    strnumlist.append(stuff) # I append what I get from each line into a huge
                             # list
    for x in stuff: # now I strip out all the empty lists in strumliss
        num = re.findall('[0-9]+', x)
        numlist.append(num)
print("here where I get all the numbers in each line")
print(strnumlist)
print()
print("here are Just the numbers, but they are still in a list")
print(numlist)
print()
print("Now I take each list element and change it to a string,\
and then add the integer value of that string to the total")
for y in numlist:
    #print(y)
    #print(type(y))
    ListToStr = ''.join([str(elem)for elem in y])
    #print(ListToStr)
    #print(int(ListToStr))
    count = count +1
    #print(count)
    sum = sum + int(ListToStr)
print()
print()
print("OK - there are",count,"values and they total",sum)
