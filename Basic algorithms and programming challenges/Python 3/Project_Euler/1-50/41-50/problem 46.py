###answer: 5777

from euler import primes
from math import sqrt


x = range(3,1000,2)



odds=[]
for y in x:
  for v in x:
    odds.append(y*v)
sc= 0
count = 0
odds.sort()


for b in odds:
    count=0
    tmp = primes(b)
    
    for m in tmp:
        if sqrt((b-m)/2).is_integer():
            count+=1
    if count==0:
        print(b)
        break
    
