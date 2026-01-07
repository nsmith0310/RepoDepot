###long 229161792008

from euler import primes,power,rmtest as r,factorize as fac
from itertools import combinations as c


def test(n):
    
    i = 0
    while i<=9:
        tmp = list(n)
        j = 0
        while j<len(tmp):
            tmp[j]=str(i)
            ###print(tmp)
            if r(int(''.join(tmp)),3)==True:
                return False
            tmp=list(n)
            j+=1
        i+=1
    return True
def f(n):
    return str(power(n[0],2)*power(n[1],3))

d = primes(200000)

count=0
e = list(c(d,2))



fi=[]
p = []
nums=[]
for x in e:
    g = f(x)
    
    n1 = [x[1],x[0]]
    h = f(n1)
    if '200' in g:
        nums.append(int(g))
    if '200' in h:
        nums.append(int(h))

nums.sort()

nums = list(map(str,nums))
for x in nums:
    if test(x)==True:
        count+=1
        ###print(x,list(set(fac(int(x)))),count)
        fi.append(x)
        
    if len(fi)==200:
        print(fi[-1])
        break
