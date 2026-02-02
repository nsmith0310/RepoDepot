###long 269533451410884183

from euler import primes, factorize,rmtest 


def t(n,l):
    if rmtest(n,5)==True:
        return n
    for x in l:
        if n%x==0:
            while n%x==0:
                
                n//=x

            if x>=n:
                return x
            elif n>=x and rmtest(n,5)==True:
                
                return n
    print(rmtest(n,3)==True)
    return n

lim = 2000000

p = primes(lim)
to=1
i =2

while i<=lim:
    k = i**2 - i + 1
    n1 = t(k,p)
    if n1>=i+1:
        to+=n1-1
        ###print(n1-1,max(factorize(i**3 + 1))-1)
    else:
        n2=t(i+1,p)
        to+=max([n1,n2])-1
        ###print(max([n1,n2])-1,max(factorize(i**3 + 1))-1)
    i+=1

print(to)
