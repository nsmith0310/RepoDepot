###2470433131948040

from math import floor

###not mine (stack user described as newton's method)
###an implementation of what wikipedia describes ^^

def isqrt(n):
    ###can select any x0 >0: selecting n allows
    ###the stop condition to be when y exceeds x in
    ###the while loop
    ###the stack users // can also probably be
    ###substituted for math.floor(n/m)
    if n<=0:
        return 0
    x = n
    ###the 1 which was  originally in the place of
    ###x//n worked because at the onset the two are
    ###equal
    y = (x+(x//n))//2
    while y<x:
        x = y
        y = (x+(n//x))//2
    return x




###A006454: these numbers translate to our targets as the
###result of isqrt, or integer square root
n = [0,3,15,120,528,4095,17955]


while len(n)<=40:
    n.append(35*(n[-2] - n[-4]) + n[-6])
t = 0

for y in n:
    t+=isqrt(y)
  
print(t)
