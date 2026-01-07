###Answer 1.710637717

###this series unexpectedly gets stuck in a loop and so we dont need to find the 10^12 part

 

from math import floor

from decimal import *

 

getcontext().prec=9

 

def func(n):

    return (floor(Decimal(pow(2,30.403243784 - pow(n,2)))))*0.000000001

 

 

t=[-1]

 

i=0

while i<1000:

    t.append(func(t[i]))

    i+=1

   

print(t[999]+t[998])
