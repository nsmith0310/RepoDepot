###long 35407281

def power(a,b):
    if b&1==True:
        return a*(a**2)**int((b-1)/2)
    else:
        return (a**2)**int(b/2)


def primes(high):
    numbers = set(range(high, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, high+1, p)))
    return primes

def prod(x):
    t=1
    for y in x:
        t*=y
    return t%500500507

p = primes(100000000)
d = p
for x in p:
    i = 1
    v = power(x,power(2,i))
    if v<=d[-1]:
        d.append(v)
        d.sort()
        i+=1

h = d[:500500]
print(prod(h))
