###1322
###referred to wiki from s braumme, followed wiki algorithm

from math import sqrt, floor
def period(n):
    m = 0
    d = 1
    a = floor(sqrt(n))
    b = a
    count = 0
    while 2*b!= a:
        count+=1
        m = d*a - m
        d = float((n-m**2)/d)
        a = floor(float(b + m)/d)
    
    return count

def check(n):
    return not (sqrt(n)).is_integer()


i = 2
count=0
while i <= 10000:
    if check(i)==True:
        if period(i)&1:
            count+=1
    i+=1
print(count)
