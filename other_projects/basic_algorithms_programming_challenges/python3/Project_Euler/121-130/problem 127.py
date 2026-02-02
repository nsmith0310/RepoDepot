###long/ very long 18407904

from math import gcd
from euler import factorize as f, prod,rmtest 


def r(n):
    return prod(list(set(f(n))))

c = 3
t=0
while c<120000:
    
    if rmtest(c,3)==False:
        sc = f(c)
        if len(list(set(sc)))!=len(sc):
            a = 1
            while a<c//2:
                b = c-a
                if gcd(a,b)==1 and r(a)*r(b)*prod(list(set(sc)))<c:
                    t+=c
                a+=1
    c+=1
    
print(t)

'''
from euler import factorize as f,prod,rmtest
from euler2 import gcd


def rad(n):
    return prod(list(set(f(n))))

###precompute radical values since the code continually returns to the same
###values

rads=[]
for i in range(2,120000):
    rads.append(rad(i))

rads.insert(0,1)
###print(rads)

t=0
for c in range(3,120000):
    if rmtest(c,3)==False:
        sc = f(c)
        if len(list(set(sc)))!=len(sc):
        
            b = 1
            while b<c//2:
                if gcd(b,c)==1:
                    a = c-b
                    if b==1:
                        rb = 1
                        ra = rads[a-1]
                        rc = prod(list(set(sc)))
                        if ra*rb*rc<c:
                            t+=c
                    else:
                        rb = rads[b-1]
                        ra = rads[a-1]
                        rc = rc = prod(list(set(sc)))
                        if ra*rb*rc<c:
                            t+=c
            
                b+=1
print(t)
'''
