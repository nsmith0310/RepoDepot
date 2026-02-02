###not my solution whatsoever 173
from euler import primes,power
prime = primes(1000000)
cubes=[]

i = 1
while i<=577:
    cubes.append(power(i,3))
    i+=1

i = 1
j = i-1
count=0
while i<len(cubes):
    j=i-1
    if (cubes[i]-cubes[j]) in prime:
        print(count)
        count+=1
        
    i+=1
print(count)
        
