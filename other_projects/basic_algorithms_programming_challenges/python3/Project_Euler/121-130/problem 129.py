###longish 1000023

from euler import primes,power
from math import gcd

def p(a,n,m):
    if m==1:
        return 0
    r = 1
    b = a%m
    while n>0:
        if n %2 ==1:
            r = (r*b)%(9*m)
        n =n >> 1
        b=(b**2)%(9*m)
    return r

i=1000000

while i!=-1:
    if gcd(i,10)==1:
        j = 1
        while p(10,j,i)!=1:
            
            j+=1
        if j>1000000:    
            print(i)
            break
        
    i+=1
