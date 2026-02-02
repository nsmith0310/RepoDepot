###long 684465067343069

from euler import factorize as f
from math import floor, sqrt

def mobius(n):
    if n==1:
        return 1
    d = f(i)
    b = len(d)
    if len(list(set(d)))==b:
        return pow(-1,b)
    else:
        return 0


num = pow(2,50)

total=1
i = 1
while i<sqrt(num):
    total+=mobius(i)*(floor(num/i**2))
    i+=1
print(total-1)
