###Answer: 16695334890

from itertools import permutations
from euler import primes

p = primes(18)

t=[]
x = list(permutations(['0','1','2','3','4','5','6','7','8','9']))
for y in x:
    t.append(''.join(y))

final = []
for v in t:
    sub2 = int(v[1:4])
    sub3 = int(v[2:5])
    sub5 = int(v[3:6])
    sub7 = int(v[4:7])
    sub11 = int(v[5:8])
    sub13 = int(v[6:9])
    sub17 = int(v[7:])
    if sub2%2==0:
        if sub3%3==0:
            if sub5%5==0:
                if sub7%7==0:
                    if sub11%11==0:
                        if sub13%13==0:
                            if sub17%17==0:
                                final.append(int(v))    

print(sum(final))
    
