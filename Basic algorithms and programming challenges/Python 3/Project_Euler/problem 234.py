###1259187438574927161


from euler import primes,rmtest as r
from math import sqrt,floor, ceil


k = ceil(sqrt(999966663333))
m = k
while 1!=-1:
    if r(m,3)==True and m**2 >999966663333:
        break
    m+=1

p = primes(m+1)

t=0
pairs=[]

i = 0
h=[]
while i<len(p)-1:
    pairs.append([p[i],p[i+1]])
    i+=1
t=0
for x in pairs:
    l = x[0]**2
    u = x[1]**2
    ls=[]
    us=[]

    j = l/x[0]
    while j*x[0]<u:
        if j*x[0]%x[1]!=0 and not (sqrt(j*x[0])).is_integer() and j*x[0]<999966663333:
            t+=int((j*x[0]))
            ###print(j*x[0])
        j+=1
        
    j = x[0]
    while j*x[1]>l:
        j-=1
    j+=1
    while j*x[1]<l:
        j+=1
    while j*x[1]<u:
        if j*x[1]%x[0]!=0 and not (sqrt(j*x[1])).is_integer() and j*x[1]<999966663333:
            t+=int((j*x[1]))
            ###print(j*x[1])
        j+=1
    

print(t)
            
