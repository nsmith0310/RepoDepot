###answer: 4075 values of nCr are above 1m for 1<=n<=100 and r<=n
from math import factorial
print("Enter upper bound for n:")
n = int(input())

i=1
r = 1
count=0
while i <= n:
    r = 1
    while r <= i:
        if factorial(i)/(factorial(r)*factorial(i-r))>1000000:
            count+=1
        r+=1
    i+=1
print(count)
