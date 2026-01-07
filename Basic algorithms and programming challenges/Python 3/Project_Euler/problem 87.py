###1097343

from euler import primes

def power(a,n):
    if n==0:
        return 1
    if n&1==False:
        return (a**2)**(n//2)
    else:
        return a*(a**2)**((n-1)//2)

def check(a,b,c):
    return power(a,2) + power(b,3) + power(c,4) < 50000000
t=[]
sq = primes(7072)
cb = primes(368)
qd = primes(84)
count = 0
for x in sq:
    for y in cb:
        for z in qd:
            if check(x,y,z)==True:
                t.append(power(x,2) + power(y,3) + power(z,4))
                
print(len(list(set(t))))
