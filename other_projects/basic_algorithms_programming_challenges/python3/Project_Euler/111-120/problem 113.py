###51161058134250

###modified OEIS code

 

import scipy.misc

 

def choose(n,k):

    x = (scipy.misc.comb(n,k, exact=True))

    return (x)

   

def r(n):

    return (n+18)*choose(n+8,8)//9

   

total=0

   

i = 1

minus = 0

while i <= 100:

    total+=r(i)

    minus+=10

    i+=1

print(total-minus)
