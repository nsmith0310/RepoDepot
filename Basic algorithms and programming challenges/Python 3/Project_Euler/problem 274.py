###1601912348822

from euler import primes,rmtest as r


def slow(n,m):
    return int(str(n)[:-1])+m*(int(str(n)[-1]))
t = 16

d = primes(10**7)[5:]
sub=[]
for x in d:
    i = 1
    while i<=x:
        ###print(x*i,int(str(x*i)[-1]))
        k = ((x*i)-int(str(x*i)[:-1]))/int(str(x*i)[-1])
        
        if k.is_integer() and k<x:
            t+=k
            
            break
        
        i+=1

print(int(t))
