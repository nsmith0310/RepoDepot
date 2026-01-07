###long 2944730
from euler import power,primes

z = primes(100)

z.sort()
count = len(z)+1
trial = 1


for x in z:
    two = len(z)
    for y in z:
        
        d = x*y
        if d <= power(10,9):
            z.append(x*y)
    z=list(set(z))
    count=len(z)
    if count==two:
        print(count+1)
        break
    
