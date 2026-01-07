###answer 892371480
###algorithm not mine (code is)

from euler import phi, primes
from numpy import prod


def times(n):
    i = 0
    total = 1
    while i < len(n):
        total*=n[i]
        i+=1
    return total

x = primes(100)
mn = 1
i = 2
while i < len(x):
    trial = x[:i]
    num = times(trial)
    if float(phi(num)/float(num-1))<float(15499/94744):
        t = times(x[:i-1])
        break
    i+=1

mx=0
z = [k for k in range(2,i)]
l = 0
while l<len(z):
    
    if float(phi(t*z[l])/float(t*z[l]-1))<float(15499/94744):
        print(t*z[l])
        break
    l+=1

