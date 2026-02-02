###Answer: slow 1677366278943
from euler import phi


def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def chain(n):
    count = 1
    x = n
    while x >1:
        count+=1
        x=phi(x)
        

    return count
tmp=[]
t = primes(40000000)
t.sort()
print("Done generating primes")
for x in t:
    if chain(x)==25:
        tmp.append(x)

print(sum(tmp))
