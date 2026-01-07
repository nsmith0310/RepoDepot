###long 3D58725572C62302

###the vast majority of the time is spent subtracting solutions with leading
###zeros using itertools
###I am still very proud of this solution- it took many days to get it under
###a personally acceptable length of time

from itertools import product as p
from math import factorial

def f(i,j):
    return int(float(factorial(i)/(factorial(i-j)*factorial(j))))
t=4 
i =4
while i<=16:
    ###subtract all combinations with none of the targets
    t+=int(pow(16,i)-pow(13,i))
    ###subtract all combinations with one but not either of the other two targets
    j=1
    while j<=i:
        t-=int(3*f(i,i-j)*pow(13,i-j))
        j+=1
    ###subtract all combinations with two but not the third target
    j=2
    while j<=i:
        k=1
        while k<j:
            t-=int(3*f(j,k)*f(i,i-j)*pow(13,i-j))
            k+=1
        j+=1
    ###the only way I could think of subtracting leading zeroes...    
    d = ["0","1","A","x"]
    
    l = p(d,repeat=i-1)
    for x in l:
        z = x.count("x")
        if x.count("0")>=1 and x.count("1")>=1 and x.count("A")>=1:
            t-=pow(13,z)
    e = ["1","A","x"]
    m = p(e,repeat=i-1)
    for x in m:
        z = x.count("x")
        if x.count("1")>=1 and x.count("A")>=1:
            t-=pow(13,z)

    i+=1

###print(t)
g= str(hex(t))[2:]
print(g.upper())
