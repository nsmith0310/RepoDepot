###LONG: 55

import itertools
import collections
from math import floor
def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

print("Number of circular primes less than: ")
lim=int(input())
tmp=get_primes(lim)
tmp.sort()

test=[]
i=0
count=0
tmp_i=0
final=[]
j=0
k=0
final_c=0
while i < len(tmp):
    de = collections.deque(list(str(tmp[i])))
    j=0
    count=0
    while j < len(list(de)):
        de = collections.deque(list(str(tmp[i])))
        de.rotate(j)
        integer = int(''.join(list(de)))
        if integer in tmp:
            count+=1
        if count==len(list(de)):
            final_c+=1
        j+=1
    i+=1
final.append(2)
final = list(dict.fromkeys(final))
final.sort()
print(final_c)
