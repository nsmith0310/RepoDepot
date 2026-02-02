###long 10057761
###possible speedup involves converting to int/float in function 1
import numpy as np

from euler import power

def trips(limit=None):
    u = np.mat(' 1  2  2; -2 -1 -2; 2 2 3')
    a = np.mat(' 1  2  2;  2  1  2; 2 2 3')
    d = np.mat('-1 -2 -2;  2  1  2; 2 2 3')
    uad = np.array([u, a, d])
    m = np.array([3, 4, 5])
    while m.size:
        m = m.reshape(-1, 3)
        if limit:
           m = m[m[:, 2] <= limit]
        yield from m
        m = np.dot(m, uad)
t=[]
count=0
u = list((trips(100000000)))

for x in u:
    tmp=[]
    for y in x:
        tmp.append(float(y))
    t.append(tmp)

for x in t:
    
    y = list(x)
    if sum(y)<100000000:
        a =pow(y[2],2)
        b = float(y[1]-y[0])
        if a%b==0:
            i=1
            while i*(sum(y))<100000000:
                count+=1
                i+=1
    
print(count)

