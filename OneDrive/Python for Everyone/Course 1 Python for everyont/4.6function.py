hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)

def computepay(h,r):
    regular = 0
    overtime = 0
    pay =0
    if h <= 40:
        regular = h #
    else:
        regular = 40
        overtime = h - regular
    pay = (regular * r) + (overtime * 1.5 *r)
    return (pay)


print("Pay",computepay(h,r))
