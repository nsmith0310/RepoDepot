###answer: 840

###I in no way designed the top two methods

###answer: 840 with 8 solutions
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
            tmp.append(i)
            i = i + prim
    x = np.array(tmp).tolist()
    return x
f = trips(1500)
y=[]

for x in f:

    if sum(x)<=1000:
        y.append(sum(x))

mx = 0
for u in y:
    if y.count(u)>mx:
        mx = y.count(u)
        n = u
print(n)


###answer: (incredibly slow), p = 840 with 8 solutions
'''
import math
print("Enter maximum perimeter:")
mx = int(input())

x=1
y=1
l = 1
p = 0
count=0
highest_p=0
big=0

while p <= mx:
    count=0
    l=1
    while l < p:
        x=1
        while x < l:
            y=1
            while y < l:
                if x*x+y*y==l*l and p == x + y + math.sqrt((x*x)+(y*y)):
                    count+=1
                y+=1
            x+=1
        l+=1
    if count > big:
        big = int(count/2)
        highest_p=p
    p+=60
    
print("Number of solutions:",big)
print("For perimeter:",highest_p)
'''
