from math import gcd
from euler import factorize
def power(a,n):
    if n==0:
        return 1
    if n&1==False:
        return (a**2)**(n//2)
    else:
        return a*(a**2)**((n-1)//2)

def rep(x):
    return int((power(10,x)-1)//9)


i = 1000001
while i!=-1:
    x = rep(i)
    t = factorize(x)
    for y in t:
        if gcd(y,10)==1:
            print(y)
            break
    i+=1
