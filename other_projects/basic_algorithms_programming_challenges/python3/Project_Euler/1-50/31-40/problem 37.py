###Answer: long 748317
from euler import primes, factorize

###get nine of eleven such numbers on this interval
p = primes(10000000)

p.remove(2)
p.remove(3)
p.remove(5)
p.remove(7)

def right(n):
    nums=[]
    i = 0
    while i < len(str(n)):
        nums.append(int(str(n)[:i+1]))
        i+=1
    return nums

def left(n):
    nums=[]
    r = str(n)[::-1]
    i = 0
    while i < len(r):
        nums.append(int(r[:i+1][::-1]))
        i+=1
    return nums

def check(n):
    status = False
    l = left(n)
    r = right(n)
    count_l=0
    count_r=0
    
    for x in l:
        if len(factorize(x))==1:
            count_l+=1
    for x in r:
        if len(factorize(x))==1:
            count_r+=1
    
    if count_l == len(str(n)) and count_r == count_l:
        status=True
    return status
        

count = 0
i = 0
nums=[]
while i < len(p):
    if check(p[i])==True:
        nums.append(p[i])
        ###print(p[i])
        count+=1
    if count==11:
        print(sum(nums))
        break
    i+=1


