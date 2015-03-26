year = int(input('enter a year'))
#cannot return something outside of function
a = year % 19
b = year % 4
c = year % 7
d = (19*a+24) %30
e = (2*b+4*c+6*d+5)%7
date_of_easter = 22 + d +e

march = 'easter is on march',date_of_easter %32
april = 'easter is on april',date_of_easter %31
if date_of_easter <= 31:
    print(march)
elif date_of_easter > 31:
    print (april)
