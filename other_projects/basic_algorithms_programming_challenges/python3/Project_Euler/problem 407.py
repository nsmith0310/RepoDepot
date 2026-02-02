###long 39782849136421
###precomputed the numbers to test as well as their largest prime power factor
###and counted the rest (all numbers which are primes or prime powers have a
###1 value)
###requires the file with the precomputed values

from euler import primes
from math import floor

file1 = "problem 407_nums.txt"


nums=[]

with open(file1) as fp:
    line = fp.readline()
    while line:
        nums.append(list(map(int,(str(line).split(".")))))
        line = fp.readline()



t=nums[-1][0]
nums.remove(nums[-1])

for y in nums:
    n = y[0]
    pw = y[1]
    i = floor((n-1)/pw)
    while i>=1:
        if (((i*pw)+1)*(((i*pw)+1)-1))%n==0:
            t+=((i*pw)+1)
            break
        if ((i*pw)*((i*pw)-1))%n==0:
            t+=i*pw
            break
        i-=1
print(t)
