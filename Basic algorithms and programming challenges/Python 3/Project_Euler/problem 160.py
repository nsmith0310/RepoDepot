### 16576

from math import floor

def p(a,b,c):
    if c==1:
        return 0
    r=1
    a = a%c
    while b >0:
        if (b % 2 == 1):
           r = (r * a) %c
        b = b >> 1
        a = (a * a) % c
    return r

t = 1
i = 1
c = 0
while i<=1000:
    if i%5!=0:
        t*=i
    else:
        c+=1
    i+=1
j = 1

while j<=c:
    t//=2
    j+=1
t = t%100000

i = 0

n=[]

while pow(5,i)<=10**12:
    x = floor(10**12/pow(5,i))
    n.append(x)
    i+=1

la=[]
lb=[]

for x in n:
    if x%1000==0:
        la.append(x//1000)
    else:
        c=1
        while x-1000 >0:
            c+=1
            x-=1000
        lb.append(x)
        la.append(c)

e = sum(la)

b=[]

for x in lb:
    i = 1
    tmp=1
    c=0
    while i<=x:
        if i%5!=0:
            tmp*=i
        else:
            c+=1
        i+=1
    j =1

    while j<=c:
        tmp//=2
        j+=1
    tmp = tmp%100000
    b.append(tmp)

q = 1

 

for x in b:
    q=q*x%100000

print((p(t,e,100000)*q)%100000)
