###long 453647705
###credit goes to geeksforgeeks for the idea for multiplicative
###order without exponentiation

from euler import primes,pmod

d = primes(100000)
d.remove(2)
d.remove(3)
d.remove(5)

def m(n):
    c=1
    r = 10%n
    while 1!=-1:
        r=10*r%n
        c+=1
        if r==1:
            break
    
    x=c
    while x%2==0:
        x/=2
    while x%5==0:
        x/=5
    return x==1

t=10
for x in d:
    if m(x)==False:
        t+=x
print(t)



