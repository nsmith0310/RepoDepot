###9350130049860600
###based loosely on the min-heap idea on stackexchange

from euler import primes, large_factorize as f,prod
from itertools import product as q
from math import floor
from euler import rmtest as r


def pw(p,l):
    t=1
    for x in p:
        t*=pow(x,l[p.index(x)])
    return t

def g(n):
    t=1
    a = f(n)
    b = list(set(a))
    for x in b:
        t*= 2*a.count(x)+1
    return floor((t+2)/2)
            
###numbers guessed based on an incorrect solution the highest intial exponent
###of which was 6 and the final answer being too large

h2 = list(q([1,2,3,4,5,6],repeat = 4))
h1=[]
for x in h2:
    if max(x)==x[0]:
        h1.append([a for a in x])
            
for x in h1:
    x.sort(reverse=True)
d = primes(50)
mn=10**20

###upper and lower limits based on the length of significantly smaller
###solutions and the upper based on the maximum needed stated by s braumme

l = 6

while l<=12:
    k = h1
    prime = d[:l]
    for x in k:
        b=0
        if l>4:
            i = 1
            b = []
            for z in x:
                b.append(z)
            while i<=l-4:
                b.append(1)
                i+=1
     
        y = pw(prime,b)
          
        if g(y)>4000000 and y<mn:
            mn=y

        ###idea is that at a certain lower value for factor number, we can
        ###skip ahead in factor length
        elif g(y)<=400:
            break       
    l+=1
    
print(mn)
            
        
