###0.5731441

 

from collections import Counter

 

from itertools import product

from decimal import *

 

getcontext().prec=7

 

t = list(product([1,2,3,4],repeat=9))

 

e = list(product([1,2,3,4,5,6],repeat=6))

 

t1=[]

e1=[]

count=0

for x in t:

    t1.append(sum(x))

for x in e:

    e1.append(sum(x))

   

tmp1 = (Counter(t1))

tmp2 = Counter(e1)

t2=[]

e2=[]

 

for x in tmp1:

    t2.append([int(x),int(tmp1[x])])

   

for x in tmp2:

    e2.append([int(x),int(tmp2[x])])

   

for x in t2:

    for y in e2:

        if x[0]>y[0]:

            count+=x[1]*y[1]

           

print(round(1.0*count/(len(t1)*len(e1)),7))
