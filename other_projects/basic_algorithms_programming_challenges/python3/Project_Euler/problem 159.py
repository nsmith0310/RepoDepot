###long 14489159

from euler import factorize as f,primes
from time import time
from math import ceil,log

t0 = time()

total=0
def div(i):
    comp=[[i]]
    tmp=[[i]]
    d = list(set(f(i)))
    final=[]
        

    
    for y in tmp:
        
        u = y[-1]
        t=[]
        for x in range(2,ceil(u/2)):
            if x<u:
                if u%x==0:
                    nums=y[:-1]
                    nums.append(x)
                    nums.append(int(u/x))
                    nums.sort()
                    
                    if nums not in comp:
                        
                        comp.append(nums)
                        tmp.append(nums)
    
    return comp

total=0
i = 2

a = [i for i in range(2,1000000)]
a.sort(reverse=True)
for i in a:
    w = list(div(i))
    final=[]
    for x in w:
        tmp=[]
        for y in x:
            
            while y>9:
                y = sum(list(map(int,list(str(y)))))
            tmp.append(y)
        final.append(sum(tmp))
    total+=max(final)
                    
    i+=1
             
print(total)
