###5437849 long
from euler import rmtest as r



def check(n):
    return pow(2,n-1,n)==1



l = primes(100)


i = 1
t=[]
count=0
while i<=50000000:
    x = 2*(power(i,2)) - 1
    if check(x)==True:
        t.append(x)
    i+=1
print(len(t))



for x in t:
    if r(x,5)==True:
        count+=1
print(count)
