###painfully slow 510510 SLOW

def primes(high):
    numbers = set(range(high, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, high+1, p)))
    return primes

def phi(n,m):
  p = m
  final = n
  if pow(2,n-1)%n==1:
    return n-1
  i = 0
  while i < len(p) and p[i]<=n:
    if n%p[i]==0:
      while n%p[i]==0:
        n=n/p[i]
      final-=final/p[i]
    i+=1
  if n>1:
    final-=final/n
  return final


i = 2
mx=0
p=0
while i <= 1000000:
  j = primes(i)
  if i/phi(i,j)>mx:
    mx=i/phi(i,j)
    p = i
  i+=1

print(p)
