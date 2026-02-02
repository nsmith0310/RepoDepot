###long 1818
###according to dreamshire, OEIS has sequence which can expedite this alot
###^^^ A143714

from math import sqrt
from euler import rmtest as r

import numpy as np

def gen_prim_pyth_trips(limit=None):
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

def trips(limit):
    tmp=[]
    for prim in gen_prim_pyth_trips(limit):
        i = prim
        for _ in range(limit//prim[2]):
            i.sort()
            tmp.append(i)
            i = i + prim
    x = np.array(tmp).tolist()
    return x

def stest(n):
    return (sqrt(n)).is_integer()

def itest(i,j):
    return (sqrt(i+j)).is_integer()

y = list(trips(5000))
x = sorted(y, key = lambda v: int(v[0]))


final=[]

for a in x:
    
    n1 = a[0]
    n2 = a[1]
    n3 = a[2]
    i = 1
    while i<n1:
        
        z = n1-i
        y = n2-(n1-i)
        x = n1
        if y>1 and y<=x:
            if stest((x+y)**2 + z**2)==False:
                if y>=z:
                    ###print([x,y,z])
                    final.append(x)
                    i=n1
        i+=1
    
    n2 = a[0]
    n1 = a[1]
    n3 = a[2]
    i = 1
    while i<n1:
        
        z = n1-i
        y = n2-(n1-i)
        x = n1
        if y>1 and y<=x:
            if stest((x+y)**2 + z**2)==False:
                if y>=z:
                    ###print([x,y,z])
                    final.append(x)
                    i=n1
        i+=1
d = list(set(final))
d.sort()
count=0
i = 1
j = 1
k = 1
f1=[]


for x in d:
    j = 1
    kill=0
    while j<=x:
        k = 1
        while k<=j:
            b = [sqrt(x**2 + (j+k)**2),sqrt((x+j)**2 + k**2)]
            b.sort()
            
            
            if (b[0]).is_integer():
                ###print([i,j,k])
                f1.append([i,j,k])
                count+=1
            k+=1
        j+=1
                
    if count>1000000:
        print(x)
        break

    

