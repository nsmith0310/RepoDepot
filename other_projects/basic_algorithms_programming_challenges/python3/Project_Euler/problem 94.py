
###518408346                                                                                                                                     
###credit for the generating formula 14*n-1 +- n-2 +- 4 goes to s braumme
###interestingly, he found a different generating function for 138 than I did

from math import sqrt

a = [17,241]
b = [5,65]

i = 2
total = 984
while i !=-1:
    x1 = 14*a[i-1] - a[i-2] + 4
    c1 = x1-1
    if 2*x1+c1< 1000000000:
        total+=2*x1+c1
        a.append(x1)
    else:
        break
    i+=1
i=2
while i !=-1:
    x2 = 14*b[i-1] - b[i-2] - 4
    c2 = x2+1
    
    if 2*x2+c2< 1000000000:
        total+=2*x2+c2
        b.append(x2)
    else:
        break
    i+=1    
print(total)

###518408346 long
'''
import numpy as np

def prims(limit=None):
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
def check1(i):
    if 2*i[0]+1 == i[2] or 2*i[0]-1 == i[2]:
        return True
    else:
        return False
def check2(i):
    if 2*i[1]+1 == i[2] or 2*i[1]-1 == i[2]:
        return True
    else:
        return False
lim = 200000000
total=0
for i in prims(lim):
    if check1(i)==True:
        if (2*i[0]+2*i[2])<= 1000000000:
            total+=(2*i[0]+2*i[2])
    if check2(i)==True:
        if (2*i[1]+2*i[2])<= 1000000000:
            total+=(2*i[1]+2*i[2])

print(total)
'''
