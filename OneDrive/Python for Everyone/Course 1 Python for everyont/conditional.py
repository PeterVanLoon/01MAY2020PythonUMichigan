hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
regular = 0
overtime = 0
if h <= 40:
    regular = h #
else:
    regular = 40
    overtime = h - regular
pay = (regular * r) + (overtime * 1.5 *r)
print (pay)
