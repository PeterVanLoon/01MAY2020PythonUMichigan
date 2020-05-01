# cut out that number and convert to a float
text = "X-DSPAM-Confidence:    0.8475";
ipos = text.find('0')
#print ("ipos =",ipos)
num = text[ipos:]
#print("This is the sting value:",num)
value=float(num)
#print("This is the float value:",value)
print(value)
