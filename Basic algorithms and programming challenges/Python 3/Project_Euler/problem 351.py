###11762187201804552
###runtime is unknown (somewhere between long and very long)
###re-used legendre's formula from problem 231

from euler import primes, factorize,phi,prod

from collections import Counter


from math import floor
def powers(n):
    x = primes(n+1)
    t=[]
    for y in x:
        total=0
        v = y
        count=1
        while v<=n:
            count+=1
            total+=floor(n/v)
            v=y**count
        i = 1
        while i <=total:
            t.append(y)
            i+=1
    return t
        
def simplify(n,m):
    a = powers(n)
    b = powers(m)
    c = powers(n-m)
    final=1
    
    l = Counter(a)
    m = Counter(b)
    n = Counter(c)

    bn = l-m-n
    
    
    for x in bn:
        i = 1
        while i<=bn[x]:
            final*=x
            i+=1
    return final
        

def ncr(n,r):
    return factorial(n)//((factorial(r))*(factorial(n-r)))


def s(n):
    t = (simplify(n+1,2))
    i = 1
    while i<=n:
        t -=phi(i)
        i+=1
    return 6*t


print(s(100000000))
    
