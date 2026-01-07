###long 843296
from euler import primes

def power(a,n):
    if n==0:
        return 1
    if n&1==False:
        return (a**2)**(n//2)
    else:
        return a*(a**2)**((n-1)//2)

def rep(n):
    return ((n-1)//9)

x = power(10,10**9)
z=(rep(x))
print(1)

t = primes(10000000)
print(2)

final=[]
for y in t:
    if z%y==0:
        final.append(y)
    if len(final)==40:
        print(sum(final))
        break

