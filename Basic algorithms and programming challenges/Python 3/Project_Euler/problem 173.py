###long 1572729

import numpy as np

from itertools import combinations as c

from functools import reduce

 

def factors(n):   

    return set(reduce(list.__add__,

                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

i = 1

 

count=0

 

while i<=1000000:

    nums = list(factors(i))

 

    t = c(nums,2)

    f=[]

    for x in t:

        if x[1]*x[0]==i:

            n=[x[0],x[1]]

            n.sort(reverse=True)

            f.append(n)

    for x in f:

        a = np.array([[1,1],[1,-1]])

        b = np.array([x[0],x[1]])

        t = (np.linalg.solve(a,b))

        q = t.tolist()

        for y in q:

           

            if (y).is_integer() and i&1==False:

               

                count+=1

    i+=1

print(int(count/2))
