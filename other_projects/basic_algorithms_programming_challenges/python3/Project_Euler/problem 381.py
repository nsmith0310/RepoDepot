###longish 139602943319822

from euler import primes
from math import factorial as f

###ripped from wikipedia
def xgcd(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0
def m(a, b):
    """return x such that (x * a) % b == 1"""
    g, x, _ = xgcd(a, b)
    if g == 1:
        return x % b

def i(a):
    j = 2
    while m(j,a)!=j:
        j+=1
    return j


z = primes(10**8)
z.remove(2)
z.remove(3)

t = 0

###based mainly on Wilson's theorem as explained by a stackexchange user
for x in z:
    n1 = x-1
    n2 = 1
    n3 = n1/2
    n4 = (m(x-2,x)*m(x-3,x))%x
    n5 = (m(x-4,x)*m(x-2,x)*m(x-3,x))%x
    t+=(n1+n2+n3+n4+n5)%x
print(int(t))
