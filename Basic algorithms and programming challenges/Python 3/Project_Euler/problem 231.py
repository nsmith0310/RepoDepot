###answer: long 7526965179680
###uses lengendres algorithm  for finding the primes of n!

from euler import primes, factorize
from numpy import prod
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
    final=[]
    
    l = Counter(a)
    m = Counter(b)
    n = Counter(c)

    bn = l-m-n
    
    
    for x in bn:
        i = 1
        while i<=bn[x]:
            final.append(x)
            i+=1
    return final
        
print(sum(simplify(20000000,15000000)))

