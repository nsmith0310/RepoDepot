###Answer: long 986262
import itertools
flatten_iter = itertools.chain.from_iterable
def pfactorize(n):
  l= list(set(flatten_iter((i, n//i) 
    for i in range(1, int(n**0.5)+1) if n % i == 0)))
  if n in l:
        
    l.remove(n)
    l.sort()
  return len(l)+1

i = 2
count=0
for i in range(2,pow(10,7)):
  if pfactorize(i)==pfactorize(i+1):
    count+=1
 
print(count)
