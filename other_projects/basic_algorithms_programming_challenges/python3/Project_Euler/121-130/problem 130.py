###long 149253
from euler import power,rmtest
from math import gcd
tmp=[]
def rep(n):
    return ((power(10,n)-1)//9)

i = 11

while i!=-1:
    if gcd(10,i)==1 and rmtest(i,5)==False:
        j = 1
        while rep(j)%i!=0:
            j+=1
        if (i-1)%j==0:
            tmp.append(i)
        if len(tmp)==25:
            print(sum(tmp))
            break
    
    i+=2

