###longish 283988410192

from euler import rmtest as r,power,pmod,factorize,period
from math import sqrt
from functools import reduce



num = 1234567891011

###not at all my method: I just added in the modulo m
def fib(n,m):
    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = (v2*v2)%m
        v1, v2, v3 = (v1*v1+calc)%m, ((v1+v3)*v2)%m, (calc+v3*v3)%m
        if rec=='1':    v1, v2, v3 = v1+v2, v1, v2
    return v2

i = 10**14

d=[]

while i!=-1:
    if r(i,3)==True:
        d.append(fib(i,num))
    if len(d)>=100000:
        print(sum(d)%num)
        break
    i+=1
