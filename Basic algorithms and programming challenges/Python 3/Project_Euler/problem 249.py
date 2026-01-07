###long 9275262564250418

from numpy import convolve as c
from euler import primes as p
import numpy as np


def m(l):
    b = sum(l)
    print(b)
    g = p(b)
    f = 0
    total = [1]
    for x in l:
        i = 1
        tmp=[1]
        while i<=x:
            if i==x:
                tmp.append(1)
            else:
                tmp.append(0)
                
            i+=1
        
        ###print(tmp,total)
        total=(c(np.array(tmp,dtype='int64'),np.array(total,dtype='int64')))
        t2 = []
        for x in total:
            t2.append(x%10**16)
        total=t2
            
        
    for x in g:
        f+=total[x]
        f = f%10**16
        
    return f
    
print(m(p(5000))%10**16)
        


