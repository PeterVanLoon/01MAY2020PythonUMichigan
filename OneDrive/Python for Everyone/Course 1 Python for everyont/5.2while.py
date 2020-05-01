largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        num = int(num)
    except:
        print ('Invalid input')
        continue
    print (num)

    if smallest is None and largest is None:
        smallest = num
        largest = num
    elif num >= largest:
        largest = num
    elif num <= smallest:
        smallest = num


    #    largest = num
#    else:
#        smallest = num



print("Minimum is", smallest)
print("Maximum is", largest)
