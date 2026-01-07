###long 1884161251122450

from functools import reduce

from math import floor

 

def f(n):   

    return list(set(reduce(list.__add__,

                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

i = 1

 

e = 0

d=set()

while i<=150000*(7/10):

    j = 1

    p = i**2 + 1

    while j<=i:

       

        

        

        c = i*(i+j)*(i+p/j)

        if p%j==0:

            d.add(c)

           

        e+=1

        j+=1

    i+=1

b = list(d)

 

b.sort()

print(b[149999])
