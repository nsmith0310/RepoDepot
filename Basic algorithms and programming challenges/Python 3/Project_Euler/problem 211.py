###answer: long 1922364685

import itertools
from math import sqrt
flatten_iter = itertools.chain.from_iterable
def p(n):
    l= list(set(flatten_iter((i, n//i) 
                for i in range(1, int(n**0.5)+1) if n % i == 0)))
    return (l)


def check(n):
    if (sqrt(n)).is_integer():
        return True
    else:
        return False

def square(list):
    return map(lambda x: x ** 2, list)

final=[]
for i in range(1,64000000):
    if check(sum(square(p(i))))==True:
        final.append(i)

print(sum(final))
